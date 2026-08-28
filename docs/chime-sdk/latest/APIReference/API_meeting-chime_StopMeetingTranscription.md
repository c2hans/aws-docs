---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_StopMeetingTranscription.html
---

# StopMeetingTranscription
<a name="API_meeting-chime_StopMeetingTranscription"></a>

Stops transcription for the specified `meetingId`. For more information, refer to [ Using Amazon Chime SDK live transcription ](https://docs.aws.amazon.com/chime-sdk/latest/dg/meeting-transcription.html) in the *Amazon Chime SDK Developer Guide*.

**Important**
By default, Amazon Transcribe may use and store audio content processed by the service to develop and improve AWS AI/ML services as further described in section 50 of the [AWS Service Terms](https://aws.amazon.com/service-terms/). Using Amazon Transcribe may be subject to federal and state laws or regulations regarding the recording or interception of electronic communications. It is your and your end users’ responsibility to comply with all applicable laws regarding the recording, including properly notifying all participants in a recorded session or communication that the session or communication is being recorded, and obtaining all necessary consents. You can opt out from AWS using audio content to develop and improve AWS AI/ML services by configuring an AI services opt out policy using AWS Organizations.

## Request Syntax
<a name="API_meeting-chime_StopMeetingTranscription_RequestSyntax"></a>

```
POST /meetings/{{MeetingId}}/transcription?operation=stop HTTP/1.1
```

## URI Request Parameters
<a name="API_meeting-chime_StopMeetingTranscription_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MeetingId](#API_meeting-chime_StopMeetingTranscription_RequestSyntax) **   <a name="chimesdk-meeting-chime_StopMeetingTranscription-request-uri-MeetingId"></a>
The unique ID of the meeting for which you stop transcription.
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: Yes

## Request Body
<a name="API_meeting-chime_StopMeetingTranscription_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_meeting-chime_StopMeetingTranscription_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_meeting-chime_StopMeetingTranscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_meeting-chime_StopMeetingTranscription_Errors"></a>

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

 ** UnprocessableEntityException **
The request was well-formed but was unable to be followed due to semantic errors.
 ** RequestId **
The request id associated with the call responsible for the exception.
HTTP Status Code: 422

## See Also
<a name="API_meeting-chime_StopMeetingTranscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-meetings-2021-07-15/StopMeetingTranscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-meetings-2021-07-15/StopMeetingTranscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-meetings-2021-07-15/StopMeetingTranscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-meetings-2021-07-15/StopMeetingTranscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-meetings-2021-07-15/StopMeetingTranscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-meetings-2021-07-15/StopMeetingTranscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-meetings-2021-07-15/StopMeetingTranscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-meetings-2021-07-15/StopMeetingTranscription)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-meetings-2021-07-15/StopMeetingTranscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-meetings-2021-07-15/StopMeetingTranscription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
