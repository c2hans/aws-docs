---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html
---

# StartChatContact
<a name="API_StartChatContact"></a>

Initiates a flow to start a new chat for the customer. Response of this API provides a token required to obtain credentials from the [CreateParticipantConnection](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html) API in the Connect Customer Participant Service.

When a new chat contact is successfully created, clients must subscribe to the participant’s connection for the created chat within 5 minutes. This is achieved by invoking [CreateParticipantConnection](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html) with WEBSOCKET and CONNECTION\_CREDENTIALS.

A 429 error occurs in the following situations:
+ API rate limit is exceeded. API TPS throttling returns a `TooManyRequests` exception.
+ The [quota for concurrent active chats](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html) is exceeded. Active chat throttling returns a `LimitExceededException`.

If you use the `ChatDurationInMinutes` parameter and receive a 400 error, your account may not support the ability to configure custom chat durations. For more information, contact Support.

For more information about chat, see the following topics in the *Connect Customer Administrator Guide*:
+  [Concepts: Web and mobile messaging capabilities in Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/web-and-mobile-chat.html)
+  [Connect Customer Chat security best practices](https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat)

## Request Syntax
<a name="API_StartChatContact_RequestSyntax"></a>

```
PUT /contact/chat HTTP/1.1
Content-type: application/json

{
   "Attributes": {
      "{{string}}" : "{{string}}"
   },
   "ChatDurationInMinutes": {{number}},
   "ClientToken": "{{string}}",
   "ContactFlowId": "{{string}}",
   "CustomerId": "{{string}}",
   "DisconnectOnCustomerExit": [ "{{string}}" ],
   "InitialMessage": {
      "Content": "{{string}}",
      "ContentType": "{{string}}"
   },
   "InstanceId": "{{string}}",
   "ParticipantConfiguration": {
      "ResponseMode": "{{string}}"
   },
   "ParticipantDetails": {
      "DisplayName": "{{string}}"
   },
   "PersistentChat": {
      "RehydrationType": "{{string}}",
      "SourceContactId": "{{string}}"
   },
   "RelatedContactId": "{{string}}",
   "SegmentAttributes": {
      "{{string}}" : {
         "ValueArn": "{{string}}",
         "ValueInteger": {{number}},
         "ValueList": [
            "SegmentAttributeValue"
         ],
         "ValueMap": {
            "{{string}}" : "SegmentAttributeValue"
         },
         "ValueString": "{{string}}"
      }
   },
   "SupportedMessagingContentTypes": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_StartChatContact_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartChatContact_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Attributes](#API_StartChatContact_RequestSyntax) **   <a name="connect-StartChatContact-request-Attributes"></a>
A custom key-value pair using an attribute map. The attributes are standard Connect Customer attributes. They can be accessed in flows just like any other contact attributes.
There can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, dash, and underscore characters.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 32767.
Value Length Constraints: Minimum length of 0. Maximum length of 32767.
Required: No

 ** [ChatDurationInMinutes](#API_StartChatContact_RequestSyntax) **   <a name="connect-StartChatContact-request-ChatDurationInMinutes"></a>
The total duration of the newly started chat session. If not specified, the chat session duration defaults to 25 hour. The minimum configurable time is 60 minutes. The maximum configurable time is 10,080 minutes (7 days).
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 10080.
Required: No

 ** [ClientToken](#API_StartChatContact_RequestSyntax) **   <a name="connect-StartChatContact-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [ContactFlowId](#API_StartChatContact_RequestSyntax) **   <a name="connect-StartChatContact-request-ContactFlowId"></a>
The identifier of the flow for initiating the chat. To see the ContactFlowId in the Connect Customer admin website, on the navigation menu go to **Routing**, **Flows**. Choose the flow. On the flow page, under the name of the flow, choose **Show additional flow information**. The ContactFlowId is the last part of the ARN, shown here in bold:
arn:aws:connect:us-west-2:xxxxxxxxxxxx:instance/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/contact-flow/**846ec553-a005-41c0-8341-xxxxxxxxxxxx**
Type: String
Length Constraints: Maximum length of 500.
Required: Yes

 ** [CustomerId](#API_StartChatContact_RequestSyntax) **   <a name="connect-StartChatContact-request-CustomerId"></a>
The customer's identification number. For example, the `CustomerId` may be a customer number from your CRM.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [DisconnectOnCustomerExit](#API_StartChatContact_RequestSyntax) **   <a name="connect-StartChatContact-request-DisconnectOnCustomerExit"></a>
A list of participant types to automatically disconnect when the end customer ends the chat session, allowing them to continue through disconnect flows such as surveys or feedback forms.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `AGENT`
Required: No

 ** [InitialMessage](#API_StartChatContact_RequestSyntax) **   <a name="connect-StartChatContact-request-InitialMessage"></a>
The initial message to be sent to the newly created chat.
Type: [ChatMessage](API_ChatMessage.md) object
Required: No

 ** [InstanceId](#API_StartChatContact_RequestSyntax) **   <a name="connect-StartChatContact-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [ParticipantConfiguration](#API_StartChatContact_RequestSyntax) **   <a name="connect-StartChatContact-request-ParticipantConfiguration"></a>
 The configuration of the participant.
Type: [ParticipantConfiguration](API_ParticipantConfiguration.md) object
Required: No

 ** [ParticipantDetails](#API_StartChatContact_RequestSyntax) **   <a name="connect-StartChatContact-request-ParticipantDetails"></a>
Information identifying the participant.
Type: [ParticipantDetails](API_ParticipantDetails.md) object
Required: Yes

 ** [PersistentChat](#API_StartChatContact_RequestSyntax) **   <a name="connect-StartChatContact-request-PersistentChat"></a>
Enable persistent chats. For more information about enabling persistent chat, and for example use cases and how to configure for them, see [Enable persistent chat](https://docs.aws.amazon.com/connect/latest/adminguide/chat-persistence.html).
Type: [PersistentChat](API_PersistentChat.md) object
Required: No

 ** [RelatedContactId](#API_StartChatContact_RequestSyntax) **   <a name="connect-StartChatContact-request-RelatedContactId"></a>
The unique identifier for an Connect Customer contact. This identifier is related to the chat starting.
You cannot provide data for both RelatedContactId and PersistentChat.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [SegmentAttributes](#API_StartChatContact_RequestSyntax) **   <a name="connect-StartChatContact-request-SegmentAttributes"></a>
A set of system defined key-value pairs stored on individual contact segments using an attribute map. The attributes are standard Connect Customer attributes. They can be accessed in flows.
Attribute keys can include only alphanumeric, -, and \_.
This field can be used to show channel subtype, such as `connect:Guide`.
The types `application/vnd.amazonaws.connect.message.interactive` and `application/vnd.amazonaws.connect.message.interactive.response` must be present in the SupportedMessagingContentTypes field of this API in order to set `SegmentAttributes` as {` "connect:Subtype": {"valueString" : "connect:Guide" }}`.
Type: String to [SegmentAttributeValue](API_SegmentAttributeValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [SupportedMessagingContentTypes](#API_StartChatContact_RequestSyntax) **   <a name="connect-StartChatContact-request-SupportedMessagingContentTypes"></a>
The supported chat message content types. Supported types are `text/plain`, `text/markdown`, `application/json`, `application/vnd.amazonaws.connect.message.interactive`, and `application/vnd.amazonaws.connect.message.interactive.response`.
Content types must always contain `text/plain`. You can then put any other supported type in the list. For example, all the following lists are valid because they contain `text/plain`: `[text/plain, text/markdown, application/json]`, `[text/markdown, text/plain]`, `[text/plain, application/json, application/vnd.amazonaws.connect.message.interactive.response]`.
The type `application/vnd.amazonaws.connect.message.interactive` is required to use the [Show view](https://docs.aws.amazon.com/connect/latest/adminguide/show-view-block.html) flow block.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## Response Syntax
<a name="API_StartChatContact_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactId": "string",
   "ContinuedFromContactId": "string",
   "ParticipantId": "string",
   "ParticipantToken": "string"
}
```

