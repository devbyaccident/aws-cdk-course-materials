from aws_cdk import (
    core,
    aws_ssm as ssm,
    aws_iam as iam
)

class ParameterStoreStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here

        # This method will pull a String from parameter store at deployment
        string_param = ssm.StringParameter.value_for_string_parameter(self,"string-parameter")
        
        # This method will pull a String from parameter store at syhtnesis
        synth_string_param = ssm.StringParameter.value_from_lookup(self,"string-parameter")

        # This method will pull a SecretString that can be used as a password in another resource
        secure_string_param = core.SecretValue.ssm_secure('secure-parameter', "1")

        iam.User(self,"user", password=secure_string_param)

        core.CfnOutput(self,"deployment-parameter", value=string_param)
        core.CfnOutput(self,"synthesis-parameter", value=synth_string_param)