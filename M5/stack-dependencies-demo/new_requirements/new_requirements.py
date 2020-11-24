from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb
)

class NewRequirements(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here

        # # create dynamo table
        dynamo_table = dynamodb.Table(
            self, "demo_table",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            )
        )

        # create lambda function
        second_function = _lambda.Function(self, "second_lambda_function",
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler="lambda-handler.main",
            function_name="second_lambda",
            environment={
                'TABLE_NAME': dynamo_table.table_name
            },
            code=_lambda.Code.asset("./lambda/write_to_dynamo")
        )

        self._lambda_function = second_function

    @property
    def second_function(self) -> _lambda.Function:
        return self._lambda_function