---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailConfiguration.html
---

# GuardrailConfiguration
<a name="API_GuardrailConfiguration"></a>

The configuration details for the guardrail.

## Contents
<a name="API_GuardrailConfiguration_Contents"></a>

 ** guardrailId **   <a name="bedrock-Type-GuardrailConfiguration-guardrailId"></a>
The unique identifier for the guardrail.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** guardrailVersion **   <a name="bedrock-Type-GuardrailConfiguration-guardrailVersion"></a>
The version of the guardrail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `(([1-9][0-9]{0,7})|(DRAFT))`
Required: Yes

## See Also
<a name="API_GuardrailConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
