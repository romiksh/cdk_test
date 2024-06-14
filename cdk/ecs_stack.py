from aws_cdk import (
    aws_certificatemanager as certificatemanager,
    aws_elasticloadbalancingv2 as elbv2,
    aws_ecs as ecs,
    aws_ecr_assets as ecr_assets,
    aws_ecs_patterns as ecs_patterns,
    aws_route53 as route53,
    Stack
)
from constructs import Construct
import yaml


class EcsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Get env variables file
        env_file = self.node.try_get_context('envFile')
        if env_file is None:
            print("No env file defined. Using 'dev.yaml' by default")
            env_file = 'dev.yaml'

        with (open(f"./envs/{env_file}") as stream):
            try:
                env_data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        cluster = ecs.Cluster(self, "Test-Task-Cluster")

        #Build Docker Image
        image_asset = ecr_assets.DockerImageAsset(self,
                                                  "NGINX-Proxy-App",
                                                  directory="../nginx-app")

        image = ecs.ContainerImage.from_docker_image_asset(image_asset)

        # ACM
        certificate = (certificatemanager.Certificate.
                       from_certificate_arn(self,
                                            'Cert',
                                            certificate_arn=env_data['certificate']['arn']
                                            ))

        # Route53
        hosted_zone = (route53.HostedZone.
                       from_hosted_zone_attributes(self,
                                                   'Zone',
                                                   hosted_zone_id=env_data['route53'][
                                                       'hosted_zone_id'],
                                                   zone_name=env_data['route53']['zone_name']))

        lb = ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "TestFargateService",
            cluster=cluster,
            cpu=env_data['ecs']['cpu'],
            memory_limit_mib=env_data['ecs']['memory'],
            desired_count=2,
            # listener_port=443,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=image,
                container_name="NGINX-Proxy-App",
                container_port=80,
            ),
            public_load_balancer=True,
            domain_name=env_data['service']['hostname'],
            domain_zone=hosted_zone,
            ssl_policy=elbv2.SslPolicy.RECOMMENDED,
            redirect_http=True,
            certificate=certificate
        )

        lb.target_group.configure_health_check(
            path="/health_check",
            port="80"
        )
