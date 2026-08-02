---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateAttendee.html
---

# CreateAttendee
<a name="API_meeting-chime_CreateAttendee"></a>

 Creates a new attendee for an active Amazon Chime SDK meeting. For more information about the Amazon Chime SDK, see [Using the Amazon Chime SDK](https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html) in the *Amazon Chime Developer Guide*.

## Request Syntax
<a name="API_meeting-chime_CreateAttendee_RequestSyntax"></a>

```
POST /meetings/{{MeetingId}}/attendees HTTP/1.1
Content-type: application/json

{
   "Capabilities": {
      "Audio": "{{string}}",
      "Content": "{{string}}",
      "Video": "{{string}}"
   },
   "ExternalUserId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_meeting-chime_CreateAttendee_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MeetingId](#API_meeting-chime_CreateAttendee_RequestSyntax) **   <a name="chimesdk-meeting-chime_CreateAttendee-request-uri-MeetingId"></a>
The unique ID of the meeting.
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: Yes

## Request Body
<a name="API_meeting-chime_CreateAttendee_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Capabilities](#API_meeting-chime_CreateAttendee_RequestSyntax) **   <a name="chimesdk-meeting-chime_CreateAttendee-request-Capabilities"></a>
The capabilities (`audio`, `video`, or `content`) that you want to grant an attendee. If you don't specify capabilities, all users have send and receive capabilities on all media channels by default.
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

 ** [ExternalUserId](#API_meeting-chime_CreateAttendee_RequestSyntax) **   <a name="chimesdk-meeting-chime_CreateAttendee-request-ExternalUserId"></a>
The Amazon Chime SDK external user ID. An idempotency token. Links the attendee to an identity managed by a builder application.
Pattern: `[-_&@+=,(){}\[\]\/«».:|'"#a-zA-Z0-9À-ÿ\s]*`
Values that begin with `aws:` are reserved. You can't configure a value that uses this prefix.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_meeting-chime_CreateAttendee_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Attendee": {
      "AttendeeId": "string",
      "Capabilities": {
         "Audio": "string",
         "Content": "string",
         "Video": "string"
      },
      "ExternalUserId": "string",
      "JoinToken": "string"
   }
}
```

## Response Elements
<a name="API_meeting-chime_CreateAttendee_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Attendee](#API_meeting-chime_CreateAttendee_ResponseSyntax) **   <a name="chimesdk-meeting-chime_CreateAttendee-response-Attendee"></a>
The attendee information, including attendee ID and join token.
Type: [Attendee](API_meeting-chime_Attendee.md) object

## Errors
<a name="API_meeting-chime_CreateAttendee_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
 ** RequestId **
The request id associated with the call responsible for the exception.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
 ** RequestId **
The request id associated with the call responsible for the exception.
HTTP Status Code: 403

 ** LimitExceededException **
The request exceeds the resource limit.
 ** RequestId **
The request id associated with the call responsible for the exception.
HTTP Status Code: 400

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 404

 ** ServiceFailureException **
The service encountered an unexpected error.
 ** RequestId **
The ID of the failed request.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
 ** RequestId **
The request id associated with the call responsible for the exception.
 ** RetryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 503

 ** ThrottlingException **
The number of customer requests exceeds the request rate limit.
 ** RequestId **
The ID of the request that exceeded the throttling limit.
HTTP Status Code: 429

 ** UnauthorizedException **
The user isn't authorized to request a resource.
 ** RequestId **
The request id associated with the call responsible for the exception.
HTTP Status Code: 401

 ** UnprocessableEntityException **
The request was well-formed but was unable to be followed due to semantic errors.
 ** RequestId **
The request id associated with the call responsible for the exception.
HTTP Status Code: 422

## See Also
<a name="API_meeting-chime_CreateAttendee_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-meetings-2021-07-15/CreateAttendee)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-meetings-2021-07-15/CreateAttendee)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-meetings-2021-07-15/CreateAttendee)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-meetings-2021-07-15/CreateAttendee)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-meetings-2021-07-15/CreateAttendee)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-meetings-2021-07-15/CreateAttendee)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-meetings-2021-07-15/CreateAttendee)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-meetings-2021-07-15/CreateAttendee)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-meetings-2021-07-15/CreateAttendee)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-meetings-2021-07-15/CreateAttendee)
