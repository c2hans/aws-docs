---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_RunMicrovm.html
---

# RunMicrovm
<a name="API_RunMicrovm"></a>

Runs a new MicroVM from the specified image. The MicroVM starts in PENDING state and transitions to RUNNING once provisioning completes. To connect, generate an authentication token using CreateMicrovmAuthToken.

## Request Syntax
<a name="API_RunMicrovm_RequestSyntax"></a>

```
POST /2025-09-09/microvms HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "egressNetworkConnectors": [ "{{string}}" ],
   "executionRoleArn": "{{string}}",
   "idlePolicy": {
      "autoResumeEnabled": {{boolean}},
      "maxIdleDurationSeconds": {{number}},
      "suspendedDurationSeconds": {{number}}
   },
   "imageIdentifier": "{{string}}",
   "imageVersion": "{{string}}",
   "ingressNetworkConnectors": [ "{{string}}" ],
   "logging": { ... },
   "maximumDurationInSeconds": {{number}},
   "runHookPayload": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RunMicrovm_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RunMicrovm_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_RunMicrovm_RequestSyntax) **   <a name="lambdamicrovm-RunMicrovm-request-clientToken"></a>
A unique, case-sensitive identifier you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [egressNetworkConnectors](#API_RunMicrovm_RequestSyntax) **   <a name="lambdamicrovm-RunMicrovm-request-egressNetworkConnectors"></a>
The list of egress network connectors to configure for the MicroVM.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [executionRoleArn](#API_RunMicrovm_RequestSyntax) **   <a name="lambdamicrovm-RunMicrovm-request-executionRoleArn"></a>
The ARN of the IAM role to be assumed by the MicroVM during execution.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::[0-9]{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** [idlePolicy](#API_RunMicrovm_RequestSyntax) **   <a name="lambdamicrovm-RunMicrovm-request-idlePolicy"></a>
Configuration to control auto-suspend and auto-resume behavior.
Type: [IdlePolicy](API_IdlePolicy.md) object
Required: No

 ** [imageIdentifier](#API_RunMicrovm_RequestSyntax) **   <a name="lambdamicrovm-RunMicrovm-request-imageIdentifier"></a>
The identifier (ARN or ID) of the MicroVM image to run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [imageVersion](#API_RunMicrovm_RequestSyntax) **   <a name="lambdamicrovm-RunMicrovm-request-imageVersion"></a>
The version of the MicroVM image to run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: No

 ** [ingressNetworkConnectors](#API_RunMicrovm_RequestSyntax) **   <a name="lambdamicrovm-RunMicrovm-request-ingressNetworkConnectors"></a>
The list of ingress network connectors to configure for the MicroVM.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [logging](#API_RunMicrovm_RequestSyntax) **   <a name="lambdamicrovm-RunMicrovm-request-logging"></a>
The logging configuration for this MicroVM instance. Specify {"cloudWatch": {"logGroup": "..."}} to stream application logs to a custom CloudWatch log group, or {"disabled": {}} to turn off logging.
Type: [Logging](API_Logging.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [maximumDurationInSeconds](#API_RunMicrovm_RequestSyntax) **   <a name="lambdamicrovm-RunMicrovm-request-maximumDurationInSeconds"></a>
The maximum duration in seconds that the MicroVM can exist before being terminated by the platform. Valid range: 1–28,800 (8 hours).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 28800.
Required: No

 ** [runHookPayload](#API_RunMicrovm_RequestSyntax) **   <a name="lambdamicrovm-RunMicrovm-request-runHookPayload"></a>
Per-MicroVM initialization data delivered as the request body of the /run lifecycle hook. Use to pass tenant-specific configuration such as session IDs or secret references. Maximum: 16,384 bytes.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

## Response Syntax
<a name="API_RunMicrovm_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "egressNetworkConnectors": [ "string" ],
   "endpoint": "string",
   "executionRoleArn": "string",
   "idlePolicy": {
      "autoResumeEnabled": boolean,
      "maxIdleDurationSeconds": number,
      "suspendedDurationSeconds": number
   },
   "imageArn": "string",
   "imageVersion": "string",
   "ingressNetworkConnectors": [ "string" ],
   "maximumDurationInSeconds": number,
   "microvmId": "string",
   "startedAt": number,
   "state": "string",
   "stateReason": "string",
   "terminatedAt": number
}
```

## Response Elements
<a name="API_RunMicrovm_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [egressNetworkConnectors](#API_RunMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-RunMicrovm-response-egressNetworkConnectors"></a>
The list of egress network connectors configured for the MicroVM.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [endpoint](#API_RunMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-RunMicrovm-response-endpoint"></a>
The HTTPS endpoint URL for communicating with the MicroVM. Include a valid authentication token in the X-aws-proxy-auth header when sending requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [executionRoleArn](#API_RunMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-RunMicrovm-response-executionRoleArn"></a>
The ARN of the IAM execution role assumed by the MicroVM.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::[0-9]{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [idlePolicy](#API_RunMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-RunMicrovm-response-idlePolicy"></a>
The idle policy configuration of the MicroVM.
Type: [IdlePolicy](API_IdlePolicy.md) object

 ** [imageArn](#API_RunMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-RunMicrovm-response-imageArn"></a>
The ARN of the MicroVM image used to run this MicroVM.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [imageVersion](#API_RunMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-RunMicrovm-response-imageVersion"></a>
The version of the MicroVM image used to run this MicroVM.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [ingressNetworkConnectors](#API_RunMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-RunMicrovm-response-ingressNetworkConnectors"></a>
The list of ingress network connectors configured for the MicroVM.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [maximumDurationInSeconds](#API_RunMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-RunMicrovm-response-maximumDurationInSeconds"></a>
The maximum duration in seconds that the MicroVM can exist.
Type: Integer

 ** [microvmId](#API_RunMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-RunMicrovm-response-microvmId"></a>
The unique identifier of the MicroVM.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [startedAt](#API_RunMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-RunMicrovm-response-startedAt"></a>
The timestamp when the MicroVM first started.
Type: Timestamp

 ** [state](#API_RunMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-RunMicrovm-response-state"></a>
The current lifecycle state of the MicroVM.
Type: String
Valid Values: `PENDING | RUNNING | SUSPENDING | SUSPENDED | TERMINATING | TERMINATED`

 ** [stateReason](#API_RunMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-RunMicrovm-response-stateReason"></a>
The reason for why the MicroVM is in the current state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [terminatedAt](#API_RunMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-RunMicrovm-response-terminatedAt"></a>
The timestamp when the MicroVM terminated.
Type: Timestamp

## Errors
<a name="API_RunMicrovm_Errors"></a>

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
<a name="API_RunMicrovm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-microvms-2025-09-09/RunMicrovm)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-microvms-2025-09-09/RunMicrovm)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/RunMicrovm)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-microvms-2025-09-09/RunMicrovm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/RunMicrovm)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-microvms-2025-09-09/RunMicrovm)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-microvms-2025-09-09/RunMicrovm)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-microvms-2025-09-09/RunMicrovm)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-microvms-2025-09-09/RunMicrovm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/RunMicrovm)
