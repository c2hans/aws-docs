---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ImportCustomWorkspaceImage.html
---

# ImportCustomWorkspaceImage
<a name="API_ImportCustomWorkspaceImage"></a>

Imports the specified Windows 10 or 11 Bring Your Own License (BYOL) image into Amazon WorkSpaces using EC2 Image Builder. The image must be an already licensed image that is in your AWS account, and you must own the image. For more information about creating BYOL images, see [ Bring Your Own Windows Desktop Licenses](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html).

## Request Syntax
<a name="API_ImportCustomWorkspaceImage_RequestSyntax"></a>

```
{
   "ComputeType": "{{string}}",
   "ImageDescription": "{{string}}",
   "ImageName": "{{string}}",
   "ImageSource": { ... },
   "InfrastructureConfigurationArn": "{{string}}",
   "OsVersion": "{{string}}",
   "Platform": "{{string}}",
   "Protocol": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_ImportCustomWorkspaceImage_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ComputeType](#API_ImportCustomWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-ImportCustomWorkspaceImage-request-ComputeType"></a>
The supported compute type for the WorkSpace image.
Type: String
Valid Values: `BASE | GRAPHICS_G4DN | GRAPHICS_G6`
Required: Yes

 ** [ImageDescription](#API_ImportCustomWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-ImportCustomWorkspaceImage-request-ImageDescription"></a>
The description of the WorkSpace image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9_./() -]+$`
Required: Yes

 ** [ImageName](#API_ImportCustomWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-ImportCustomWorkspaceImage-request-ImageName"></a>
The name of the WorkSpace image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_./()\\-]+$`
Required: Yes

 ** [ImageSource](#API_ImportCustomWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-ImportCustomWorkspaceImage-request-ImageSource"></a>
The options for image import source.
Type: [ImageSourceIdentifier](API_ImageSourceIdentifier.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [InfrastructureConfigurationArn](#API_ImportCustomWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-ImportCustomWorkspaceImage-request-InfrastructureConfigurationArn"></a>
The infrastructure configuration ARN that specifies how the WorkSpace image is built.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):infrastructure-configuration/[a-z0-9-_]+$`
Required: Yes

 ** [OsVersion](#API_ImportCustomWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-ImportCustomWorkspaceImage-request-OsVersion"></a>
The OS version for the WorkSpace image source.
Type: String
Valid Values: `Windows_10 | Windows_11`
Required: Yes

 ** [Platform](#API_ImportCustomWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-ImportCustomWorkspaceImage-request-Platform"></a>
The platform for the WorkSpace image source.
Type: String
Valid Values: `WINDOWS`
Required: Yes

 ** [Protocol](#API_ImportCustomWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-ImportCustomWorkspaceImage-request-Protocol"></a>
The supported protocol for the WorkSpace image. Windows 11 does not support PCOIP protocol.
Type: String
Valid Values: `PCOIP | DCV | BYOP`
Required: Yes

 ** [Tags](#API_ImportCustomWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-ImportCustomWorkspaceImage-request-Tags"></a>
The resource tags. Each WorkSpaces resource can have a maximum of 50 tags.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_ImportCustomWorkspaceImage_ResponseSyntax"></a>

```
{
   "ImageId": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_ImportCustomWorkspaceImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ImageId](#API_ImportCustomWorkspaceImage_ResponseSyntax) **   <a name="WorkSpaces-ImportCustomWorkspaceImage-response-ImageId"></a>
The identifier of the WorkSpace image.
Type: String
Pattern: `wsi-[0-9a-z]{9,63}$`

 ** [State](#API_ImportCustomWorkspaceImage_ResponseSyntax) **   <a name="WorkSpaces-ImportCustomWorkspaceImage-response-State"></a>
The state of the WorkSpace image.
Type: String
Valid Values: `PENDING | IN_PROGRESS | PROCESSING_SOURCE_IMAGE | IMAGE_TESTING_START | UPDATING_OPERATING_SYSTEM | IMAGE_COMPATIBILITY_CHECKING | IMAGE_TESTING_GENERALIZATION | CREATING_TEST_INSTANCE | INSTALLING_COMPONENTS | GENERALIZING | VALIDATING | PUBLISHING | COMPLETED | ERROR`

## Errors
<a name="API_ImportCustomWorkspaceImage_Errors"></a>

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
<a name="API_ImportCustomWorkspaceImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/ImportCustomWorkspaceImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/ImportCustomWorkspaceImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ImportCustomWorkspaceImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/ImportCustomWorkspaceImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ImportCustomWorkspaceImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/ImportCustomWorkspaceImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/ImportCustomWorkspaceImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/ImportCustomWorkspaceImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/ImportCustomWorkspaceImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ImportCustomWorkspaceImage)
