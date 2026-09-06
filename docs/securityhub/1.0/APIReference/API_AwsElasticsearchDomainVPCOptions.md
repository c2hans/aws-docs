---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsElasticsearchDomainVPCOptions.html
---

# AwsElasticsearchDomainVPCOptions
<a name="API_AwsElasticsearchDomainVPCOptions"></a>

Information that OpenSearch derives based on `VPCOptions` for the domain.

## Contents
<a name="API_AwsElasticsearchDomainVPCOptions_Contents"></a>

 ** AvailabilityZones **   <a name="securityhub-Type-AwsElasticsearchDomainVPCOptions-AvailabilityZones"></a>
The list of Availability Zones associated with the VPC subnets.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** SecurityGroupIds **   <a name="securityhub-Type-AwsElasticsearchDomainVPCOptions-SecurityGroupIds"></a>
The list of security group IDs associated with the VPC endpoints for the domain.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** SubnetIds **   <a name="securityhub-Type-AwsElasticsearchDomainVPCOptions-SubnetIds"></a>
A list of subnet IDs associated with the VPC endpoints for the domain.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** VPCId **   <a name="securityhub-Type-AwsElasticsearchDomainVPCOptions-VPCId"></a>
ID for the VPC.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsElasticsearchDomainVPCOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsElasticsearchDomainVPCOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsElasticsearchDomainVPCOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsElasticsearchDomainVPCOptions)
