---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRdsDbSecurityGroupDetails.html
---

# AwsRdsDbSecurityGroupDetails
<a name="API_AwsRdsDbSecurityGroupDetails"></a>

Provides information about an Amazon RDS DB security group.

## Contents
<a name="API_AwsRdsDbSecurityGroupDetails_Contents"></a>

 ** DbSecurityGroupArn **   <a name="securityhub-Type-AwsRdsDbSecurityGroupDetails-DbSecurityGroupArn"></a>
The ARN for the DB security group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DbSecurityGroupDescription **   <a name="securityhub-Type-AwsRdsDbSecurityGroupDetails-DbSecurityGroupDescription"></a>
Provides the description of the DB security group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DbSecurityGroupName **   <a name="securityhub-Type-AwsRdsDbSecurityGroupDetails-DbSecurityGroupName"></a>
Specifies the name of the DB security group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Ec2SecurityGroups **   <a name="securityhub-Type-AwsRdsDbSecurityGroupDetails-Ec2SecurityGroups"></a>
Contains a list of EC2 security groups.
Type: Array of [AwsRdsDbSecurityGroupEc2SecurityGroup](API_AwsRdsDbSecurityGroupEc2SecurityGroup.md) objects
Required: No

 ** IpRanges **   <a name="securityhub-Type-AwsRdsDbSecurityGroupDetails-IpRanges"></a>
Contains a list of IP ranges.
Type: Array of [AwsRdsDbSecurityGroupIpRange](API_AwsRdsDbSecurityGroupIpRange.md) objects
Required: No

 ** OwnerId **   <a name="securityhub-Type-AwsRdsDbSecurityGroupDetails-OwnerId"></a>
Provides the AWS ID of the owner of a specific DB security group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VpcId **   <a name="securityhub-Type-AwsRdsDbSecurityGroupDetails-VpcId"></a>
Provides VPC ID associated with the DB security group.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsRdsDbSecurityGroupDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRdsDbSecurityGroupDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRdsDbSecurityGroupDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRdsDbSecurityGroupDetails)
