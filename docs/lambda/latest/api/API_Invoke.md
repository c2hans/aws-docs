---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_Invoke.html
---

# Invoke
<a name="API_Invoke"></a>

Invokes a Lambda function. You can invoke a function synchronously (and wait for the response), or asynchronously. By default, Lambda invokes your function synchronously (i.e. the`InvocationType` is `RequestResponse`). To invoke a function asynchronously, set `InvocationType` to `Event`. Lambda passes the `ClientContext` object to your function for synchronous invocations only.

For synchronous invocations, the maximum payload size is 6 MB. For asynchronous invocations, the maximum payload size is 1 MB.

For [synchronous invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-sync.html), details about the function response, including errors, are included in the response body and headers. For either invocation type, you can find more information in the [execution log](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions.html) and [trace](https://docs.aws.amazon.com/lambda/latest/dg/lambda-x-ray.html).

When an error occurs, your function may be invoked multiple times. Retry behavior varies by error type, client, event source, and invocation type. For example, if you invoke a function asynchronously and it returns an error, Lambda executes the function up to two more times. For more information, see [Error handling and automatic retries in Lambda](https://docs.aws.amazon.com/lambda/latest/dg/invocation-retries.html).

For [asynchronous invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html), Lambda adds events to a queue before sending them to your function. If your function does not have enough capacity to keep up with the queue, events may be lost. Occasionally, your function may receive the same event multiple times, even if no error occurs. To retain events that were not processed, configure your function with a [dead-letter queue](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq).

The status code in the API response doesn't reflect function errors. Error codes are reserved for errors that prevent your function from executing, such as permissions errors, [quota](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) errors, or issues with your function's code and configuration. For example, Lambda returns `TooManyRequestsException` if running the function would cause you to exceed a concurrency limit at either the account level (`ConcurrentInvocationLimitExceeded`) or function level (`ReservedFunctionConcurrentInvocationLimitExceeded`).

For functions with a long timeout, your client might disconnect during synchronous invocation while it waits for a response. Configure your HTTP client, SDK, firewall, proxy, or operating system to allow for long connections with timeout or keep-alive settings.

This operation requires permission for the [lambda:InvokeFunction](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awslambda.html) action. For details on how to set up permissions for cross-account invocations, see [Granting function access to other accounts](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html#permissions-resource-xaccountinvoke).

## Request Syntax
<a name="API_Invoke_RequestSyntax"></a>

```
POST /2015-03-31/functions/{{FunctionName}}/invocations?Qualifier={{Qualifier}} HTTP/1.1
X-Amz-Invocation-Type: {{InvocationType}}
X-Amz-Log-Type: {{LogType}}
X-Amz-Client-Context: {{ClientContext}}
X-Amz-Durable-Execution-Name: {{DurableExecutionName}}
X-Amz-Tenant-Id: {{TenantId}}

{{Payload}}
```

## URI Request Parameters
<a name="API_Invoke_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ClientContext](#API_Invoke_RequestSyntax) **   <a name="lambda-Invoke-request-ClientContext"></a>
Up to 3,583 bytes of base64-encoded data about the invoking client to pass to the function in the context object. Lambda passes the `ClientContext` object to your function for synchronous invocations only.

 ** [DurableExecutionName](#API_Invoke_RequestSyntax) **   <a name="lambda-Invoke-request-DurableExecutionName"></a>
A unique name for the durable execution. If you invoke a durable function using a name that already exists with the same payload, Lambda returns the existing execution instead of creating a duplicate. If the payload differs, Lambda returns a `DurableExecutionAlreadyStartedException` error.
If not specified, Lambda generates a unique identifier automatically. For more information, see [Execution names](https://docs.aws.amazon.com/lambda/latest/dg/durable-execution-idempotency.html#durable-idempotency-execution-names).
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`

 ** [FunctionName](#API_Invoke_RequestSyntax) **   <a name="lambda-Invoke-request-uri-FunctionName"></a>
The name or ARN of the Lambda function, version, or alias.

**Name formats**
+  **Function name** – `my-function` (name-only), `my-function:v1` (with alias).
+  **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
+  **Partial ARN** – `123456789012:function:my-function`.
You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_\.]+)(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`
Required: Yes

 ** [InvocationType](#API_Invoke_RequestSyntax) **   <a name="lambda-Invoke-request-InvocationType"></a>
Choose from the following options.
+  `RequestResponse` (default) – Invoke the function synchronously. Keep the connection open until the function returns a response or times out. The API response includes the function response and additional data.
+  `Event` – Invoke the function asynchronously. Send events that fail multiple times to the function's dead-letter queue (if one is configured). The API response only includes a status code.
+  `DryRun` – Validate parameter values and verify that the user or role has permission to invoke the function.
Valid Values: `Event | RequestResponse | DryRun`

 ** [LogType](#API_Invoke_RequestSyntax) **   <a name="lambda-Invoke-request-LogType"></a>
Set to `Tail` to include the execution log in the response. Applies to synchronously invoked functions only.
Valid Values: `None | Tail`

 ** [Qualifier](#API_Invoke_RequestSyntax) **   <a name="lambda-Invoke-request-uri-Qualifier"></a>
Specify a version or alias to invoke a published version of the function.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\$(LATEST(\.PUBLISHED)?)|[a-zA-Z0-9-_$]+`

 ** [TenantId](#API_Invoke_RequestSyntax) **   <a name="lambda-Invoke-request-TenantId"></a>
The identifier of the tenant in a multi-tenant Lambda function.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\._:\/=+\-@ ]+`

## Request Body
<a name="API_Invoke_RequestBody"></a>

The request accepts the following binary data.

 ** [Payload](#API_Invoke_RequestSyntax) **   <a name="lambda-Invoke-request-Payload"></a>
The JSON that you want to provide to your Lambda function as input. The maximum payload size is 6 MB for synchronous invocations and 1 MB for asynchronous invocations.
You can enter the JSON directly. For example, `--payload '{ "key": "value" }'`. You can also specify a file path. For example, `--payload file://payload.json`.

## Response Syntax
<a name="API_Invoke_ResponseSyntax"></a>

```
HTTP/1.1 {{StatusCode}}
X-Amz-Function-Error: {{FunctionError}}
X-Amz-Log-Result: {{LogResult}}
X-Amz-Executed-Version: {{ExecutedVersion}}
X-Amz-Durable-Execution-Arn: {{DurableExecutionArn}}

{{Payload}}
```

## Response Elements
<a name="API_Invoke_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [StatusCode](#API_Invoke_ResponseSyntax) **   <a name="lambda-Invoke-response-StatusCode"></a>
The HTTP status code is in the 200 range for a successful request. For the `RequestResponse` invocation type, this status code is 200. For the `Event` invocation type, this status code is 202. For the `DryRun` invocation type, the status code is 204.

The response returns the following HTTP headers.

 ** [DurableExecutionArn](#API_Invoke_ResponseSyntax) **   <a name="lambda-Invoke-response-DurableExecutionArn"></a>
The ARN of the durable execution that was started. This is returned when invoking a durable function and provides a unique identifier for tracking the execution.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:([a-zA-Z0-9-]+):lambda:([a-zA-Z0-9-]+):(\d{12}):function:([a-zA-Z0-9_-]+):(\$LATEST(?:\.PUBLISHED)?|[0-9]+)/durable-execution/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_-]+)`

 ** [ExecutedVersion](#API_Invoke_ResponseSyntax) **   <a name="lambda-Invoke-response-ExecutedVersion"></a>
The version of the function that executed. When you invoke a function with an alias, this indicates which version the alias resolved to.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(\$LATEST|[0-9]+)`

 ** [FunctionError](#API_Invoke_ResponseSyntax) **   <a name="lambda-Invoke-response-FunctionError"></a>
If present, indicates that an error occurred during function execution. Details about the error are included in the response payload.

 ** [LogResult](#API_Invoke_ResponseSyntax) **   <a name="lambda-Invoke-response-LogResult"></a>
The last 4 KB of the execution log, which is base64-encoded.

The response returns the following as the HTTP body.

 ** [Payload](#API_Invoke_ResponseSyntax) **   <a name="lambda-Invoke-response-Payload"></a>
The response from the function, or an error object.

## Errors
<a name="API_Invoke_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CodeArtifactUserDeletedException **
The Lambda function couldn't be invoked because its code artifact user has been deleted. Wait for Lambda to provision a new code artifact user, or update the function's code package to recreate it.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 409

 ** CodeArtifactUserFailedException **
The Lambda function couldn't be invoked because provisioning of its code artifact user failed. Update the function's code package or check the Lambda function's `State` and `StateReasonCode` for additional context.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 409

 ** CodeArtifactUserPendingException **
The Lambda function couldn't be invoked because its code artifact user is still being provisioned. Wait for the function's `State` to become `Active` and try the request again.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 409

 ** DurableExecutionAlreadyStartedException **
The durable execution with the specified name has already been started. Each durable execution name must be unique within the function. Use a different name or check the status of the existing execution.
 ** Type **
The exception type.
HTTP Status Code: 409

 ** EC2AccessDeniedException **
Need additional permissions to configure VPC settings.
HTTP Status Code: 502

 ** EC2ThrottledException **
Amazon EC2 throttled AWS Lambda during Lambda function initialization using the execution role provided for the function.
HTTP Status Code: 502

 ** EC2UnexpectedException **
 AWS Lambda received an unexpected Amazon EC2 client exception while setting up for the Lambda function.
HTTP Status Code: 502

 ** EFSIOException **
An error occurred when reading from or writing to a connected file system.
HTTP Status Code: 410

 ** EFSMountConnectivityException **
The Lambda function couldn't make a network connection to the configured file system.
HTTP Status Code: 408

 ** EFSMountFailureException **
The Lambda function couldn't mount the configured file system due to a permission or configuration issue.
HTTP Status Code: 403

 ** EFSMountTimeoutException **
The Lambda function made a network connection to the configured file system, but the mount operation timed out.
HTTP Status Code: 408

 ** ENILimitReachedException **
 AWS Lambda couldn't create an elastic network interface in the VPC, specified as part of Lambda function configuration, because the limit for network interfaces has been reached. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html).
HTTP Status Code: 502

 ** ENINotReadyException **
 AWS Lambda couldn't invoke the Lambda function because the elastic network interface (ENI) configured for its VPC connection isn't ready yet. Wait a few moments and try the request again. For more information about VPC configuration, see [Configuring a Lambda function to access resources in a VPC](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html).
 ** Message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 502

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** InvalidRequestContentException **
The request body could not be parsed as JSON, or a request header is invalid. For example, the 'x-amzn-RequestId' header is not a valid UUID string.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** InvalidRuntimeException **
The runtime or runtime version specified is not supported.
HTTP Status Code: 502

 ** InvalidSecurityGroupIDException **
The security group ID provided in the Lambda function VPC configuration is not valid.
HTTP Status Code: 502

 ** InvalidSubnetIDException **
The subnet ID provided in the Lambda function VPC configuration is not valid.
HTTP Status Code: 502

 ** InvalidZipFileException **
 AWS Lambda could not unzip the deployment package.
HTTP Status Code: 502

 ** KMSAccessDeniedException **
Lambda couldn't decrypt the environment variables because AWS KMS access was denied. Check the Lambda function's KMS permissions.
HTTP Status Code: 502

 ** KMSDisabledException **
Lambda couldn't decrypt the environment variables because the AWS KMS key used is disabled. Check the Lambda function's KMS key settings.
HTTP Status Code: 502

 ** KMSInvalidStateException **
Lambda couldn't decrypt the environment variables because the state of the AWS KMS key used is not valid for Decrypt. Check the function's KMS key settings.
HTTP Status Code: 502

 ** KMSNotFoundException **
Lambda couldn't decrypt the environment variables because the AWS KMS key was not found. Check the function's KMS key settings.
HTTP Status Code: 502

 ** ModeNotSupportedException **
The Lambda function doesn't support the invocation mode requested. For example, calling `Invoke` with `InvocationType=RequestResponse` on a function configured for asynchronous-only invocation, or vice versa. For more information about invocation types, see [Invoking Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/invocation-options.html).
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** NoPublishedVersionException **
The function has no published versions available.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** RecursiveInvocationException **
Lambda has detected your function being invoked in a recursive loop with other AWS resources and stopped your function's invocation.
 ** Message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** RequestTooLargeException **
The request payload exceeded the `Invoke` request body JSON input quota. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html).
HTTP Status Code: 413

 ** ResourceConflictException **
The resource already exists, or another operation is in progress.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The resource specified in the request does not exist.
HTTP Status Code: 404

 ** ResourceNotReadyException **
The function is inactive and its VPC connection is no longer available. Wait for the VPC connection to reestablish and try again.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 502

 ** S3FilesMountConnectivityException **
The Lambda function couldn't make a network connection to the configured S3 Files access point.
 ** Message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 408

 ** S3FilesMountFailureException **
The Lambda function couldn't mount the configured S3 Files access point due to a permission or configuration issue.
 ** Message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 403

 ** S3FilesMountTimeoutException **
The Lambda function made a network connection to the configured S3 Files access point, but the mount operation timed out.
 ** Message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 408

 ** SerializedRequestEntityTooLargeException **
The request payload exceeded the maximum allowed size for serialized request entities.
 ** Type **
The error type.
HTTP Status Code: 413

 ** ServiceException **
The AWS Lambda service encountered an internal error.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request would exceed a service quota. For more information about Lambda service quotas, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html). To request a quota increase, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.
 ** Message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 402

 ** SnapStartException **
The `afterRestore()` [runtime hook](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-runtime-hooks.html) encountered an error. For more information, check the Amazon CloudWatch logs.
HTTP Status Code: 400

 ** SnapStartNotReadyException **
Lambda is initializing your function. You can invoke the function when the [function state](https://docs.aws.amazon.com/lambda/latest/dg/functions-states.html) becomes `Active`.
HTTP Status Code: 409

 ** SnapStartRegenerationFailureException **
Lambda couldn't regenerate the SnapStart snapshot for the function. SnapStart-enabled functions periodically regenerate snapshots when their underlying runtime or dependencies change; this regeneration failed. Wait for Lambda to retry, or update the function's configuration to trigger a new snapshot. For more information, see [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html).
 ** Message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 409

 ** SnapStartTimeoutException **
Lambda couldn't restore the snapshot within the timeout limit.
HTTP Status Code: 408

 ** SubnetIPAddressLimitReachedException **
 AWS Lambda couldn't set up VPC access for the Lambda function because one or more configured subnets has no available IP addresses.
HTTP Status Code: 502

 ** TooManyRequestsException **
The request throughput limit was exceeded. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests).
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 429

 ** UnsupportedMediaTypeException **
The content type of the `Invoke` request body is not JSON.
HTTP Status Code: 415

## See Also
<a name="API_Invoke_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/Invoke)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/Invoke)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/Invoke)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/Invoke)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/Invoke)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/Invoke)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/Invoke)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/Invoke)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/Invoke)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/Invoke)
