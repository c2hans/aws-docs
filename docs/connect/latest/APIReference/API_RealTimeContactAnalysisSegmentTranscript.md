---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RealTimeContactAnalysisSegmentTranscript.html
---

# RealTimeContactAnalysisSegmentTranscript
<a name="API_RealTimeContactAnalysisSegmentTranscript"></a>

The analyzed transcript segment.

## Contents
<a name="API_RealTimeContactAnalysisSegmentTranscript_Contents"></a>

 ** Content **   <a name="connect-Type-RealTimeContactAnalysisSegmentTranscript-Content"></a>
The content of the transcript. Can be redacted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Required: Yes

 ** Id **   <a name="connect-Type-RealTimeContactAnalysisSegmentTranscript-Id"></a>
The identifier of the transcript.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** ParticipantId **   <a name="connect-Type-RealTimeContactAnalysisSegmentTranscript-ParticipantId"></a>
The identifier of the participant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** ParticipantRole **   <a name="connect-Type-RealTimeContactAnalysisSegmentTranscript-ParticipantRole"></a>
The role of the participant. For example, is it a customer, agent, or system.
Type: String
Valid Values: `AGENT | CUSTOMER | SYSTEM | CUSTOM_BOT | SUPERVISOR`
Required: Yes

 ** Time **   <a name="connect-Type-RealTimeContactAnalysisSegmentTranscript-Time"></a>
Field describing the time of the event. It can have different representations of time.
Type: [RealTimeContactAnalysisTimeData](API_RealTimeContactAnalysisTimeData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** ContentType **   <a name="connect-Type-RealTimeContactAnalysisSegmentTranscript-ContentType"></a>
The type of content of the item. For example, `text/plain`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** DisplayName **   <a name="connect-Type-RealTimeContactAnalysisSegmentTranscript-DisplayName"></a>
The display name of the participant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Redaction **   <a name="connect-Type-RealTimeContactAnalysisSegmentTranscript-Redaction"></a>
Object describing redaction that was applied to the transcript. If transcript has the field it means part of the transcript was redacted.
Type: [RealTimeContactAnalysisTranscriptItemRedaction](API_RealTimeContactAnalysisTranscriptItemRedaction.md) object
Required: No

 ** Sentiment **   <a name="connect-Type-RealTimeContactAnalysisSegmentTranscript-Sentiment"></a>
The sentiment detected for this piece of transcript.
Type: String
Valid Values: `POSITIVE | NEGATIVE | NEUTRAL`
Required: No

## See Also
<a name="API_RealTimeContactAnalysisSegmentTranscript_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RealTimeContactAnalysisSegmentTranscript)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RealTimeContactAnalysisSegmentTranscript)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RealTimeContactAnalysisSegmentTranscript)
