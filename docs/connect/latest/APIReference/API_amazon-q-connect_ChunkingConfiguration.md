---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_ChunkingConfiguration.html
---

# ChunkingConfiguration
<a name="API_amazon-q-connect_ChunkingConfiguration"></a>

Details about how to chunk the documents in the data source. A chunk refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried.

## Contents
<a name="API_amazon-q-connect_ChunkingConfiguration_Contents"></a>

 ** chunkingStrategy **   <a name="connect-Type-amazon-q-connect_ChunkingConfiguration-chunkingStrategy"></a>
Knowledge base can split your source data into chunks. A chunk refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried. You have the following options for chunking your data. If you opt for `NONE`, then you may want to pre-process your files by splitting them up such that each file corresponds to a chunk.
Type: String
Valid Values: `FIXED_SIZE | NONE | HIERARCHICAL | SEMANTIC`
Required: Yes

 ** fixedSizeChunkingConfiguration **   <a name="connect-Type-amazon-q-connect_ChunkingConfiguration-fixedSizeChunkingConfiguration"></a>
Configurations for when you choose fixed-size chunking. If you set the `chunkingStrategy` as `NONE`, exclude this field.
Type: [FixedSizeChunkingConfiguration](API_amazon-q-connect_FixedSizeChunkingConfiguration.md) object
Required: No

 ** hierarchicalChunkingConfiguration **   <a name="connect-Type-amazon-q-connect_ChunkingConfiguration-hierarchicalChunkingConfiguration"></a>
Settings for hierarchical document chunking for a data source. Hierarchical chunking splits documents into layers of chunks where the first layer contains large chunks, and the second layer contains smaller chunks derived from the first layer.
Type: [HierarchicalChunkingConfiguration](API_amazon-q-connect_HierarchicalChunkingConfiguration.md) object
Required: No

 ** semanticChunkingConfiguration **   <a name="connect-Type-amazon-q-connect_ChunkingConfiguration-semanticChunkingConfiguration"></a>
Settings for semantic document chunking for a data source. Semantic chunking splits a document into smaller documents based on groups of similar content derived from the text with natural language processing.
Type: [SemanticChunkingConfiguration](API_amazon-q-connect_SemanticChunkingConfiguration.md) object
Required: No

## See Also
<a name="API_amazon-q-connect_ChunkingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ChunkingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ChunkingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ChunkingConfiguration)
