---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_CreateMicrovmImage.html
---

# CreateMicrovmImage
<a name="API_CreateMicrovmImage"></a>

Creates a MicroVM image from the specified code artifact and base image. The build is asynchronous — the image transitions from CREATING to CREATED on success, or CREATE\_FAILED on failure. Use GetMicrovmImage to poll for completion.

## Request Syntax
<a name="API_CreateMicrovmImage_RequestSyntax"></a>

```
POST /2025-09-09/microvm-images HTTP/1.1
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
   "name": "{{string}}",
   "resources": [
      {
         "minimumMemoryInMiB": {{number}}
      }
   ],
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateMicrovmImage_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateMicrovmImage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [additionalOsCapabilities](#API_CreateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-request-additionalOsCapabilities"></a>
Additional OS capabilities granted to the MicroVM runtime environment.
Type: Array of strings
Valid Values: `ALL`
Required: No

 ** [baseImageArn](#API_CreateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-request-baseImageArn"></a>
The ARN of the Lambda-managed base MicroVM image to build upon. Use ListManagedMicrovmImages to discover available base images.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: Yes

 ** [baseImageVersion](#API_CreateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-request-baseImageVersion"></a>
The specific version of the base MicroVM image to use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: No

 ** [buildRoleArn](#API_CreateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-request-buildRoleArn"></a>
The ARN of the IAM role assumed during the image build process. This role must have permissions to access the code artifact and any required resources.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::[0-9]{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [clientToken](#API_CreateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-request-clientToken"></a>
A unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token, the operation returns the successful response without performing any further actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [codeArtifact](#API_CreateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-request-codeArtifact"></a>
The code artifact containing the application code and metadata for the MicroVM image.
Type: [CodeArtifact](API_CodeArtifact.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [cpuConfigurations](#API_CreateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-request-cpuConfigurations"></a>
The list of supported CPU configurations for the MicroVM.
Type: Array of [CpuConfiguration](API_CpuConfiguration.md) objects
Required: No

 ** [description](#API_CreateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-request-description"></a>
A description of the MicroVM image.
Type: String
Required: No

 ** [egressNetworkConnectors](#API_CreateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-request-egressNetworkConnectors"></a>
The list of egress network connectors available to the MicroVM at runtime.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [environmentVariables](#API_CreateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-request-environmentVariables"></a>
Environment variables set in the MicroVM runtime environment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[^\s]+`
Value Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [hooks](#API_CreateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-request-hooks"></a>
Lifecycle hook configuration for MicroVMs and MicroVM images.
Type: [Hooks](API_Hooks.md) object
Required: No

 ** [logging](#API_CreateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-request-logging"></a>
The logging configuration for build-time and runtime logs. Specify {"cloudWatch": {"logGroup": "..."}} to stream logs to a custom CloudWatch log group, or {"disabled": {}} to turn off logging.
Type: [Logging](API_Logging.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [name](#API_CreateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-request-name"></a>
The name of the MicroVM image. Must be unique within the AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`
Required: Yes

 ** [resources](#API_CreateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-request-resources"></a>
The resource requirements for the MicroVM.
Type: Array of [Resources](API_Resources.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** [tags](#API_CreateMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-request-tags"></a>
A set of key-value pairs that you can attach to the resource. Use tags to categorize resources for cost allocation, access control (ABAC), and organization.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

## Response Syntax
<a name="API_CreateMicrovmImage_ResponseSyntax"></a>

```
HTTP/1.1 201
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
   "tags": {
      "string" : "string"
   },
   "updatedAt": number
}
```

## Response Elements
<a name="API_CreateMicrovmImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [additionalOsCapabilities](#API_CreateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-response-additionalOsCapabilities"></a>
Additional OS capabilities granted to the MicroVM runtime environment.
Type: Array of strings
Valid Values: `ALL`

 ** [baseImageArn](#API_CreateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-response-baseImageArn"></a>
The ARN of the base MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [baseImageVersion](#API_CreateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-response-baseImageVersion"></a>
The specific version of the base MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [buildRoleArn](#API_CreateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-response-buildRoleArn"></a>
The ARN of the IAM build role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::[0-9]{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [codeArtifact](#API_CreateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-response-codeArtifact"></a>
The code artifact containing the application code and metadata for the MicroVM image.
Type: [CodeArtifact](API_CodeArtifact.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [cpuConfigurations](#API_CreateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-response-cpuConfigurations"></a>
The list of supported CPU configurations for the MicroVM.
Type: Array of [CpuConfiguration](API_CpuConfiguration.md) objects

 ** [createdAt](#API_CreateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-response-createdAt"></a>
The timestamp when the MicroVM image was created.
Type: Timestamp

 ** [description](#API_CreateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-response-description"></a>
The description of the MicroVM image.
Type: String

 ** [egressNetworkConnectors](#API_CreateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-response-egressNetworkConnectors"></a>
The list of egress network connectors available to the MicroVM at runtime.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [environmentVariables](#API_CreateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-response-environmentVariables"></a>
Environment variables set in the MicroVM runtime environment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[^\s]+`
Value Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [hooks](#API_CreateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-response-hooks"></a>
Lifecycle hook configuration for MicroVMs and MicroVM images.
Type: [Hooks](API_Hooks.md) object

 ** [imageArn](#API_CreateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-response-imageArn"></a>
The ARN of the created MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [imageVersion](#API_CreateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-response-imageVersion"></a>
The version of the MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [latestActiveImageVersion](#API_CreateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-response-latestActiveImageVersion"></a>
The latest active version of the MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [latestFailedImageVersion](#API_CreateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-response-latestFailedImageVersion"></a>
The latest failed version of the MicroVM image, if any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [logging](#API_CreateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-response-logging"></a>
The logging configuration for build-time and runtime logs. Specify {"cloudWatch": {"logGroup": "..."}} to stream logs to a custom CloudWatch log group, or {"disabled": {}} to turn off logging.
Type: [Logging](API_Logging.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [name](#API_CreateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-response-name"></a>
The name of the MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`

 ** [resources](#API_CreateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-response-resources"></a>
The resource requirements for the MicroVM.
Type: Array of [Resources](API_Resources.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [state](#API_CreateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-response-state"></a>
The current state of the MicroVM image.
Type: String
Valid Values: `CREATING | CREATED | CREATE_FAILED | UPDATING | UPDATED | UPDATE_FAILED | DELETING | DELETE_FAILED | DELETED`

 ** [tags](#API_CreateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-response-tags"></a>
A set of key-value pairs that you can attach to the resource. Use tags to categorize resources for cost allocation, access control (ABAC), and organization.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`

 ** [updatedAt](#API_CreateMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-CreateMicrovmImage-response-updatedAt"></a>
The timestamp when the MicroVM image was last updated.
Type: Timestamp

## Errors
<a name="API_CreateMicrovmImage_Errors"></a>

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
<a name="API_CreateMicrovmImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-microvms-2025-09-09/CreateMicrovmImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-microvms-2025-09-09/CreateMicrovmImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/CreateMicrovmImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-microvms-2025-09-09/CreateMicrovmImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/CreateMicrovmImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-microvms-2025-09-09/CreateMicrovmImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-microvms-2025-09-09/CreateMicrovmImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-microvms-2025-09-09/CreateMicrovmImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-microvms-2025-09-09/CreateMicrovmImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/CreateMicrovmImage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda MicroVMs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
