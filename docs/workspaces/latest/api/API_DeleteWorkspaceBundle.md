---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteWorkspaceBundle.html
---

# DeleteWorkspaceBundle
<a name="API_DeleteWorkspaceBundle"></a>

Deletes the specified WorkSpace bundle. For more information about deleting WorkSpace bundles, see [ Delete a Custom WorkSpaces Bundle or Image](https://docs.aws.amazon.com/workspaces/latest/adminguide/delete_bundle.html).

## Request Syntax
<a name="API_DeleteWorkspaceBundle_RequestSyntax"></a>

```
{
   "BundleId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteWorkspaceBundle_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [BundleId](#API_DeleteWorkspaceBundle_RequestSyntax) **   <a name="WorkSpaces-DeleteWorkspaceBundle-request-BundleId"></a>
The identifier of the bundle.
Type: String
Pattern: `^wsb-[0-9a-z]{8,63}$`
Required: No

## Response Elements
<a name="API_DeleteWorkspaceBundle_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteWorkspaceBundle_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** ResourceAssociatedException **
The resource is associated with a directory.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

## See Also
<a name="API_DeleteWorkspaceBundle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DeleteWorkspaceBundle)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DeleteWorkspaceBundle)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DeleteWorkspaceBundle)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DeleteWorkspaceBundle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DeleteWorkspaceBundle)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DeleteWorkspaceBundle)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DeleteWorkspaceBundle)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DeleteWorkspaceBundle)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DeleteWorkspaceBundle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DeleteWorkspaceBundle)
