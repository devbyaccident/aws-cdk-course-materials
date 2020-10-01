from aws_cdk import core
from aws_cdk import aws_s3

class DemoAppStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        aws_s3.Bucket(self, "cdk-source-bucket")