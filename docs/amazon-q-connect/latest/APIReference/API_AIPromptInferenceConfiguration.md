---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_AIPromptInferenceConfiguration.html
---

# AIPromptInferenceConfiguration
<a name="API_amazon-q-connect_AIPromptInferenceConfiguration"></a>

The configuration for inference parameters when using AI Prompts.

## Contents
<a name="API_amazon-q-connect_AIPromptInferenceConfiguration_Contents"></a>

 ** maxTokensToSample **   <a name="connect-Type-amazon-q-connect_AIPromptInferenceConfiguration-maxTokensToSample"></a>
The maximum number of tokens to generate in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 4096.
Required: No

 ** temperature **   <a name="connect-Type-amazon-q-connect_AIPromptInferenceConfiguration-temperature"></a>
The temperature setting for controlling randomness in the generated response.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** topK **   <a name="connect-Type-amazon-q-connect_AIPromptInferenceConfiguration-topK"></a>
The top-K sampling parameter for token selection.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 200.
Required: No

 ** topP **   <a name="connect-Type-amazon-q-connect_AIPromptInferenceConfiguration-topP"></a>
The top-P sampling parameter for nucleus sampling.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

## See Also
<a name="API_amazon-q-connect_AIPromptInferenceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/AIPromptInferenceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/AIPromptInferenceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/AIPromptInferenceConfiguration)
