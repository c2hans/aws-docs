---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_ResumeDurableExecution.html
---

# ResumeDurableExecution

Resumes a paused [durable execution](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html). If the pause interrupted an invocation, or an operation completed while the execution was paused, Lambda invokes your function. Otherwise, the execution continues to wait for its pending operations.

If the execution status is `PAUSING`, this operation cancels the pause, and the in-progress invocation continues. This operation returns a successful response while the execution status is still `PAUSED` or `PAUSING`, and the status changes to `RUNNING` when Lambda processes the request. For more information about resuming executions, see [Pausing and resuming durable executions](https://docs.aws.amazon.com/lambda/latest/dg/durable-pause-resume.html).

## Request Syntax
<a name="API_ResumeDurableExecution_RequestSyntax"></a>

```
POST /2025-12-01/durable-executions/{{DurableExecutionArn}}/resume HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Reason": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ResumeDurableExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DurableExecutionArn](#API_ResumeDurableExecution_RequestSyntax) **   <a name="lambda-ResumeDurableExecution-request-uri-DurableExecutionArn"></a>
The Amazon Resource Name (ARN) of the durable execution.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:([a-zA-Z0-9-]+):lambda:([a-zA-Z0-9-]+):(\d{12}):function:([a-zA-Z0-9_-]+):(\$LATEST(?:\.PUBLISHED)?|[0-9]+)/durable-execution/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_ResumeDurableExecution_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_ResumeDurableExecution_RequestSyntax) **   <a name="lambda-ResumeDurableExecution-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide so that the request completes no more than one time. If you repeat a request with the same client token and parameters within 15 minutes, Lambda doesn't resume the execution again and returns a successful response instead of an error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [Reason](#API_ResumeDurableExecution_RequestSyntax) **   <a name="lambda-ResumeDurableExecution-request-Reason"></a>
A description of why you're resuming the execution. Lambda records the reason in the execution history.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ResumeDurableExecution_ResponseSyntax"></a>

```
HTTP/1.1 202
```

## Response Elements
<a name="API_ResumeDurableExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response with an empty HTTP body.

## Errors
<a name="API_ResumeDurableExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

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

 ** ServiceException **
The AWS Lambda service encountered an internal error.
HTTP Status Code: 500

 ** TooManyRequestsException **
The request throughput limit was exceeded. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests).
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 429

## See Also
<a name="API_ResumeDurableExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/ResumeDurableExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/ResumeDurableExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/ResumeDurableExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/ResumeDurableExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/ResumeDurableExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/ResumeDurableExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/ResumeDurableExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/ResumeDurableExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/ResumeDurableExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/ResumeDurableExecution)
