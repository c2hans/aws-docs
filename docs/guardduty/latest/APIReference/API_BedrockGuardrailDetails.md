---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_BedrockGuardrailDetails.html
---

# BedrockGuardrailDetails
<a name="API_BedrockGuardrailDetails"></a>

Contains information about the Bedrock guardrail that was involved in a finding.

## Contents
<a name="API_BedrockGuardrailDetails_Contents"></a>

 ** contentPolicyFilters **   <a name="guardduty-Type-BedrockGuardrailDetails-contentPolicyFilters"></a>
The list of content policy filters that matched during the guardrail evaluation.
Type: Array of [ContentPolicyFilter](API_ContentPolicyFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** guardrailAction **   <a name="guardduty-Type-BedrockGuardrailDetails-guardrailAction"></a>
Indicates whether the guardrail intervened or not.
Type: String
Valid Values: `GUARDRAIL_INTERVENED | NONE`
Required: No

 ** guardrailArn **   <a name="guardduty-Type-BedrockGuardrailDetails-guardrailArn"></a>
The ARN of the Bedrock guardrail. This field is deprecated. Use the `guardrails` list instead.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+`
Required: No

 ** guardrails **   <a name="guardduty-Type-BedrockGuardrailDetails-guardrails"></a>
The list of Bedrock guardrails associated with the finding.
Type: Array of [BedrockGuardrail](API_BedrockGuardrail.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** guardrailSource **   <a name="guardduty-Type-BedrockGuardrailDetails-guardrailSource"></a>
Indicates whether the guardrail was applied on the input or output of the model invocation.
Type: String
Valid Values: `INPUT | OUTPUT`
Required: No

 ** guardrailVersion **   <a name="guardduty-Type-BedrockGuardrailDetails-guardrailVersion"></a>
The version of the Bedrock guardrail. This field is deprecated. Use the `guardrails` list instead.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8.
Pattern: `(([1-9][0-9]{0,7})|(DRAFT))`
Required: No

## See Also
<a name="API_BedrockGuardrailDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/BedrockGuardrailDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/BedrockGuardrailDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/BedrockGuardrailDetails)
