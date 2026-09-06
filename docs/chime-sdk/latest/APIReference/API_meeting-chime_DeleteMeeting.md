---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_DeleteMeeting.html
---

# DeleteMeeting
<a name="API_meeting-chime_DeleteMeeting"></a>

Deletes the specified Amazon Chime SDK meeting. The operation deletes all attendees, disconnects all clients, and prevents new clients from joining the meeting. For more information about the Amazon Chime SDK, see [Using the Amazon Chime SDK](https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html) in the *Amazon Chime Developer Guide*.

## Request Syntax
<a name="API_meeting-chime_DeleteMeeting_RequestSyntax"></a>

```
DELETE /meetings/{{MeetingId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_meeting-chime_DeleteMeeting_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MeetingId](#API_meeting-chime_DeleteMeeting_RequestSyntax) **   <a name="chimesdk-meeting-chime_DeleteMeeting-request-uri-MeetingId"></a>
The Amazon Chime SDK meeting ID.
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: Yes

## Request Body
<a name="API_meeting-chime_DeleteMeeting_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_meeting-chime_DeleteMeeting_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_meeting-chime_DeleteMeeting_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_meeting-chime_DeleteMeeting_Errors"></a>

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
<a name="API_meeting-chime_DeleteMeeting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-meetings-2021-07-15/DeleteMeeting)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-meetings-2021-07-15/DeleteMeeting)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-meetings-2021-07-15/DeleteMeeting)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-meetings-2021-07-15/DeleteMeeting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-meetings-2021-07-15/DeleteMeeting)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-meetings-2021-07-15/DeleteMeeting)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-meetings-2021-07-15/DeleteMeeting)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-meetings-2021-07-15/DeleteMeeting)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-meetings-2021-07-15/DeleteMeeting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-meetings-2021-07-15/DeleteMeeting)
