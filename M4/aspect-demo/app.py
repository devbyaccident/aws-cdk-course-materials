#!/usr/bin/env python3

from aws_cdk import core
import os
from aspect_demo.aspect_demo_stack import AspectDemoStack


app = core.App()
AspectDemoStack(app, "aspect-demo",env={
  'account': os.environ['CDK_DEFAULT_ACCOUNT'], 
  'region': os.environ['CDK_DEFAULT_REGION']
})

app.synth()