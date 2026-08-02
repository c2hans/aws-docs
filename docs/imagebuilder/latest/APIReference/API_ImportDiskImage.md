---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImportDiskImage.html
---

# ImportDiskImage
<a name="API_ImportDiskImage"></a>

Import a Windows operating system image from a verified Microsoft ISO disk file. The following disk images are supported:
+ Windows 11 Enterprise

## Request Syntax
<a name="API_ImportDiskImage_RequestSyntax"></a>

```
PUT /ImportDiskImage HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "executionRole": "{{string}}",
   "infrastructureConfigurationArn": "{{string}}",
   "loggingConfiguration": {
      "logGroupName": "{{string}}"
   },
   "name": "{{string}}",
   "osVersion": "{{string}}",
   "platform": "{{string}}",
   "registerImageOptions": {
      "secureBootEnabled": {{boolean}},
      "uefiData": "{{string}}"
   },
   "semanticVersion": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "uri": "{{string}}",
   "windowsConfiguration": {
      "imageIndex": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_ImportDiskImage_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ImportDiskImage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_ImportDiskImage_RequestSyntax) **   <a name="imagebuilder-ImportDiskImage-request-clientToken"></a>
Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [description](#API_ImportDiskImage_RequestSyntax) **   <a name="imagebuilder-ImportDiskImage-request-description"></a>
The description for your disk image import.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [executionRole](#API_ImportDiskImage_RequestSyntax) **   <a name="imagebuilder-ImportDiskImage-request-executionRole"></a>
The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions to import an image from a Microsoft ISO file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(?:arn:aws(?:-[a-z]+)*:iam::[0-9]{12}:role/)?[a-zA-Z_0-9+=,.@\-_/]+$`
Required: No

 ** [infrastructureConfigurationArn](#API_ImportDiskImage_RequestSyntax) **   <a name="imagebuilder-ImportDiskImage-request-infrastructureConfigurationArn"></a>
The Amazon Resource Name (ARN) of the infrastructure configuration resource that's used for launching the EC2 instance on which the ISO image is built.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):infrastructure-configuration/[a-z0-9-_]+$`
Required: Yes

 ** [loggingConfiguration](#API_ImportDiskImage_RequestSyntax) **   <a name="imagebuilder-ImportDiskImage-request-loggingConfiguration"></a>
Define logging configuration for the image build process.
Type: [ImageLoggingConfiguration](API_ImageLoggingConfiguration.md) object
Required: No

 ** [name](#API_ImportDiskImage_RequestSyntax) **   <a name="imagebuilder-ImportDiskImage-request-name"></a>
The name of the image resource that's created from the import.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: Yes

 ** [osVersion](#API_ImportDiskImage_RequestSyntax) **   <a name="imagebuilder-ImportDiskImage-request-osVersion"></a>
The operating system version for the imported image. Allowed values include the following: `Microsoft Windows 11`.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [platform](#API_ImportDiskImage_RequestSyntax) **   <a name="imagebuilder-ImportDiskImage-request-platform"></a>
The operating system platform for the imported image. Allowed values include the following: `Windows`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [registerImageOptions](#API_ImportDiskImage_RequestSyntax) **   <a name="imagebuilder-ImportDiskImage-request-registerImageOptions"></a>
Configures Secure Boot and UEFI settings for the imported image.
Type: [RegisterImageOptions](API_RegisterImageOptions.md) object
Required: No

 ** [semanticVersion](#API_ImportDiskImage_RequestSyntax) **   <a name="imagebuilder-ImportDiskImage-request-semanticVersion"></a>
The semantic version to attach to the image that's created during the import process. This version follows the semantic version syntax.
Type: String
Pattern: `^[0-9]+\.[0-9]+\.[0-9]+$`
Required: Yes

 ** [tags](#API_ImportDiskImage_RequestSyntax) **   <a name="imagebuilder-ImportDiskImage-request-tags"></a>
Tags that are attached to image resources created from the import.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [uri](#API_ImportDiskImage_RequestSyntax) **   <a name="imagebuilder-ImportDiskImage-request-uri"></a>
The `uri` of the ISO disk file that's stored in Amazon S3.
Type: String
Required: Yes

 ** [windowsConfiguration](#API_ImportDiskImage_RequestSyntax) **   <a name="imagebuilder-ImportDiskImage-request-windowsConfiguration"></a>
Specifies Windows settings for ISO imports.
Type: [WindowsConfiguration](API_WindowsConfiguration.md) object
Required: No

## Response Syntax
<a name="API_ImportDiskImage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "imageBuildVersionArn": "string"
}
```

## Response Elements
<a name="API_ImportDiskImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_ImportDiskImage_ResponseSyntax) **   <a name="imagebuilder-ImportDiskImage-response-clientToken"></a>
The client token that uniquely identifies the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [imageBuildVersionArn](#API_ImportDiskImage_ResponseSyntax) **   <a name="imagebuilder-ImportDiskImage-response-imageBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the output AMI that was created from the ISO disk file.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

## Errors
<a name="API_ImportDiskImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permissions to perform the requested operation.
HTTP Status Code: 403

 ** ClientException **
These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.
HTTP Status Code: 400

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

 ** TooManyRequestsException **
You have attempted too many requests for the specific operation.
HTTP Status Code: 429

## See Also
<a name="API_ImportDiskImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ImportDiskImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ImportDiskImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ImportDiskImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ImportDiskImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ImportDiskImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ImportDiskImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ImportDiskImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ImportDiskImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ImportDiskImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ImportDiskImage)
