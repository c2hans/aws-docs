---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RealTimeContactAnalysisSegmentAttachments.html
---

# RealTimeContactAnalysisSegmentAttachments
<a name="API_RealTimeContactAnalysisSegmentAttachments"></a>

Segment containing list of attachments.

## Contents
<a name="API_RealTimeContactAnalysisSegmentAttachments_Contents"></a>

 ** Attachments **   <a name="connect-Type-RealTimeContactAnalysisSegmentAttachments-Attachments"></a>
List of objects describing an individual attachment.
Type: Array of [RealTimeContactAnalysisAttachment](API_RealTimeContactAnalysisAttachment.md) objects
Array Members: Maximum number of 10 items.
Required: Yes

 ** Id **   <a name="connect-Type-RealTimeContactAnalysisSegmentAttachments-Id"></a>
The identifier of the segment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** ParticipantId **   <a name="connect-Type-RealTimeContactAnalysisSegmentAttachments-ParticipantId"></a>
The identifier of the participant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** ParticipantRole **   <a name="connect-Type-RealTimeContactAnalysisSegmentAttachments-ParticipantRole"></a>
The role of the participant. For example, is it a customer, agent, or system.
Type: String
Valid Values: `AGENT | CUSTOMER | SYSTEM | CUSTOM_BOT | SUPERVISOR`
Required: Yes

 ** Time **   <a name="connect-Type-RealTimeContactAnalysisSegmentAttachments-Time"></a>
Field describing the time of the event. It can have different representations of time.
Type: [RealTimeContactAnalysisTimeData](API_RealTimeContactAnalysisTimeData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** DisplayName **   <a name="connect-Type-RealTimeContactAnalysisSegmentAttachments-DisplayName"></a>
The display name of the participant. Can be redacted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_RealTimeContactAnalysisSegmentAttachments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RealTimeContactAnalysisSegmentAttachments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RealTimeContactAnalysisSegmentAttachments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RealTimeContactAnalysisSegmentAttachments)
