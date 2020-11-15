#!/usr/bin/env python3

import os
from aws_cdk import core
from demo_app.demo_app_stack import DemoAppStack

default = core.Environment(account='<dev_account_number>', region='us-east-1')
prod = core.Environment(account='<prod_account_number>', region='us-west-2')

app = core.App()
DemoAppStack(app, "demo-app-default",env=default,prod_env=False)
DemoAppStack(app, "demo-app-prod",env=prod,prod_env=True)

app.synth()
