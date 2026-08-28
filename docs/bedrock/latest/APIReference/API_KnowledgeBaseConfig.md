---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_KnowledgeBaseConfig.html
---

# KnowledgeBaseConfig
<a name="API_KnowledgeBaseConfig"></a>

The configuration details for retrieving information from a knowledge base and generating responses.

## Contents
<a name="API_KnowledgeBaseConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** retrieveAndGenerateConfig **   <a name="bedrock-Type-KnowledgeBaseConfig-retrieveAndGenerateConfig"></a>
Contains configuration details for retrieving information from a knowledge base and generating responses.
Type: [RetrieveAndGenerateConfiguration](API_RetrieveAndGenerateConfiguration.md) object
Required: No

 ** retrieveConfig **   <a name="bedrock-Type-KnowledgeBaseConfig-retrieveConfig"></a>
Contains configuration details for retrieving information from a knowledge base.
Type: [RetrieveConfig](API_RetrieveConfig.md) object
Required: No

## See Also
<a name="API_KnowledgeBaseConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/KnowledgeBaseConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/KnowledgeBaseConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/KnowledgeBaseConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
