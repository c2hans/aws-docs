---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ManagedSearchRerankingConfiguration.html
---

# ManagedSearchRerankingConfiguration
<a name="API_agent-runtime_ManagedSearchRerankingConfiguration"></a>

Configuration for the reranking model used in managed search.

## Contents
<a name="API_agent-runtime_ManagedSearchRerankingConfiguration_Contents"></a>

 ** type **   <a name="bedrock-Type-agent-runtime_ManagedSearchRerankingConfiguration-type"></a>
The type of reranking configuration.
Type: String
Valid Values: `BEDROCK_RERANKING_MODEL`
Required: Yes

 ** bedrockRerankingConfiguration **   <a name="bedrock-Type-agent-runtime_ManagedSearchRerankingConfiguration-bedrockRerankingConfiguration"></a>
The Bedrock reranking model configuration for managed search.
Type: [ManagedSearchBedrockRerankingConfiguration](API_agent-runtime_ManagedSearchBedrockRerankingConfiguration.md) object
Required: No

## See Also
<a name="API_agent-runtime_ManagedSearchRerankingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ManagedSearchRerankingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ManagedSearchRerankingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ManagedSearchRerankingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
