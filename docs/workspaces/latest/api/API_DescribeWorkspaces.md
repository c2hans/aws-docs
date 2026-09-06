---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaces.html
---

# DescribeWorkspaces
<a name="API_DescribeWorkspaces"></a>

Describes the specified WorkSpaces.

You can filter the results by using the bundle identifier, directory identifier, or owner, but you can specify only one filter at a time.

## Request Syntax
<a name="API_DescribeWorkspaces_RequestSyntax"></a>

```
{
   "BundleId": "{{string}}",
   "DirectoryId": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "UserName": "{{string}}",
   "WorkspaceIds": [ "{{string}}" ],
   "WorkspaceName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeWorkspaces_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [BundleId](#API_DescribeWorkspaces_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaces-request-BundleId"></a>
The identifier of the bundle. All WorkSpaces that are created from this bundle are retrieved. You cannot combine this parameter with any other filter.
Type: String
Pattern: `^wsb-[0-9a-z]{8,63}$`
Required: No

 ** [DirectoryId](#API_DescribeWorkspaces_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaces-request-DirectoryId"></a>
The identifier of the directory. In addition, you can optionally specify a specific directory user (see `UserName`). You cannot combine this parameter with any other filter.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: No

 ** [Limit](#API_DescribeWorkspaces_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaces-request-Limit"></a>
The maximum number of items to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [NextToken](#API_DescribeWorkspaces_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaces-request-NextToken"></a>
If you received a `NextToken` from a previous call that was paginated, provide this token to receive the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [UserName](#API_DescribeWorkspaces_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaces-request-UserName"></a>
The name of the directory user. You must specify this parameter with `DirectoryId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Required: No

 ** [WorkspaceIds](#API_DescribeWorkspaces_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaces-request-WorkspaceIds"></a>
The identifiers of the WorkSpaces. You cannot combine this parameter with any other filter.
Because the [CreateWorkspaces](API_CreateWorkspaces.md) operation is asynchronous, the identifier it returns is not immediately available. If you immediately call [DescribeWorkspaces](#API_DescribeWorkspaces) with this identifier, no information is returned.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Pattern: `^ws-[0-9a-z]{8,63}$`
Required: No

 ** [WorkspaceName](#API_DescribeWorkspaces_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaces-request-WorkspaceName"></a>
The name of the user-decoupled WorkSpace.
Type: String
Pattern: `^[a-zA-Z0-9_()][a-zA-Z0-9_.()-]{1,63}$`
Required: No

## Response Syntax
<a name="API_DescribeWorkspaces_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Workspaces": [
      {
         "BundleId": "string",
         "ComputerName": "string",
         "DataReplicationSettings": {
            "DataReplication": "string",
            "RecoverySnapshotTime": number
         },
         "DirectoryId": "string",
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "IpAddress": "string",
         "Ipv6Address": "string",
         "ModificationStates": [
            {
               "Resource": "string",
               "State": "string"
            }
         ],
         "RelatedWorkspaces": [
            {
               "Region": "string",
               "State": "string",
               "Type": "string",
               "WorkspaceId": "string"
            }
         ],
         "RootVolumeEncryptionEnabled": boolean,
         "StandbyWorkspacesProperties": [
            {
               "DataReplication": "string",
               "RecoverySnapshotTime": number,
               "StandbyWorkspaceId": "string"
            }
         ],
         "State": "string",
         "SubnetId": "string",
         "UserName": "string",
         "UserVolumeEncryptionEnabled": boolean,
         "VolumeEncryptionKey": "string",
         "WorkspaceId": "string",
         "WorkspaceName": "string",
         "WorkspaceProperties": {
            "ComputeTypeName": "string",
            "GlobalAccelerator": {
               "Mode": "string",
               "PreferredProtocol": "string"
            },
            "NestedVirtualizationEnabled": boolean,
            "OperatingSystemName": "string",
            "Protocols": [ "string" ],
            "RootVolumeSizeGib": number,
            "RunningMode": "string",
            "RunningModeAutoStopTimeoutInMinutes": number,
            "UserVolumeSizeGib": number
         }
      }
   ]
}
```

## Response Elements
<a name="API_DescribeWorkspaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeWorkspaces_ResponseSyntax) **   <a name="WorkSpaces-DescribeWorkspaces-response-NextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Workspaces](#API_DescribeWorkspaces_ResponseSyntax) **   <a name="WorkSpaces-DescribeWorkspaces-response-Workspaces"></a>
Information about the WorkSpaces.
Because [CreateWorkspaces](API_CreateWorkspaces.md) is an asynchronous operation, some of the returned information could be incomplete.
Type: Array of [Workspace](API_Workspace.md) objects

## Errors
<a name="API_DescribeWorkspaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** ResourceUnavailableException **
The specified resource is not available.
 ** message **
The exception error message.
 ** ResourceId **
The identifier of the resource that is not available.
HTTP Status Code: 400

## See Also
<a name="API_DescribeWorkspaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DescribeWorkspaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DescribeWorkspaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DescribeWorkspaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DescribeWorkspaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DescribeWorkspaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DescribeWorkspaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DescribeWorkspaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DescribeWorkspaces)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DescribeWorkspaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DescribeWorkspaces)
