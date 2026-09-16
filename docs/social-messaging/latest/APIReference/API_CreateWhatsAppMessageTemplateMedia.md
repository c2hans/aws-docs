---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_CreateWhatsAppMessageTemplateMedia.html
---

# CreateWhatsAppMessageTemplateMedia
<a name="API_CreateWhatsAppMessageTemplateMedia"></a>

Uploads media for use in a WhatsApp message template.

## Request Syntax
<a name="API_CreateWhatsAppMessageTemplateMedia_RequestSyntax"></a>

```
POST /v1/whatsapp/template/media HTTP/1.1
Content-type: application/json

{
   "id": "{{string}}",
   "sourceS3File": {
      "bucketName": "{{string}}",
      "key": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateWhatsAppMessageTemplateMedia_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateWhatsAppMessageTemplateMedia_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [id](#API_CreateWhatsAppMessageTemplateMedia_RequestSyntax) **   <a name="Social-CreateWhatsAppMessageTemplateMedia-request-id"></a>
The ID of the WhatsApp Business Account associated with this media upload.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^waba-.*$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`
Required: Yes

 ** [sourceS3File](#API_CreateWhatsAppMessageTemplateMedia_RequestSyntax) **   <a name="Social-CreateWhatsAppMessageTemplateMedia-request-sourceS3File"></a>
Contains information for the S3 bucket that contains media files.
Type: [S3File](API_S3File.md) object
Required: No

## Response Syntax
<a name="API_CreateWhatsAppMessageTemplateMedia_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "metaHeaderHandle": "string"
}
```

## Response Elements
<a name="API_CreateWhatsAppMessageTemplateMedia_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [metaHeaderHandle](#API_CreateWhatsAppMessageTemplateMedia_ResponseSyntax) **   <a name="Social-CreateWhatsAppMessageTemplateMedia-response-metaHeaderHandle"></a>
The handle assigned to the uploaded media by Meta, used to reference the media in templates.
Type: String

## Errors
<a name="API_CreateWhatsAppMessageTemplateMedia_Errors"></a>

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
<a name="API_CreateWhatsAppMessageTemplateMedia_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/CreateWhatsAppMessageTemplateMedia)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/CreateWhatsAppMessageTemplateMedia)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/CreateWhatsAppMessageTemplateMedia)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/CreateWhatsAppMessageTemplateMedia)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/CreateWhatsAppMessageTemplateMedia)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/CreateWhatsAppMessageTemplateMedia)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/CreateWhatsAppMessageTemplateMedia)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/CreateWhatsAppMessageTemplateMedia)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/CreateWhatsAppMessageTemplateMedia)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/CreateWhatsAppMessageTemplateMedia)
