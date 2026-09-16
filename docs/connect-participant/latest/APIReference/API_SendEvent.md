---
source_url: https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_SendEvent.html
---

# SendEvent
<a name="API_connect-participant_SendEvent"></a>

**Note**
The `application/vnd.amazonaws.connect.event.connection.acknowledged` ContentType is no longer maintained since December 31, 2024. This event has been migrated to the [CreateParticipantConnection](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html) API using the `ConnectParticipant` field.

Sends an event. Message receipts are not supported when there are more than two active participants in the chat. Using the SendEvent API for message receipts when a supervisor is barged-in will result in a conflict exception.

For security recommendations, see [Connect Customer Chat security best practices](https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat).

**Note**
 `ConnectionToken` is used for invoking this API instead of `ParticipantToken`.

The Amazon Connect Participant Service APIs do not use [Signature Version 4 authentication](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).

## Request Syntax
<a name="API_connect-participant_SendEvent_RequestSyntax"></a>

```
POST /participant/event HTTP/1.1
X-Amz-Bearer: {{ConnectionToken}}
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Content": "{{string}}",
   "ContentType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-participant_SendEvent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectionToken](#API_connect-participant_SendEvent_RequestSyntax) **   <a name="connect-connect-participant_SendEvent-request-ConnectionToken"></a>
The authentication token associated with the participant's connection.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

## Request Body
<a name="API_connect-participant_SendEvent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_connect-participant_SendEvent_RequestSyntax) **   <a name="connect-connect-participant_SendEvent-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [Content](#API_connect-participant_SendEvent_RequestSyntax) **   <a name="connect-connect-participant_SendEvent-request-Content"></a>
The content of the event to be sent (for example, message text). For content related to message receipts, this is supported in the form of a JSON string.
Sample Content: "{\\"messageId\\":\\"11111111-aaaa-bbbb-cccc-EXAMPLE01234\\"}"
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Required: No

 ** [ContentType](#API_connect-participant_SendEvent_RequestSyntax) **   <a name="connect-connect-participant_SendEvent-request-ContentType"></a>
The content type of the request. Supported types are:
+ application/vnd.amazonaws.connect.event.typing
+ application/vnd.amazonaws.connect.event.connection.acknowledged (is no longer maintained since December 31, 2024)
+ application/vnd.amazonaws.connect.event.message.delivered
+ application/vnd.amazonaws.connect.event.message.read
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_connect-participant_SendEvent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AbsoluteTime": "string",
   "Id": "string"
}
```

## Response Elements
<a name="API_connect-participant_SendEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AbsoluteTime](#API_connect-participant_SendEvent_ResponseSyntax) **   <a name="connect-connect-participant_SendEvent-response-AbsoluteTime"></a>
The time when the event was sent.
It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [Id](#API_connect-participant_SendEvent_ResponseSyntax) **   <a name="connect-connect-participant_SendEvent-response-Id"></a>
The ID of the response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_connect-participant_SendEvent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The requested operation conflicts with the current state of a service resource associated with the request.
HTTP Status Code: 409

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
<a name="API_connect-participant_SendEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectparticipant-2018-09-07/SendEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectparticipant-2018-09-07/SendEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectparticipant-2018-09-07/SendEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectparticipant-2018-09-07/SendEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectparticipant-2018-09-07/SendEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectparticipant-2018-09-07/SendEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectparticipant-2018-09-07/SendEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectparticipant-2018-09-07/SendEvent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connectparticipant-2018-09-07/SendEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectparticipant-2018-09-07/SendEvent)
