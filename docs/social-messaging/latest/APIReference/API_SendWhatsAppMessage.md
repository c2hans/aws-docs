---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_SendWhatsAppMessage.html
---

# SendWhatsAppMessage
<a name="API_SendWhatsAppMessage"></a>

Send a WhatsApp message. For examples of sending a message using the AWS CLI, see [Sending messages](https://docs.aws.amazon.com/social-messaging/latest/userguide/send-message.html) in the * * AWS End User Messaging Social User Guide* *.

## Request Syntax
<a name="API_SendWhatsAppMessage_RequestSyntax"></a>

```
POST /v1/whatsapp/send HTTP/1.1
Content-type: application/json

{
   "message": {{blob}},
   "metaApiVersion": "{{string}}",
   "originationPhoneNumberId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SendWhatsAppMessage_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SendWhatsAppMessage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [message](#API_SendWhatsAppMessage_RequestSyntax) **   <a name="Social-SendWhatsAppMessage-request-message"></a>
The message to send through WhatsApp. The length is in KB. The message field passes through a WhatsApp Message object, see [Messages](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/messages) in the *WhatsApp Business Platform Cloud API Reference*.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 2048000.
Required: Yes

 ** [metaApiVersion](#API_SendWhatsAppMessage_RequestSyntax) **   <a name="Social-SendWhatsAppMessage-request-metaApiVersion"></a>
The API version for the request formatted as `v{VersionNumber}`. For a list of supported API versions and AWS Regions, see [* AWS End User Messaging Social API* Service Endpoints](https://docs.aws.amazon.com/general/latest/gr/end-user-messaging.html) in the * AWS General Reference*.
Type: String
Required: Yes

 ** [originationPhoneNumberId](#API_SendWhatsAppMessage_RequestSyntax) **   <a name="Social-SendWhatsAppMessage-request-originationPhoneNumberId"></a>
The ID of the phone number used to send the WhatsApp message. If you are sending a media file only the `originationPhoneNumberId` used to upload the file can be used. Phone number identifiers are formatted as `phone-number-id-01234567890123456789012345678901`. Use [GetLinkedWhatsAppBusinessAccount](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html) to find a phone number's id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^phone-number-id-.*$)|(^arn:.*:phone-number-id/[0-9a-zA-Z]+$).*`
Required: Yes

## Response Syntax
<a name="API_SendWhatsAppMessage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "messageId": "string"
}
```

## Response Elements
<a name="API_SendWhatsAppMessage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [messageId](#API_SendWhatsAppMessage_ResponseSyntax) **   <a name="Social-SendWhatsAppMessage-response-messageId"></a>
The unique identifier of the message.
Type: String

## Errors
<a name="API_SendWhatsAppMessage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_SendWhatsAppMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/SendWhatsAppMessage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/SendWhatsAppMessage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/SendWhatsAppMessage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/SendWhatsAppMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/SendWhatsAppMessage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/SendWhatsAppMessage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/SendWhatsAppMessage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/SendWhatsAppMessage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/SendWhatsAppMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/SendWhatsAppMessage)
