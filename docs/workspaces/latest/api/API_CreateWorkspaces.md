---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_CreateWorkspaces.html
---

# CreateWorkspaces
<a name="API_CreateWorkspaces"></a>

Creates one or more WorkSpaces.

This operation is asynchronous and returns before the WorkSpaces are created.

**Note**
The `MANUAL` running mode value is only supported by Amazon WorkSpaces Core. Contact your account team to be allow-listed to use this value. For more information, see [Amazon WorkSpaces Core](http://aws.amazon.com/workspaces/core/).
You don't need to specify the `PCOIP` protocol for Linux bundles because `DCV` (formerly WSP) is the default protocol for those bundles.
User-decoupled WorkSpaces are only supported by Amazon WorkSpaces Core.
Review your running mode to ensure you are using one that is optimal for your needs and budget. For more information on switching running modes, see [ Can I switch between hourly and monthly billing?](http://aws.amazon.com/workspaces-family/workspaces/faqs/#:~:text=Can%20I%20switch%20between%20hourly%20and%20monthly%20billing%20on%20WorkSpaces%20Personal%3F)

## Request Syntax
<a name="API_CreateWorkspaces_RequestSyntax"></a>

```
{
   "Workspaces": [
      {
         "BundleId": "{{string}}",
         "DirectoryId": "{{string}}",
         "Ipv6Address": "{{string}}",
         "RootVolumeEncryptionEnabled": {{boolean}},
         "Tags": [
            {
               "Key": "{{string}}",
               "Value": "{{string}}"
            }
         ],
         "UserName": "{{string}}",
         "UserVolumeEncryptionEnabled": {{boolean}},
         "VolumeEncryptionKey": "{{string}}",
         "WorkspaceName": "{{string}}",
         "WorkspaceProperties": {
            "ComputeTypeName": "{{string}}",
            "GlobalAccelerator": {
               "Mode": "{{string}}",
               "PreferredProtocol": "{{string}}"
            },
            "OperatingSystemName": "{{string}}",
            "Protocols": [ "{{string}}" ],
            "RootVolumeSizeGib": {{number}},
            "RunningMode": "{{string}}",
            "RunningModeAutoStopTimeoutInMinutes": {{number}},
            "UserVolumeSizeGib": {{number}}
         }
      }
   ]
}
```

## Request Parameters
<a name="API_CreateWorkspaces_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Workspaces](#API_CreateWorkspaces_RequestSyntax) **   <a name="WorkSpaces-CreateWorkspaces-request-Workspaces"></a>
The WorkSpaces to create. You can specify up to 25 WorkSpaces.
Type: Array of [WorkspaceRequest](API_WorkspaceRequest.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: Yes

## Response Syntax
<a name="API_CreateWorkspaces_ResponseSyntax"></a>

```
{
   "FailedRequests": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "WorkspaceRequest": {
            "BundleId": "string",
            "DirectoryId": "string",
            "Ipv6Address": "string",
            "RootVolumeEncryptionEnabled": boolean,
            "Tags": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ],
            "UserName": "string",
            "UserVolumeEncryptionEnabled": boolean,
            "VolumeEncryptionKey": "string",
            "WorkspaceName": "string",
            "WorkspaceProperties": {
               "ComputeTypeName": "string",
               "GlobalAccelerator": {
                  "Mode": "string",
                  "PreferredProtocol": "string"
               },
               "OperatingSystemName": "string",
               "Protocols": [ "string" ],
               "RootVolumeSizeGib": number,
               "RunningMode": "string",
               "RunningModeAutoStopTimeoutInMinutes": number,
               "UserVolumeSizeGib": number
            }
         }
      }
   ],
   "PendingRequests": [
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
<a name="API_CreateWorkspaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedRequests](#API_CreateWorkspaces_ResponseSyntax) **   <a name="WorkSpaces-CreateWorkspaces-response-FailedRequests"></a>
Information about the WorkSpaces that could not be created.
Type: Array of [FailedCreateWorkspaceRequest](API_FailedCreateWorkspaceRequest.md) objects

 ** [PendingRequests](#API_CreateWorkspaces_ResponseSyntax) **   <a name="WorkSpaces-CreateWorkspaces-response-PendingRequests"></a>
Information about the WorkSpaces that were created.
Because this operation is asynchronous, the identifier returned is not immediately available for use with other operations. For example, if you call [DescribeWorkspaces](API_DescribeWorkspaces.md) before the WorkSpace is created, the information returned can be incomplete.
Type: Array of [Workspace](API_Workspace.md) objects

## Errors
<a name="API_CreateWorkspaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** ResourceLimitExceededException **
Your resource limits have been exceeded.
 ** message **
The exception error message.
HTTP Status Code: 400

## See Also
<a name="API_CreateWorkspaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/CreateWorkspaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/CreateWorkspaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/CreateWorkspaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/CreateWorkspaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/CreateWorkspaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/CreateWorkspaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/CreateWorkspaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/CreateWorkspaces)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/CreateWorkspaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/CreateWorkspaces)
