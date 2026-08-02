---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_NetworkConfiguration.html
---

# NetworkConfiguration
<a name="API_NetworkConfiguration"></a>

The network configuration for customer VPC connectivity.

## Contents
<a name="API_NetworkConfiguration_Contents"></a>

 ** securityGroupIds **   <a name="emrserverless-Type-NetworkConfiguration-securityGroupIds"></a>
The array of security group Ids for customer VPC connectivity.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[-0-9a-zA-Z]+.*`
Required: No

 ** subnetIds **   <a name="emrserverless-Type-NetworkConfiguration-subnetIds"></a>
The array of subnet Ids for customer VPC connectivity.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 16 items.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[-0-9a-zA-Z]+.*`
Required: No

## See Also
<a name="API_NetworkConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/NetworkConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/NetworkConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/NetworkConfiguration)
