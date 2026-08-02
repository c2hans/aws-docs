---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_VectorIngestionConfiguration.html
---

# VectorIngestionConfiguration
<a name="API_amazon-q-connect_VectorIngestionConfiguration"></a>

Contains details about how to ingest the documents in a data source.

## Contents
<a name="API_amazon-q-connect_VectorIngestionConfiguration_Contents"></a>

 ** chunkingConfiguration **   <a name="connect-Type-amazon-q-connect_VectorIngestionConfiguration-chunkingConfiguration"></a>
Details about how to chunk the documents in the data source. A chunk refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried.
Type: [ChunkingConfiguration](API_amazon-q-connect_ChunkingConfiguration.md) object
Required: No

 ** parsingConfiguration **   <a name="connect-Type-amazon-q-connect_VectorIngestionConfiguration-parsingConfiguration"></a>
A custom parser for data source documents.
Type: [ParsingConfiguration](API_amazon-q-connect_ParsingConfiguration.md) object
Required: No

## See Also
<a name="API_amazon-q-connect_VectorIngestionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/VectorIngestionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/VectorIngestionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/VectorIngestionConfiguration)
