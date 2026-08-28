---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SecurityGroupForVpc.html
---

# SecurityGroupForVpc
<a name="API_SecurityGroupForVpc"></a>

A security group that can be used by interfaces in the VPC.

## Contents
<a name="API_SecurityGroupForVpc_Contents"></a>

 ** description **
The security group's description.
Type: String
Required: No

 ** groupId **
The security group ID.
Type: String
Required: No

 ** groupName **
The security group name.
Type: String
Required: No

 ** ownerId **
The security group owner ID.
Type: String
Required: No

 ** primaryVpcId **
The VPC ID in which the security group was created.
Type: String
Required: No

 ** TagSet.N **
The security group tags.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_SecurityGroupForVpc_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SecurityGroupForVpc)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SecurityGroupForVpc)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SecurityGroupForVpc)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
