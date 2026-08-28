---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_TextToSqlKnowledgeBaseConfiguration.html
---

# TextToSqlKnowledgeBaseConfiguration
<a name="API_agent-runtime_TextToSqlKnowledgeBaseConfiguration"></a>

Contains configurations for a knowledge base to use in transformation.

## Contents
<a name="API_agent-runtime_TextToSqlKnowledgeBaseConfiguration_Contents"></a>

 ** knowledgeBaseArn **   <a name="bedrock-Type-agent-runtime_TextToSqlKnowledgeBaseConfiguration-knowledgeBaseArn"></a>
The ARN of the knowledge base
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:knowledge-base/[0-9a-zA-Z]+`
Required: Yes

## See Also
<a name="API_agent-runtime_TextToSqlKnowledgeBaseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/TextToSqlKnowledgeBaseConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/TextToSqlKnowledgeBaseConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/TextToSqlKnowledgeBaseConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
