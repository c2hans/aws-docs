---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_StartWorkspaces.html
---

# StartWorkspaces
<a name="API_StartWorkspaces"></a>

Starts the specified WorkSpaces.

You cannot start a WorkSpace unless it has a running mode of `AutoStop` or `Manual` and a state of `STOPPED`.

## Request Syntax
<a name="API_StartWorkspaces_RequestSyntax"></a>

```
{
   "StartWorkspaceRequests": [
      {
         "WorkspaceId": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_StartWorkspaces_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [StartWorkspaceRequests](#API_StartWorkspaces_RequestSyntax) **   <a name="WorkSpaces-StartWorkspaces-request-StartWorkspaceRequests"></a>
The WorkSpaces to start. You can specify up to 25 WorkSpaces.
Type: Array of [StartRequest](API_StartRequest.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: Yes

## Response Syntax
<a name="API_StartWorkspaces_ResponseSyntax"></a>

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
<a name="API_StartWorkspaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedRequests](#API_StartWorkspaces_ResponseSyntax) **   <a name="WorkSpaces-StartWorkspaces-response-FailedRequests"></a>
Information about the WorkSpaces that could not be started.
Type: Array of [FailedWorkspaceChangeRequest](API_FailedWorkspaceChangeRequest.md) objects

## Errors
<a name="API_StartWorkspaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_StartWorkspaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/StartWorkspaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/StartWorkspaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/StartWorkspaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/StartWorkspaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/StartWorkspaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/StartWorkspaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/StartWorkspaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/StartWorkspaces)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/StartWorkspaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/StartWorkspaces)
