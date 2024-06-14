# Quick notes for project CDK Deployment

---
## This project make deployment Containerized app (Nginx) to the AWS ECS cluster. Program language Python

ECS Stack described in file [./cdk/ecs_stack.py](../cdk/ecs_stack.py)

It use [./nginx-app/Dockerfile](../nginx-app/Dockerfile) for build Docker image and store it in AWS ECR

ECS Cluster deploy to Fargate.

Application using Application Load Balancer.

HTTP requests redirected to HTTPS by ALB.

Project has environment depended deployment. Environment variable files stores in ./envs

Dev is default environment for build.

For build use [./deploy.sh](../deploy.sh) script with arguments:

            - command [bootstrap|deploy]

            - AWS Account

            - AWS Region

            - any other args for cdk bui