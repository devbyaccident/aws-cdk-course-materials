#!/usr/bin/env python3

import os
from aws_cdk import core
from secrets_manager.secrets_manager_stack import SecretsManagerStack


app = core.App()
SecretsManagerStack(app, "secrets-manager",env={
    'account': os.environ['CDK_DEFAULT_ACCOUNT'], 
    'region': os.environ['CDK_DEFAULT_REGION']
  })

app.synth()
