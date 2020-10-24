#!/usr/bin/env python3
import os
from aws_cdk import core

from parameter_store.parameter_store_stack import ParameterStoreStack


app = core.App()
ParameterStoreStack(app, "parameter-store",env={
    'account': os.environ['CDK_DEFAULT_ACCOUNT'], 
    'region': os.environ['CDK_DEFAULT_REGION']
  })

app.synth()