---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_GenerativeChunkDataDetails.html
---

# GenerativeChunkDataDetails
<a name="API_amazon-q-connect_GenerativeChunkDataDetails"></a>

Details about the generative chunk data.

## Contents
<a name="API_amazon-q-connect_GenerativeChunkDataDetails_Contents"></a>

 ** completion **   <a name="connect-Type-amazon-q-connect_GenerativeChunkDataDetails-completion"></a>
A chunk of the LLM response.
Type: String
Required: No

 ** nextChunkToken **   <a name="connect-Type-amazon-q-connect_GenerativeChunkDataDetails-nextChunkToken"></a>
The token for the next set of chunks. Use the value returned in the previous response in the next request to retrieve the next set of chunks.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** references **   <a name="connect-Type-amazon-q-connect_GenerativeChunkDataDetails-references"></a>
The references used to generate the LLM response.
Type: Array of [DataSummary](API_amazon-q-connect_DataSummary.md) objects
Required: No

## See Also
<a name="API_amazon-q-connect_GenerativeChunkDataDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/GenerativeChunkDataDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/GenerativeChunkDataDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/GenerativeChunkDataDetails)
