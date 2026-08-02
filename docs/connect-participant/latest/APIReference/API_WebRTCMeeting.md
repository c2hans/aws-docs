---
source_url: https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_WebRTCMeeting.html
---

# WebRTCMeeting
<a name="API_connect-participant_WebRTCMeeting"></a>

A meeting created using the Amazon Chime SDK.

## Contents
<a name="API_connect-participant_WebRTCMeeting_Contents"></a>

 ** MediaPlacement **   <a name="connect-Type-connect-participant_WebRTCMeeting-MediaPlacement"></a>
The media placement for the meeting.
Type: [WebRTCMediaPlacement](API_connect-participant_WebRTCMediaPlacement.md) object
Required: No

 ** MeetingFeatures **   <a name="connect-Type-connect-participant_WebRTCMeeting-MeetingFeatures"></a>
The configuration settings of the features available to a meeting.
Type: [MeetingFeaturesConfiguration](API_connect-participant_MeetingFeaturesConfiguration.md) object
Required: No

 ** MeetingId **   <a name="connect-Type-connect-participant_WebRTCMeeting-MeetingId"></a>
The Amazon Chime SDK meeting ID.
Type: String
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: No

## See Also
<a name="API_connect-participant_WebRTCMeeting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectparticipant-2018-09-07/WebRTCMeeting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectparticipant-2018-09-07/WebRTCMeeting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectparticipant-2018-09-07/WebRTCMeeting)
