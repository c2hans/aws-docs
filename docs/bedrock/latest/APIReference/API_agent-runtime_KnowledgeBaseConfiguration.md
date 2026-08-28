---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_KnowledgeBaseConfiguration.html
---

# KnowledgeBaseConfiguration
<a name="API_agent-runtime_KnowledgeBaseConfiguration"></a>

Configurations to apply to a knowledge base attached to the agent during query. For more information, see [Knowledge base retrieval configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-session-state.html#session-state-kb).

## Contents
<a name="API_agent-runtime_KnowledgeBaseConfiguration_Contents"></a>

 ** knowledgeBaseId **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseConfiguration-knowledgeBaseId"></a>
The unique identifier for a knowledge base attached to the agent.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10.
Pattern: `[0-9a-zA-Z]+`
Required: Yes

 ** retrievalConfiguration **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseConfiguration-retrievalConfiguration"></a>
The configurations to apply to the knowledge base during query. For more information, see [Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html).
Type: [KnowledgeBaseRetrievalConfiguration](API_agent-runtime_KnowledgeBaseRetrievalConfiguration.md) object
Required: Yes

## See Also
<a name="API_agent-runtime_KnowledgeBaseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/KnowledgeBaseConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/KnowledgeBaseConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/KnowledgeBaseConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
