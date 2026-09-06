---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveMemoryRetrievalConfig.html
---

# AgenticRetrieveMemoryRetrievalConfig
<a name="API_agent-runtime_AgenticRetrieveMemoryRetrievalConfig"></a>

The long-term memory namespace that the agent might retrieve memory records from, and the filters applied to that retrieval. You must specify either namespace or namespacePath.

## Contents
<a name="API_agent-runtime_AgenticRetrieveMemoryRetrievalConfig_Contents"></a>

 ** metadataFilters **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemoryRetrievalConfig-metadataFilters"></a>
The metadata filter expressions that restrict retrieval to matching memory records. You can specify a maximum of 5 expressions.
Type: Array of [AgenticRetrieveMemoryMetadataFilter](API_agent-runtime_AgenticRetrieveMemoryMetadataFilter.md) objects
Required: No

 ** namespace **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemoryRetrievalConfig-namespace"></a>
The namespace prefix to filter memory records by. The agent retrieves memory records in namespaces that start with the provided prefix. You must specify either namespace or namespacePath.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9/*][a-zA-Z0-9\-_/*]*(?::[a-zA-Z0-9\-_/*]+)*[a-zA-Z0-9\-_/*]*`
Required: No

 ** namespacePath **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemoryRetrievalConfig-namespacePath"></a>
The parent namespace to use for hierarchical retrievals. The agent retrieves all memory records whose namespace falls under the same parent hierarchy. You must specify either namespace or namespacePath.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9/*][a-zA-Z0-9\-_/*]*(?::[a-zA-Z0-9\-_/*]+)*[a-zA-Z0-9\-_/*]*`
Required: No

 ** strategyId **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemoryRetrievalConfig-strategyId"></a>
The extraction strategy ID that restricts retrieval to memory records produced by a single strategy. Omit this parameter to retrieve records from every strategy on the memory resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9\-_]*`
Required: No

## See Also
<a name="API_agent-runtime_AgenticRetrieveMemoryRetrievalConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMemoryRetrievalConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMemoryRetrievalConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMemoryRetrievalConfig)
