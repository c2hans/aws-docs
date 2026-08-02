---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RealTimeContactAnalysisSegmentEvent.html
---

# RealTimeContactAnalysisSegmentEvent
<a name="API_RealTimeContactAnalysisSegmentEvent"></a>

Segment type describing a contact event.

## Contents
<a name="API_RealTimeContactAnalysisSegmentEvent_Contents"></a>

 ** EventType **   <a name="connect-Type-RealTimeContactAnalysisSegmentEvent-EventType"></a>
Type of the event. For example, `application/vnd.amazonaws.connect.event.participant.left`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Id **   <a name="connect-Type-RealTimeContactAnalysisSegmentEvent-Id"></a>
The identifier of the contact event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** Time **   <a name="connect-Type-RealTimeContactAnalysisSegmentEvent-Time"></a>
Field describing the time of the event. It can have different representations of time.
Type: [RealTimeContactAnalysisTimeData](API_RealTimeContactAnalysisTimeData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** DisplayName **   <a name="connect-Type-RealTimeContactAnalysisSegmentEvent-DisplayName"></a>
The display name of the participant. Can be redacted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ParticipantId **   <a name="connect-Type-RealTimeContactAnalysisSegmentEvent-ParticipantId"></a>
The identifier of the participant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ParticipantRole **   <a name="connect-Type-RealTimeContactAnalysisSegmentEvent-ParticipantRole"></a>
The role of the participant. For example, is it a customer, agent, or system.
Type: String
Valid Values: `AGENT | CUSTOMER | SYSTEM | CUSTOM_BOT | SUPERVISOR`
Required: No

## See Also
<a name="API_RealTimeContactAnalysisSegmentEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RealTimeContactAnalysisSegmentEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RealTimeContactAnalysisSegmentEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RealTimeContactAnalysisSegmentEvent)
