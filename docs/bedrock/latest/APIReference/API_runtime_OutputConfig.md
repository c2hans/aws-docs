---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_OutputConfig.html
---

# OutputConfig

Output configuration for a model response in a call to [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) or [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html).

## Contents
<a name="API_runtime_OutputConfig_Contents"></a>

 ** effort **   <a name="bedrock-Type-runtime_OutputConfig-effort"></a>
The effort level for the model to use when generating a response. Higher effort levels allow the model to spend more time reasoning before responding. Supported values are `low`, `medium`, `high`, `xhigh`, and `max`.
When extended thinking is disabled, the effort level is capped at `high`. Use effort `high` or below, or enable thinking to use higher effort levels.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16.
Required: No

 ** textFormat **   <a name="bedrock-Type-runtime_OutputConfig-textFormat"></a>
Structured output parameters to control the model's text response.
Type: [OutputFormat](API_runtime_OutputFormat.md) object
Required: No

## See Also
<a name="API_runtime_OutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/OutputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/OutputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/OutputConfig)
