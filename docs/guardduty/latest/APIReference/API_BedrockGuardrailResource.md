---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_BedrockGuardrailResource.html
---

# BedrockGuardrailResource
<a name="API_BedrockGuardrailResource"></a>

Contains details about an Amazon Bedrock guardrail evaluated during a model invocation.

## Contents
<a name="API_BedrockGuardrailResource_Contents"></a>

 ** guardrailAction **   <a name="guardduty-Type-BedrockGuardrailResource-guardrailAction"></a>
Indicates whether the guardrail intervened during the model invocation.
Type: String
Valid Values: `GUARDRAIL_INTERVENED | NONE`
Required: No

 ** guardrailSource **   <a name="guardduty-Type-BedrockGuardrailResource-guardrailSource"></a>
Indicates whether the guardrail was applied on the input or output of the model invocation.
Type: String
Valid Values: `INPUT | OUTPUT`
Required: No

 ** version **   <a name="guardduty-Type-BedrockGuardrailResource-version"></a>
The version of the Amazon Bedrock guardrail. Valid values are a numeric version, `DRAFT`, or `ENFORCED`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8.
Pattern: `(([1-9][0-9]{0,7})|(DRAFT)|(ENFORCED))`
Required: No

## See Also
<a name="API_BedrockGuardrailResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/BedrockGuardrailResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/BedrockGuardrailResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/BedrockGuardrailResource)
