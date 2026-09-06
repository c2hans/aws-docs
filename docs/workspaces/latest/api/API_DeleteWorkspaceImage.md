---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteWorkspaceImage.html
---

# DeleteWorkspaceImage
<a name="API_DeleteWorkspaceImage"></a>

Deletes the specified image from your account. To delete an image, you must first delete any bundles that are associated with the image and unshare the image if it is shared with other accounts.

## Request Syntax
<a name="API_DeleteWorkspaceImage_RequestSyntax"></a>

```
{
   "ImageId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteWorkspaceImage_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ImageId](#API_DeleteWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-DeleteWorkspaceImage-request-ImageId"></a>
The identifier of the image.
Type: String
Pattern: `wsi-[0-9a-z]{9,63}$`
Required: Yes

## Response Elements
<a name="API_DeleteWorkspaceImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteWorkspaceImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidResourceStateException **
The state of the resource is not valid for this operation.
HTTP Status Code: 400

 ** ResourceAssociatedException **
The resource is associated with a directory.
HTTP Status Code: 400

## See Also
<a name="API_DeleteWorkspaceImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DeleteWorkspaceImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DeleteWorkspaceImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DeleteWorkspaceImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DeleteWorkspaceImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DeleteWorkspaceImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DeleteWorkspaceImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DeleteWorkspaceImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DeleteWorkspaceImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DeleteWorkspaceImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DeleteWorkspaceImage)
