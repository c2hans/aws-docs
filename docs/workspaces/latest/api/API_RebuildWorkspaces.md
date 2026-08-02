---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_RebuildWorkspaces.html
---

# RebuildWorkspaces
<a name="API_RebuildWorkspaces"></a>

Rebuilds the specified WorkSpace.

You cannot rebuild a WorkSpace unless its state is `AVAILABLE`, `ERROR`, `UNHEALTHY`, `STOPPED`, or `REBOOTING`.

Rebuilding a WorkSpace is a potentially destructive action that can result in the loss of data. For more information, see [Rebuild a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/reset-workspace.html).

This operation is asynchronous and returns before the WorkSpaces have been completely rebuilt.

## Request Syntax
<a name="API_RebuildWorkspaces_RequestSyntax"></a>

```
{
   "RebuildWorkspaceRequests": [
      {
         "WorkspaceId": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_RebuildWorkspaces_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [RebuildWorkspaceRequests](#API_RebuildWorkspaces_RequestSyntax) **   <a name="WorkSpaces-RebuildWorkspaces-request-RebuildWorkspaceRequests"></a>
The WorkSpace to rebuild. You can specify a single WorkSpace.
Type: Array of [RebuildRequest](API_RebuildRequest.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

## Response Syntax
<a name="API_RebuildWorkspaces_ResponseSyntax"></a>

```
{
   "FailedRequests": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "WorkspaceId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_RebuildWorkspaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedRequests](#API_RebuildWorkspaces_ResponseSyntax) **   <a name="WorkSpaces-RebuildWorkspaces-response-FailedRequests"></a>
Information about the WorkSpace that could not be rebuilt.
Type: Array of [FailedWorkspaceChangeRequest](API_FailedWorkspaceChangeRequest.md) objects

## Errors
<a name="API_RebuildWorkspaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationNotSupportedException **
This operation is not supported.
 ** message **
The exception error message.
 ** reason **
The exception error reason.
HTTP Status Code: 400

## See Also
<a name="API_RebuildWorkspaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/RebuildWorkspaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/RebuildWorkspaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/RebuildWorkspaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/RebuildWorkspaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/RebuildWorkspaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/RebuildWorkspaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/RebuildWorkspaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/RebuildWorkspaces)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/RebuildWorkspaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/RebuildWorkspaces)
