---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_QueryGenerationConfiguration.html
---

# QueryGenerationConfiguration
<a name="API_agent_QueryGenerationConfiguration"></a>

Contains configurations for query generation. For more information, see [Build a knowledge base by connecting to a structured data source](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build-structured.html) in the Amazon Bedrock User Guide..

## Contents
<a name="API_agent_QueryGenerationConfiguration_Contents"></a>

 ** executionTimeoutSeconds **   <a name="bedrock-Type-agent_QueryGenerationConfiguration-executionTimeoutSeconds"></a>
The time after which query generation will time out.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

 ** generationContext **   <a name="bedrock-Type-agent_QueryGenerationConfiguration-generationContext"></a>
Specifies configurations for context to use during query generation.
Type: [QueryGenerationContext](API_agent_QueryGenerationContext.md) object
Required: No

## See Also
<a name="API_agent_QueryGenerationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/QueryGenerationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/QueryGenerationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/QueryGenerationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
