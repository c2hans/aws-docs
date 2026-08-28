---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2SecurityGroupUserIdGroupPair.html
---

# AwsEc2SecurityGroupUserIdGroupPair
<a name="API_AwsEc2SecurityGroupUserIdGroupPair"></a>

A relationship between a security group and a user.

## Contents
<a name="API_AwsEc2SecurityGroupUserIdGroupPair_Contents"></a>

 ** GroupId **   <a name="securityhub-Type-AwsEc2SecurityGroupUserIdGroupPair-GroupId"></a>
The ID of the security group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** GroupName **   <a name="securityhub-Type-AwsEc2SecurityGroupUserIdGroupPair-GroupName"></a>
The name of the security group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PeeringStatus **   <a name="securityhub-Type-AwsEc2SecurityGroupUserIdGroupPair-PeeringStatus"></a>
The status of a VPC peering connection, if applicable.
Type: String
Pattern: `.*\S.*`
Required: No

 ** UserId **   <a name="securityhub-Type-AwsEc2SecurityGroupUserIdGroupPair-UserId"></a>
The ID of an AWS account.
For a referenced security group in another VPC, the account ID of the referenced security group is returned in the response. If the referenced security group is deleted, this value is not returned.
[EC2-Classic] Required when adding or removing rules that reference a security group in another VPC.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VpcId **   <a name="securityhub-Type-AwsEc2SecurityGroupUserIdGroupPair-VpcId"></a>
The ID of the VPC for the referenced security group, if applicable.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VpcPeeringConnectionId **   <a name="securityhub-Type-AwsEc2SecurityGroupUserIdGroupPair-VpcPeeringConnectionId"></a>
The ID of the VPC peering connection, if applicable.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2SecurityGroupUserIdGroupPair_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2SecurityGroupUserIdGroupPair)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2SecurityGroupUserIdGroupPair)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2SecurityGroupUserIdGroupPair)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
