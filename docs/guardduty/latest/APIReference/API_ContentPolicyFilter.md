---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ContentPolicyFilter.html
---

# ContentPolicyFilter
<a name="API_ContentPolicyFilter"></a>

Contains information about a content policy filter that matched during a guardrail evaluation.

## Contents
<a name="API_ContentPolicyFilter_Contents"></a>

 ** action **   <a name="guardduty-Type-ContentPolicyFilter-action"></a>
The action taken by the guardrail filter.
Type: String
Valid Values: `BLOCKED | NONE`
Required: No

 ** confidence **   <a name="guardduty-Type-ContentPolicyFilter-confidence"></a>
The confidence level that the content matched the filter.
Type: String
Valid Values: `HIGH | MEDIUM | LOW | NONE`
Required: No

 ** type **   <a name="guardduty-Type-ContentPolicyFilter-type"></a>
The type of content that was filtered by the guardrail.
Type: String
Valid Values: `PROMPT_ATTACK | JAILBREAK | HATE | INSULTS | SEXUAL | VIOLENCE | MISCONDUCT`
Required: No

## See Also
<a name="API_ContentPolicyFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ContentPolicyFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ContentPolicyFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ContentPolicyFilter)
