---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_InvokeWithResponseStream.html
---

# InvokeWithResponseStream
<a name="API_InvokeWithResponseStream"></a>

Configure your Lambda functions to stream response payloads back to clients. For more information, see [Configuring a Lambda function to stream responses](https://docs.aws.amazon.com/lambda/latest/dg/configuration-response-streaming.html).

This operation requires permission for the [lambda:InvokeFunction](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awslambda.html) action. For details on how to set up permissions for cross-account invocations, see [Granting function access to other accounts](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html#permissions-resource-xaccountinvoke).

## Request Syntax
<a name="API_InvokeWithResponseStream_RequestSyntax"></a>

```
POST /2021-11-15/functions/{{FunctionName}}/response-streaming-invocations?Qualifier={{Qualifier}} HTTP/1.1
X-Amz-Invocation-Type: {{InvocationType}}
X-Amz-Log-Type: {{LogType}}
X-Amz-Client-Context: {{ClientContext}}
X-Amz-Tenant-Id: {{TenantId}}

{{Payload}}
```

## URI Request Parameters
<a name="API_InvokeWithResponseStream_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ClientContext](#API_InvokeWithResponseStream_RequestSyntax) **   <a name="lambda-InvokeWithResponseStream-request-ClientContext"></a>
Up to 3,583 bytes of base64-encoded data about the invoking client to pass to the function in the context object.

 ** [FunctionName](#API_InvokeWithResponseStream_RequestSyntax) **   <a name="lambda-InvokeWithResponseStream-request-uri-FunctionName"></a>
The name or ARN of the Lambda function.

**Name formats**
+  **Function name** – `my-function`.
+  **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
+  **Partial ARN** – `123456789012:function:my-function`.
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_\.]+)(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`
Required: Yes

 ** [InvocationType](#API_InvokeWithResponseStream_RequestSyntax) **   <a name="lambda-InvokeWithResponseStream-request-InvocationType"></a>
Use one of the following options:
+  `RequestResponse` (default) – Invoke the function synchronously. Keep the connection open until the function returns a response or times out. The API operation response includes the function response and additional data.
+  `DryRun` – Validate parameter values and verify that the IAM user or role has permission to invoke the function.
Valid Values: `RequestResponse | DryRun`

 ** [LogType](#API_InvokeWithResponseStream_RequestSyntax) **   <a name="lambda-InvokeWithResponseStream-request-LogType"></a>
Set to `Tail` to include the execution log in the response. Applies to synchronously invoked functions only.
Valid Values: `None | Tail`

 ** [Qualifier](#API_InvokeWithResponseStream_RequestSyntax) **   <a name="lambda-InvokeWithResponseStream-request-uri-Qualifier"></a>
The alias name.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\$(LATEST(\.PUBLISHED)?)|[a-zA-Z0-9-_$]+`

 ** [TenantId](#API_InvokeWithResponseStream_RequestSyntax) **   <a name="lambda-InvokeWithResponseStream-request-TenantId"></a>
The identifier of the tenant in a multi-tenant Lambda function.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\._:\/=+\-@ ]+`

## Request Body
<a name="API_InvokeWithResponseStream_RequestBody"></a>

The request accepts the following binary data.

 ** [Payload](#API_InvokeWithResponseStream_RequestSyntax) **   <a name="lambda-InvokeWithResponseStream-request-Payload"></a>
The JSON that you want to provide to your Lambda function as input.
You can enter the JSON directly. For example, `--payload '{ "key": "value" }'`. You can also specify a file path. For example, `--payload file://payload.json`.

## Response Syntax
<a name="API_InvokeWithResponseStream_ResponseSyntax"></a>

```
HTTP/1.1 {{StatusCode}}
X-Amz-Executed-Version: {{ExecutedVersion}}
Content-Type: {{ResponseStreamContentType}}
Content-type: application/json

{
   "InvokeComplete": {
      "ErrorCode": "string",
      "ErrorDetails": "string",
      "LogResult": "string"
   },
   "PayloadChunk": {
      "Payload": blob
   }
}
```

## Response Elements
<a name="API_InvokeWithResponseStream_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [StatusCode](#API_InvokeWithResponseStream_ResponseSyntax) **   <a name="lambda-InvokeWithResponseStream-response-StatusCode"></a>
For a successful request, the HTTP status code is in the 200 range. For the `RequestResponse` invocation type, this status code is 200. For the `DryRun` invocation type, this status code is 204.

The response returns the following HTTP headers.

 ** [ExecutedVersion](#API_InvokeWithResponseStream_ResponseSyntax) **   <a name="lambda-InvokeWithResponseStream-response-ExecutedVersion"></a>
The version of the function that executed. When you invoke a function with an alias, this indicates which version the alias resolved to.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(\$LATEST|[0-9]+)`

 ** [ResponseStreamContentType](#API_InvokeWithResponseStream_ResponseSyntax) **   <a name="lambda-InvokeWithResponseStream-response-ResponseStreamContentType"></a>
The type of data the stream is returning.

The following data is returned in JSON format by the service.

 ** [InvokeComplete](#API_InvokeWithResponseStream_ResponseSyntax) **   <a name="lambda-InvokeWithResponseStream-response-InvokeComplete"></a>
An object that's returned when the stream has ended and all the payload chunks have been returned.
Type: [InvokeWithResponseStreamCompleteEvent](API_InvokeWithResponseStreamCompleteEvent.md) object

 ** [PayloadChunk](#API_InvokeWithResponseStream_ResponseSyntax) **   <a name="lambda-InvokeWithResponseStream-response-PayloadChunk"></a>
A chunk of the streamed response payload.
Type: [InvokeResponseStreamUpdate](API_InvokeResponseStreamUpdate.md) object

## Errors
<a name="API_InvokeWithResponseStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_InvokeWithResponseStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/InvokeWithResponseStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/InvokeWithResponseStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/InvokeWithResponseStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/InvokeWithResponseStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/InvokeWithResponseStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/InvokeWithResponseStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/InvokeWithResponseStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/InvokeWithResponseStream)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/InvokeWithResponseStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/InvokeWithResponseStream)
