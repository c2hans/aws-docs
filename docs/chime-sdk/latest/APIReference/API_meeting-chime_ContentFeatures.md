---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_ContentFeatures.html
---

# ContentFeatures
<a name="API_meeting-chime_ContentFeatures"></a>

Lists the content (screen share) features for the meeting. Applies to all attendees.

**Note**
If you specify `MeetingFeatures:Content:MaxResolution:None` when you create a meeting, all API requests that include `SendReceive`, `Send`, or `Receive` for `AttendeeCapabilities:Content` will be rejected with `ValidationError 400`.

## Contents
<a name="API_meeting-chime_ContentFeatures_Contents"></a>

 ** MaxResolution **   <a name="chimesdk-Type-meeting-chime_ContentFeatures-MaxResolution"></a>
The maximum resolution for the meeting content.
Defaults to `FHD`. To use `UHD`, you must also provide a `MeetingFeatures:Attendee:MaxCount` value and override the default size limit of 250 attendees.
Type: String
Valid Values: `None | FHD | UHD`
Required: No

## See Also
<a name="API_meeting-chime_ContentFeatures_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-meetings-2021-07-15/ContentFeatures)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-meetings-2021-07-15/ContentFeatures)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-meetings-2021-07-15/ContentFeatures)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
