
# Welcome to Test CDK Python project!


---

## Task definition:
#### NGINX Configuration:
Configure NGINX to proxy requests based on the URI path.
```
Example:
/google.com proxies to https://google.com
/wikipedia.org proxies to https://wikipedia.org
```
### Containerization:
Dockerize the NGINX application.

Ensure the Dockerfile is optimized for size and performance.
### AWS ECS + Fargate Deployment:
Define the ECS Task Definition with appropriate CPU and memory allocations.

Deploy the application in ECS using Fargate.
### AWS ALB Configuration:
Use AWS ALB to route HTTP requests to HTTPS.

Integrate ACM for SSL certificate management.

Use Route 53 for DNS management.
### AWS CDK Deployment:
### Create an AWS CDK stack that:
Deploys the ECS service.

Configures the ALB.

Sets up Route 53 and ACM.

The CDK stack should accept an env_name parameter.

Read environment-specific parameters (such as ECS memory/CPU allocation, service hostname, etc.) from a YAML file named after the environment (envs/env_name.yaml).
``` yaml
# envs/dev.yaml
ecs:
  memory: 512
  cpu: 256
service:
  hostname: dev.example.com
```
Adherence to PEP 8 and Python coding standards.

Documentation and ease of deployment.

Submit your solution as a public Git repository.

---
## Prepare the project

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

# Prepare env file:
Create envs dir:

`mkdir envs`

`cd envs`

Put file with environment variables:

For example:

```yaml
ecs:
  memory: 512
  cpu: 256
service:
  hostname: 'dev.example.com'
certificate:
  arn: 'arn:aws:<certificate arn>'
route53:
  hosted_zone_id: '<route 53 hosted zone ID>'
  zone_name: 'example.com'
```

# Deploy to AWS:
Set `chmod +x deploy.sh`

Deploy bootstrap to AWS
```
./deploy.sh bootstrap <account> <region>
```
Deploy ECS
```
./deploy.sh deploy <account> <region> -c env_name=dev
```
`dev` - environment variables file in `./envs/dev.yaml`

# Quick notes for reference
[Notes](doc/QuickNotes.md)
