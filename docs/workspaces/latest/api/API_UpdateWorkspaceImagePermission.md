---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateWorkspaceImagePermission.html
---

# UpdateWorkspaceImagePermission
<a name="API_UpdateWorkspaceImagePermission"></a>

Shares or unshares an image with one account in the same AWS Region by specifying whether that account has permission to copy the image. If the copy image permission is granted, the image is shared with that account. If the copy image permission is revoked, the image is unshared with the account.

After an image has been shared, the recipient account can copy the image to other Regions as needed.

In the China (Ningxia) Region, you can copy images only within the same Region.

In AWS GovCloud (US), to copy images to and from other Regions, contact Support.

For more information about sharing images, see [ Share or Unshare a Custom WorkSpaces Image](https://docs.aws.amazon.com/workspaces/latest/adminguide/share-custom-image.html).

**Note**
To delete an image that has been shared, you must unshare the image before you delete it.
Sharing Bring Your Own License (BYOL) images across AWS accounts isn't supported at this time in AWS GovCloud (US). To share BYOL images across accounts in AWS GovCloud (US), contact Support.

## Request Syntax
<a name="API_UpdateWorkspaceImagePermission_RequestSyntax"></a>

```
{
   "AllowCopyImage": {{boolean}},
   "ImageId": "{{string}}",
   "SharedAccountId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateWorkspaceImagePermission_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AllowCopyImage](#API_UpdateWorkspaceImagePermission_RequestSyntax) **   <a name="WorkSpaces-UpdateWorkspaceImagePermission-request-AllowCopyImage"></a>
The permission to copy the image. This permission can be revoked only after an image has been shared.
Type: Boolean
Required: Yes

 ** [ImageId](#API_UpdateWorkspaceImagePermission_RequestSyntax) **   <a name="WorkSpaces-UpdateWorkspaceImagePermission-request-ImageId"></a>
The identifier of the image.
Type: String
Pattern: `wsi-[0-9a-z]{9,63}$`
Required: Yes

 ** [SharedAccountId](#API_UpdateWorkspaceImagePermission_RequestSyntax) **   <a name="WorkSpaces-UpdateWorkspaceImagePermission-request-SharedAccountId"></a>
The identifier of the AWS account to share or unshare the image with.
Before sharing the image, confirm that you are sharing to the correct AWS account ID.
Type: String
Pattern: `^\d{12}$`
Required: Yes

## Response Elements
<a name="API_UpdateWorkspaceImagePermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateWorkspaceImagePermission_Errors"></a>

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
<a name="API_UpdateWorkspaceImagePermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/UpdateWorkspaceImagePermission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/UpdateWorkspaceImagePermission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/UpdateWorkspaceImagePermission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/UpdateWorkspaceImagePermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/UpdateWorkspaceImagePermission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/UpdateWorkspaceImagePermission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/UpdateWorkspaceImagePermission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/UpdateWorkspaceImagePermission)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/UpdateWorkspaceImagePermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/UpdateWorkspaceImagePermission)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
