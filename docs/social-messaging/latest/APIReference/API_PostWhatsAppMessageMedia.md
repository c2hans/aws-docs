---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_PostWhatsAppMessageMedia.html
---

# PostWhatsAppMessageMedia
<a name="API_PostWhatsAppMessageMedia"></a>

Upload a media file to the WhatsApp service. Only the specified `originationPhoneNumberId` has the permissions to send the media file when using [SendWhatsAppMessage](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_SendWhatsAppMessage.html). You must use either `sourceS3File` or `sourceS3PresignedUrl` for the source. If both or neither are specified then an `InvalidParameterException` is returned.

## Request Syntax
<a name="API_PostWhatsAppMessageMedia_RequestSyntax"></a>

```
POST /v1/whatsapp/media HTTP/1.1
Content-type: application/json

{
   "originationPhoneNumberId": "{{string}}",
   "sourceS3File": {
      "bucketName": "{{string}}",
      "key": "{{string}}"
   },
   "sourceS3PresignedUrl": {
      "headers": {
         "{{string}}" : "{{string}}"
      },
      "url": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_PostWhatsAppMessageMedia_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PostWhatsAppMessageMedia_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [originationPhoneNumberId](#API_PostWhatsAppMessageMedia_RequestSyntax) **   <a name="Social-PostWhatsAppMessageMedia-request-originationPhoneNumberId"></a>
The ID of the phone number to associate with the WhatsApp media file. The phone number identifiers are formatted as `phone-number-id-01234567890123456789012345678901`. Use [GetLinkedWhatsAppBusinessAccount](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html) to find a phone number's id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^phone-number-id-.*$)|(^arn:.*:phone-number-id/[0-9a-zA-Z]+$).*`
Required: Yes

 ** [sourceS3File](#API_PostWhatsAppMessageMedia_RequestSyntax) **   <a name="Social-PostWhatsAppMessageMedia-request-sourceS3File"></a>
The source S3 url for the media file.
Type: [S3File](API_S3File.md) object
Required: No

 ** [sourceS3PresignedUrl](#API_PostWhatsAppMessageMedia_RequestSyntax) **   <a name="Social-PostWhatsAppMessageMedia-request-sourceS3PresignedUrl"></a>
The source presign url of the media file.
Type: [S3PresignedUrl](API_S3PresignedUrl.md) object
Required: No

## Response Syntax
<a name="API_PostWhatsAppMessageMedia_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "mediaId": "string"
}
```

## Response Elements
<a name="API_PostWhatsAppMessageMedia_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [mediaId](#API_PostWhatsAppMessageMedia_ResponseSyntax) **   <a name="Social-PostWhatsAppMessageMedia-response-mediaId"></a>
The unique identifier of the posted WhatsApp message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9]+`

## Errors
<a name="API_PostWhatsAppMessageMedia_Errors"></a>

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
<a name="API_PostWhatsAppMessageMedia_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/PostWhatsAppMessageMedia)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/PostWhatsAppMessageMedia)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/PostWhatsAppMessageMedia)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/PostWhatsAppMessageMedia)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/PostWhatsAppMessageMedia)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/PostWhatsAppMessageMedia)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/PostWhatsAppMessageMedia)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/PostWhatsAppMessageMedia)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/PostWhatsAppMessageMedia)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/PostWhatsAppMessageMedia)
