---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_VectorSearchBedrockRerankingModelConfiguration.html
---

# VectorSearchBedrockRerankingModelConfiguration
<a name="API_agent-runtime_VectorSearchBedrockRerankingModelConfiguration"></a>

Contains configurations for an Amazon Bedrock reranker model.

## Contents
<a name="API_agent-runtime_VectorSearchBedrockRerankingModelConfiguration_Contents"></a>

 ** modelArn **   <a name="bedrock-Type-agent-runtime_VectorSearchBedrockRerankingModelConfiguration-modelArn"></a>
The ARN of the reranker model to use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model/(.*))?`
Required: Yes

 ** additionalModelRequestFields **   <a name="bedrock-Type-agent-runtime_VectorSearchBedrockRerankingModelConfiguration-additionalModelRequestFields"></a>
A JSON object whose keys are request fields for the model and whose values are values for those fields.
Type: String to JSON value map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_agent-runtime_VectorSearchBedrockRerankingModelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/VectorSearchBedrockRerankingModelConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/VectorSearchBedrockRerankingModelConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/VectorSearchBedrockRerankingModelConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
