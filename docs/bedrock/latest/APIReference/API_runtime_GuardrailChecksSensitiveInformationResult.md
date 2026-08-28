---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_GuardrailChecksSensitiveInformationResult.html
---

# GuardrailChecksSensitiveInformationResult
<a name="API_runtime_GuardrailChecksSensitiveInformationResult"></a>

The sensitive information check results.

## Contents
<a name="API_runtime_GuardrailChecksSensitiveInformationResult_Contents"></a>

 ** results **   <a name="bedrock-Type-runtime_GuardrailChecksSensitiveInformationResult-results"></a>
The detected sensitive information entities.
Type: Array of [GuardrailChecksSensitiveInformationResultEntry](API_runtime_GuardrailChecksSensitiveInformationResultEntry.md) objects
Required: Yes

 ** truncated **   <a name="bedrock-Type-runtime_GuardrailChecksSensitiveInformationResult-truncated"></a>
Specifies whether the results were truncated because the number of detected entities exceeded the maximum limit.
Type: Boolean
Required: No

## See Also
<a name="API_runtime_GuardrailChecksSensitiveInformationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailChecksSensitiveInformationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailChecksSensitiveInformationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailChecksSensitiveInformationResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
