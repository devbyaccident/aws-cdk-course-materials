#!/usr/bin/env python3
import os
from aws_cdk import core

from vpc_lookup.vpc_lookup_stack import VpcLookupStack


app = core.App()
VpcLookupStack(app, "vpc-lookup",env={
    'account': os.environ['CDK_DEFAULT_ACCOUNT'], 
    'region': os.environ['CDK_DEFAULT_REGION']
  })

app.synth()
