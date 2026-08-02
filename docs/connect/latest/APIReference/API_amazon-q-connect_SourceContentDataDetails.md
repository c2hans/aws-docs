---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_SourceContentDataDetails.html
---

# SourceContentDataDetails
<a name="API_amazon-q-connect_SourceContentDataDetails"></a>

Details about the source content data.

## Contents
<a name="API_amazon-q-connect_SourceContentDataDetails_Contents"></a>

 ** id **   <a name="connect-Type-amazon-q-connect_SourceContentDataDetails-id"></a>
The identifier of the source content.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** rankingData **   <a name="connect-Type-amazon-q-connect_SourceContentDataDetails-rankingData"></a>
Details about the source content ranking data.
Type: [RankingData](API_amazon-q-connect_RankingData.md) object
Required: Yes

 ** textData **   <a name="connect-Type-amazon-q-connect_SourceContentDataDetails-textData"></a>
 Details about the source content text data.
Type: [TextData](API_amazon-q-connect_TextData.md) object
Required: Yes

 ** type **   <a name="connect-Type-amazon-q-connect_SourceContentDataDetails-type"></a>
The type of the source content.
Type: String
Valid Values: `KNOWLEDGE_CONTENT`
Required: Yes

 ** citationSpan **   <a name="connect-Type-amazon-q-connect_SourceContentDataDetails-citationSpan"></a>
Contains information about where the text with a citation begins and ends in the generated output.
Type: [CitationSpan](API_amazon-q-connect_CitationSpan.md) object
Required: No

## See Also
<a name="API_amazon-q-connect_SourceContentDataDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/SourceContentDataDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/SourceContentDataDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/SourceContentDataDetails)
