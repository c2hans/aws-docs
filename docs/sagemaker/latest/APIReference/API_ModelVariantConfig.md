---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelVariantConfig.html
---

# ModelVariantConfig
<a name="API_ModelVariantConfig"></a>

Contains information about the deployment options of a model.

## Contents
<a name="API_ModelVariantConfig_Contents"></a>

 ** InfrastructureConfig **   <a name="sagemaker-Type-ModelVariantConfig-InfrastructureConfig"></a>
The configuration for the infrastructure that the model will be deployed to.
Type: [ModelInfrastructureConfig](API_ModelInfrastructureConfig.md) object
Required: Yes

 ** ModelName **   <a name="sagemaker-Type-ModelVariantConfig-ModelName"></a>
The name of the Amazon SageMaker Model entity.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: Yes

 ** VariantName **   <a name="sagemaker-Type-ModelVariantConfig-VariantName"></a>
The name of the variant.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: Yes

## See Also
<a name="API_ModelVariantConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelVariantConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelVariantConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelVariantConfig)
