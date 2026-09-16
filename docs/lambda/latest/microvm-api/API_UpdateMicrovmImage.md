---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_UpdateMicrovmImage.html
---

# UpdateMicrovmImage
<a name="API_UpdateMicrovmImage"></a>

Updates the configuration of a MicroVM image and triggers a new version build. This operation uses PUT semantics — all required fields (codeArtifact, baseImageArn, buildRoleArn) must be provided with every request.

## Request Syntax
<a name="API_UpdateMicrovmImage_RequestSyntax"></a>

```
PUT /2025-09-09/microvm-images/{{imageIdentifier}} HTTP/1.1
Content-type: application/json

{
   "additionalOsCapabilities": [ "{{string}}" ],
   "baseImageArn": "{{string}}",
   "baseImageVersion": "{{string}}",
   "buildRoleArn": "{{string}}",
   "clientToken": "{{string}}",
   "codeArtifact": { ... },
   "cpuConfigurations": [
      {
         "architecture": "{{string}}"
      }
   ],
   "description": "{{string}}",
   "egressNetworkConnectors": [ "{{string}}" ],
   "environmentVariables": {
      "{{string}}" : "{{string}}"
   },
   "hooks": {
      "microvmHooks": {
         "resume": "{{string}}",
         "resumeTimeoutInSeconds": {{number}},
         "run": "{{string}}",
         "runTimeoutInSeconds": {{number}},
         "suspend": "{{string}}",
         "suspendTimeoutInSeconds": {{number}},
         "terminate": "{{string}}",
         "terminateTimeoutInSeconds": {{number}}
      },
      "microvmImageHooks": {
         "ready": "{{string}}",
         "readyTimeoutInSeconds": {{number}},
         "validate": "{{string}}",
         "validateTimeoutInSeconds": {{number}}
      },
      "port": {{number}}
   },
   "logging": { ... },
   "resources": [
      {
         "minimumMemoryInMiB": {{number}}
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateMicrovmImage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [imageIdentifier](#API_UpdateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-request-uri-imageIdentifier"></a>
The unique identifier (ARN or ID) of the MicroVM image to update.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Request Body
<a name="API_UpdateMicrovmImage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [additionalOsCapabilities](#API_UpdateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-request-additionalOsCapabilities"></a>
Additional OS capabilities granted to the MicroVM runtime environment.
Type: Array of strings
Valid Values: `ALL`
Required: No

 ** [baseImageArn](#API_UpdateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-request-baseImageArn"></a>
The ARN of the base MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: Yes

 ** [baseImageVersion](#API_UpdateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-request-baseImageVersion"></a>
The specific version of the base MicroVM image to use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: No

 ** [buildRoleArn](#API_UpdateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-request-buildRoleArn"></a>
The ARN of the IAM build role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::[0-9]{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [clientToken](#API_UpdateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-request-clientToken"></a>
A unique, case-sensitive identifier you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [codeArtifact](#API_UpdateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-request-codeArtifact"></a>
The code artifact containing the application code and metadata for the MicroVM image.
Type: [CodeArtifact](API_CodeArtifact.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [cpuConfigurations](#API_UpdateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-request-cpuConfigurations"></a>
The list of supported CPU configurations for the MicroVM.
Type: Array of [CpuConfiguration](API_CpuConfiguration.md) objects
Required: No

 ** [description](#API_UpdateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-request-description"></a>
The description of the MicroVM image.
Type: String
Required: No

 ** [egressNetworkConnectors](#API_UpdateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-request-egressNetworkConnectors"></a>
The list of egress network connectors available to the MicroVM at runtime.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [environmentVariables](#API_UpdateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-request-environmentVariables"></a>
Environment variables set in the MicroVM runtime environment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[^\s]+`
Value Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [hooks](#API_UpdateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-request-hooks"></a>
Lifecycle hook configuration for MicroVMs and MicroVM images.
Type: [Hooks](API_Hooks.md) object
Required: No

 ** [logging](#API_UpdateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-request-logging"></a>
The logging configuration for build-time and runtime logs. Specify {"cloudWatch": {"logGroup": "..."}} to stream logs to a custom CloudWatch log group, or {"disabled": {}} to turn off logging.
Type: [Logging](API_Logging.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [resources](#API_UpdateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-request-resources"></a>
The resource requirements for the MicroVM.
Type: Array of [Resources](API_Resources.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## Response Syntax
<a name="API_UpdateMicrovmImage_ResponseSyntax"></a>

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
   "latestActiveImageVersion": "string",
   "latestFailedImageVersion": "string",
   "logging": { ... },
   "name": "string",
   "resources": [
      {
         "minimumMemoryInMiB": number
      }
   ],
   "state": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_UpdateMicrovmImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [additionalOsCapabilities](#API_UpdateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-response-additionalOsCapabilities"></a>
Additional OS capabilities granted to the MicroVM runtime environment.
Type: Array of strings
Valid Values: `ALL`

 ** [baseImageArn](#API_UpdateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-response-baseImageArn"></a>
The ARN of the base MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [baseImageVersion](#API_UpdateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-response-baseImageVersion"></a>
The specific version of the base MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [buildRoleArn](#API_UpdateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-response-buildRoleArn"></a>
The ARN of the IAM build role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::[0-9]{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [codeArtifact](#API_UpdateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-response-codeArtifact"></a>
The code artifact containing the application code and metadata for the MicroVM image.
Type: [CodeArtifact](API_CodeArtifact.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [cpuConfigurations](#API_UpdateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-response-cpuConfigurations"></a>
The list of supported CPU configurations for the MicroVM.
Type: Array of [CpuConfiguration](API_CpuConfiguration.md) objects

 ** [createdAt](#API_UpdateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-response-createdAt"></a>
The timestamp when the MicroVM image was created.
Type: Timestamp

 ** [description](#API_UpdateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-response-description"></a>
The description of the MicroVM image.
Type: String

 ** [egressNetworkConnectors](#API_UpdateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-response-egressNetworkConnectors"></a>
The list of egress network connectors available to the MicroVM at runtime.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [environmentVariables](#API_UpdateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-response-environmentVariables"></a>
Environment variables set in the MicroVM runtime environment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[^\s]+`
Value Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [hooks](#API_UpdateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-response-hooks"></a>
Lifecycle hook configuration for MicroVMs and MicroVM images.
Type: [Hooks](API_Hooks.md) object

 ** [imageArn](#API_UpdateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-response-imageArn"></a>
The ARN of the MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [imageVersion](#API_UpdateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-response-imageVersion"></a>
The version of the MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [latestActiveImageVersion](#API_UpdateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-response-latestActiveImageVersion"></a>
The latest active version of the MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [latestFailedImageVersion](#API_UpdateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-response-latestFailedImageVersion"></a>
The latest failed version of the MicroVM image, if any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [logging](#API_UpdateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-response-logging"></a>
The logging configuration for build-time and runtime logs. Specify {"cloudWatch": {"logGroup": "..."}} to stream logs to a custom CloudWatch log group, or {"disabled": {}} to turn off logging.
Type: [Logging](API_Logging.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [name](#API_UpdateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-response-name"></a>
The name of the MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`

 ** [resources](#API_UpdateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-response-resources"></a>
The resource requirements for the MicroVM.
Type: Array of [Resources](API_Resources.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [state](#API_UpdateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-response-state"></a>
The current state of the MicroVM image.
Type: String
Valid Values: `CREATING | CREATED | CREATE_FAILED | UPDATING | UPDATED | UPDATE_FAILED | DELETING | DELETE_FAILED | DELETED`

 ** [updatedAt](#API_UpdateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-UpdateMicrovmImage-response-updatedAt"></a>
The timestamp when the MicroVM image was last updated.
Type: Timestamp

## Errors
<a name="API_UpdateMicrovmImage_Errors"></a>

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

 ** ServiceQuotaExceededException **
You have exceeded a service quota for Lambda MicroVMs.
 ** quotaCode **
The quota code of the exceeded service quota.
 ** resourceId **
The identifier of the resource that exceeded the quota.
 ** resourceType **
The type of the resource that exceeded the quota.
 ** serviceCode **
The service code of the exceeded service quota.
HTTP Status Code: 402

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
<a name="API_UpdateMicrovmImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-microvms-2025-09-09/UpdateMicrovmImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-microvms-2025-09-09/UpdateMicrovmImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/UpdateMicrovmImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-microvms-2025-09-09/UpdateMicrovmImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/UpdateMicrovmImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-microvms-2025-09-09/UpdateMicrovmImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-microvms-2025-09-09/UpdateMicrovmImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-microvms-2025-09-09/UpdateMicrovmImage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-microvms-2025-09-09/UpdateMicrovmImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/UpdateMicrovmImage)
