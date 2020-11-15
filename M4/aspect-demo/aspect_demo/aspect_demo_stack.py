from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_s3_notifications
)
import jsii

class AspectDemoStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
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
        source_bucket = s3.Bucket(self, "cdk-source-bucket",
            bucket_name="demo-source-865"
        )

        dest_bucket = s3.Bucket(self, "cdk-dest-bucket",
            bucket_name="demo-dest-865",
            encryption=s3.BucketEncryption.KMS_MANAGED
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
        
        # This will apply the Aspect class defined below
        core.Aspects.of(self).add(EncryptionAspect())
        
        # This will apply an aspect to tag all resources in the stack
        core.Tags.of(self).add("Key","Value")
        core.Tags.of(self).add("Project","Demo-App")


# Here is the aspect class
@jsii.implements(core.IAspect)
class EncryptionAspect:
    def visit(self, construct):
        if isinstance(construct, s3.CfnBucket):
            if str(construct.bucket_name) == 'demo-dest-865':
                if str(construct.bucket_encryption) == 'None':
                    construct.node.add_error("Destination must be encrypted")