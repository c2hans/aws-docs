---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreatePersistentContactAssociation.html
---

# CreatePersistentContactAssociation
<a name="API_CreatePersistentContactAssociation"></a>

Enables rehydration of chats for the lifespan of a contact. For more information about chat rehydration, see [Enable persistent chat](https://docs.aws.amazon.com/connect/latest/adminguide/chat-persistence.html) in the *Connect Customer Administrator Guide*.

## Request Syntax
<a name="API_CreatePersistentContactAssociation_RequestSyntax"></a>

```
POST /contact/persistent-contact-association/{{InstanceId}}/{{InitialContactId}} HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "RehydrationType": "{{string}}",
   "SourceContactId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreatePersistentContactAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InitialContactId](#API_CreatePersistentContactAssociation_RequestSyntax) **   <a name="connect-CreatePersistentContactAssociation-request-uri-InitialContactId"></a>
This is the contactId of the current contact that the `CreatePersistentContactAssociation` API is being called from.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_CreatePersistentContactAssociation_RequestSyntax) **   <a name="connect-CreatePersistentContactAssociation-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreatePersistentContactAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreatePersistentContactAssociation_RequestSyntax) **   <a name="connect-CreatePersistentContactAssociation-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [RehydrationType](#API_CreatePersistentContactAssociation_RequestSyntax) **   <a name="connect-CreatePersistentContactAssociation-request-RehydrationType"></a>
The contactId chosen for rehydration depends on the type chosen.
+  `ENTIRE_PAST_SESSION`: Rehydrates a chat from the most recently terminated past chat contact of the specified past ended chat session. To use this type, provide the `initialContactId` of the past ended chat session in the `sourceContactId` field. In this type, Connect Customer determines what the most recent chat contact on the past ended chat session and uses it to start a persistent chat.
+  `FROM_SEGMENT`: Rehydrates a chat from the specified past chat contact provided in the `sourceContactId` field.
The actual contactId used for rehydration is provided in the response of this API.
To illustrate how to use rehydration type, consider the following example: A customer starts a chat session. Agent a1 accepts the chat and a conversation starts between the customer and Agent a1. This first contact creates a contact ID **C1**. Agent a1 then transfers the chat to Agent a2. This creates another contact ID **C2**. At this point Agent a2 ends the chat. The customer is forwarded to the disconnect flow for a post chat survey that creates another contact ID **C3**. After the chat survey, the chat session ends. Later, the customer returns and wants to resume their past chat session. At this point, the customer can have following use cases:
+  **Use Case 1**: The customer wants to continue the past chat session but they want to hide the post chat survey. For this they will use the following configuration:
  +  **Configuration**
    + SourceContactId = "C2"
    + RehydrationType = "FROM\_SEGMENT"
  +  **Expected behavior**
    + This starts a persistent chat session from the specified past ended contact (C2). Transcripts of past chat sessions C2 and C1 are accessible in the current persistent chat session. Note that chat segment C3 is dropped from the persistent chat session.
+  **Use Case 2**: The customer wants to continue the past chat session and see the transcript of the entire past engagement, including the post chat survey. For this they will use the following configuration:
  +  **Configuration**
    + SourceContactId = "C1"
    + RehydrationType = "ENTIRE\_PAST\_SESSION"
  +  **Expected behavior**
    + This starts a persistent chat session from the most recently ended chat contact (C3). Transcripts of past chat sessions C3, C2 and C1 are accessible in the current persistent chat session.
Type: String
Valid Values: `ENTIRE_PAST_SESSION | FROM_SEGMENT`
Required: Yes

 ** [SourceContactId](#API_CreatePersistentContactAssociation_RequestSyntax) **   <a name="connect-CreatePersistentContactAssociation-request-SourceContactId"></a>
The contactId from which a persistent chat session must be started.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_CreatePersistentContactAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContinuedFromContactId": "string"
}
```

## Response Elements
<a name="API_CreatePersistentContactAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContinuedFromContactId](#API_CreatePersistentContactAssociation_ResponseSyntax) **   <a name="connect-CreatePersistentContactAssociation-response-ContinuedFromContactId"></a>
The contactId from which a persistent chat session is started. This field is populated only for persistent chat.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_CreatePersistentContactAssociation_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreatePersistentContactAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreatePersistentContactAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreatePersistentContactAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreatePersistentContactAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreatePersistentContactAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreatePersistentContactAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreatePersistentContactAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreatePersistentContactAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreatePersistentContactAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreatePersistentContactAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreatePersistentContactAssociation)
