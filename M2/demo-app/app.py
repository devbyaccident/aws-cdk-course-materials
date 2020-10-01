#!/usr/bin/env python3

from aws_cdk import core

from demo_app.demo_app_stack import DemoAppStack


app = core.App()
DemoAppStack(app, "demo-app")

app.synth()
