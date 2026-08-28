---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateUpdatedImage.html
---

# CreateUpdatedImage
<a name="API_CreateUpdatedImage"></a>

Creates a new image with the latest Windows operating system updates, driver updates, and WorkSpaces Applications agent software.

For more information, see the "Update an Image by Using Managed WorkSpaces Applications Image Updates" section in [Administer Your WorkSpaces Applications Images](https://docs.aws.amazon.com/appstream2/latest/developerguide/administer-images.html), in the *Amazon WorkSpaces Applications Administration Guide*.

## Request Syntax
<a name="API_CreateUpdatedImage_RequestSyntax"></a>

```
{
   "dryRun": {{boolean}},
   "existingImageName": "{{string}}",
   "newImageDescription": "{{string}}",
   "newImageDisplayName": "{{string}}",
   "newImageName": "{{string}}",
   "newImageTags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateUpdatedImage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [dryRun](#API_CreateUpdatedImage_RequestSyntax) **   <a name="WorkSpacesApplications-CreateUpdatedImage-request-dryRun"></a>
Indicates whether to display the status of image update availability before WorkSpaces Applications initiates the process of creating a new updated image. If this value is set to `true`, WorkSpaces Applications displays whether image updates are available. If this value is set to `false`, WorkSpaces Applications initiates the process of creating a new updated image without displaying whether image updates are available.
Type: Boolean
Required: No

 ** [existingImageName](#API_CreateUpdatedImage_RequestSyntax) **   <a name="WorkSpacesApplications-CreateUpdatedImage-request-existingImageName"></a>
The name of the image to update.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** [newImageDescription](#API_CreateUpdatedImage_RequestSyntax) **   <a name="WorkSpacesApplications-CreateUpdatedImage-request-newImageDescription"></a>
The description to display for the new image.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [newImageDisplayName](#API_CreateUpdatedImage_RequestSyntax) **   <a name="WorkSpacesApplications-CreateUpdatedImage-request-newImageDisplayName"></a>
The name to display for the new image.
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [newImageName](#API_CreateUpdatedImage_RequestSyntax) **   <a name="WorkSpacesApplications-CreateUpdatedImage-request-newImageName"></a>
The name of the new image. The name must be unique within the AWS account and Region.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** [newImageTags](#API_CreateUpdatedImage_RequestSyntax) **   <a name="WorkSpacesApplications-CreateUpdatedImage-request-newImageTags"></a>
The tags to associate with the new image. A tag is a key-value pair, and the value is optional. For example, Environment=Test. If you do not specify a value, Environment=.
Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following special characters:
\_ . : / = \+ \\ - @
If you do not specify a value, the value is set to an empty string.
For more information about tags, see [Tagging Your Resources](https://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-basic.html) in the *Amazon WorkSpaces Applications Administration Guide*.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(^(?!aws:).[\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_CreateUpdatedImage_ResponseSyntax"></a>

```
{
   "canUpdateImage": boolean,
   "image": {
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
<a name="API_CreateUpdatedImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [canUpdateImage](#API_CreateUpdatedImage_ResponseSyntax) **   <a name="WorkSpacesApplications-CreateUpdatedImage-response-canUpdateImage"></a>
Indicates whether a new image can be created.
Type: Boolean

 ** [image](#API_CreateUpdatedImage_ResponseSyntax) **   <a name="WorkSpacesApplications-CreateUpdatedImage-response-image"></a>
Describes an image.
Type: [Image](API_Image.md) object

## Errors
<a name="API_CreateUpdatedImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
An API error occurred. Wait a few minutes and try again.
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
<a name="API_CreateUpdatedImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/CreateUpdatedImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/CreateUpdatedImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/CreateUpdatedImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/CreateUpdatedImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/CreateUpdatedImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/CreateUpdatedImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/CreateUpdatedImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/CreateUpdatedImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/CreateUpdatedImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/CreateUpdatedImage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