## Response Elements
<a name="API_StartChatContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactId](#API_StartChatContact_ResponseSyntax) **   <a name="connect-StartChatContact-response-ContactId"></a>
The identifier of this contact within the Connect Customer instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [ContinuedFromContactId](#API_StartChatContact_ResponseSyntax) **   <a name="connect-StartChatContact-response-ContinuedFromContactId"></a>
The contactId from which a persistent chat session is started. This field is populated only for persistent chats.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [ParticipantId](#API_StartChatContact_ResponseSyntax) **   <a name="connect-StartChatContact-response-ParticipantId"></a>
The identifier for a chat participant. The participantId for a chat participant is the same throughout the chat lifecycle.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [ParticipantToken](#API_StartChatContact_ResponseSyntax) **   <a name="connect-StartChatContact-response-ParticipantToken"></a>
The token used by the chat participant to call [CreateParticipantConnection](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html). The participant token is valid for the lifetime of a chat participant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

## Errors
<a name="API_StartChatContact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** LimitExceededException **
The allowed limit for the resource has been exceeded.
 ** Message **
The message about the limit.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

## See Also
<a name="API_StartChatContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/StartChatContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/StartChatContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/StartChatContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/StartChatContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/StartChatContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/StartChatContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/StartChatContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/StartChatContact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/StartChatContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/StartChatContact)
