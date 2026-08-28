---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SecurityGroupVpcAssociation.html
---

# SecurityGroupVpcAssociation
<a name="API_SecurityGroupVpcAssociation"></a>

A security group association with a VPC that you made with [AssociateSecurityGroupVpc](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateSecurityGroupVpc.html).

## Contents
<a name="API_SecurityGroupVpcAssociation_Contents"></a>

 ** groupId **
The association's security group ID.
Type: String
Required: No

 ** groupOwnerId **
The AWS account ID of the owner of the security group.
Type: String
Required: No

 ** state **
The association's state.
Type: String
Valid Values: `associating | associated | association-failed | disassociating | disassociated | disassociation-failed`
Required: No

 ** stateReason **
The association's state reason.
Type: String
Required: No

 ** vpcId **
The association's VPC ID.
Type: String
Required: No

 ** vpcOwnerId **
The AWS account ID of the owner of the VPC.
Type: String
Required: No

## See Also
<a name="API_SecurityGroupVpcAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SecurityGroupVpcAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SecurityGroupVpcAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SecurityGroupVpcAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
