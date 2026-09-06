---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RealTimeContactAnalysisTranscriptItemWithCharacterOffsets.html
---

# RealTimeContactAnalysisTranscriptItemWithCharacterOffsets
<a name="API_RealTimeContactAnalysisTranscriptItemWithCharacterOffsets"></a>

Transcript representation containing Id and list of character intervals that are associated with analysis data. For example, this object within a `RealTimeContactAnalysisPointOfInterest` in `Category.MatchedDetails` would have character interval describing part of the text that matched category.

## Contents
<a name="API_RealTimeContactAnalysisTranscriptItemWithCharacterOffsets_Contents"></a>

 ** Id **   <a name="connect-Type-RealTimeContactAnalysisTranscriptItemWithCharacterOffsets-Id"></a>
Transcript identifier. Matches the identifier from one of the TranscriptSegments.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** CharacterOffsets **   <a name="connect-Type-RealTimeContactAnalysisTranscriptItemWithCharacterOffsets-CharacterOffsets"></a>
List of character intervals within transcript content/text.
Type: [RealTimeContactAnalysisCharacterInterval](API_RealTimeContactAnalysisCharacterInterval.md) object
Required: No

## See Also
<a name="API_RealTimeContactAnalysisTranscriptItemWithCharacterOffsets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RealTimeContactAnalysisTranscriptItemWithCharacterOffsets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RealTimeContactAnalysisTranscriptItemWithCharacterOffsets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RealTimeContactAnalysisTranscriptItemWithCharacterOffsets)
