---
source_url: https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CancelParticipantAuthentication.html
---

# CancelParticipantAuthentication
<a name="API_connect-participant_CancelParticipantAuthentication"></a>

Cancels the authentication session. The opted out branch of the Authenticate Customer flow block will be taken.

**Note**
The current supported channel is chat. This API is not supported for Apple Messages for Business, WhatsApp, or SMS chats.

**Note**
 `ConnectionToken` is used for invoking this API instead of `ParticipantToken`.

The Amazon Connect Participant Service APIs do not use [Signature Version 4 authentication](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).

## Request Syntax
<a name="API_connect-participant_CancelParticipantAuthentication_RequestSyntax"></a>

```
POST /participant/cancel-authentication HTTP/1.1
X-Amz-Bearer: {{ConnectionToken}}
Content-type: application/json

{
   "SessionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-participant_CancelParticipantAuthentication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectionToken](#API_connect-participant_CancelParticipantAuthentication_RequestSyntax) **   <a name="connect-connect-participant_CancelParticipantAuthentication-request-ConnectionToken"></a>
The authentication token associated with the participant's connection.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

## Request Body
<a name="API_connect-participant_CancelParticipantAuthentication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SessionId](#API_connect-participant_CancelParticipantAuthentication_RequestSyntax) **   <a name="connect-connect-participant_CancelParticipantAuthentication-request-SessionId"></a>
The `sessionId` provided in the `authenticationInitiated` event.
Type: String
Length Constraints: Fixed length of 36.
Required: Yes

## Response Syntax
<a name="API_connect-participant_CancelParticipantAuthentication_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-participant_CancelParticipantAuthentication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-participant_CancelParticipantAuthentication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the Amazon Connect service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by Amazon Connect.
HTTP Status Code: 400

## See Also
<a name="API_connect-participant_CancelParticipantAuthentication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectparticipant-2018-09-07/CancelParticipantAuthentication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectparticipant-2018-09-07/CancelParticipantAuthentication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectparticipant-2018-09-07/CancelParticipantAuthentication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectparticipant-2018-09-07/CancelParticipantAuthentication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectparticipant-2018-09-07/CancelParticipantAuthentication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectparticipant-2018-09-07/CancelParticipantAuthentication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectparticipant-2018-09-07/CancelParticipantAuthentication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectparticipant-2018-09-07/CancelParticipantAuthentication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectparticipant-2018-09-07/CancelParticipantAuthentication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectparticipant-2018-09-07/CancelParticipantAuthentication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
