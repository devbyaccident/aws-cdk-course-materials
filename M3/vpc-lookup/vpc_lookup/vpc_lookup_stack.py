from aws_cdk import (
    core,
    aws_ec2 as ec2
)


class VpcLookupStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        # vpcid = self.node.try_get_context("vpcid")
        vpc = ec2.Vpc.from_lookup(self, "VPC", is_default=True)

        subnets = vpc.select_subnets(subnet_type=ec2.SubnetType.PUBLIC)

        core.CfnOutput(self, "publicSubnets",
                value=str(subnets.subnet_ids))