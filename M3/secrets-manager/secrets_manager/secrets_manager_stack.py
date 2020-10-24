from aws_cdk import (
    core,
    aws_secretsmanager as sm,
    aws_iam as iam,
    aws_kms as kms
)


class SecretsManagerStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        key = kms.Key.from_key_arn(self, 'kms-key',
            "arn:aws:kms:us-east-1:481877421625:key/46f9b783-09b8-4b81-b0f5-e9b6b3b096f7"
        )

        secret = sm.Secret.from_secret_attributes(self,"secret",
            secret_arn="arn:aws:secretsmanager:us-east-1:481877421625:secret:user_password-7pv8IQ",
            encryption_key=key
        )

        iam.User(self,"user", password=secret.secret_value)