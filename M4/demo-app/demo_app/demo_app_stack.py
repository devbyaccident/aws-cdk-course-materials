from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_s3_notifications
)

class DemoAppStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, prod_env=False, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here

        # Lambda Role
        role = iam.Role(self, "lambda_role", 
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            role_name="lambda_role"
        )

        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess")
        )
        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AWSLambdaBasicExecutionRole")
        )

        # create s3 buckets
        if prod_env:
            source_bucket = s3.Bucket(self, "cdk-source-bucket",
                bucket_name="demo-source-865-prod"
            )
            dest_bucket = s3.Bucket(self, "cdk-dest-bucket",
                bucket_name="demo-dest-865-prod"
            )
        else:
            source_bucket = s3.Bucket(self, "cdk-source-bucket",
                bucket_name="demo-source-865-nonprod"
            )
            
            dest_bucket = s3.Bucket(self, "cdk-dest-bucket",
                bucket_name="demo-dest-865-nonprod"
            )

        

        # create lambda function
        function = _lambda.Function(self, "lambda_function",
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler="lambda-handler.main",
            environment={
                'DestinationBucket': dest_bucket.bucket_name
            },
            role=role,
            code=_lambda.Code.asset("./lambda")
        )

        # create s3 notification for lambda function
        notification = aws_s3_notifications.LambdaDestination(function)

        # assign notification for the s3 event type (ex: OBJECT_CREATED)
        source_bucket.add_object_created_notification(notification)
