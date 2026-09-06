---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariantServerlessUpdateConfig.html
---

# ProductionVariantServerlessUpdateConfig
<a name="API_ProductionVariantServerlessUpdateConfig"></a>

Specifies the serverless update concurrency configuration for an endpoint variant.

## Contents
<a name="API_ProductionVariantServerlessUpdateConfig_Contents"></a>

 ** MaxConcurrency **   <a name="sagemaker-Type-ProductionVariantServerlessUpdateConfig-MaxConcurrency"></a>
The updated maximum number of concurrent invocations your serverless endpoint can process.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

 ** ProvisionedConcurrency **   <a name="sagemaker-Type-ProductionVariantServerlessUpdateConfig-ProvisionedConcurrency"></a>
The updated amount of provisioned concurrency to allocate for the serverless endpoint. Should be less than or equal to `MaxConcurrency`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

## See Also
<a name="API_ProductionVariantServerlessUpdateConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ProductionVariantServerlessUpdateConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ProductionVariantServerlessUpdateConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ProductionVariantServerlessUpdateConfig)
