---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_AttendeeFeatures.html
---

# AttendeeFeatures
<a name="API_meeting-chime_AttendeeFeatures"></a>

Lists the maximum number of attendees allowed into the meeting.

**Note**
If you specify `FHD` for `MeetingFeatures:Video:MaxResolution`, or if you specify `UHD` for `MeetingFeatures:Content:MaxResolution`, the maximum number of attendees changes from the default of `250` to `25`.

## Contents
<a name="API_meeting-chime_AttendeeFeatures_Contents"></a>

 ** MaxCount **   <a name="chimesdk-Type-meeting-chime_AttendeeFeatures-MaxCount"></a>
The maximum number of attendees allowed into the meeting.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 250.
Required: No

## See Also
<a name="API_meeting-chime_AttendeeFeatures_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-meetings-2021-07-15/AttendeeFeatures)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-meetings-2021-07-15/AttendeeFeatures)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-meetings-2021-07-15/AttendeeFeatures)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
