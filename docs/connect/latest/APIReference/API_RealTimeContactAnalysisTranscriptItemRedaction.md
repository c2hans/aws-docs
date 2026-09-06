---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RealTimeContactAnalysisTranscriptItemRedaction.html
---

# RealTimeContactAnalysisTranscriptItemRedaction
<a name="API_RealTimeContactAnalysisTranscriptItemRedaction"></a>

Object describing redaction applied to the segment.

## Contents
<a name="API_RealTimeContactAnalysisTranscriptItemRedaction_Contents"></a>

 ** CharacterOffsets **   <a name="connect-Type-RealTimeContactAnalysisTranscriptItemRedaction-CharacterOffsets"></a>
List of character intervals each describing a part of the text that was redacted. For `OutputType.Raw`, part of the original text that contains data that can be redacted. For ` OutputType.Redacted`, part of the string with redaction tag.
Type: Array of [RealTimeContactAnalysisCharacterInterval](API_RealTimeContactAnalysisCharacterInterval.md) objects
Required: No

## See Also
<a name="API_RealTimeContactAnalysisTranscriptItemRedaction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RealTimeContactAnalysisTranscriptItemRedaction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RealTimeContactAnalysisTranscriptItemRedaction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RealTimeContactAnalysisTranscriptItemRedaction)
