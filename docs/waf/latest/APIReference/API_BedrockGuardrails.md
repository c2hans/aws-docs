---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_BedrockGuardrails.html
---

# BedrockGuardrails

Specifies whether the AI security managed rule group, `AWSManagedRulesAISecurityRuleSet`, uses Amazon Bedrock Guardrails to inspect web requests, or web requests and responses.

Specify exactly one of the following settings: `Disable`, `ProtectRequestOnly`, or `ProtectRequestAndResponse`.

## Contents
<a name="API_BedrockGuardrails_Contents"></a>

 ** Disable **   <a name="WAF-Type-BedrockGuardrails-Disable"></a>
Turns off the use of Amazon Bedrock Guardrails. The rule group continues to run its own inspections.
JSON specification: `"Disable": {}`
Type: [DisableBedrockGuardrails](API_DisableBedrockGuardrails.md) object
Required: No

 ** ProtectRequestAndResponse **   <a name="WAF-Type-BedrockGuardrails-ProtectRequestAndResponse"></a>
Uses Amazon Bedrock Guardrails to inspect web requests and the responses to them.
Type: [BedrockGuardrailsRequestAndResponse](API_BedrockGuardrailsRequestAndResponse.md) object
Required: No

 ** ProtectRequestOnly **   <a name="WAF-Type-BedrockGuardrails-ProtectRequestOnly"></a>
Uses Amazon Bedrock Guardrails to inspect web requests.
Type: [BedrockGuardrailsRequestOnly](API_BedrockGuardrailsRequestOnly.md) object
Required: No

## See Also
<a name="API_BedrockGuardrails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/BedrockGuardrails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/BedrockGuardrails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/BedrockGuardrails)
