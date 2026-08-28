---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_GuardrailChecksContentFilterResultEntry.html
---

# GuardrailChecksContentFilterResultEntry
<a name="API_runtime_GuardrailChecksContentFilterResultEntry"></a>

The evaluation result for a single content filter category.

## Contents
<a name="API_runtime_GuardrailChecksContentFilterResultEntry_Contents"></a>

 ** category **   <a name="bedrock-Type-runtime_GuardrailChecksContentFilterResultEntry-category"></a>
The content filter category that was evaluated.
Type: String
Valid Values: `VIOLENCE | HATE | SEXUAL | MISCONDUCT | INSULTS`
Required: Yes

 ** severityScore **   <a name="bedrock-Type-runtime_GuardrailChecksContentFilterResultEntry-severityScore"></a>
The severity score for the category, ranging from 0.0 to 1.0. Higher values indicate greater severity.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 1.0.
Required: Yes

## See Also
<a name="API_runtime_GuardrailChecksContentFilterResultEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailChecksContentFilterResultEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailChecksContentFilterResultEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailChecksContentFilterResultEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
