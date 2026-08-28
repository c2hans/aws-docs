---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReferencedSecurityGroup.html
---

# ReferencedSecurityGroup
<a name="API_ReferencedSecurityGroup"></a>

 Describes the security group that is referenced in the security group rule.

## Contents
<a name="API_ReferencedSecurityGroup_Contents"></a>

 ** groupId **
The ID of the security group.
Type: String
Required: No

 ** peeringStatus **
The status of a VPC peering connection, if applicable.
Type: String
Required: No

 ** userId **
The AWS account ID.
Type: String
Required: No

 ** vpcId **
The ID of the VPC.
Type: String
Required: No

 ** vpcPeeringConnectionId **
The ID of the VPC peering connection (if applicable).
Type: String
Required: No

## See Also
<a name="API_ReferencedSecurityGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ReferencedSecurityGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ReferencedSecurityGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ReferencedSecurityGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
