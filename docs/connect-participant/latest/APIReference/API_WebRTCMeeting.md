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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
