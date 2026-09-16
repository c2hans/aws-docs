---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_RestoreWorkspace.html
---

# RestoreWorkspace
<a name="API_RestoreWorkspace"></a>

Restores the specified WorkSpace to its last known healthy state.

You cannot restore a WorkSpace unless its state is ` AVAILABLE`, `ERROR`, `UNHEALTHY`, or `STOPPED`.

Restoring a WorkSpace is a potentially destructive action that can result in the loss of data. For more information, see [Restore a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/restore-workspace.html).

This operation is asynchronous and returns before the WorkSpace is completely restored.

## Request Syntax
<a name="API_RestoreWorkspace_RequestSyntax"></a>

```
{
   "WorkspaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_RestoreWorkspace_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [WorkspaceId](#API_RestoreWorkspace_RequestSyntax) **   <a name="WorkSpaces-RestoreWorkspace-request-WorkspaceId"></a>
The identifier of the WorkSpace.
Type: String
Pattern: `^ws-[0-9a-z]{8,63}$`
Required: Yes

## Response Elements
<a name="API_RestoreWorkspace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RestoreWorkspace_Errors"></a>

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

## See Also
<a name="API_RestoreWorkspace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/RestoreWorkspace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/RestoreWorkspace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/RestoreWorkspace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/RestoreWorkspace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/RestoreWorkspace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/RestoreWorkspace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/RestoreWorkspace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/RestoreWorkspace)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/RestoreWorkspace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/RestoreWorkspace)
