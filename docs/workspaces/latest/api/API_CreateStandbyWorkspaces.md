---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_CreateStandbyWorkspaces.html
---

# CreateStandbyWorkspaces
<a name="API_CreateStandbyWorkspaces"></a>

Creates a standby WorkSpace in a secondary Region.

## Request Syntax
<a name="API_CreateStandbyWorkspaces_RequestSyntax"></a>

```
{
   "PrimaryRegion": "{{string}}",
   "StandbyWorkspaces": [
      {
         "DataReplication": "{{string}}",
         "DirectoryId": "{{string}}",
         "PrimaryWorkspaceId": "{{string}}",
         "Tags": [
            {
               "Key": "{{string}}",
               "Value": "{{string}}"
            }
         ],
         "VolumeEncryptionKey": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateStandbyWorkspaces_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [PrimaryRegion](#API_CreateStandbyWorkspaces_RequestSyntax) **   <a name="WorkSpaces-CreateStandbyWorkspaces-request-PrimaryRegion"></a>
The Region of the primary WorkSpace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 31.
Pattern: `^[-0-9a-z]{1,31}$`
Required: Yes

 ** [StandbyWorkspaces](#API_CreateStandbyWorkspaces_RequestSyntax) **   <a name="WorkSpaces-CreateStandbyWorkspaces-request-StandbyWorkspaces"></a>
Information about the standby WorkSpace to be created.
Type: Array of [StandbyWorkspace](API_StandbyWorkspace.md) objects
Required: Yes

## Response Syntax
<a name="API_CreateStandbyWorkspaces_ResponseSyntax"></a>

```
{
   "FailedStandbyRequests": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "StandbyWorkspaceRequest": {
            "DataReplication": "string",
            "DirectoryId": "string",
            "PrimaryWorkspaceId": "string",
            "Tags": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ],
            "VolumeEncryptionKey": "string"
         }
      }
   ],
   "PendingStandbyRequests": [
      {
         "DirectoryId": "string",
         "State": "string",
         "UserName": "string",
         "WorkspaceId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreateStandbyWorkspaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedStandbyRequests](#API_CreateStandbyWorkspaces_ResponseSyntax) **   <a name="WorkSpaces-CreateStandbyWorkspaces-response-FailedStandbyRequests"></a>
Information about the standby WorkSpace that could not be created.
Type: Array of [FailedCreateStandbyWorkspacesRequest](API_FailedCreateStandbyWorkspacesRequest.md) objects

 ** [PendingStandbyRequests](#API_CreateStandbyWorkspaces_ResponseSyntax) **   <a name="WorkSpaces-CreateStandbyWorkspaces-response-PendingStandbyRequests"></a>
Information about the standby WorkSpace that was created.
Type: Array of [PendingCreateStandbyWorkspacesRequest](API_PendingCreateStandbyWorkspacesRequest.md) objects

## Errors
<a name="API_CreateStandbyWorkspaces_Errors"></a>

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

 ** ResourceLimitExceededException **
Your resource limits have been exceeded.
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
<a name="API_CreateStandbyWorkspaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/CreateStandbyWorkspaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/CreateStandbyWorkspaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/CreateStandbyWorkspaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/CreateStandbyWorkspaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/CreateStandbyWorkspaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/CreateStandbyWorkspaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/CreateStandbyWorkspaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/CreateStandbyWorkspaces)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/CreateStandbyWorkspaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/CreateStandbyWorkspaces)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
