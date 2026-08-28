---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateWorkspaceBundle.html
---

# UpdateWorkspaceBundle
<a name="API_UpdateWorkspaceBundle"></a>

Updates a WorkSpace bundle with a new image. For more information about updating WorkSpace bundles, see [ Update a Custom WorkSpaces Bundle](https://docs.aws.amazon.com/workspaces/latest/adminguide/update-custom-bundle.html).

**Important**
Existing WorkSpaces aren't automatically updated when you update the bundle that they're based on. To update existing WorkSpaces that are based on a bundle that you've updated, you must either rebuild the WorkSpaces or delete and recreate them.

## Request Syntax
<a name="API_UpdateWorkspaceBundle_RequestSyntax"></a>

```
{
   "BundleId": "{{string}}",
   "ImageId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateWorkspaceBundle_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [BundleId](#API_UpdateWorkspaceBundle_RequestSyntax) **   <a name="WorkSpaces-UpdateWorkspaceBundle-request-BundleId"></a>
The identifier of the bundle.
Type: String
Pattern: `^wsb-[0-9a-z]{8,63}$`
Required: No

 ** [ImageId](#API_UpdateWorkspaceBundle_RequestSyntax) **   <a name="WorkSpaces-UpdateWorkspaceBundle-request-ImageId"></a>
The identifier of the image.
Type: String
Pattern: `wsi-[0-9a-z]{9,63}$`
Required: No

## Response Elements
<a name="API_UpdateWorkspaceBundle_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateWorkspaceBundle_Errors"></a>

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
<a name="API_UpdateWorkspaceBundle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/UpdateWorkspaceBundle)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/UpdateWorkspaceBundle)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/UpdateWorkspaceBundle)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/UpdateWorkspaceBundle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/UpdateWorkspaceBundle)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/UpdateWorkspaceBundle)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/UpdateWorkspaceBundle)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/UpdateWorkspaceBundle)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/UpdateWorkspaceBundle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/UpdateWorkspaceBundle)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
