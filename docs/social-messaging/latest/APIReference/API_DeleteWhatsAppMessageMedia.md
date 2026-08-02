---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_DeleteWhatsAppMessageMedia.html
---

# DeleteWhatsAppMessageMedia
<a name="API_DeleteWhatsAppMessageMedia"></a>

Delete a media object from the WhatsApp service. If the object is still in an Amazon S3 bucket you should delete it from there too.

## Request Syntax
<a name="API_DeleteWhatsAppMessageMedia_RequestSyntax"></a>

```
DELETE /v1/whatsapp/media?mediaId={{mediaId}}&originationPhoneNumberId={{originationPhoneNumberId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteWhatsAppMessageMedia_RequestParameters"></a>

The request uses the following URI parameters.

 ** [mediaId](#API_DeleteWhatsAppMessageMedia_RequestSyntax) **   <a name="Social-DeleteWhatsAppMessageMedia-request-uri-mediaId"></a>
The unique identifier of the media file to delete. Use the `mediaId` returned from [PostWhatsAppMessageMedia](https://console.aws.amazon.com/social-messaging/latest/APIReference/API_PostWhatsAppMessageMedia.html).
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9]+`
Required: Yes

 ** [originationPhoneNumberId](#API_DeleteWhatsAppMessageMedia_RequestSyntax) **   <a name="Social-DeleteWhatsAppMessageMedia-request-uri-originationPhoneNumberId"></a>
The unique identifier of the originating phone number associated with the media. Phone number identifiers are formatted as `phone-number-id-01234567890123456789012345678901`. Use [GetLinkedWhatsAppBusinessAccount](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html) to find a phone number's id.
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^phone-number-id-.*$)|(^arn:.*:phone-number-id/[0-9a-zA-Z]+$).*`
Required: Yes

## Request Body
<a name="API_DeleteWhatsAppMessageMedia_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteWhatsAppMessageMedia_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "success": boolean
}
```

## Response Elements
<a name="API_DeleteWhatsAppMessageMedia_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [success](#API_DeleteWhatsAppMessageMedia_ResponseSyntax) **   <a name="Social-DeleteWhatsAppMessageMedia-response-success"></a>
Success indicator for deleting the media file.
Type: Boolean

## Errors
<a name="API_DeleteWhatsAppMessageMedia_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedByMetaException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_DeleteWhatsAppMessageMedia_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/DeleteWhatsAppMessageMedia)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/DeleteWhatsAppMessageMedia)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/DeleteWhatsAppMessageMedia)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/DeleteWhatsAppMessageMedia)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/DeleteWhatsAppMessageMedia)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/DeleteWhatsAppMessageMedia)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/DeleteWhatsAppMessageMedia)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/DeleteWhatsAppMessageMedia)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/DeleteWhatsAppMessageMedia)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/DeleteWhatsAppMessageMedia)
