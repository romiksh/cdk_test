#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk.ecs_stack import EcsStack

app = cdk.App()

EcsStack(app, "EcsStack", env=cdk.Environment(
    account=os.environ.get("CDK_DEPLOY_ACCOUNT", os.environ["CDK_DEFAULT_ACCOUNT"]),
    region=os.environ.get("CDK_DEPLOY_REGION", os.environ["CDK_DEFAULT_REGION"]))
         )

app.synth()
