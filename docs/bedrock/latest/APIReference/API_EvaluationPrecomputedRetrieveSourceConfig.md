---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_EvaluationPrecomputedRetrieveSourceConfig.html
---

# EvaluationPrecomputedRetrieveSourceConfig
<a name="API_EvaluationPrecomputedRetrieveSourceConfig"></a>

A summary of a RAG source used for a retrieve-only Knowledge Base evaluation job where you provide your own inference response data.

## Contents
<a name="API_EvaluationPrecomputedRetrieveSourceConfig_Contents"></a>

 ** ragSourceIdentifier **   <a name="bedrock-Type-EvaluationPrecomputedRetrieveSourceConfig-ragSourceIdentifier"></a>
A label that identifies the RAG source used for a retrieve-only Knowledge Base evaluation job where you provide your own inference response data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9._-]){0,255}`
Required: Yes

## See Also
<a name="API_EvaluationPrecomputedRetrieveSourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/EvaluationPrecomputedRetrieveSourceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/EvaluationPrecomputedRetrieveSourceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/EvaluationPrecomputedRetrieveSourceConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
