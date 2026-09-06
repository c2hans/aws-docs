---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspacesPools.html
---

# DescribeWorkspacesPools
<a name="API_DescribeWorkspacesPools"></a>

**Note**
End of support notice: On December 31, 2027, AWS will end support for Amazon WorkSpaces Pools. After December 31, 2027, you will no longer be able to access the Amazon WorkSpaces Pools console or Amazon WorkSpaces Pools resources. For more information, see [Amazon WorkSpaces Pools end of support](https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-pools-end-of-support.html).

Describes the specified WorkSpaces Pools.

## Request Syntax
<a name="API_DescribeWorkspacesPools_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Operator": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "PoolIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeWorkspacesPools_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeWorkspacesPools_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspacesPools-request-Filters"></a>
The filter conditions for the WorkSpaces Pool to return.
Type: Array of [DescribeWorkspacesPoolsFilter](API_DescribeWorkspacesPoolsFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: No

 ** [Limit](#API_DescribeWorkspacesPools_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspacesPools-request-Limit"></a>
The maximum number of items to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [NextToken](#API_DescribeWorkspacesPools_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspacesPools-request-NextToken"></a>
If you received a `NextToken` from a previous call that was paginated, provide this token to receive the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [PoolIds](#API_DescribeWorkspacesPools_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspacesPools-request-PoolIds"></a>
The identifier of the WorkSpaces Pools.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Pattern: `^wspool-[0-9a-z]{9}$`
Required: No

## Response Syntax
<a name="API_DescribeWorkspacesPools_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "WorkspacesPools": [
      {
         "ApplicationSettings": {
            "S3BucketName": "string",
            "SettingsGroup": "string",
            "Status": "string"
         },
         "BundleId": "string",
         "CapacityStatus": {
            "ActiveUserSessions": number,
            "ActualUserSessions": number,
            "AvailableUserSessions": number,
            "DesiredUserSessions": number
         },
         "CreatedAt": number,
         "Description": "string",
         "DirectoryId": "string",
         "Errors": [
            {
               "ErrorCode": "string",
               "ErrorMessage": "string"
            }
         ],
         "PoolArn": "string",
         "PoolId": "string",
         "PoolName": "string",
         "RunningMode": "string",
         "State": "string",
         "TimeoutSettings": {
            "DisconnectTimeoutInSeconds": number,
            "IdleDisconnectTimeoutInSeconds": number,
            "MaxUserDurationInSeconds": number
         }
      }
   ]
}
```

## Response Elements
<a name="API_DescribeWorkspacesPools_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeWorkspacesPools_ResponseSyntax) **   <a name="WorkSpaces-DescribeWorkspacesPools-response-NextToken"></a>
If you received a `NextToken` from a previous call that was paginated, provide this token to receive the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [WorkspacesPools](#API_DescribeWorkspacesPools_ResponseSyntax) **   <a name="WorkSpaces-DescribeWorkspacesPools-response-WorkspacesPools"></a>
Information about the WorkSpaces Pools.
Type: Array of [WorkspacesPool](API_WorkspacesPool.md) objects

## Errors
<a name="API_DescribeWorkspacesPools_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
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
<a name="API_DescribeWorkspacesPools_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DescribeWorkspacesPools)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DescribeWorkspacesPools)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DescribeWorkspacesPools)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DescribeWorkspacesPools)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DescribeWorkspacesPools)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DescribeWorkspacesPools)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DescribeWorkspacesPools)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DescribeWorkspacesPools)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DescribeWorkspacesPools)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DescribeWorkspacesPools)
