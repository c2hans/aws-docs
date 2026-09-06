---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_UpdateWebAppVpcConfig.html
---

# UpdateWebAppVpcConfig
<a name="API_UpdateWebAppVpcConfig"></a>

Contains the VPC configuration settings for updating a web app endpoint, including the subnet IDs where the endpoint should be deployed.

## Contents
<a name="API_UpdateWebAppVpcConfig_Contents"></a>

 ** IpAddressType **   <a name="TransferFamily-Type-UpdateWebAppVpcConfig-IpAddressType"></a>
The IP address type for the web app's VPC endpoint. This determines whether the endpoint is accessible over IPv4 only, or over both IPv4 and IPv6.
Type: String
Valid Values: `IPV4 | DUALSTACK`
Required: No

 ** SubnetIds **   <a name="TransferFamily-Type-UpdateWebAppVpcConfig-SubnetIds"></a>
The list of subnet IDs within the VPC where the web app endpoint should be deployed during the update operation.
Type: Array of strings
Required: No

## See Also
<a name="API_UpdateWebAppVpcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/UpdateWebAppVpcConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/UpdateWebAppVpcConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/UpdateWebAppVpcConfig)
