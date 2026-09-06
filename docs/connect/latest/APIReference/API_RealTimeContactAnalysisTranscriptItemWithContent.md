---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RealTimeContactAnalysisTranscriptItemWithContent.html
---

# RealTimeContactAnalysisTranscriptItemWithContent
<a name="API_RealTimeContactAnalysisTranscriptItemWithContent"></a>

Transcript representation containing Id, Content and list of character intervals that are associated with analysis data. For example, this object within an issue detected would describe both content that contains identified issue and intervals where that content is taken from.

## Contents
<a name="API_RealTimeContactAnalysisTranscriptItemWithContent_Contents"></a>

 ** Id **   <a name="connect-Type-RealTimeContactAnalysisTranscriptItemWithContent-Id"></a>
Transcript identifier. Matches the identifier from one of the TranscriptSegments.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** CharacterOffsets **   <a name="connect-Type-RealTimeContactAnalysisTranscriptItemWithContent-CharacterOffsets"></a>
Begin and end offsets for a part of text.
Type: [RealTimeContactAnalysisCharacterInterval](API_RealTimeContactAnalysisCharacterInterval.md) object
Required: No

 ** Content **   <a name="connect-Type-RealTimeContactAnalysisTranscriptItemWithContent-Content"></a>
Part of the transcript content that contains identified issue. Can be redacted
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Required: No

## See Also
<a name="API_RealTimeContactAnalysisTranscriptItemWithContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RealTimeContactAnalysisTranscriptItemWithContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RealTimeContactAnalysisTranscriptItemWithContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RealTimeContactAnalysisTranscriptItemWithContent)
