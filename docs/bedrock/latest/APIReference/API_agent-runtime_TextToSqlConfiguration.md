---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_TextToSqlConfiguration.html
---

# TextToSqlConfiguration
<a name="API_agent-runtime_TextToSqlConfiguration"></a>

Contains configurations for transforming text to SQL.

## Contents
<a name="API_agent-runtime_TextToSqlConfiguration_Contents"></a>

 ** type **   <a name="bedrock-Type-agent-runtime_TextToSqlConfiguration-type"></a>
The type of resource to use in transformation.
Type: String
Valid Values: `KNOWLEDGE_BASE`
Required: Yes

 ** knowledgeBaseConfiguration **   <a name="bedrock-Type-agent-runtime_TextToSqlConfiguration-knowledgeBaseConfiguration"></a>
Specifies configurations for a knowledge base to use in transformation.
Type: [TextToSqlKnowledgeBaseConfiguration](API_agent-runtime_TextToSqlKnowledgeBaseConfiguration.md) object
Required: No

## See Also
<a name="API_agent-runtime_TextToSqlConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/TextToSqlConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/TextToSqlConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/TextToSqlConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
