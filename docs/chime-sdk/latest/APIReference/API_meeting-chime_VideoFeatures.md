---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_VideoFeatures.html
---

# VideoFeatures
<a name="API_meeting-chime_VideoFeatures"></a>

The video features set for the meeting. Applies to all attendees.

**Note**
If you specify `MeetingFeatures:Video:MaxResolution:None` when you create a meeting, all API requests that include `SendReceive`, `Send`, or `Receive` for `AttendeeCapabilities:Video` will be rejected with `ValidationError 400`.

## Contents
<a name="API_meeting-chime_VideoFeatures_Contents"></a>

 ** MaxResolution **   <a name="chimesdk-Type-meeting-chime_VideoFeatures-MaxResolution"></a>
The maximum video resolution for the meeting. Applies to all attendees.
Defaults to `HD`. To use `FHD`, you must also provide a `MeetingFeatures:Attendee:MaxCount` value and override the default size limit of 250 attendees.
Type: String
Valid Values: `None | HD | FHD`
Required: No

## See Also
<a name="API_meeting-chime_VideoFeatures_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-meetings-2021-07-15/VideoFeatures)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-meetings-2021-07-15/VideoFeatures)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-meetings-2021-07-15/VideoFeatures)
