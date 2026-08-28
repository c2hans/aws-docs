---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_Attendee.html
---

# Attendee
<a name="API_meeting-chime_Attendee"></a>

An Amazon Chime SDK meeting attendee. Includes a unique `AttendeeId` and `JoinToken`. The `JoinToken` allows a client to authenticate and join as the specified attendee. The `JoinToken` expires when the meeting ends, or when [DeleteAttendee](API_meeting-chime_DeleteAttendee.md) is called. After that, the attendee is unable to join the meeting.

We recommend securely transferring each `JoinToken` from your server application to the client so that no other client has access to the token except for the one authorized to represent the attendee.

## Contents
<a name="API_meeting-chime_Attendee_Contents"></a>

 ** AttendeeId **   <a name="chimesdk-Type-meeting-chime_Attendee-AttendeeId"></a>
The Amazon Chime SDK attendee ID.
Type: String
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: No

 ** Capabilities **   <a name="chimesdk-Type-meeting-chime_Attendee-Capabilities"></a>
The capabilities assigned to an attendee: audio, video, or content.
You use the capabilities with a set of values that control what the capabilities can do, such as `SendReceive` data. For more information about those values, see [AttendeeCapabilities](API_meeting-chime_AttendeeCapabilities.md).
When using capabilities, be aware of these corner cases:
+ If you specify `MeetingFeatures:Video:MaxResolution:None` when you create a meeting, all API requests that include `SendReceive`, `Send`, or `Receive` for `AttendeeCapabilities:Video` will be rejected with `ValidationError 400`.
+ If you specify `MeetingFeatures:Content:MaxResolution:None` when you create a meeting, all API requests that include `SendReceive`, `Send`, or `Receive` for `AttendeeCapabilities:Content` will be rejected with `ValidationError 400`.
+ You can't set `content` capabilities to `SendReceive` or `Receive` unless you also set `video` capabilities to `SendReceive` or `Receive`. If you don't set the `video` capability to receive, the response will contain an HTTP 400 Bad Request status code. However, you can set your `video` capability to receive and you set your `content` capability to not receive.
+ If meeting features is defined as `Video:MaxResolution:None` but `Content:MaxResolution` is defined as something other than `None` and attendee capabilities are not defined in the API request, then the default attendee video capability is set to `Receive` and attendee content capability is set to `SendReceive`. This is because content `SendReceive` requires video to be at least `Receive`.
+ When you change an `audio` capability from `None` or `Receive` to `Send` or `SendReceive` , and if the attendee left their microphone unmuted, audio will flow from the attendee to the other meeting participants.
+ When you change a `video` or `content` capability from `None` or `Receive` to `Send` or `SendReceive` , and if the attendee turned on their video or content streams, remote attendees can receive those streams, but only after media renegotiation between the client and the Amazon Chime back-end server.
Type: [AttendeeCapabilities](API_meeting-chime_AttendeeCapabilities.md) object
Required: No

 ** ExternalUserId **   <a name="chimesdk-Type-meeting-chime_Attendee-ExternalUserId"></a>
The Amazon Chime SDK external user ID. An idempotency token. Links the attendee to an identity managed by a builder application.
Pattern: `[-_&@+=,(){}\[\]\/«».:|'"#a-zA-Z0-9À-ÿ\s]*`
Values that begin with `aws:` are reserved. You can't configure a value that uses this prefix. Case insensitive.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Required: No

 ** JoinToken **   <a name="chimesdk-Type-meeting-chime_Attendee-JoinToken"></a>
The join token used by the Amazon Chime SDK attendee.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 2048.
Required: No

## See Also
<a name="API_meeting-chime_Attendee_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-meetings-2021-07-15/Attendee)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-meetings-2021-07-15/Attendee)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-meetings-2021-07-15/Attendee)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
