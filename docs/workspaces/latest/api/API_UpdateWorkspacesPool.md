---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateWorkspacesPool.html
---

# UpdateWorkspacesPool
<a name="API_UpdateWorkspacesPool"></a>

**Note**
End of support notice: On December 31, 2027, AWS will end support for Amazon WorkSpaces Pools. After December 31, 2027, you will no longer be able to access the Amazon WorkSpaces Pools console or Amazon WorkSpaces Pools resources. For more information, see [Amazon WorkSpaces Pools end of support](https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-pools-end-of-support.html).

Updates the specified pool.

## Request Syntax
<a name="API_UpdateWorkspacesPool_RequestSyntax"></a>

```
{
   "ApplicationSettings": {
      "SettingsGroup": "{{string}}",
      "Status": "{{string}}"
   },
   "BundleId": "{{string}}",
   "Capacity": {
      "DesiredUserSessions": {{number}}
   },
   "Description": "{{string}}",
   "DirectoryId": "{{string}}",
   "PoolId": "{{string}}",
   "RunningMode": "{{string}}",
   "TimeoutSettings": {
      "DisconnectTimeoutInSeconds": {{number}},
      "IdleDisconnectTimeoutInSeconds": {{number}},
      "MaxUserDurationInSeconds": {{number}}
   }
}
```

## Request Parameters
<a name="API_UpdateWorkspacesPool_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationSettings](#API_UpdateWorkspacesPool_RequestSyntax) **   <a name="WorkSpaces-UpdateWorkspacesPool-request-ApplicationSettings"></a>
The persistent application settings for users in the pool.
Type: [ApplicationSettingsRequest](API_ApplicationSettingsRequest.md) object
Required: No

 ** [BundleId](#API_UpdateWorkspacesPool_RequestSyntax) **   <a name="WorkSpaces-UpdateWorkspacesPool-request-BundleId"></a>
The identifier of the bundle.
Type: String
Pattern: `^wsb-[0-9a-z]{8,63}$`
Required: No

 ** [Capacity](#API_UpdateWorkspacesPool_RequestSyntax) **   <a name="WorkSpaces-UpdateWorkspacesPool-request-Capacity"></a>
The desired capacity for the pool.
Type: [Capacity](API_Capacity.md) object
Required: No

 ** [Description](#API_UpdateWorkspacesPool_RequestSyntax) **   <a name="WorkSpaces-UpdateWorkspacesPool-request-Description"></a>
Describes the specified pool to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9_./() -]+$`
Required: No

 ** [DirectoryId](#API_UpdateWorkspacesPool_RequestSyntax) **   <a name="WorkSpaces-UpdateWorkspacesPool-request-DirectoryId"></a>
The identifier of the directory.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: No

 ** [PoolId](#API_UpdateWorkspacesPool_RequestSyntax) **   <a name="WorkSpaces-UpdateWorkspacesPool-request-PoolId"></a>
The identifier of the specified pool to update.
Type: String
Pattern: `^wspool-[0-9a-z]{9}$`
Required: Yes

 ** [RunningMode](#API_UpdateWorkspacesPool_RequestSyntax) **   <a name="WorkSpaces-UpdateWorkspacesPool-request-RunningMode"></a>
The desired running mode for the pool. The running mode can only be updated when the pool is in a stopped state.
Type: String
Valid Values: `AUTO_STOP | ALWAYS_ON`
Required: No

 ** [TimeoutSettings](#API_UpdateWorkspacesPool_RequestSyntax) **   <a name="WorkSpaces-UpdateWorkspacesPool-request-TimeoutSettings"></a>
Indicates the timeout settings of the specified pool.
Type: [TimeoutSettings](API_TimeoutSettings.md) object
Required: No

## Response Syntax
<a name="API_UpdateWorkspacesPool_ResponseSyntax"></a>

```
{
   "WorkspacesPool": {
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
}
```

## Response Elements
<a name="API_UpdateWorkspacesPool_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WorkspacesPool](#API_UpdateWorkspacesPool_ResponseSyntax) **   <a name="WorkSpaces-UpdateWorkspacesPool-response-WorkspacesPool"></a>
Describes the specified pool.
Type: [WorkspacesPool](API_WorkspacesPool.md) object

## Errors
<a name="API_UpdateWorkspacesPool_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** InvalidResourceStateException **
The state of the resource is not valid for this operation.
HTTP Status Code: 400

 ** OperationInProgressException **
The properties of this WorkSpace are currently being modified. Try again in a moment.
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
<a name="API_UpdateWorkspacesPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/UpdateWorkspacesPool)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/UpdateWorkspacesPool)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/UpdateWorkspacesPool)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/UpdateWorkspacesPool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/UpdateWorkspacesPool)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/UpdateWorkspacesPool)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/UpdateWorkspacesPool)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/UpdateWorkspacesPool)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/UpdateWorkspacesPool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/UpdateWorkspacesPool)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
