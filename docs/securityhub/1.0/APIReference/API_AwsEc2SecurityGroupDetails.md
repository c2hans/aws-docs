---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2SecurityGroupDetails.html
---

# AwsEc2SecurityGroupDetails
<a name="API_AwsEc2SecurityGroupDetails"></a>

Details about an Amazon EC2 security group.

## Contents
<a name="API_AwsEc2SecurityGroupDetails_Contents"></a>

 ** GroupId **   <a name="securityhub-Type-AwsEc2SecurityGroupDetails-GroupId"></a>
The ID of the security group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** GroupName **   <a name="securityhub-Type-AwsEc2SecurityGroupDetails-GroupName"></a>
The name of the security group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IpPermissions **   <a name="securityhub-Type-AwsEc2SecurityGroupDetails-IpPermissions"></a>
The inbound rules associated with the security group.
Type: Array of [AwsEc2SecurityGroupIpPermission](API_AwsEc2SecurityGroupIpPermission.md) objects
Required: No

 ** IpPermissionsEgress **   <a name="securityhub-Type-AwsEc2SecurityGroupDetails-IpPermissionsEgress"></a>
[VPC only] The outbound rules associated with the security group.
Type: Array of [AwsEc2SecurityGroupIpPermission](API_AwsEc2SecurityGroupIpPermission.md) objects
Required: No

 ** OwnerId **   <a name="securityhub-Type-AwsEc2SecurityGroupDetails-OwnerId"></a>
The AWS account ID of the owner of the security group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VpcId **   <a name="securityhub-Type-AwsEc2SecurityGroupDetails-VpcId"></a>
[VPC only] The ID of the VPC for the security group.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2SecurityGroupDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2SecurityGroupDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2SecurityGroupDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2SecurityGroupDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
