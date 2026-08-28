---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateMeetingDialOut.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# CreateMeetingDialOut
<a name="API_CreateMeetingDialOut"></a>

Uses the join token and call metadata in a meeting request (From number, To number, and so forth) to initiate an outbound call to a public switched telephone network (PSTN) and join them into a Chime meeting. Also ensures that the From number belongs to the customer.

To play welcome audio or implement an interactive voice response (IVR), use the `CreateSipMediaApplicationCall` action with the corresponding SIP media application ID.

**Important**
 **This API is not available in a dedicated namespace.**

## Request Syntax
<a name="API_CreateMeetingDialOut_RequestSyntax"></a>

```
POST /meetings/{{meetingId}}/dial-outs HTTP/1.1
Content-type: application/json

{
   "FromPhoneNumber": "{{string}}",
   "JoinToken": "{{string}}",
   "ToPhoneNumber": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateMeetingDialOut_RequestParameters"></a>

The request uses the following URI parameters.

 ** [meetingId](#API_CreateMeetingDialOut_RequestSyntax) **   <a name="chime-CreateMeetingDialOut-request-uri-MeetingId"></a>
The Amazon Chime SDK meeting ID.
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: Yes

## Request Body
<a name="API_CreateMeetingDialOut_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [FromPhoneNumber](#API_CreateMeetingDialOut_RequestSyntax) **   <a name="chime-CreateMeetingDialOut-request-FromPhoneNumber"></a>
Phone number used as the caller ID when the remote party receives a call.
Type: String
Pattern: `^\+?[1-9]\d{1,14}$`
Required: Yes

 ** [JoinToken](#API_CreateMeetingDialOut_RequestSyntax) **   <a name="chime-CreateMeetingDialOut-request-JoinToken"></a>
Token used by the Amazon Chime SDK attendee. Call the [CreateAttendee](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateAttendee.html) action to get a join token.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9+/]+$`
Required: Yes

 ** [ToPhoneNumber](#API_CreateMeetingDialOut_RequestSyntax) **   <a name="chime-CreateMeetingDialOut-request-ToPhoneNumber"></a>
Phone number called when inviting someone to a meeting.
Type: String
Pattern: `^\+?[1-9]\d{1,14}$`
Required: Yes

## Response Syntax
<a name="API_CreateMeetingDialOut_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "TransactionId": "string"
}
```

## Response Elements
<a name="API_CreateMeetingDialOut_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [TransactionId](#API_CreateMeetingDialOut_ResponseSyntax) **   <a name="chime-CreateMeetingDialOut-response-TransactionId"></a>
Unique ID that tracks API calls.
Type: String
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`

## Errors
<a name="API_CreateMeetingDialOut_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to perform the requested operation.
HTTP Status Code: 403

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** ResourceLimitExceededException **
The request exceeds the resource limit.
HTTP Status Code: 400

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The client exceeded its request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client is not currently authorized to make the request.
HTTP Status Code: 401

## See Also
<a name="API_CreateMeetingDialOut_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/CreateMeetingDialOut)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/CreateMeetingDialOut)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/CreateMeetingDialOut)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/CreateMeetingDialOut)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/CreateMeetingDialOut)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/CreateMeetingDialOut)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/CreateMeetingDialOut)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/CreateMeetingDialOut)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/CreateMeetingDialOut)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/CreateMeetingDialOut)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
