---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_KnowledgeBaseLookupOutput.html
---

# KnowledgeBaseLookupOutput
<a name="API_agent-runtime_KnowledgeBaseLookupOutput"></a>

Contains details about the results from looking up the knowledge base.

## Contents
<a name="API_agent-runtime_KnowledgeBaseLookupOutput_Contents"></a>

 ** metadata **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseLookupOutput-metadata"></a>
Contains information about the knowledge base output.
Type: [Metadata](API_agent-runtime_Metadata.md) object
Required: No

 ** retrievedReferences **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseLookupOutput-retrievedReferences"></a>
Contains metadata about the sources cited for the generated response.
Type: Array of [RetrievedReference](API_agent-runtime_RetrievedReference.md) objects
Required: No

## See Also
<a name="API_agent-runtime_KnowledgeBaseLookupOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/KnowledgeBaseLookupOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/KnowledgeBaseLookupOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/KnowledgeBaseLookupOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
