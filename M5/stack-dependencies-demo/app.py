#!/usr/bin/env python3

from aws_cdk import core
import os
from demo_app.demo_app import DemoApp
from new_requirements.new_requirements import NewRequirements

env = core.Environment(
  account=os.environ['CDK_DEFAULT_ACCOUNT'],
  region=os.environ['CDK_DEFAULT_REGION']
)


app = core.App()

demo_app = DemoApp(app, "demo-app", env=env)
new_reqs = NewRequirements(app, "new-requirements", env=env)

demo_app.add_dependency(new_reqs)

app.synth()