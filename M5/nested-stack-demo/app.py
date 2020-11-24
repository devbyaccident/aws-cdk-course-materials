#!/usr/bin/env python3

from aws_cdk import core

from nested_stack_demo.nested_stack_demo_stack import DemoStack


app = core.App()
DemoStack(app, "nested-stack-demo")

app.synth()
