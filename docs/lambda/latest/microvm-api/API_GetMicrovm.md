---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_GetMicrovm.html
---

# GetMicrovm
<a name="API_GetMicrovm"></a>

Retrieves the details of a specific MicroVM, including its state, endpoint, image information, and configuration. The state field is eventually consistent — determine readiness by connecting to the endpoint.

## Request Syntax
<a name="API_GetMicrovm_RequestSyntax"></a>

```
GET /2025-09-09/microvms/{{microvmIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMicrovm_RequestParameters"></a>

The request uses the following URI parameters.

 ** [microvmIdentifier](#API_GetMicrovm_RequestSyntax) **   <a name="lambdamicrovm-GetMicrovm-request-uri-microvmIdentifier"></a>
The ID of the MicroVM to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Request Body
<a name="API_GetMicrovm_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMicrovm_ResponseSyntax"></a>

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
<a name="API_GetMicrovm_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [egressNetworkConnectors](#API_GetMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovm-response-egressNetworkConnectors"></a>
The list of egress network connectors configured for the MicroVM.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [endpoint](#API_GetMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovm-response-endpoint"></a>
The HTTPS endpoint URL for communicating with the MicroVM. Include a valid authentication token in the X-aws-proxy-auth header when sending requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [executionRoleArn](#API_GetMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovm-response-executionRoleArn"></a>
The ARN of the IAM execution role assumed by the MicroVM.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::[0-9]{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [idlePolicy](#API_GetMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovm-response-idlePolicy"></a>
The idle policy configuration of the MicroVM, controlling auto-suspend and auto-resume behavior.
Type: [IdlePolicy](API_IdlePolicy.md) object

 ** [imageArn](#API_GetMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovm-response-imageArn"></a>
The ARN of the MicroVM image used to run this MicroVM.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [imageVersion](#API_GetMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovm-response-imageVersion"></a>
The version of the MicroVM image used to run this MicroVM.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [ingressNetworkConnectors](#API_GetMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovm-response-ingressNetworkConnectors"></a>
The list of ingress network connectors configured for the MicroVM.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [maximumDurationInSeconds](#API_GetMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovm-response-maximumDurationInSeconds"></a>
The maximum duration in seconds that the MicroVM can exist before being terminated by the platform.
Type: Integer

 ** [microvmId](#API_GetMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovm-response-microvmId"></a>
The unique identifier of the MicroVM.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [startedAt](#API_GetMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovm-response-startedAt"></a>
The timestamp when the MicroVM first started.
Type: Timestamp

 ** [state](#API_GetMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovm-response-state"></a>
The current lifecycle state of the MicroVM.
Type: String
Valid Values: `PENDING | RUNNING | SUSPENDING | SUSPENDED | TERMINATING | TERMINATED`

 ** [stateReason](#API_GetMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovm-response-stateReason"></a>
The reason for why the MicroVM is in the current state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [terminatedAt](#API_GetMicrovm_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovm-response-terminatedAt"></a>
The timestamp when the MicroVM terminated.
Type: Timestamp

## Errors
<a name="API_GetMicrovm_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_GetMicrovm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-microvms-2025-09-09/GetMicrovm)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-microvms-2025-09-09/GetMicrovm)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/GetMicrovm)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-microvms-2025-09-09/GetMicrovm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/GetMicrovm)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-microvms-2025-09-09/GetMicrovm)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-microvms-2025-09-09/GetMicrovm)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-microvms-2025-09-09/GetMicrovm)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-microvms-2025-09-09/GetMicrovm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/GetMicrovm)
