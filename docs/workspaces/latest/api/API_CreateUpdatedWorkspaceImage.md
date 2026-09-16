---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_CreateUpdatedWorkspaceImage.html
---

# CreateUpdatedWorkspaceImage
<a name="API_CreateUpdatedWorkspaceImage"></a>

Creates a new updated WorkSpace image based on the specified source image. The new updated WorkSpace image has the latest drivers and other updates required by the Amazon WorkSpaces components.

To determine which WorkSpace images need to be updated with the latest Amazon WorkSpaces requirements, use [ DescribeWorkspaceImages](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceImages.html).

**Note**
Only Windows 10, Windows Server 2016, and Windows Server 2019 WorkSpace images can be programmatically updated at this time.
Microsoft Windows updates and other application updates are not included in the update process.
The source WorkSpace image is not deleted. You can delete the source image after you've verified your new updated image and created a new bundle.

## Request Syntax
<a name="API_CreateUpdatedWorkspaceImage_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "SourceImageId": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateUpdatedWorkspaceImage_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreateUpdatedWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-CreateUpdatedWorkspaceImage-request-Description"></a>
A description of whether updates for the WorkSpace image are available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9_./() -]+$`
Required: Yes

 ** [Name](#API_CreateUpdatedWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-CreateUpdatedWorkspaceImage-request-Name"></a>
The name of the new updated WorkSpace image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_./()\\-]+$`
Required: Yes

 ** [SourceImageId](#API_CreateUpdatedWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-CreateUpdatedWorkspaceImage-request-SourceImageId"></a>
The identifier of the source WorkSpace image.
Type: String
Pattern: `wsi-[0-9a-z]{9,63}$`
Required: Yes

 ** [Tags](#API_CreateUpdatedWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-CreateUpdatedWorkspaceImage-request-Tags"></a>
The tags that you want to add to the new updated WorkSpace image.
To add tags at the same time when you're creating the updated image, you must create an IAM policy that grants your IAM user permissions to use `workspaces:CreateTags`.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateUpdatedWorkspaceImage_ResponseSyntax"></a>

```
{
   "ImageId": "string"
}
```

## Response Elements
<a name="API_CreateUpdatedWorkspaceImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ImageId](#API_CreateUpdatedWorkspaceImage_ResponseSyntax) **   <a name="WorkSpaces-CreateUpdatedWorkspaceImage-response-ImageId"></a>
The identifier of the new updated WorkSpace image.
Type: String
Pattern: `wsi-[0-9a-z]{9,63}$`

## Errors
<a name="API_CreateUpdatedWorkspaceImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** InvalidResourceStateException **
The state of the resource is not valid for this operation.
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
<a name="API_CreateUpdatedWorkspaceImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/CreateUpdatedWorkspaceImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/CreateUpdatedWorkspaceImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/CreateUpdatedWorkspaceImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/CreateUpdatedWorkspaceImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/CreateUpdatedWorkspaceImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/CreateUpdatedWorkspaceImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/CreateUpdatedWorkspaceImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/CreateUpdatedWorkspaceImage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/CreateUpdatedWorkspaceImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/CreateUpdatedWorkspaceImage)
