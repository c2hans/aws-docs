---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_HierarchicalChunkingConfiguration.html
---

# HierarchicalChunkingConfiguration
<a name="API_amazon-q-connect_HierarchicalChunkingConfiguration"></a>

Settings for hierarchical document chunking for a data source. Hierarchical chunking splits documents into layers of chunks where the first layer contains large chunks, and the second layer contains smaller chunks derived from the first layer.

## Contents
<a name="API_amazon-q-connect_HierarchicalChunkingConfiguration_Contents"></a>

 ** levelConfigurations **   <a name="connect-Type-amazon-q-connect_HierarchicalChunkingConfiguration-levelConfigurations"></a>
Token settings for each layer.
Type: Array of [HierarchicalChunkingLevelConfiguration](API_amazon-q-connect_HierarchicalChunkingLevelConfiguration.md) objects
Array Members: Fixed number of 2 items.
Required: Yes

 ** overlapTokens **   <a name="connect-Type-amazon-q-connect_HierarchicalChunkingConfiguration-overlapTokens"></a>
The number of tokens to repeat across chunks in the same layer.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

## See Also
<a name="API_amazon-q-connect_HierarchicalChunkingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/HierarchicalChunkingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/HierarchicalChunkingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/HierarchicalChunkingConfiguration)
