---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_GuardrailTextBlock.html
---

# GuardrailTextBlock
<a name="API_runtime_GuardrailTextBlock"></a>

The text block to be evaluated by the guardrail.

## Contents
<a name="API_runtime_GuardrailTextBlock_Contents"></a>

 ** text **   <a name="bedrock-Type-runtime_GuardrailTextBlock-text"></a>
The input text details to be evaluated by the guardrail.
Type: String
Required: Yes

 ** qualifiers **   <a name="bedrock-Type-runtime_GuardrailTextBlock-qualifiers"></a>
The qualifiers describing the text block.
Type: Array of strings
Valid Values: `grounding_source | query | guard_content`
Required: No

## See Also
<a name="API_runtime_GuardrailTextBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailTextBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailTextBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailTextBlock)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
