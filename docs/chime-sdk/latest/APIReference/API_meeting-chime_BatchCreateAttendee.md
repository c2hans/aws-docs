---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_BatchCreateAttendee.html
---

# BatchCreateAttendee
<a name="API_meeting-chime_BatchCreateAttendee"></a>

Creates up to 100 attendees for an active Amazon Chime SDK meeting. For more information about the Amazon Chime SDK, see [Using the Amazon Chime SDK](https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html) in the *Amazon Chime Developer Guide*.

## Request Syntax
<a name="API_meeting-chime_BatchCreateAttendee_RequestSyntax"></a>

```
POST /meetings/{{MeetingId}}/attendees?operation=batch-create HTTP/1.1
Content-type: application/json

{
   "Attendees": [
      {
         "Capabilities": {
            "Audio": "{{string}}",
            "Content": "{{string}}",
            "Video": "{{string}}"
         },
         "ExternalUserId": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_meeting-chime_BatchCreateAttendee_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MeetingId](#API_meeting-chime_BatchCreateAttendee_RequestSyntax) **   <a name="chimesdk-meeting-chime_BatchCreateAttendee-request-uri-MeetingId"></a>
The Amazon Chime SDK ID of the meeting to which you're adding attendees.
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: Yes

## Request Body
<a name="API_meeting-chime_BatchCreateAttendee_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Attendees](#API_meeting-chime_BatchCreateAttendee_RequestSyntax) **   <a name="chimesdk-meeting-chime_BatchCreateAttendee-request-Attendees"></a>
The attendee information, including attendees' IDs and join tokens.
Type: Array of [CreateAttendeeRequestItem](API_meeting-chime_CreateAttendeeRequestItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_meeting-chime_BatchCreateAttendee_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Attendees": [
      {
         "AttendeeId": "string",
         "Capabilities": {
            "Audio": "string",
            "Content": "string",
            "Video": "string"
         },
         "ExternalUserId": "string",
         "JoinToken": "string"
      }
   ],
   "Errors": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "ExternalUserId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_meeting-chime_BatchCreateAttendee_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Attendees](#API_meeting-chime_BatchCreateAttendee_ResponseSyntax) **   <a name="chimesdk-meeting-chime_BatchCreateAttendee-response-Attendees"></a>
The attendee information, including attendees' IDs and join tokens.
Type: Array of [Attendee](API_meeting-chime_Attendee.md) objects

 ** [Errors](#API_meeting-chime_BatchCreateAttendee_ResponseSyntax) **   <a name="chimesdk-meeting-chime_BatchCreateAttendee-response-Errors"></a>
If the action fails for one or more of the attendees in the request, a list of the attendees is returned, along with error codes and error messages.
Type: Array of [CreateAttendeeError](API_meeting-chime_CreateAttendeeError.md) objects

## Errors
<a name="API_meeting-chime_BatchCreateAttendee_Errors"></a>

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
<a name="API_meeting-chime_BatchCreateAttendee_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-meetings-2021-07-15/BatchCreateAttendee)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-meetings-2021-07-15/BatchCreateAttendee)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-meetings-2021-07-15/BatchCreateAttendee)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-meetings-2021-07-15/BatchCreateAttendee)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-meetings-2021-07-15/BatchCreateAttendee)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-meetings-2021-07-15/BatchCreateAttendee)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-meetings-2021-07-15/BatchCreateAttendee)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-meetings-2021-07-15/BatchCreateAttendee)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-meetings-2021-07-15/BatchCreateAttendee)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-meetings-2021-07-15/BatchCreateAttendee)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
