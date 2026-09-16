---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ModelConfiguration.html
---

# ModelConfiguration
<a name="API_ModelConfiguration"></a>

Configuration for a model used in advanced prompt optimization.

## Contents
<a name="API_ModelConfiguration_Contents"></a>

 ** modelId **   <a name="bedrock-Type-ModelConfiguration-modelId"></a>
The model to use for optimization. The value depends on the resource that you use:
+ If you use a base model, specify the model ID or its ARN. For a list of model IDs, see [Models at a glance](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html) in the Amazon Bedrock User Guide.
+ If you use a cross-Region (system-defined) inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see [Supported Regions and models for inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html) in the Amazon Bedrock User Guide.
+ If you use an application inference profile, specify its full ARN, including the account ID and Region.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `(([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}(/[a-z0-9]{12}|))|(arn:aws(|-us-gov|-cn|-iso|-iso-b|-iso-f):bedrock:[a-z0-9-]{1,20}:[0-9]{12}:application-inference-profile/[a-zA-Z0-9-:.]+)|(arn:aws(|-us-gov|-cn|-iso|-iso-b|-iso-f):bedrock:[a-z0-9-]{1,20}:([0-9]{12})?:inference-profile/[a-zA-Z0-9-:.]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63})))`
Required: Yes

 ** additionalModelRequestFields **   <a name="bedrock-Type-ModelConfiguration-additionalModelRequestFields"></a>
Additional model-specific request fields.
Type: String to JSON value map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** inferenceConfig **   <a name="bedrock-Type-ModelConfiguration-inferenceConfig"></a>
The inference configuration for the model.
Type: [InferenceConfiguration](API_InferenceConfiguration.md) object
Required: No

## See Also
<a name="API_ModelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ModelConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ModelConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ModelConfiguration)
