---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_StopDurableExecution.html
---

# StopDurableExecution
<a name="API_StopDurableExecution"></a>

Stops a running [durable execution](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html). The execution transitions to STOPPED status and cannot be resumed. Any in-progress operations are terminated.

## Request Syntax
<a name="API_StopDurableExecution_RequestSyntax"></a>

```
POST /2025-12-01/durable-executions/{{DurableExecutionArn}}/stop HTTP/1.1
Content-type: application/json

{
   "ErrorData": "{{string}}",
   "ErrorMessage": "{{string}}",
   "ErrorType": "{{string}}",
   "StackTrace": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_StopDurableExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DurableExecutionArn](#API_StopDurableExecution_RequestSyntax) **   <a name="lambda-StopDurableExecution-request-uri-DurableExecutionArn"></a>
The Amazon Resource Name (ARN) of the durable execution.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:([a-zA-Z0-9-]+):lambda:([a-zA-Z0-9-]+):(\d{12}):function:([a-zA-Z0-9_-]+):(\$LATEST(?:\.PUBLISHED)?|[0-9]+)/durable-execution/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_StopDurableExecution_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ErrorData](#API_StopDurableExecution_RequestSyntax) **   <a name="lambda-StopDurableExecution-request-ErrorData"></a>
Machine-readable error data.
Type: String
Required: No

 ** [ErrorMessage](#API_StopDurableExecution_RequestSyntax) **   <a name="lambda-StopDurableExecution-request-ErrorMessage"></a>
A human-readable error message.
Type: String
Required: No

 ** [ErrorType](#API_StopDurableExecution_RequestSyntax) **   <a name="lambda-StopDurableExecution-request-ErrorType"></a>
The error type.
Type: String
Required: No

 ** [StackTrace](#API_StopDurableExecution_RequestSyntax) **   <a name="lambda-StopDurableExecution-request-StackTrace"></a>
Stack trace information for the error.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_StopDurableExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "StopTimestamp": number
}
```

## Response Elements
<a name="API_StopDurableExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StopTimestamp](#API_StopDurableExecution_ResponseSyntax) **   <a name="lambda-StopDurableExecution-response-StopTimestamp"></a>
The timestamp when the execution was stopped (ISO 8601 format).
Type: Timestamp

## Errors
<a name="API_StopDurableExecution_Errors"></a>

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
<a name="API_StopDurableExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/StopDurableExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/StopDurableExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/StopDurableExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/StopDurableExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/StopDurableExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/StopDurableExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/StopDurableExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/StopDurableExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/StopDurableExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/StopDurableExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
