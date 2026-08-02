---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ImportWorkspaceImage.html
---

# ImportWorkspaceImage
<a name="API_ImportWorkspaceImage"></a>

Imports the specified Windows 10 or 11 Bring Your Own License (BYOL) image into Amazon WorkSpaces. The image must be an already licensed Amazon EC2 image that is in your AWS account, and you must own the image. For more information about creating BYOL images, see [ Bring Your Own Windows Desktop Licenses](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html).

## Request Syntax
<a name="API_ImportWorkspaceImage_RequestSyntax"></a>

```
{
   "Applications": [ "{{string}}" ],
   "Ec2ImageId": "{{string}}",
   "ImageDescription": "{{string}}",
   "ImageName": "{{string}}",
   "IngestionProcess": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_ImportWorkspaceImage_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Applications](#API_ImportWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-ImportWorkspaceImage-request-Applications"></a>
If specified, the version of Microsoft Office to subscribe to. Valid only for Windows 10 and 11 BYOL images. For more information about subscribing to Office for BYOL images, see [ Bring Your Own Windows Desktop Licenses](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html).
+ Although this parameter is an array, only one item is allowed at this time.
+ During the image import process, non-GPU DCV (formerly WSP) WorkSpaces with Windows 11 support only `Microsoft_Office_2019`. GPU DCV (formerly WSP) WorkSpaces with Windows 11 do not support Office installation.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `Microsoft_Office_2016 | Microsoft_Office_2019`
Required: No

 ** [Ec2ImageId](#API_ImportWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-ImportWorkspaceImage-request-Ec2ImageId"></a>
The identifier of the EC2 image.
Type: String
Pattern: `^ami\-([a-f0-9]{8}|[a-f0-9]{17})$`
Required: Yes

 ** [ImageDescription](#API_ImportWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-ImportWorkspaceImage-request-ImageDescription"></a>
The description of the WorkSpace image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9_./() -]+$`
Required: Yes

 ** [ImageName](#API_ImportWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-ImportWorkspaceImage-request-ImageName"></a>
The name of the WorkSpace image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_./()\\-]+$`
Required: Yes

 ** [IngestionProcess](#API_ImportWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-ImportWorkspaceImage-request-IngestionProcess"></a>
The ingestion process to be used when importing the image, depending on which protocol you want to use for your BYOL Workspace image, either PCoIP, WSP, or bring your own protocol (BYOP). To use DCV, specify a value that ends in `_WSP`. To use PCoIP, specify a value that does not end in `_WSP`. To use BYOP, specify a value that ends in `_BYOP`.
For non-GPU-enabled bundles (bundles other than Graphics or GraphicsPro), specify `BYOL_REGULAR`, `BYOL_REGULAR_WSP`, or `BYOL_REGULAR_BYOP`, depending on the protocol.
The `BYOL_REGULAR_BYOP` and `BYOL_GRAPHICS_G4DN_BYOP` values are only supported by Amazon WorkSpaces Core. Contact your account team to be allow-listed to use these values. For more information, see [Amazon WorkSpaces Core](http://aws.amazon.com/workspaces/core/).
Type: String
Valid Values: `BYOL_REGULAR | BYOL_GRAPHICS | BYOL_GRAPHICSPRO | BYOL_GRAPHICS_G4DN | BYOL_REGULAR_WSP | BYOL_GRAPHICS_G4DN_WSP | BYOL_REGULAR_BYOP | BYOL_GRAPHICS_G4DN_BYOP`
Required: Yes

 ** [Tags](#API_ImportWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-ImportWorkspaceImage-request-Tags"></a>
The tags. Each WorkSpaces resource can have a maximum of 50 tags.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_ImportWorkspaceImage_ResponseSyntax"></a>

```
{
   "ImageId": "string"
}
```

## Response Elements
<a name="API_ImportWorkspaceImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ImageId](#API_ImportWorkspaceImage_ResponseSyntax) **   <a name="WorkSpaces-ImportWorkspaceImage-response-ImageId"></a>
The identifier of the WorkSpace image.
Type: String
Pattern: `wsi-[0-9a-z]{9,63}$`

## Errors
<a name="API_ImportWorkspaceImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** OperationNotSupportedException **
This operation is not supported.
 ** message **
The exception error message.
 ** reason **
The exception error reason.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The specified resource already exists.
HTTP Status Code: 400

 ** ResourceLimitExceededException **
Your resource limits have been exceeded.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

## See Also
<a name="API_ImportWorkspaceImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/ImportWorkspaceImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/ImportWorkspaceImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ImportWorkspaceImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/ImportWorkspaceImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ImportWorkspaceImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/ImportWorkspaceImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/ImportWorkspaceImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/ImportWorkspaceImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/ImportWorkspaceImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ImportWorkspaceImage)
