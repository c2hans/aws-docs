---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetWhatsAppMessageMedia.html
---

# GetWhatsAppMessageMedia
<a name="API_GetWhatsAppMessageMedia"></a>

Get a media file from the WhatsApp service. On successful completion the media file is retrieved from Meta and stored in the specified Amazon S3 bucket. Use either `destinationS3File` or `destinationS3PresignedUrl` for the destination. If both are used then an `InvalidParameterException` is returned.

## Request Syntax
<a name="API_GetWhatsAppMessageMedia_RequestSyntax"></a>

```
POST /v1/whatsapp/media/get HTTP/1.1
Content-type: application/json

{
   "destinationS3File": {
      "bucketName": "{{string}}",
      "key": "{{string}}"
   },
   "destinationS3PresignedUrl": {
      "headers": {
         "{{string}}" : "{{string}}"
      },
      "url": "{{string}}"
   },
   "mediaId": "{{string}}",
   "metadataOnly": {{boolean}},
   "originationPhoneNumberId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetWhatsAppMessageMedia_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetWhatsAppMessageMedia_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [destinationS3File](#API_GetWhatsAppMessageMedia_RequestSyntax) **   <a name="Social-GetWhatsAppMessageMedia-request-destinationS3File"></a>
The `bucketName` and `key` of the S3 media file.
Type: [S3File](API_S3File.md) object
Required: No

 ** [destinationS3PresignedUrl](#API_GetWhatsAppMessageMedia_RequestSyntax) **   <a name="Social-GetWhatsAppMessageMedia-request-destinationS3PresignedUrl"></a>
The presign url of the media file.
Type: [S3PresignedUrl](API_S3PresignedUrl.md) object
Required: No

 ** [mediaId](#API_GetWhatsAppMessageMedia_RequestSyntax) **   <a name="Social-GetWhatsAppMessageMedia-request-mediaId"></a>
The unique identifier for the media file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9]+`
Required: Yes

 ** [metadataOnly](#API_GetWhatsAppMessageMedia_RequestSyntax) **   <a name="Social-GetWhatsAppMessageMedia-request-metadataOnly"></a>
Set to `True` to get only the metadata for the file.
Type: Boolean
Required: No

 ** [originationPhoneNumberId](#API_GetWhatsAppMessageMedia_RequestSyntax) **   <a name="Social-GetWhatsAppMessageMedia-request-originationPhoneNumberId"></a>
The unique identifier of the originating phone number for the WhatsApp message media. The phone number identifiers are formatted as `phone-number-id-01234567890123456789012345678901`. Use [GetLinkedWhatsAppBusinessAccount](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html) to find a phone number's id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^phone-number-id-.*$)|(^arn:.*:phone-number-id/[0-9a-zA-Z]+$).*`
Required: Yes

## Response Syntax
<a name="API_GetWhatsAppMessageMedia_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "fileSize": number,
   "mimeType": "string"
}
```

## Response Elements
<a name="API_GetWhatsAppMessageMedia_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [fileSize](#API_GetWhatsAppMessageMedia_ResponseSyntax) **   <a name="Social-GetWhatsAppMessageMedia-response-fileSize"></a>
The size of the media file, in KB.
Type: Long

 ** [mimeType](#API_GetWhatsAppMessageMedia_ResponseSyntax) **   <a name="Social-GetWhatsAppMessageMedia-response-mimeType"></a>
The MIME type of the media.
Type: String

## Errors
<a name="API_GetWhatsAppMessageMedia_Errors"></a>

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
<a name="API_GetWhatsAppMessageMedia_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/GetWhatsAppMessageMedia)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/GetWhatsAppMessageMedia)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/GetWhatsAppMessageMedia)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/GetWhatsAppMessageMedia)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/GetWhatsAppMessageMedia)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/GetWhatsAppMessageMedia)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/GetWhatsAppMessageMedia)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/GetWhatsAppMessageMedia)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/GetWhatsAppMessageMedia)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/GetWhatsAppMessageMedia)
