---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SecurityGroup.html
---

# SecurityGroup
<a name="API_SecurityGroup"></a>

Describes a security group.

## Contents
<a name="API_SecurityGroup_Contents"></a>

 ** groupDescription **
A description of the security group.
Type: String
Required: No

 ** groupId **
The ID of the security group.
Type: String
Required: No

 ** groupName **
The name of the security group.
Type: String
Required: No

 ** IpPermissions.N **
The inbound rules associated with the security group.
Type: Array of [IpPermission](API_IpPermission.md) objects
Required: No

 ** IpPermissionsEgress.N **
The outbound rules associated with the security group.
Type: Array of [IpPermission](API_IpPermission.md) objects
Required: No

 ** ownerId **
The AWS account ID of the owner of the security group.
Type: String
Required: No

 ** securityGroupArn **
The ARN of the security group.
Type: String
Required: No

 ** TagSet.N **
Any tags assigned to the security group.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** vpcId **
The ID of the VPC for the security group.
Type: String
Required: No

## See Also
<a name="API_SecurityGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SecurityGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SecurityGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SecurityGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
