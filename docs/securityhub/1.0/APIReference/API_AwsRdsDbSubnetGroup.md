---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRdsDbSubnetGroup.html
---

# AwsRdsDbSubnetGroup
<a name="API_AwsRdsDbSubnetGroup"></a>

Information about the subnet group for the database instance.

## Contents
<a name="API_AwsRdsDbSubnetGroup_Contents"></a>

 ** DbSubnetGroupArn **   <a name="securityhub-Type-AwsRdsDbSubnetGroup-DbSubnetGroupArn"></a>
The ARN of the subnet group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DbSubnetGroupDescription **   <a name="securityhub-Type-AwsRdsDbSubnetGroup-DbSubnetGroupDescription"></a>
The description of the subnet group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DbSubnetGroupName **   <a name="securityhub-Type-AwsRdsDbSubnetGroup-DbSubnetGroupName"></a>
The name of the subnet group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SubnetGroupStatus **   <a name="securityhub-Type-AwsRdsDbSubnetGroup-SubnetGroupStatus"></a>
The status of the subnet group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Subnets **   <a name="securityhub-Type-AwsRdsDbSubnetGroup-Subnets"></a>
A list of subnets in the subnet group.
Type: Array of [AwsRdsDbSubnetGroupSubnet](API_AwsRdsDbSubnetGroupSubnet.md) objects
Required: No

 ** VpcId **   <a name="securityhub-Type-AwsRdsDbSubnetGroup-VpcId"></a>
The VPC ID of the subnet group.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsRdsDbSubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRdsDbSubnetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRdsDbSubnetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRdsDbSubnetGroup)
