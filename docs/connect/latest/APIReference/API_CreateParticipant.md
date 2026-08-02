---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateParticipant.html
---

# CreateParticipant
<a name="API_CreateParticipant"></a>

Adds a new participant into an on-going chat contact or webRTC call. For more information, see [Customize chat flow experiences by integrating custom participants](https://docs.aws.amazon.com/connect/latest/adminguide/chat-customize-flow.html) or [Enable multi-user web, in-app, and video calling](https://docs.aws.amazon.com/connect/latest/adminguide/enable-multiuser-inapp.html).

## Request Syntax
<a name="API_CreateParticipant_RequestSyntax"></a>

```
POST /contact/create-participant HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "ContactId": "{{string}}",
   "InstanceId": "{{string}}",
   "ParticipantDetails": {
      "DisplayName": "{{string}}",
      "ParticipantCapabilities": {
         "ScreenShare": "{{string}}",
         "Video": "{{string}}"
      },
      "ParticipantRole": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateParticipant_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateParticipant_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateParticipant_RequestSyntax) **   <a name="connect-CreateParticipant-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [ContactId](#API_CreateParticipant_RequestSyntax) **   <a name="connect-CreateParticipant-request-ContactId"></a>
The identifier of the contact in this instance of Connect Customer. Supports contacts in the CHAT channel and VOICE (WebRTC) channels. For WebRTC calls, this should be the initial contact ID that was generated when the contact was first created (from the StartWebRTCContact API) in the VOICE channel
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_CreateParticipant_RequestSyntax) **   <a name="connect-CreateParticipant-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [ParticipantDetails](#API_CreateParticipant_RequestSyntax) **   <a name="connect-CreateParticipant-request-ParticipantDetails"></a>
Information identifying the participant.
The only valid value for `ParticipantRole` is `CUSTOM_BOT` for chat contact and `CUSTOMER` for voice contact.
Type: [ParticipantDetailsToAdd](API_ParticipantDetailsToAdd.md) object
Required: Yes

## Response Syntax
<a name="API_CreateParticipant_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ParticipantCredentials": {
      "Expiry": "string",
      "ParticipantToken": "string"
   },
   "ParticipantId": "string"
}
```

## Response Elements
<a name="API_CreateParticipant_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ParticipantCredentials](#API_CreateParticipant_ResponseSyntax) **   <a name="connect-CreateParticipant-response-ParticipantCredentials"></a>
The token used by the chat participant to call `CreateParticipantConnection`. The participant token is valid for the lifetime of a chat participant.
Type: [ParticipantTokenCredentials](API_ParticipantTokenCredentials.md) object

 ** [ParticipantId](#API_CreateParticipant_ResponseSyntax) **   <a name="connect-CreateParticipant-response-ParticipantId"></a>
The identifier for a chat participant. The participantId for a chat participant is the same throughout the chat lifecycle.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_CreateParticipant_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreateParticipant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateParticipant)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateParticipant)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateParticipant)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateParticipant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateParticipant)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateParticipant)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateParticipant)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateParticipant)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateParticipant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateParticipant)
