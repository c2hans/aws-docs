---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_FixedSizeChunkingConfiguration.html
---

# FixedSizeChunkingConfiguration
<a name="API_amazon-q-connect_FixedSizeChunkingConfiguration"></a>

Configurations for when you choose fixed-size chunking. If you set the `chunkingStrategy` as `NONE`, exclude this field.

## Contents
<a name="API_amazon-q-connect_FixedSizeChunkingConfiguration_Contents"></a>

 ** maxTokens **   <a name="connect-Type-amazon-q-connect_FixedSizeChunkingConfiguration-maxTokens"></a>
The maximum number of tokens to include in a chunk.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** overlapPercentage **   <a name="connect-Type-amazon-q-connect_FixedSizeChunkingConfiguration-overlapPercentage"></a>
The percentage of overlap between adjacent chunks of a data source.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 99.
Required: Yes

## See Also
<a name="API_amazon-q-connect_FixedSizeChunkingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/FixedSizeChunkingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/FixedSizeChunkingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/FixedSizeChunkingConfiguration)
