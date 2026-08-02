---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_DataDetails.html
---

# DataDetails
<a name="API_amazon-q-connect_DataDetails"></a>

Details about the data.

## Contents
<a name="API_amazon-q-connect_DataDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** caseSummarizationChunkData **   <a name="connect-Type-amazon-q-connect_DataDetails-caseSummarizationChunkData"></a>
Details about case summarization chunk data.
Type: [CaseSummarizationChunkDataDetails](API_amazon-q-connect_CaseSummarizationChunkDataDetails.md) object
Required: No

 ** contentData **   <a name="connect-Type-amazon-q-connect_DataDetails-contentData"></a>
Details about the content data.
Type: [ContentDataDetails](API_amazon-q-connect_ContentDataDetails.md) object
Required: No

 ** emailGenerativeAnswerChunkData **   <a name="connect-Type-amazon-q-connect_DataDetails-emailGenerativeAnswerChunkData"></a>
Streaming chunk data for email generative answers containing partial knowledge-based response content.
Type: [EmailGenerativeAnswerChunkDataDetails](API_amazon-q-connect_EmailGenerativeAnswerChunkDataDetails.md) object
Required: No

 ** emailOverviewChunkData **   <a name="connect-Type-amazon-q-connect_DataDetails-emailOverviewChunkData"></a>
Streaming chunk data for email overview containing partial overview content.
Type: [EmailOverviewChunkDataDetails](API_amazon-q-connect_EmailOverviewChunkDataDetails.md) object
Required: No

 ** emailResponseChunkData **   <a name="connect-Type-amazon-q-connect_DataDetails-emailResponseChunkData"></a>
Streaming chunk data for email response generation containing partial response content.
Type: [EmailResponseChunkDataDetails](API_amazon-q-connect_EmailResponseChunkDataDetails.md) object
Required: No

 ** generativeChunkData **   <a name="connect-Type-amazon-q-connect_DataDetails-generativeChunkData"></a>
Details about the generative chunk data.
Type: [GenerativeChunkDataDetails](API_amazon-q-connect_GenerativeChunkDataDetails.md) object
Required: No

 ** generativeData **   <a name="connect-Type-amazon-q-connect_DataDetails-generativeData"></a>
 Details about the generative data.
Type: [GenerativeDataDetails](API_amazon-q-connect_GenerativeDataDetails.md) object
Required: No

 ** intentDetectedData **   <a name="connect-Type-amazon-q-connect_DataDetails-intentDetectedData"></a>
Details about the intent data.
Type: [IntentDetectedDataDetails](API_amazon-q-connect_IntentDetectedDataDetails.md) object
Required: No

 ** notesChunkData **   <a name="connect-Type-amazon-q-connect_DataDetails-notesChunkData"></a>
Details about notes chunk data.
Type: [NotesChunkDataDetails](API_amazon-q-connect_NotesChunkDataDetails.md) object
Required: No

 ** notesData **   <a name="connect-Type-amazon-q-connect_DataDetails-notesData"></a>
Details about notes data.
Type: [NotesDataDetails](API_amazon-q-connect_NotesDataDetails.md) object
Required: No

 ** sourceContentData **   <a name="connect-Type-amazon-q-connect_DataDetails-sourceContentData"></a>
Details about the content data.
Type: [SourceContentDataDetails](API_amazon-q-connect_SourceContentDataDetails.md) object
Required: No

 ** suggestedMessageData **   <a name="connect-Type-amazon-q-connect_DataDetails-suggestedMessageData"></a>
Details about suggested message data.
Type: [SuggestedMessageDataDetails](API_amazon-q-connect_SuggestedMessageDataDetails.md) object
Required: No

## See Also
<a name="API_amazon-q-connect_DataDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/DataDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/DataDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/DataDetails)
