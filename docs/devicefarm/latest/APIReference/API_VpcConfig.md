---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_VpcConfig.html
---

# VpcConfig
<a name="API_VpcConfig"></a>

Contains the VPC configuration data necessary to interface with AWS Device Farm's services.

## Contents
<a name="API_VpcConfig_Contents"></a>

 ** securityGroupIds **   <a name="devicefarm-Type-VpcConfig-securityGroupIds"></a>
An array of one or more security groups IDs in your Amazon VPC.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^sg-[0-9a-fA-F]{8,}$`
Required: Yes

 ** subnetIds **   <a name="devicefarm-Type-VpcConfig-subnetIds"></a>
An array of one or more subnet IDs in your Amazon VPC.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^subnet-[0-9a-fA-F]{8,}$`
Required: Yes

 ** vpcId **   <a name="devicefarm-Type-VpcConfig-vpcId"></a>
The ID of the Amazon VPC.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_VpcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/VpcConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/VpcConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/VpcConfig)
