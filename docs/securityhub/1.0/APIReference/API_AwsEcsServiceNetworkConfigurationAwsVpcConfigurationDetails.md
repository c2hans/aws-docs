---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetails.html
---

# AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetails
<a name="API_AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetails"></a>

For tasks that use the `awsvpc` networking mode, the VPC subnet and security group configuration.

## Contents
<a name="API_AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetails_Contents"></a>

 ** AssignPublicIp **   <a name="securityhub-Type-AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetails-AssignPublicIp"></a>
Whether the task's elastic network interface receives a public IP address. The default value is `DISABLED`.
Valid values: `ENABLED` \| `DISABLED`
Type: String
Pattern: `.*\S.*`
Required: No

 ** SecurityGroups **   <a name="securityhub-Type-AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetails-SecurityGroups"></a>
The IDs of the security groups associated with the task or service.
You can provide up to five security groups.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Subnets **   <a name="securityhub-Type-AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetails-Subnets"></a>
The IDs of the subnets associated with the task or service.
You can provide up to 16 subnets.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetails)
