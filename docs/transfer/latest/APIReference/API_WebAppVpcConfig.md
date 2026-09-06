---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_WebAppVpcConfig.html
---

# WebAppVpcConfig
<a name="API_WebAppVpcConfig"></a>

Contains the VPC configuration settings for hosting a web app endpoint, including the VPC ID, subnet IDs, and security group IDs for access control.

## Contents
<a name="API_WebAppVpcConfig_Contents"></a>

 ** IpAddressType **   <a name="TransferFamily-Type-WebAppVpcConfig-IpAddressType"></a>
The IP address type for the web app's VPC endpoint. This determines whether the endpoint is accessible over IPv4 only, or over both IPv4 and IPv6.
Type: String
Valid Values: `IPV4 | DUALSTACK`
Required: No

 ** SecurityGroupIds **   <a name="TransferFamily-Type-WebAppVpcConfig-SecurityGroupIds"></a>
The list of security group IDs that control access to the web app endpoint. These security groups determine which sources can access the endpoint based on IP addresses and port configurations.
Type: Array of strings
Length Constraints: Minimum length of 11. Maximum length of 20.
Pattern: `sg-[0-9a-f]{8,17}`
Required: No

 ** SubnetIds **   <a name="TransferFamily-Type-WebAppVpcConfig-SubnetIds"></a>
The list of subnet IDs within the VPC where the web app endpoint will be deployed. These subnets must be in the same VPC specified in the VpcId parameter.
Type: Array of strings
Required: No

 ** VpcId **   <a name="TransferFamily-Type-WebAppVpcConfig-VpcId"></a>
The identifier of the VPC where the web app endpoint will be hosted.
Type: String
Required: No

## See Also
<a name="API_WebAppVpcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/WebAppVpcConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/WebAppVpcConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/WebAppVpcConfig)
