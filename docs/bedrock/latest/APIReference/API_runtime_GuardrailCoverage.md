---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_GuardrailCoverage.html
---

# GuardrailCoverage
<a name="API_runtime_GuardrailCoverage"></a>

The action of the guardrail coverage details.

## Contents
<a name="API_runtime_GuardrailCoverage_Contents"></a>

 ** images **   <a name="bedrock-Type-runtime_GuardrailCoverage-images"></a>
The guardrail coverage for images (the number of images that guardrails guarded).
Type: [GuardrailImageCoverage](API_runtime_GuardrailImageCoverage.md) object
Required: No

 ** textCharacters **   <a name="bedrock-Type-runtime_GuardrailCoverage-textCharacters"></a>
The text characters of the guardrail coverage details.
Type: [GuardrailTextCharactersCoverage](API_runtime_GuardrailTextCharactersCoverage.md) object
Required: No

## See Also
<a name="API_runtime_GuardrailCoverage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailCoverage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailCoverage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailCoverage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
