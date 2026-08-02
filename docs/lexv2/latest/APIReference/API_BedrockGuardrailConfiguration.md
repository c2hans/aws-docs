---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_BedrockGuardrailConfiguration.html
---

# BedrockGuardrailConfiguration
<a name="API_BedrockGuardrailConfiguration"></a>

The details on the Bedrock guardrail configuration.

## Contents
<a name="API_BedrockGuardrailConfiguration_Contents"></a>

 ** identifier **   <a name="lexv2-Type-BedrockGuardrailConfiguration-identifier"></a>
The unique guardrail id for the Bedrock guardrail configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(([a-z0-9]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+))$`
Required: Yes

 ** version **   <a name="lexv2-Type-BedrockGuardrailConfiguration-version"></a>
The guardrail version for the Bedrock guardrail configuration.
Type: String
Pattern: `^(([1-9][0-9]{0,7})|(DRAFT))$`
Required: Yes

## See Also
<a name="API_BedrockGuardrailConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/BedrockGuardrailConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/BedrockGuardrailConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/BedrockGuardrailConfiguration)
