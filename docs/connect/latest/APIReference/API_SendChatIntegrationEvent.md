---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SendChatIntegrationEvent.html
---

# SendChatIntegrationEvent
<a name="API_SendChatIntegrationEvent"></a>

Processes chat integration events from AWS or external integrations to Connect Customer. A chat integration event includes:
+ SourceId, DestinationId, and Subtype: a set of identifiers, uniquely representing a chat
+  ChatEvent: details of the chat action to perform such as sending a message, event, or disconnecting from a chat

When a chat integration event is sent with chat identifiers that do not map to an active chat contact, a new chat contact is also created before handling chat action.

Access to this API is currently restricted to AWS End User Messaging for supporting SMS integration.

## Request Syntax
<a name="API_SendChatIntegrationEvent_RequestSyntax"></a>

```
POST /chat-integration-event HTTP/1.1
Content-type: application/json

{
   "DestinationId": "{{string}}",
   "Event": {
      "Content": "{{string}}",
      "ContentType": "{{string}}",
      "Type": "{{string}}"
   },
   "NewSessionDetails": {
      "Attributes": {
         "{{string}}" : "{{string}}"
      },
      "ParticipantDetails": {
         "DisplayName": "{{string}}"
      },
      "StreamingConfiguration": {
         "StreamingEndpointArn": "{{string}}"
      },
      "SupportedMessagingContentTypes": [ "{{string}}" ]
   },
   "SourceId": "{{string}}",
   "Subtype": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SendChatIntegrationEvent_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SendChatIntegrationEvent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DestinationId](#API_SendChatIntegrationEvent_RequestSyntax) **   <a name="connect-SendChatIntegrationEvent-request-DestinationId"></a>
Chat system identifier, used in part to uniquely identify chat. This is associated with the Connect Customer instance and flow to be used to start chats. For AWS SMS, this is the phone number destination of inbound AWS SMS messages represented by an AWS End User Messaging phone number ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [Event](#API_SendChatIntegrationEvent_RequestSyntax) **   <a name="connect-SendChatIntegrationEvent-request-Event"></a>
Chat integration event payload
Type: [ChatEvent](API_ChatEvent.md) object
Required: Yes

 ** [NewSessionDetails](#API_SendChatIntegrationEvent_RequestSyntax) **   <a name="connect-SendChatIntegrationEvent-request-NewSessionDetails"></a>
Contact properties to apply when starting a new chat. If the integration event is handled with an existing chat, this is ignored.
Type: [NewSessionDetails](API_NewSessionDetails.md) object
Required: No

 ** [SourceId](#API_SendChatIntegrationEvent_RequestSyntax) **   <a name="connect-SendChatIntegrationEvent-request-SourceId"></a>
External identifier of chat customer participant, used in part to uniquely identify a chat. For SMS, this is the E164 phone number of the chat customer participant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [Subtype](#API_SendChatIntegrationEvent_RequestSyntax) **   <a name="connect-SendChatIntegrationEvent-request-Subtype"></a>
Classification of a channel. This is used in part to uniquely identify chat.
Valid value: `["connect:sms", connect:"WhatsApp"]`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## Response Syntax
<a name="API_SendChatIntegrationEvent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "InitialContactId": "string",
   "NewChatCreated": boolean
}
```

## Response Elements
<a name="API_SendChatIntegrationEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InitialContactId](#API_SendChatIntegrationEvent_ResponseSyntax) **   <a name="connect-SendChatIntegrationEvent-response-InitialContactId"></a>
Identifier of chat contact used to handle integration event. This may be null if the integration event is not valid without an already existing chat contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [NewChatCreated](#API_SendChatIntegrationEvent_ResponseSyntax) **   <a name="connect-SendChatIntegrationEvent-response-NewChatCreated"></a>
Whether handling the integration event resulted in creating a new chat or acting on existing chat.
Type: Boolean

## Errors
<a name="API_SendChatIntegrationEvent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_SendChatIntegrationEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SendChatIntegrationEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SendChatIntegrationEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SendChatIntegrationEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SendChatIntegrationEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SendChatIntegrationEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SendChatIntegrationEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SendChatIntegrationEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SendChatIntegrationEvent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SendChatIntegrationEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SendChatIntegrationEvent)
