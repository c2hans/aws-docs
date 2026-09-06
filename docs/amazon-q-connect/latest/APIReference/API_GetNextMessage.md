---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_GetNextMessage.html
---

# GetNextMessage
<a name="API_amazon-q-connect_GetNextMessage"></a>

Retrieves next message on an Amazon Q in Connect session.

## Request Syntax
<a name="API_amazon-q-connect_GetNextMessage_RequestSyntax"></a>

```
GET /assistants/{{assistantId}}/sessions/{{sessionId}}/messages/next?nextMessageToken={{nextMessageToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_amazon-q-connect_GetNextMessage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assistantId](#API_amazon-q-connect_GetNextMessage_RequestSyntax) **   <a name="connect-amazon-q-connect_GetNextMessage-request-uri-assistantId"></a>
The identifier of the Amazon Q in Connect assistant.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [nextMessageToken](#API_amazon-q-connect_GetNextMessage_RequestSyntax) **   <a name="connect-amazon-q-connect_GetNextMessage-request-uri-nextMessageToken"></a>
The token for the next message. Use the value returned in the SendMessage or previous response in the next request to retrieve the next message.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [sessionId](#API_amazon-q-connect_GetNextMessage_RequestSyntax) **   <a name="connect-amazon-q-connect_GetNextMessage-request-uri-sessionId"></a>
The identifier of the Amazon Q in Connect session.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_GetNextMessage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_amazon-q-connect_GetNextMessage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "chunkedResponseTerminated": boolean,
   "conversationSessionData": [
      {
         "key": "string",
         "value": { ... }
      }
   ],
   "conversationState": {
      "reason": "string",
      "status": "string"
   },
   "nextMessageToken": "string",
   "requestMessageId": "string",
   "response": {
      "messageId": "string",
      "participant": "string",
      "timestamp": number,
      "value": { ... }
   },
   "type": "string"
}
```

## Response Elements
<a name="API_amazon-q-connect_GetNextMessage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [chunkedResponseTerminated](#API_amazon-q-connect_GetNextMessage_ResponseSyntax) **   <a name="connect-amazon-q-connect_GetNextMessage-response-chunkedResponseTerminated"></a>
Indicates whether the chunked response has been terminated.
Type: Boolean

 ** [conversationSessionData](#API_amazon-q-connect_GetNextMessage_ResponseSyntax) **   <a name="connect-amazon-q-connect_GetNextMessage-response-conversationSessionData"></a>
The conversation data stored on an Amazon Q in Connect Session.
Type: Array of [RuntimeSessionData](API_amazon-q-connect_RuntimeSessionData.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [conversationState](#API_amazon-q-connect_GetNextMessage_ResponseSyntax) **   <a name="connect-amazon-q-connect_GetNextMessage-response-conversationState"></a>
The state of current conversation.
Type: [ConversationState](API_amazon-q-connect_ConversationState.md) object

 ** [nextMessageToken](#API_amazon-q-connect_GetNextMessage_ResponseSyntax) **   <a name="connect-amazon-q-connect_GetNextMessage-response-nextMessageToken"></a>
The token for the next message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [requestMessageId](#API_amazon-q-connect_GetNextMessage_ResponseSyntax) **   <a name="connect-amazon-q-connect_GetNextMessage-response-requestMessageId"></a>
The identifier of the submitted message.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [response](#API_amazon-q-connect_GetNextMessage_ResponseSyntax) **   <a name="connect-amazon-q-connect_GetNextMessage-response-response"></a>
The message response to the requested message.
Type: [MessageOutput](API_amazon-q-connect_MessageOutput.md) object

 ** [type](#API_amazon-q-connect_GetNextMessage_ResponseSyntax) **   <a name="connect-amazon-q-connect_GetNextMessage-response-type"></a>
The type of message response.
Type: String
Valid Values: `TEXT | TOOL_USE_RESULT`

## Errors
<a name="API_amazon-q-connect_GetNextMessage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

 ** UnprocessableContentException **
The server has a failure of processing the message
HTTP Status Code: 422

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_GetNextMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/GetNextMessage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/GetNextMessage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/GetNextMessage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/GetNextMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/GetNextMessage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/GetNextMessage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/GetNextMessage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/GetNextMessage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/GetNextMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/GetNextMessage)
