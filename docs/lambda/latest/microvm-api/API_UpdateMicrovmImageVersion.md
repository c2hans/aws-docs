---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_UpdateMicrovmImageVersion.html
---

# UpdateMicrovmImageVersion
<a name="API_UpdateMicrovmImageVersion"></a>

Updates the status of a specific MicroVM image version.

## Request Syntax
<a name="API_UpdateMicrovmImageVersion_RequestSyntax"></a>

```
PATCH /2025-09-09/microvm-images/{{imageIdentifier}}/versions/{{imageVersion}} HTTP/1.1
Content-type: application/json

{
   "status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateMicrovmImageVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [imageIdentifier](#API_UpdateMicrovmImageVersion_RequestSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-request-uri-imageIdentifier"></a>
The unique identifier (ARN or ID) of the MicroVM image.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [imageVersion](#API_UpdateMicrovmImageVersion_RequestSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-request-uri-imageVersion"></a>
The version of the MicroVM image to update.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: Yes

## Request Body
<a name="API_UpdateMicrovmImageVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [status](#API_UpdateMicrovmImageVersion_RequestSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-request-status"></a>
The new status to set for the MicroVM image version.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: Yes

## Response Syntax
<a name="API_UpdateMicrovmImageVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "additionalOsCapabilities": [ "string" ],
   "baseImageArn": "string",
   "baseImageVersion": "string",
   "buildRoleArn": "string",
   "codeArtifact": { ... },
   "cpuConfigurations": [
      {
         "architecture": "string"
      }
   ],
   "createdAt": number,
   "description": "string",
   "egressNetworkConnectors": [ "string" ],
   "environmentVariables": {
      "string" : "string"
   },
   "hooks": {
      "microvmHooks": {
         "resume": "string",
         "resumeTimeoutInSeconds": number,
         "run": "string",
         "runTimeoutInSeconds": number,
         "suspend": "string",
         "suspendTimeoutInSeconds": number,
         "terminate": "string",
         "terminateTimeoutInSeconds": number
      },
      "microvmImageHooks": {
         "ready": "string",
         "readyTimeoutInSeconds": number,
         "validate": "string",
         "validateTimeoutInSeconds": number
      },
      "port": number
   },
   "imageArn": "string",
   "imageVersion": "string",
   "logging": { ... },
   "resources": [
      {
         "minimumMemoryInMiB": number
      }
   ],
   "state": "string",
   "stateReason": "string",
   "status": "string",
   "tags": {
      "string" : "string"
   },
   "updatedAt": number
}
```

## Response Elements
<a name="API_UpdateMicrovmImageVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [additionalOsCapabilities](#API_UpdateMicrovmImageVersion_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-response-additionalOsCapabilities"></a>
Additional OS capabilities granted to the MicroVM runtime environment.
Type: Array of strings
Valid Values: `ALL`

 ** [baseImageArn](#API_UpdateMicrovmImageVersion_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-response-baseImageArn"></a>
The ARN of the base MicroVM image used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [baseImageVersion](#API_UpdateMicrovmImageVersion_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-response-baseImageVersion"></a>
The specific version of the base MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [buildRoleArn](#API_UpdateMicrovmImageVersion_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-response-buildRoleArn"></a>
The ARN of the IAM build role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::[0-9]{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [codeArtifact](#API_UpdateMicrovmImageVersion_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-response-codeArtifact"></a>
The code artifact for this version.
Type: [CodeArtifact](API_CodeArtifact.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [cpuConfigurations](#API_UpdateMicrovmImageVersion_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-response-cpuConfigurations"></a>
The list of supported CPU configurations for the MicroVM.
Type: Array of [CpuConfiguration](API_CpuConfiguration.md) objects

 ** [createdAt](#API_UpdateMicrovmImageVersion_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-response-createdAt"></a>
The timestamp when the version was created.
Type: Timestamp

 ** [description](#API_UpdateMicrovmImageVersion_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-response-description"></a>
The description of the version.
Type: String

 ** [egressNetworkConnectors](#API_UpdateMicrovmImageVersion_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-response-egressNetworkConnectors"></a>
The list of egress network connectors available to the MicroVM at runtime.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [environmentVariables](#API_UpdateMicrovmImageVersion_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-response-environmentVariables"></a>
Environment variables set in the MicroVM runtime environment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[^\s]+`
Value Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [hooks](#API_UpdateMicrovmImageVersion_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-response-hooks"></a>
Lifecycle hook configuration for MicroVMs and MicroVM images.
Type: [Hooks](API_Hooks.md) object

 ** [imageArn](#API_UpdateMicrovmImageVersion_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-response-imageArn"></a>
The ARN of the MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [imageVersion](#API_UpdateMicrovmImageVersion_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-response-imageVersion"></a>
The version of the MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [logging](#API_UpdateMicrovmImageVersion_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-response-logging"></a>
The logging configuration for this version.
Type: [Logging](API_Logging.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [resources](#API_UpdateMicrovmImageVersion_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-response-resources"></a>
The resource requirements for the MicroVM.
Type: Array of [Resources](API_Resources.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [state](#API_UpdateMicrovmImageVersion_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-response-state"></a>
The current state of the version.
Type: String
Valid Values: `PENDING | IN_PROGRESS | SUCCESSFUL | FAILED | DELETING | DELETED | DELETE_FAILED`

 ** [stateReason](#API_UpdateMicrovmImageVersion_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-response-stateReason"></a>
The reason for the current state. For example, one or more builds failed.
Type: String

 ** [status](#API_UpdateMicrovmImageVersion_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-response-status"></a>
The availability status of the version: ACTIVE (can be used by RunMicrovm) or INACTIVE (blocked from launching new MicroVMs).
Type: String
Valid Values: `ACTIVE | INACTIVE`

 ** [tags](#API_UpdateMicrovmImageVersion_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-response-tags"></a>
Key-value pairs associated with the version.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`

 ** [updatedAt](#API_UpdateMicrovmImageVersion_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImageVersion-response-updatedAt"></a>
The timestamp when the version was last updated.
Type: Timestamp

## Errors
<a name="API_UpdateMicrovmImageVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource.
 ** resourceId **
The identifier of the resource that caused the conflict.
 ** resourceType **
The type of the resource that caused the conflict.
HTTP Status Code: 409

 ** InternalServerException **
An internal server error occurred. Retry the request later.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of the resource that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling. Retry the request later.
 ** quotaCode **
The quota code of the throttled service quota.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
 ** serviceCode **
The service code of the throttled service quota.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateMicrovmImageVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-microvms-2025-09-09/UpdateMicrovmImageVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-microvms-2025-09-09/UpdateMicrovmImageVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/UpdateMicrovmImageVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-microvms-2025-09-09/UpdateMicrovmImageVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/UpdateMicrovmImageVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-microvms-2025-09-09/UpdateMicrovmImageVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-microvms-2025-09-09/UpdateMicrovmImageVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-microvms-2025-09-09/UpdateMicrovmImageVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-microvms-2025-09-09/UpdateMicrovmImageVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/UpdateMicrovmImageVersion)
