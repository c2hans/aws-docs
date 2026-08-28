---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_VectorSearchBedrockRerankingModelConfiguration.html
---

# VectorSearchBedrockRerankingModelConfiguration
<a name="API_VectorSearchBedrockRerankingModelConfiguration"></a>

Configuration for the Amazon Bedrock foundation model used for reranking vector search results. This specifies which model to use and any additional parameters required by the model.

## Contents
<a name="API_VectorSearchBedrockRerankingModelConfiguration_Contents"></a>

 ** modelArn **   <a name="bedrock-Type-VectorSearchBedrockRerankingModelConfiguration-modelArn"></a>
The Amazon Resource Name (ARN) of the foundation model to use for reranking. This model processes the query and search results to determine a more relevant ordering.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model/(.*))?`
Required: Yes

 ** additionalModelRequestFields **   <a name="bedrock-Type-VectorSearchBedrockRerankingModelConfiguration-additionalModelRequestFields"></a>
A list of additional fields to include in the model request during reranking. These fields provide extra context or configuration options specific to the selected foundation model.
Type: String to JSON value map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_VectorSearchBedrockRerankingModelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/VectorSearchBedrockRerankingModelConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/VectorSearchBedrockRerankingModelConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/VectorSearchBedrockRerankingModelConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
