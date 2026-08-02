---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_VPCEConfiguration.html
---

# VPCEConfiguration
<a name="API_VPCEConfiguration"></a>

Represents an Amazon Virtual Private Cloud (VPC) endpoint configuration.

## Contents
<a name="API_VPCEConfiguration_Contents"></a>

 ** arn **   <a name="devicefarm-Type-VPCEConfiguration-arn"></a>
The Amazon Resource Name (ARN) of the VPC endpoint configuration.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** serviceDnsName **   <a name="devicefarm-Type-VPCEConfiguration-serviceDnsName"></a>
The DNS name that maps to the private IP address of the service you want to access.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** vpceConfigurationDescription **   <a name="devicefarm-Type-VPCEConfiguration-vpceConfigurationDescription"></a>
An optional description that provides details about your VPC endpoint configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** vpceConfigurationName **   <a name="devicefarm-Type-VPCEConfiguration-vpceConfigurationName"></a>
The friendly name you give to your VPC endpoint configuration to manage your configurations more easily.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** vpceServiceName **   <a name="devicefarm-Type-VPCEConfiguration-vpceServiceName"></a>
The name of the VPC endpoint service running in your AWS account that you want Device Farm to test.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## See Also
<a name="API_VPCEConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/VPCEConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/VPCEConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/VPCEConfiguration)
