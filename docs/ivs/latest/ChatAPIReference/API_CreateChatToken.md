---
source_url: https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_CreateChatToken.html
---

# CreateChatToken
<a name="API_CreateChatToken"></a>

Creates an encrypted token that is used by a chat participant to establish an individual WebSocket chat connection to a room. When the token is used to connect to chat, the connection is valid for the session duration specified in the request. The token becomes invalid at the token-expiration timestamp included in the response.

Use the `capabilities` field to permit an end user to send messages or moderate a room.

The `attributes` field securely attaches structured data to the chat session; the data is included within each message sent by the end user and received by other participants in the room. Common use cases for attributes include passing end-user profile data like an icon, display name, colors, badges, and other display features.

Encryption keys are owned by Amazon IVS Chat and never used directly by your application.

## Request Syntax
<a name="API_CreateChatToken_RequestSyntax"></a>

```
POST /CreateChatToken HTTP/1.1
Content-type: application/json

{
   "attributes": {
      "{{string}}" : "{{string}}"
   },
   "capabilities": [ "{{string}}" ],
   "roomIdentifier": "{{string}}",
   "sessionDurationInMinutes": {{number}},
   "userId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateChatToken_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateChatToken_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [attributes](#API_CreateChatToken_RequestSyntax) **   <a name="ivs-CreateChatToken-request-attributes"></a>
Application-provided attributes to encode into the token and attach to a chat session. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total.
Type: String to string map
Required: No

 ** [capabilities](#API_CreateChatToken_RequestSyntax) **   <a name="ivs-CreateChatToken-request-capabilities"></a>
Set of capabilities that the user is allowed to perform in the room. Default: None (the capability to view messages is implicitly included in all requests).
Type: Array of strings
Valid Values: `SEND_MESSAGE | DISCONNECT_USER | DELETE_MESSAGE`
Required: No

 ** [roomIdentifier](#API_CreateChatToken_RequestSyntax) **   <a name="ivs-CreateChatToken-request-roomIdentifier"></a>
Identifier of the room that the client is trying to access. Currently this must be an ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivschat:[a-z0-9-]+:[0-9]+:room/[a-zA-Z0-9-]+`
Required: Yes

 ** [sessionDurationInMinutes](#API_CreateChatToken_RequestSyntax) **   <a name="ivs-CreateChatToken-request-sessionDurationInMinutes"></a>
Session duration (in minutes), after which the session expires. Default: 60 (1 hour).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 180.
Required: No

 ** [userId](#API_CreateChatToken_RequestSyntax) **   <a name="ivs-CreateChatToken-request-userId"></a>
Application-provided ID that uniquely identifies the user associated with this token. This can be any UTF-8 encoded text.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Response Syntax
<a name="API_CreateChatToken_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "sessionExpirationTime": "string",
   "token": "string",
   "tokenExpirationTime": "string"
}
```

## Response Elements
<a name="API_CreateChatToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [sessionExpirationTime](#API_CreateChatToken_ResponseSyntax) **   <a name="ivs-CreateChatToken-response-sessionExpirationTime"></a>
Time after which an end user's session is no longer valid. This is an ISO 8601 timestamp; *note that this is returned as a string*.
Type: Timestamp

 ** [token](#API_CreateChatToken_ResponseSyntax) **   <a name="ivs-CreateChatToken-response-token"></a>
The issued client token, encrypted.
Type: String

 ** [tokenExpirationTime](#API_CreateChatToken_ResponseSyntax) **   <a name="ivs-CreateChatToken-response-tokenExpirationTime"></a>
Time after which the token is no longer valid and cannot be used to connect to a room. This is an ISO 8601 timestamp; *note that this is returned as a string*.
Type: Timestamp

## Errors
<a name="API_CreateChatToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

HTTP Status Code: 403

 ** PendingVerification **

HTTP Status Code: 403

 ** ResourceNotFoundException **

HTTP Status Code: 404

 ** ValidationException **

HTTP Status Code: 400

## See Also
<a name="API_CreateChatToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivschat-2020-07-14/CreateChatToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivschat-2020-07-14/CreateChatToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivschat-2020-07-14/CreateChatToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivschat-2020-07-14/CreateChatToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivschat-2020-07-14/CreateChatToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivschat-2020-07-14/CreateChatToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivschat-2020-07-14/CreateChatToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivschat-2020-07-14/CreateChatToken)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivschat-2020-07-14/CreateChatToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivschat-2020-07-14/CreateChatToken)
