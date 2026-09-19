---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_SendWhatsAppCallEvent.html
---

# SendWhatsAppCallEvent
<a name="API_SendWhatsAppCallEvent"></a>

Sends a WhatsApp calling event, such as connecting or terminating a call, for a business phone number. This operation passes the event through to Meta. To use this operation, the origination phone number must belong to a WhatsApp Business Account that is linked to your AWS account.

## Request Syntax
<a name="API_SendWhatsAppCallEvent_RequestSyntax"></a>

```
POST /v1/whatsapp/call/event HTTP/1.1
Content-type: application/json

{
   "callEvent": {{blob}},
   "metaApiVersion": "{{string}}",
   "originationPhoneNumberId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SendWhatsAppCallEvent_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SendWhatsAppCallEvent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [callEvent](#API_SendWhatsAppCallEvent_RequestSyntax) **   <a name="Social-SendWhatsAppCallEvent-request-callEvent"></a>
The call event payload to send, as a JSON blob in the format defined by the Meta calling API.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 2048000.
Required: Yes

 ** [metaApiVersion](#API_SendWhatsAppCallEvent_RequestSyntax) **   <a name="Social-SendWhatsAppCallEvent-request-metaApiVersion"></a>
The version of the Meta Graph API to use for the request.
Type: String
Required: Yes

 ** [originationPhoneNumberId](#API_SendWhatsAppCallEvent_RequestSyntax) **   <a name="Social-SendWhatsAppCallEvent-request-originationPhoneNumberId"></a>
The unique identifier of the origination phone number for the call. The phone number identifiers are formatted as `phone-number-id-01234567890123456789012345678901`. Use `GetLinkedWhatsAppBusinessAccount` to find a phone number's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^phone-number-id-.*$)|(^arn:.*:phone-number-id/[0-9a-zA-Z]+$).*`
Required: Yes

## Response Syntax
<a name="API_SendWhatsAppCallEvent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "callId": "string"
}
```

## Response Elements
<a name="API_SendWhatsAppCallEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [callId](#API_SendWhatsAppCallEvent_ResponseSyntax) **   <a name="Social-SendWhatsAppCallEvent-response-callId"></a>
The unique identifier that Meta assigns to the call.
Type: String

## Errors
<a name="API_SendWhatsAppCallEvent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedByMetaException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
HTTP Status Code: 409

 ** DependencyException **
Thrown when performing an action because a dependency would be broken.
HTTP Status Code: 502

 ** InternalServiceException **
The request processing has failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** InvalidParametersException **
One or more parameters provided to the action are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource was not found.
HTTP Status Code: 404

 ** ThrottledRequestException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request contains an invalid parameter value.
HTTP Status Code: 400

## See Also
<a name="API_SendWhatsAppCallEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/SendWhatsAppCallEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/SendWhatsAppCallEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/SendWhatsAppCallEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/SendWhatsAppCallEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/SendWhatsAppCallEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/SendWhatsAppCallEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/SendWhatsAppCallEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/SendWhatsAppCallEvent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/SendWhatsAppCallEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/SendWhatsAppCallEvent)
