from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_s3_notifications as s3_notifications,
    aws_lambda as _lambda,
    aws_iam as iam
)

class DemoApp(core.Stack):

    def __init__(self, scope: core.Construct, id: str,
    #    new_lambda: _lambda.Function,
       **kwargs) -> None:
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
        # role.add_managed_policy(
        #     iam.ManagedPolicy.from_aws_managed_policy_name("AWSLambdaBasicExecutionRole")
        # )

        # create s3 buckets
        source_bucket = s3.Bucket(self, "cdk-source-bucket",
            bucket_name="demo-source-865"
        )
        dest_bucket = s3.Bucket(self, "cdk-dest-bucket",
            bucket_name="demo-dest-865",
            encryption=s3.BucketEncryption.KMS_MANAGED
        )

        # create lambda function
        first_function = _lambda.Function(self, "first_lambda_function",
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler="lambda-handler.main",
            environment={
                'DestinationBucket': dest_bucket.bucket_name
            },
            role=role,
            code=_lambda.Code.asset("./lambda/copy_object")
        )

        # create s3 notification for lambda function
        notification = s3_notifications.LambdaDestination(first_function)

        # assign notification for the s3 event type (ex: OBJECT_CREATED)
        source_bucket.add_object_created_notification(notification)

        # new_notification = s3_notifications.LambdaDestination(new_lambda)
        # dest_bucket.add_object_created_notification(new_notification)
        