---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_CreateWorkspacesPool.html
---

# CreateWorkspacesPool
<a name="API_CreateWorkspacesPool"></a>

**Note**
End of support notice: On December 31, 2027, AWS will end support for Amazon WorkSpaces Pools. After December 31, 2027, you will no longer be able to access the Amazon WorkSpaces Pools console or Amazon WorkSpaces Pools resources. For more information, see [Amazon WorkSpaces Pools end of support](https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-pools-end-of-support.html).

Creates a pool of WorkSpaces.

## Request Syntax
<a name="API_CreateWorkspacesPool_RequestSyntax"></a>

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
   "PoolName": "{{string}}",
   "RunningMode": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TimeoutSettings": {
      "DisconnectTimeoutInSeconds": {{number}},
      "IdleDisconnectTimeoutInSeconds": {{number}},
      "MaxUserDurationInSeconds": {{number}}
   }
}
```

## Request Parameters
<a name="API_CreateWorkspacesPool_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationSettings](#API_CreateWorkspacesPool_RequestSyntax) **   <a name="WorkSpaces-CreateWorkspacesPool-request-ApplicationSettings"></a>
Indicates the application settings of the pool.
Type: [ApplicationSettingsRequest](API_ApplicationSettingsRequest.md) object
Required: No

 ** [BundleId](#API_CreateWorkspacesPool_RequestSyntax) **   <a name="WorkSpaces-CreateWorkspacesPool-request-BundleId"></a>
The identifier of the bundle for the pool.
Type: String
Pattern: `^wsb-[0-9a-z]{8,63}$`
Required: Yes

 ** [Capacity](#API_CreateWorkspacesPool_RequestSyntax) **   <a name="WorkSpaces-CreateWorkspacesPool-request-Capacity"></a>
The user capacity of the pool.
Type: [Capacity](API_Capacity.md) object
Required: Yes

 ** [Description](#API_CreateWorkspacesPool_RequestSyntax) **   <a name="WorkSpaces-CreateWorkspacesPool-request-Description"></a>
The pool description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9_./() -]+$`
Required: Yes

 ** [DirectoryId](#API_CreateWorkspacesPool_RequestSyntax) **   <a name="WorkSpaces-CreateWorkspacesPool-request-DirectoryId"></a>
The identifier of the directory for the pool.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: Yes

 ** [PoolName](#API_CreateWorkspacesPool_RequestSyntax) **   <a name="WorkSpaces-CreateWorkspacesPool-request-PoolName"></a>
The name of the pool.
Type: String
Pattern: `^[A-Za-z0-9][A-Za-z0-9_.-]{0,63}$`
Required: Yes

 ** [RunningMode](#API_CreateWorkspacesPool_RequestSyntax) **   <a name="WorkSpaces-CreateWorkspacesPool-request-RunningMode"></a>
The running mode for the pool.
Type: String
Valid Values: `AUTO_STOP | ALWAYS_ON`
Required: No

 ** [Tags](#API_CreateWorkspacesPool_RequestSyntax) **   <a name="WorkSpaces-CreateWorkspacesPool-request-Tags"></a>
The tags for the pool.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [TimeoutSettings](#API_CreateWorkspacesPool_RequestSyntax) **   <a name="WorkSpaces-CreateWorkspacesPool-request-TimeoutSettings"></a>
Indicates the timeout settings of the pool.
Type: [TimeoutSettings](API_TimeoutSettings.md) object
Required: No

## Response Syntax
<a name="API_CreateWorkspacesPool_ResponseSyntax"></a>

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
<a name="API_CreateWorkspacesPool_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WorkspacesPool](#API_CreateWorkspacesPool_ResponseSyntax) **   <a name="WorkSpaces-CreateWorkspacesPool-response-WorkspacesPool"></a>
Indicates the pool to create.
Type: [WorkspacesPool](API_WorkspacesPool.md) object

## Errors
<a name="API_CreateWorkspacesPool_Errors"></a>

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

 ** ResourceAlreadyExistsException **
The specified resource already exists.
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
<a name="API_CreateWorkspacesPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/CreateWorkspacesPool)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/CreateWorkspacesPool)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/CreateWorkspacesPool)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/CreateWorkspacesPool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/CreateWorkspacesPool)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/CreateWorkspacesPool)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/CreateWorkspacesPool)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/CreateWorkspacesPool)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/CreateWorkspacesPool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/CreateWorkspacesPool)
