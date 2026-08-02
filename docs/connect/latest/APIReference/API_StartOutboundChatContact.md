---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_StartOutboundChatContact.html
---

# StartOutboundChatContact
<a name="API_StartOutboundChatContact"></a>

Initiates a new outbound SMS or WhatsApp contact to a customer. Response of this API provides the `ContactId` of the outbound SMS or WhatsApp contact created.

 **SourceEndpoint** only supports Endpoints with `CONNECT_PHONENUMBER_ARN` as Type and **DestinationEndpoint** only supports Endpoints with `TELEPHONE_NUMBER` as Type. **ContactFlowId** initiates the flow to manage the new contact created.

This API can be used to initiate outbound SMS or WhatsApp contacts for an agent, or it can also deflect an ongoing contact to an outbound SMS or WhatsApp contact by using the [StartOutboundChatContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartOutboundChatContact.html) Flow Action.

For more information about using SMS or WhatsApp in Connect Customer, see the following topics in the *Connect Customer Administrator Guide*:
+  [Set up SMS messaging](https://docs.aws.amazon.com/connect/latest/adminguide/setup-sms-messaging.html)
+  [Request an SMS-enabled phone number through AWS End User Messaging SMS](https://docs.aws.amazon.com/connect/latest/adminguide/sms-number.html)
+  [Set up WhatsApp Business messaging](https://docs.aws.amazon.com/connect/latest/adminguide/whatsapp-integration.html)

## Request Syntax
<a name="API_StartOutboundChatContact_RequestSyntax"></a>

```
PUT /contact/outbound-chat HTTP/1.1
Content-type: application/json

{
   "Attributes": {
      "{{string}}" : "{{string}}"
   },
   "ChatDurationInMinutes": {{number}},
   "ClientToken": "{{string}}",
   "ContactFlowId": "{{string}}",
   "DestinationEndpoint": {
      "Address": "{{string}}",
      "Type": "{{string}}"
   },
   "InitialSystemMessage": {
      "Content": "{{string}}",
      "ContentType": "{{string}}"
   },
   "InitialTemplatedSystemMessage": {
      "KnowledgeBaseId": "{{string}}",
      "MessageTemplateId": "{{string}}",
      "TemplateAttributes": {
         "CustomAttributes": {
            "{{string}}" : "{{string}}"
         },
         "CustomerProfileAttributes": "{{string}}"
      }
   },
   "InstanceId": "{{string}}",
   "ParticipantDetails": {
      "DisplayName": "{{string}}"
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
   "SourceEndpoint": {
      "Address": "{{string}}",
      "Type": "{{string}}"
   },
   "SupportedMessagingContentTypes": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_StartOutboundChatContact_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartOutboundChatContact_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Attributes](#API_StartOutboundChatContact_RequestSyntax) **   <a name="connect-StartOutboundChatContact-request-Attributes"></a>
A custom key-value pair using an attribute map. The attributes are standard Connect Customer attributes, and can be accessed in flows just like any other contact attributes.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 32767.
Value Length Constraints: Minimum length of 0. Maximum length of 32767.
Required: No

 ** [ChatDurationInMinutes](#API_StartOutboundChatContact_RequestSyntax) **   <a name="connect-StartOutboundChatContact-request-ChatDurationInMinutes"></a>
The total duration of the newly started chat session. If not specified, the chat session duration defaults to 25 hour. The minimum configurable time is 60 minutes. The maximum configurable time is 10,080 minutes (7 days).
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 10080.
Required: No

 ** [ClientToken](#API_StartOutboundChatContact_RequestSyntax) **   <a name="connect-StartOutboundChatContact-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/). The token is valid for 7 days after creation. If a contact is already started, the contact ID is returned.
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [ContactFlowId](#API_StartOutboundChatContact_RequestSyntax) **   <a name="connect-StartOutboundChatContact-request-ContactFlowId"></a>
The identifier of the flow for the call. To see the ContactFlowId in the Connect Customer console user interface, on the navigation menu go to **Routing, Contact Flows**. Choose the flow. On the flow page, under the name of the flow, choose **Show additional flow information**. The ContactFlowId is the last part of the ARN, shown here in bold:
+ arn:aws:connect:us-west-2:xxxxxxxxxxxx:instance/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/contact-flow/**123ec456-a007-89c0-1234-xxxxxxxxxxxx**
Type: String
Length Constraints: Maximum length of 500.
Required: Yes

 ** [DestinationEndpoint](#API_StartOutboundChatContact_RequestSyntax) **   <a name="connect-StartOutboundChatContact-request-DestinationEndpoint"></a>
Information about the endpoint.
Type: [Endpoint](API_Endpoint.md) object
Required: Yes

 ** [InitialSystemMessage](#API_StartOutboundChatContact_RequestSyntax) **   <a name="connect-StartOutboundChatContact-request-InitialSystemMessage"></a>
A chat message.
Type: [ChatMessage](API_ChatMessage.md) object
Required: No

 ** [InitialTemplatedSystemMessage](#API_StartOutboundChatContact_RequestSyntax) **   <a name="connect-StartOutboundChatContact-request-InitialTemplatedSystemMessage"></a>
Information about template message configuration.
Type: [TemplatedMessageConfig](API_TemplatedMessageConfig.md) object
Required: No

 ** [InstanceId](#API_StartOutboundChatContact_RequestSyntax) **   <a name="connect-StartOutboundChatContact-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [ParticipantDetails](#API_StartOutboundChatContact_RequestSyntax) **   <a name="connect-StartOutboundChatContact-request-ParticipantDetails"></a>
The customer's details.
Type: [ParticipantDetails](API_ParticipantDetails.md) object
Required: No

 ** [RelatedContactId](#API_StartOutboundChatContact_RequestSyntax) **   <a name="connect-StartOutboundChatContact-request-RelatedContactId"></a>
The unique identifier for an Connect Customer contact. This identifier is related to the contact starting.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [SegmentAttributes](#API_StartOutboundChatContact_RequestSyntax) **   <a name="connect-StartOutboundChatContact-request-SegmentAttributes"></a>
A set of system defined key-value pairs stored on individual contact segments using an attribute map. The attributes are standard Connect Customer attributes. They can be accessed in flows.
+ Attribute keys can include only alphanumeric, `-`, and `_`.
+ This field can be used to show channel subtype, such as `connect:SMS` and `connect:WhatsApp`.
Type: String to [SegmentAttributeValue](API_SegmentAttributeValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [SourceEndpoint](#API_StartOutboundChatContact_RequestSyntax) **   <a name="connect-StartOutboundChatContact-request-SourceEndpoint"></a>
Information about the endpoint.
Type: [Endpoint](API_Endpoint.md) object
Required: Yes

 ** [SupportedMessagingContentTypes](#API_StartOutboundChatContact_RequestSyntax) **   <a name="connect-StartOutboundChatContact-request-SupportedMessagingContentTypes"></a>
The supported chat message content types. Supported types are:
+  `text/plain`
+  `text/markdown`
+  `application/json, application/vnd.amazonaws.connect.message.interactive`
+  `application/vnd.amazonaws.connect.message.interactive.response`
Content types must always contain `text/plain`. You can then put any other supported type in the list. For example, all the following lists are valid because they contain `text/plain`:
+  `[text/plain, text/markdown, application/json]`
+  `[text/markdown, text/plain]`
+  `[text/plain, application/json, application/vnd.amazonaws.connect.message.interactive.response]`
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## Response Syntax
<a name="API_StartOutboundChatContact_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactId": "string"
}
```

## Response Elements
<a name="API_StartOutboundChatContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactId](#API_StartOutboundChatContact_ResponseSyntax) **   <a name="connect-StartOutboundChatContact-response-ContactId"></a>
The identifier of this contact within the Connect Customer instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_StartOutboundChatContact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Operation cannot be performed at this time as there is a conflict with another operation or contact state.
HTTP Status Code: 409

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

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_StartOutboundChatContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/StartOutboundChatContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/StartOutboundChatContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/StartOutboundChatContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/StartOutboundChatContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/StartOutboundChatContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/StartOutboundChatContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/StartOutboundChatContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/StartOutboundChatContact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/StartOutboundChatContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/StartOutboundChatContact)
