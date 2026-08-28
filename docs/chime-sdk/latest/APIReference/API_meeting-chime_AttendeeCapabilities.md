---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_AttendeeCapabilities.html
---

# AttendeeCapabilities
<a name="API_meeting-chime_AttendeeCapabilities"></a>

The media capabilities of an attendee: audio, video, or content.

**Note**
You use the capabilities with a set of values that control what the capabilities can do, such as `SendReceive` data. For more information, refer to [AudioFeatures](API_meeting-chime_AudioFeatures.md) and [VideoFeatures](API_meeting-chime_VideoFeatures.md).

When using capabilities, be aware of these corner cases:
+ If you specify `MeetingFeatures:Video:MaxResolution:None` when you create a meeting, all API requests that include `SendReceive`, `Send`, or `Receive` for `AttendeeCapabilities:Video` will be rejected with `ValidationError 400`.
+ If you specify `MeetingFeatures:Content:MaxResolution:None` when you create a meeting, all API requests that include `SendReceive`, `Send`, or `Receive` for `AttendeeCapabilities:Content` will be rejected with `ValidationError 400`.
+ You can't set `content` capabilities to `SendReceive` or `Receive` unless you also set `video` capabilities to `SendReceive` or `Receive`. If you don't set the `video` capability to receive, the response will contain an HTTP 400 Bad Request status code. However, you can set your `video` capability to receive and you set your `content` capability to not receive.
+ If meeting features is defined as `Video:MaxResolution:None` but `Content:MaxResolution` is defined as something other than `None` and attendee capabilities are not defined in the API request, then the default attendee video capability is set to `Receive` and attendee content capability is set to `SendReceive`. This is because content `SendReceive` requires video to be at least `Receive`.
+ When you change an `audio` capability from `None` or `Receive` to `Send` or `SendReceive` , and an attendee unmutes their microphone, audio flows from the attendee to the other meeting participants.
+ When you change a `video` or `content` capability from `None` or `Receive` to `Send` or `SendReceive` , and the attendee turns on their video or content streams, remote attendees can receive those streams, but only after media renegotiation between the client and the Amazon Chime back-end server.

## Contents
<a name="API_meeting-chime_AttendeeCapabilities_Contents"></a>

 ** Audio **   <a name="chimesdk-Type-meeting-chime_AttendeeCapabilities-Audio"></a>
The audio capability assigned to an attendee.
Type: String
Valid Values: `SendReceive | Send | Receive | None`
Required: Yes

 ** Content **   <a name="chimesdk-Type-meeting-chime_AttendeeCapabilities-Content"></a>
The content capability assigned to an attendee.
Type: String
Valid Values: `SendReceive | Send | Receive | None`
Required: Yes

 ** Video **   <a name="chimesdk-Type-meeting-chime_AttendeeCapabilities-Video"></a>
The video capability assigned to an attendee.
Type: String
Valid Values: `SendReceive | Send | Receive | None`
Required: Yes

## See Also
<a name="API_meeting-chime_AttendeeCapabilities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-meetings-2021-07-15/AttendeeCapabilities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-meetings-2021-07-15/AttendeeCapabilities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-meetings-2021-07-15/AttendeeCapabilities)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
