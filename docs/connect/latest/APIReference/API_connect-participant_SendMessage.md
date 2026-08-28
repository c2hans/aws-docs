---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-participant_SendMessage.html
---

# SendMessage
<a name="API_connect-participant_SendMessage"></a>

Sends a message.

For security recommendations, see [Connect Customer Chat security best practices](https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat).

**Note**
 `ConnectionToken` is used for invoking this API instead of `ParticipantToken`.

The Amazon Connect Participant Service APIs do not use [Signature Version 4 authentication](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).

## Request Syntax
<a name="API_connect-participant_SendMessage_RequestSyntax"></a>

```
POST /participant/message HTTP/1.1
X-Amz-Bearer: {{ConnectionToken}}
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Content": "{{string}}",
   "ContentType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-participant_SendMessage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectionToken](#API_connect-participant_SendMessage_RequestSyntax) **   <a name="connect-connect-participant_SendMessage-request-ConnectionToken"></a>
The authentication token associated with the connection.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

## Request Body
<a name="API_connect-participant_SendMessage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_connect-participant_SendMessage_RequestSyntax) **   <a name="connect-connect-participant_SendMessage-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [Content](#API_connect-participant_SendMessage_RequestSyntax) **   <a name="connect-connect-participant_SendMessage-request-Content"></a>
The content of the message. Maximum of 16,384 bytes for all content types (`text/plain`, `text/markdown`, `application/json`, and `application/vnd.amazonaws.connect.message.interactive.response`).
Some messaging channels enforce lower limits. For channel-specific message size limits, see [Chat message size limits by channel](https://docs.aws.amazon.com/connect/latest/adminguide/feature-limits.html#chat-message-size-limits) in the *Amazon Connect Customer Administrator Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Required: Yes

 ** [ContentType](#API_connect-participant_SendMessage_RequestSyntax) **   <a name="connect-connect-participant_SendMessage-request-ContentType"></a>
The type of the content. Possible types are `text/plain`, `text/markdown`, `application/json`, and `application/vnd.amazonaws.connect.message.interactive.response`.
Supported types on the contact are configured through `SupportedMessagingContentTypes` on [StartChatContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html) and [StartOutboundChatContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartOutboundChatContact.html).
 For Apple Messages for Business, SMS, and WhatsApp Business Messaging contacts, only `text/plain` is supported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_connect-participant_SendMessage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AbsoluteTime": "string",
   "Id": "string",
   "MessageMetadata": {
      "MessageProcessingStatus": "string"
   }
}
```

## Response Elements
<a name="API_connect-participant_SendMessage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AbsoluteTime](#API_connect-participant_SendMessage_ResponseSyntax) **   <a name="connect-connect-participant_SendMessage-response-AbsoluteTime"></a>
The time when the message was sent.
It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [Id](#API_connect-participant_SendMessage_ResponseSyntax) **   <a name="connect-connect-participant_SendMessage-response-Id"></a>
The ID of the message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [MessageMetadata](#API_connect-participant_SendMessage_ResponseSyntax) **   <a name="connect-connect-participant_SendMessage-response-MessageMetadata"></a>
Contains metadata for the message.
Type: [MessageProcessingMetadata](API_connect-participant_MessageProcessingMetadata.md) object

## Errors
<a name="API_connect-participant_SendMessage_Errors"></a>

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
<a name="API_connect-participant_SendMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectparticipant-2018-09-07/SendMessage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectparticipant-2018-09-07/SendMessage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectparticipant-2018-09-07/SendMessage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectparticipant-2018-09-07/SendMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectparticipant-2018-09-07/SendMessage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectparticipant-2018-09-07/SendMessage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectparticipant-2018-09-07/SendMessage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectparticipant-2018-09-07/SendMessage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectparticipant-2018-09-07/SendMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectparticipant-2018-09-07/SendMessage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
