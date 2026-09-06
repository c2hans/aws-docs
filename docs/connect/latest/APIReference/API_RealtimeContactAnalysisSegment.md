---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RealtimeContactAnalysisSegment.html
---

# RealtimeContactAnalysisSegment
<a name="API_RealtimeContactAnalysisSegment"></a>

An analyzed segment for a real-time analysis session.

## Contents
<a name="API_RealtimeContactAnalysisSegment_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Attachments **   <a name="connect-Type-RealtimeContactAnalysisSegment-Attachments"></a>
The analyzed attachments.
Type: [RealTimeContactAnalysisSegmentAttachments](API_RealTimeContactAnalysisSegmentAttachments.md) object
Required: No

 ** Categories **   <a name="connect-Type-RealtimeContactAnalysisSegment-Categories"></a>
The matched category rules.
Type: [RealTimeContactAnalysisSegmentCategories](API_RealTimeContactAnalysisSegmentCategories.md) object
Required: No

 ** Event **   <a name="connect-Type-RealtimeContactAnalysisSegment-Event"></a>
Segment type describing a contact event.
Type: [RealTimeContactAnalysisSegmentEvent](API_RealTimeContactAnalysisSegmentEvent.md) object
Required: No

 ** ExtractedInformation **   <a name="connect-Type-RealtimeContactAnalysisSegment-ExtractedInformation"></a>
The extracted information from the conversation.
Type: [RealTimeContactAnalysisSegmentExtractedInformation](API_RealTimeContactAnalysisSegmentExtractedInformation.md) object
Required: No

 ** Issues **   <a name="connect-Type-RealtimeContactAnalysisSegment-Issues"></a>
Segment type containing a list of detected issues.
Type: [RealTimeContactAnalysisSegmentIssues](API_RealTimeContactAnalysisSegmentIssues.md) object
Required: No

 ** PostContactSummary **   <a name="connect-Type-RealtimeContactAnalysisSegment-PostContactSummary"></a>
Information about the post-contact summary.
Type: [RealTimeContactAnalysisSegmentPostContactSummary](API_RealTimeContactAnalysisSegmentPostContactSummary.md) object
Required: No

 ** Transcript **   <a name="connect-Type-RealtimeContactAnalysisSegment-Transcript"></a>
The analyzed transcript segment.
Type: [RealTimeContactAnalysisSegmentTranscript](API_RealTimeContactAnalysisSegmentTranscript.md) object
Required: No

## See Also
<a name="API_RealtimeContactAnalysisSegment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RealtimeContactAnalysisSegment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RealtimeContactAnalysisSegment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RealtimeContactAnalysisSegment)
