---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_SpanGuardrailAssessment.html
---

# SpanGuardrailAssessment
<a name="API_amazon-q-connect_SpanGuardrailAssessment"></a>

Result of a single guardrail assessment, covering either the input (customer/user message) or the output (LLM response) of a Bedrock Converse call.

## Contents
<a name="API_amazon-q-connect_SpanGuardrailAssessment_Contents"></a>

 ** action **   <a name="connect-Type-amazon-q-connect_SpanGuardrailAssessment-action"></a>
Outcome of the guardrail assessment.
Type: String
Valid Values: `NONE | BLOCKED | MASKED`
Required: Yes

 ** guardrailId **   <a name="connect-Type-amazon-q-connect_SpanGuardrailAssessment-guardrailId"></a>
Unique AI Guardrail identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** guardrailName **   <a name="connect-Type-amazon-q-connect_SpanGuardrailAssessment-guardrailName"></a>
Customer-defined display name of the AI Guardrail resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** source **   <a name="connect-Type-amazon-q-connect_SpanGuardrailAssessment-source"></a>
Content source the guardrail was evaluated against.
Type: String
Valid Values: `INPUT | OUTPUT`
Required: Yes

 ** policies **   <a name="connect-Type-amazon-q-connect_SpanGuardrailAssessment-policies"></a>
Per-policy assessment results. Absent or empty when action is NONE.
Type: Array of [GuardrailPolicyResult](API_amazon-q-connect_GuardrailPolicyResult.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_amazon-q-connect_SpanGuardrailAssessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/SpanGuardrailAssessment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/SpanGuardrailAssessment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/SpanGuardrailAssessment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
