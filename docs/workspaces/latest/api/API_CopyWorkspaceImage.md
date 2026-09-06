---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_CopyWorkspaceImage.html
---

# CopyWorkspaceImage
<a name="API_CopyWorkspaceImage"></a>

Copies the specified image from the specified Region to the current Region. For more information about copying images, see [ Copy a Custom WorkSpaces Image](https://docs.aws.amazon.com/workspaces/latest/adminguide/copy-custom-image.html).

In the China (Ningxia) Region, you can copy images only within the same Region.

In AWS GovCloud (US), to copy images to and from other Regions, contact Support.

**Important**
Before copying a shared image, be sure to verify that it has been shared from the correct AWS account. To determine if an image has been shared and to see the ID of the AWS account that owns an image, use the [DescribeWorkSpaceImages](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceImages.html) and [DescribeWorkspaceImagePermissions](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceImagePermissions.html) API operations.

## Request Syntax
<a name="API_CopyWorkspaceImage_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "SourceImageId": "{{string}}",
   "SourceRegion": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CopyWorkspaceImage_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CopyWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-CopyWorkspaceImage-request-Description"></a>
A description of the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9_./() -]+$`
Required: No

 ** [Name](#API_CopyWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-CopyWorkspaceImage-request-Name"></a>
The name of the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_./()\\-]+$`
Required: Yes

 ** [SourceImageId](#API_CopyWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-CopyWorkspaceImage-request-SourceImageId"></a>
The identifier of the source image.
Type: String
Pattern: `wsi-[0-9a-z]{9,63}$`
Required: Yes

 ** [SourceRegion](#API_CopyWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-CopyWorkspaceImage-request-SourceRegion"></a>
The identifier of the source Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 31.
Pattern: `^[-0-9a-z]{1,31}$`
Required: Yes

 ** [Tags](#API_CopyWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-CopyWorkspaceImage-request-Tags"></a>
The tags for the image.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CopyWorkspaceImage_ResponseSyntax"></a>

```
{
   "ImageId": "string"
}
```

## Response Elements
<a name="API_CopyWorkspaceImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ImageId](#API_CopyWorkspaceImage_ResponseSyntax) **   <a name="WorkSpaces-CopyWorkspaceImage-response-ImageId"></a>
The identifier of the image.
Type: String
Pattern: `wsi-[0-9a-z]{9,63}$`

## Errors
<a name="API_CopyWorkspaceImage_Errors"></a>

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

 ** ResourceUnavailableException **
The specified resource is not available.
 ** message **
The exception error message.
 ** ResourceId **
The identifier of the resource that is not available.
HTTP Status Code: 400

## See Also
<a name="API_CopyWorkspaceImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/CopyWorkspaceImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/CopyWorkspaceImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/CopyWorkspaceImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/CopyWorkspaceImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/CopyWorkspaceImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/CopyWorkspaceImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/CopyWorkspaceImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/CopyWorkspaceImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/CopyWorkspaceImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/CopyWorkspaceImage)
