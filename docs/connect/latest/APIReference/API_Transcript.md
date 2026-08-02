---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Transcript.html
---

# Transcript
<a name="API_Transcript"></a>

A structure that defines search criteria and matching logic to search for contacts by matching text with transcripts analyzed by Connect Customer Contact Lens.

## Contents
<a name="API_Transcript_Contents"></a>

 ** Criteria **   <a name="connect-Type-Transcript-Criteria"></a>
The list of search criteria based on Contact Lens conversational analytics transcript.
Type: Array of [TranscriptCriteria](API_TranscriptCriteria.md) objects
Array Members: Minimum number of 0 items. Maximum number of 6 items.
Required: Yes

 ** MatchType **   <a name="connect-Type-Transcript-MatchType"></a>
The match type combining search criteria using multiple transcript criteria.
Type: String
Valid Values: `MATCH_ALL | MATCH_ANY | MATCH_EXACT | MATCH_NONE`
Required: No

## See Also
<a name="API_Transcript_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/Transcript)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/Transcript)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/Transcript)
