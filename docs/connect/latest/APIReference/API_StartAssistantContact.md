---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_StartAssistantContact.html
---

# StartAssistantContact
<a name="API_StartAssistantContact"></a>

Starts a chat contact with an AI agent.

Use the returned `ParticipantToken` with the [CreateParticipantConnection](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html) operation.

For more information about chat, see the following topics in the *Connect Customer Administrator Guide*:
+  [Concepts: Web and mobile messaging capabilities in Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/web-and-mobile-chat.html)
+  [Connect Customer Chat security best practices](https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat)

## Request Syntax
<a name="API_StartAssistantContact_RequestSyntax"></a>

```
PUT /contact/assistant HTTP/1.1
Content-type: application/json

{
   "AiAgent": {
      "AiAgentId": "{{string}}"
   },
   "Attributes": {
      "{{string}}" : "{{string}}"
   },
   "ClientToken": "{{string}}",
   "InitialMessage": {
      "Content": "{{string}}",
      "ContentType": "{{string}}"
   },
   "InstanceId": "{{string}}",
   "ParticipantDetails": {
      "DisplayName": "{{string}}"
   },
   "PersistentChat": {
      "RehydrationType": "{{string}}",
      "SourceContactId": "{{string}}"
   },
   "RelatedContactId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartAssistantContact_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartAssistantContact_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AiAgent](#API_StartAssistantContact_RequestSyntax) **   <a name="connect-StartAssistantContact-request-AiAgent"></a>
The AI agent configuration for this contact.
Type: [AiAgentInput](API_AiAgentInput.md) object
Required: Yes

 ** [Attributes](#API_StartAssistantContact_RequestSyntax) **   <a name="connect-StartAssistantContact-request-Attributes"></a>
A map of key-value pairs to associate with the contact. We make these attributes available to flows as standard contact attributes.
You can provide up to 32,768 UTF-8 bytes across all key-value pairs for each contact.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 32767.
Value Length Constraints: Minimum length of 0. Maximum length of 32767.
Required: No

 ** [ClientToken](#API_StartAssistantContact_RequestSyntax) **   <a name="connect-StartAssistantContact-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [InitialMessage](#API_StartAssistantContact_RequestSyntax) **   <a name="connect-StartAssistantContact-request-InitialMessage"></a>
The initial message to send to the newly created chat.
Type: [ChatMessage](API_ChatMessage.md) object
Required: No

 ** [InstanceId](#API_StartAssistantContact_RequestSyntax) **   <a name="connect-StartAssistantContact-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [ParticipantDetails](#API_StartAssistantContact_RequestSyntax) **   <a name="connect-StartAssistantContact-request-ParticipantDetails"></a>
The display name and other details that identify the chat participant.
Type: [ParticipantDetails](API_ParticipantDetails.md) object
Required: Yes

 ** [PersistentChat](#API_StartAssistantContact_RequestSyntax) **   <a name="connect-StartAssistantContact-request-PersistentChat"></a>
The configuration that enables persistent chat. For more information about persistent chat and its use cases, see [Enable persistent chat](https://docs.aws.amazon.com/connect/latest/adminguide/chat-persistence.html).
Type: [PersistentChat](API_PersistentChat.md) object
Required: No

 ** [RelatedContactId](#API_StartAssistantContact_RequestSyntax) **   <a name="connect-StartAssistantContact-request-RelatedContactId"></a>
The identifier of an Connect Customer contact related to the new assistant contact.
You cannot provide both `RelatedContactId` and `PersistentChat`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_StartAssistantContact_ResponseSyntax"></a>

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
<a name="API_StartAssistantContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactId](#API_StartAssistantContact_ResponseSyntax) **   <a name="connect-StartAssistantContact-response-ContactId"></a>
The identifier of the contact within the Connect Customer instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [ContinuedFromContactId](#API_StartAssistantContact_ResponseSyntax) **   <a name="connect-StartAssistantContact-response-ContinuedFromContactId"></a>
The identifier of the contact from which the chat continues, returned only for persistent chats.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [ParticipantId](#API_StartAssistantContact_ResponseSyntax) **   <a name="connect-StartAssistantContact-response-ParticipantId"></a>
The identifier of the chat participant. The participant identifier remains the same throughout the chat lifecycle.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [ParticipantToken](#API_StartAssistantContact_ResponseSyntax) **   <a name="connect-StartAssistantContact-response-ParticipantToken"></a>
The token that the chat participant uses with the [CreateParticipantConnection](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html) operation. The token remains valid for the lifetime of the chat participant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

## Errors
<a name="API_StartAssistantContact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

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

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_StartAssistantContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/StartAssistantContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/StartAssistantContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/StartAssistantContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/StartAssistantContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/StartAssistantContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/StartAssistantContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/StartAssistantContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/StartAssistantContact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/StartAssistantContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/StartAssistantContact)
