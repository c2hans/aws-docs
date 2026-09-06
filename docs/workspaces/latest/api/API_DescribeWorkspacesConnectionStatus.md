---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspacesConnectionStatus.html
---

# DescribeWorkspacesConnectionStatus
<a name="API_DescribeWorkspacesConnectionStatus"></a>

Describes the connection status of the specified WorkSpaces.

## Request Syntax
<a name="API_DescribeWorkspacesConnectionStatus_RequestSyntax"></a>

```
{
   "NextToken": "{{string}}",
   "WorkspaceIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeWorkspacesConnectionStatus_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [NextToken](#API_DescribeWorkspacesConnectionStatus_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspacesConnectionStatus-request-NextToken"></a>
If you received a `NextToken` from a previous call that was paginated, provide this token to receive the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [WorkspaceIds](#API_DescribeWorkspacesConnectionStatus_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspacesConnectionStatus-request-WorkspaceIds"></a>
The identifiers of the WorkSpaces. You can specify up to 25 WorkSpaces.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Pattern: `^ws-[0-9a-z]{8,63}$`
Required: No

## Response Syntax
<a name="API_DescribeWorkspacesConnectionStatus_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "WorkspacesConnectionStatus": [
      {
         "ConnectionState": "string",
         "ConnectionStateCheckTimestamp": number,
         "LastKnownUserConnectionTimestamp": number,
         "WorkspaceId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeWorkspacesConnectionStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeWorkspacesConnectionStatus_ResponseSyntax) **   <a name="WorkSpaces-DescribeWorkspacesConnectionStatus-response-NextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [WorkspacesConnectionStatus](#API_DescribeWorkspacesConnectionStatus_ResponseSyntax) **   <a name="WorkSpaces-DescribeWorkspacesConnectionStatus-response-WorkspacesConnectionStatus"></a>
Information about the connection status of the WorkSpace.
Type: Array of [WorkspaceConnectionStatus](API_WorkspaceConnectionStatus.md) objects

## Errors
<a name="API_DescribeWorkspacesConnectionStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

## See Also
<a name="API_DescribeWorkspacesConnectionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DescribeWorkspacesConnectionStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DescribeWorkspacesConnectionStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DescribeWorkspacesConnectionStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DescribeWorkspacesConnectionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DescribeWorkspacesConnectionStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DescribeWorkspacesConnectionStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DescribeWorkspacesConnectionStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DescribeWorkspacesConnectionStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DescribeWorkspacesConnectionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DescribeWorkspacesConnectionStatus)
