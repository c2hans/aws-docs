---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_BatchUpdateAttendeeCapabilitiesExcept.html
---

# BatchUpdateAttendeeCapabilitiesExcept
<a name="API_meeting-chime_BatchUpdateAttendeeCapabilitiesExcept"></a>

Updates `AttendeeCapabilities` except the capabilities listed in an `ExcludedAttendeeIds` table.

**Note**
You use the capabilities with a set of values that control what the capabilities can do, such as `SendReceive` data. For more information about those values, see [AttendeeCapabilities](API_meeting-chime_AttendeeCapabilities.md).

When using capabilities, be aware of these corner cases:
+ If you specify `MeetingFeatures:Video:MaxResolution:None` when you create a meeting, all API requests that include `SendReceive`, `Send`, or `Receive` for `AttendeeCapabilities:Video` will be rejected with `ValidationError 400`.
+ If you specify `MeetingFeatures:Content:MaxResolution:None` when you create a meeting, all API requests that include `SendReceive`, `Send`, or `Receive` for `AttendeeCapabilities:Content` will be rejected with `ValidationError 400`.
+ You can't set `content` capabilities to `SendReceive` or `Receive` unless you also set `video` capabilities to `SendReceive` or `Receive`. If you don't set the `video` capability to receive, the response will contain an HTTP 400 Bad Request status code. However, you can set your `video` capability to receive and you set your `content` capability to not receive.
+ If meeting features is defined as `Video:MaxResolution:None` but `Content:MaxResolution` is defined as something other than `None` and attendee capabilities are not defined in the API request, then the default attendee video capability is set to `Receive` and attendee content capability is set to `SendReceive`. This is because content `SendReceive` requires video to be at least `Receive`.
+ When you change an `audio` capability from `None` or `Receive` to `Send` or `SendReceive` , and if the attendee left their microphone unmuted, audio will flow from the attendee to the other meeting participants.
+ When you change a `video` or `content` capability from `None` or `Receive` to `Send` or `SendReceive` , and if the attendee turned on their video or content streams, remote attendees can receive those streams, but only after media renegotiation between the client and the Amazon Chime back-end server.

## Request Syntax
<a name="API_meeting-chime_BatchUpdateAttendeeCapabilitiesExcept_RequestSyntax"></a>

```
PUT /meetings/{{MeetingId}}/attendees/capabilities?operation=batch-update-except HTTP/1.1
Content-type: application/json

{
   "Capabilities": {
      "Audio": "{{string}}",
      "Content": "{{string}}",
      "Video": "{{string}}"
   },
   "ExcludedAttendeeIds": [
      {
         "AttendeeId": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_meeting-chime_BatchUpdateAttendeeCapabilitiesExcept_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MeetingId](#API_meeting-chime_BatchUpdateAttendeeCapabilitiesExcept_RequestSyntax) **   <a name="chimesdk-meeting-chime_BatchUpdateAttendeeCapabilitiesExcept-request-uri-MeetingId"></a>
The ID of the meeting associated with the update request.
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: Yes

## Request Body
<a name="API_meeting-chime_BatchUpdateAttendeeCapabilitiesExcept_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Capabilities](#API_meeting-chime_BatchUpdateAttendeeCapabilitiesExcept_RequestSyntax) **   <a name="chimesdk-meeting-chime_BatchUpdateAttendeeCapabilitiesExcept-request-Capabilities"></a>
The capabilities (`audio`, `video`, or `content`) that you want to update.
Type: [AttendeeCapabilities](API_meeting-chime_AttendeeCapabilities.md) object
Required: Yes

 ** [ExcludedAttendeeIds](#API_meeting-chime_BatchUpdateAttendeeCapabilitiesExcept_RequestSyntax) **   <a name="chimesdk-meeting-chime_BatchUpdateAttendeeCapabilitiesExcept-request-ExcludedAttendeeIds"></a>
The `AttendeeIDs` that you want to exclude from one or more capabilities.
Type: Array of [AttendeeIdItem](API_meeting-chime_AttendeeIdItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 250 items.
Required: Yes

## Response Syntax
<a name="API_meeting-chime_BatchUpdateAttendeeCapabilitiesExcept_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_meeting-chime_BatchUpdateAttendeeCapabilitiesExcept_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_meeting-chime_BatchUpdateAttendeeCapabilitiesExcept_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
 ** RequestId **
The request id associated with the call responsible for the exception.
HTTP Status Code: 400

 ** ConflictException **
Multiple instances of the same request have been made simultaneously.
 ** RequestId **
The ID of the request involved in the conflict.
HTTP Status Code: 409

 ** ForbiddenException **
The client is permanently forbidden from making the request.
 ** RequestId **
The request id associated with the call responsible for the exception.
HTTP Status Code: 403

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

## See Also
<a name="API_meeting-chime_BatchUpdateAttendeeCapabilitiesExcept_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-meetings-2021-07-15/BatchUpdateAttendeeCapabilitiesExcept)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-meetings-2021-07-15/BatchUpdateAttendeeCapabilitiesExcept)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-meetings-2021-07-15/BatchUpdateAttendeeCapabilitiesExcept)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-meetings-2021-07-15/BatchUpdateAttendeeCapabilitiesExcept)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-meetings-2021-07-15/BatchUpdateAttendeeCapabilitiesExcept)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-meetings-2021-07-15/BatchUpdateAttendeeCapabilitiesExcept)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-meetings-2021-07-15/BatchUpdateAttendeeCapabilitiesExcept)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-meetings-2021-07-15/BatchUpdateAttendeeCapabilitiesExcept)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-meetings-2021-07-15/BatchUpdateAttendeeCapabilitiesExcept)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-meetings-2021-07-15/BatchUpdateAttendeeCapabilitiesExcept)
