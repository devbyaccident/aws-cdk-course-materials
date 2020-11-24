from aws_cdk import (
    core,
    aws_s3 as s3
)

class NestedStack(core.NestedStack):

    def __init__(self, scope: core.Construct, construct_id: str,
       bucket: str,
       **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        s3.Bucket(self,'bucket-id',
            bucket_name='demo-'+bucket+'-865'
        )

class DemoStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        count = 0
        buckets = ['source','dest','third-bucket']
        for bucket in buckets:
            NestedStack(self, 'nested-stack-id-'+str(count), bucket)
            count = count+1