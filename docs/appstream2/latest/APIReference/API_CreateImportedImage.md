---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateImportedImage.html
---

# CreateImportedImage
<a name="API_CreateImportedImage"></a>

Creates a custom WorkSpaces Applications image by importing an EC2 AMI. This allows you to use your own customized AMI to create WorkSpaces Applications images that support additional instance types beyond the standard stream.\* instances.

## Request Syntax
<a name="API_CreateImportedImage_RequestSyntax"></a>

```
{
   "AgentSoftwareVersion": "{{string}}",
   "AppCatalogConfig": [
      {
         "AbsoluteAppPath": "{{string}}",
         "AbsoluteIconPath": "{{string}}",
         "AbsoluteManifestPath": "{{string}}",
         "DisplayName": "{{string}}",
         "LaunchParameters": "{{string}}",
         "Name": "{{string}}",
         "WorkingDirectory": "{{string}}"
      }
   ],
   "Description": "{{string}}",
   "DisplayName": "{{string}}",
   "DryRun": {{boolean}},
   "IamRoleArn": "{{string}}",
   "Name": "{{string}}",
   "RuntimeValidationConfig": {
      "IntendedInstanceType": "{{string}}"
   },
   "SourceAmiId": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "WorkspaceImageId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateImportedImage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AgentSoftwareVersion](#API_CreateImportedImage_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImportedImage-request-AgentSoftwareVersion"></a>
The version of the WorkSpaces Applications agent to use for the imported image. Choose CURRENT\_LATEST to use the agent version available at the time of import, or ALWAYS\_LATEST to automatically update to the latest agent version when new versions are released.
Type: String
Valid Values: `CURRENT_LATEST | ALWAYS_LATEST`
Required: No

 ** [AppCatalogConfig](#API_CreateImportedImage_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImportedImage-request-AppCatalogConfig"></a>
Configuration for the application catalog of the imported image. This allows you to specify applications available for streaming, including their paths, icons, and launch parameters. This field contains sensitive data.
Type: Array of [ApplicationConfig](API_ApplicationConfig.md) objects
Array Members: Maximum number of 50 items.
Required: No

 ** [Description](#API_CreateImportedImage_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImportedImage-request-Description"></a>
An optional description for the imported image. The description must match approved regex patterns and can be up to 256 characters.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^[a-zA-Z0-9_.() -]+$`
Required: No

 ** [DisplayName](#API_CreateImportedImage_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImportedImage-request-DisplayName"></a>
An optional display name for the imported image. The display name must match approved regex patterns and can be up to 100 characters.
Type: String
Length Constraints: Maximum length of 100.
Pattern: `^[a-zA-Z0-9_.() -]+$`
Required: No

 ** [DryRun](#API_CreateImportedImage_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImportedImage-request-DryRun"></a>
When set to true, performs validation checks without actually creating the imported image. Use this to verify your configuration before executing the actual import operation.
Type: Boolean
Required: No

 ** [IamRoleArn](#API_CreateImportedImage_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImportedImage-request-IamRoleArn"></a>
The ARN of the IAM role that allows WorkSpaces Applications to access your AMI. The role must have permissions to modify image attributes and describe images, with a trust relationship allowing appstream.amazonaws.com to assume the role.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** [Name](#API_CreateImportedImage_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImportedImage-request-Name"></a>
A unique name for the imported image. The name must be between 1 and 100 characters and can contain letters, numbers, underscores, periods, and hyphens.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** [RuntimeValidationConfig](#API_CreateImportedImage_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImportedImage-request-RuntimeValidationConfig"></a>
Configuration for runtime validation of the imported image. When specified, WorkSpaces Applications provisions an instance to test streaming functionality, which helps ensure the image is suitable for use.
Type: [RuntimeValidationConfig](API_RuntimeValidationConfig.md) object
Required: No

 ** [SourceAmiId](#API_CreateImportedImage_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImportedImage-request-SourceAmiId"></a>
The ID of the EC2 AMI to import.
Type: String
Pattern: `^ami-[a-z0-9]{8,17}$`
Required: No

 ** [Tags](#API_CreateImportedImage_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImportedImage-request-Tags"></a>
The tags to apply to the imported image. Tags help you organize and manage your WorkSpaces Applications resources.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(^(?!aws:).[\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** [WorkspaceImageId](#API_CreateImportedImage_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImportedImage-request-WorkspaceImageId"></a>
The ID of the Workspaces Image to import.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 67.
Pattern: `^wsi-[0-9a-z]{8,63}$`
Required: No

## Response Syntax
<a name="API_CreateImportedImage_ResponseSyntax"></a>

```
{
   "Image": {
      "Applications": [
         {
            "AppBlockArn": "string",
            "Arn": "string",
            "CreatedTime": number,
            "Description": "string",
            "DisplayName": "string",
            "Enabled": boolean,
            "IconS3Location": {
               "S3Bucket": "string",
               "S3Key": "string"
            },
            "IconURL": "string",
            "InstanceFamilies": [ "string" ],
            "LaunchParameters": "string",
            "LaunchPath": "string",
            "Metadata": {
               "string" : "string"
            },
            "Name": "string",
            "Platforms": [ "string" ],
            "WorkingDirectory": "string"
         }
      ],
      "AppstreamAgentVersion": "string",
      "Arn": "string",
      "BaseImageArn": "string",
      "CreatedTime": number,
      "Description": "string",
      "DisplayName": "string",
      "DynamicAppProvidersEnabled": "string",
      "ImageBuilderName": "string",
      "ImageBuilderSupported": boolean,
      "ImageErrors": [
         {
            "ErrorCode": "string",
            "ErrorMessage": "string",
            "ErrorTimestamp": number
         }
      ],
      "ImagePermissions": {
         "allowFleet": boolean,
         "allowImageBuilder": boolean
      },
      "ImageSharedWithOthers": "string",
      "ImageType": "string",
      "LatestAppstreamAgentVersion": "string",
      "ManagedSoftwareIncluded": boolean,
      "Name": "string",
      "Platform": "string",
      "PublicBaseImageReleasedDate": number,
      "State": "string",
      "StateChangeReason": {
         "Code": "string",
         "Message": "string"
      },
      "SupportedInstanceFamilies": [ "string" ],
      "Visibility": "string"
   }
}
```

## Response Elements
<a name="API_CreateImportedImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Image](#API_CreateImportedImage_ResponseSyntax) **   <a name="WorkSpacesApplications-CreateImportedImage-response-Image"></a>
Describes an image.
Type: [Image](API_Image.md) object

## Errors
<a name="API_CreateImportedImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DryRunOperationException **
The exception that is thrown when a dry run operation is requested. This indicates that the validation checks have been performed successfully, but no actual resources were created or modified.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** IncompatibleImageException **
The image can't be updated because it's not compatible for updates.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** InvalidAccountStatusException **
The resource cannot be created because your AWS account is suspended. For assistance, contact AWS Support.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** InvalidParameterCombinationException **
Indicates an incorrect combination of parameters, or a missing parameter.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** InvalidRoleException **
The specified role is invalid.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** LimitExceededException **
The requested limit exceeds the permitted limit for an account.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The specified resource already exists.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateImportedImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/CreateImportedImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/CreateImportedImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/CreateImportedImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/CreateImportedImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/CreateImportedImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/CreateImportedImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/CreateImportedImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/CreateImportedImage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/CreateImportedImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/CreateImportedImage)
