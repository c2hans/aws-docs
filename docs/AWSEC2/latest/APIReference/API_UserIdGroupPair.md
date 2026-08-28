---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UserIdGroupPair.html
---

# UserIdGroupPair
<a name="API_UserIdGroupPair"></a>

Describes a security group and AWS account ID pair.

## Contents
<a name="API_UserIdGroupPair_Contents"></a>

 ** Description ** (request), ** description ** (response)
A description for the security group rule that references this user ID group pair.
Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and .\_-:/()\#,@[]\+=;{}\!$\*
Type: String
Required: No

 ** GroupId ** (request), ** groupId ** (response)
The ID of the security group.
Type: String
Required: No

 ** GroupName ** (request), ** groupName ** (response)
[Default VPC] The name of the security group. For a security group in a nondefault VPC, use the security group ID.
For a referenced security group in another VPC, this value is not returned if the referenced security group is deleted.
Type: String
Required: No

 ** PeeringStatus ** (request), ** peeringStatus ** (response)
The status of a VPC peering connection, if applicable.
Type: String
Required: No

 ** UserId ** (request), ** userId ** (response)
The ID of an AWS account.
For a referenced security group in another VPC, the account ID of the referenced security group is returned in the response. If the referenced security group is deleted, this value is not returned.
Type: String
Required: No

 ** VpcId ** (request), ** vpcId ** (response)
The ID of the VPC for the referenced security group, if applicable.
Type: String
Required: No

 ** VpcPeeringConnectionId ** (request), ** vpcPeeringConnectionId ** (response)
The ID of the VPC peering connection, if applicable.
Type: String
Required: No

## See Also
<a name="API_UserIdGroupPair_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/UserIdGroupPair)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/UserIdGroupPair)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/UserIdGroupPair)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
