---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_GetDurableExecution.html
---

# GetDurableExecution
<a name="API_GetDurableExecution"></a>

Retrieves detailed information about a specific [durable execution](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html), including its current status, input payload, result or error information, and execution metadata such as start time and usage statistics.

## Request Syntax
<a name="API_GetDurableExecution_RequestSyntax"></a>

```
GET /2025-12-01/durable-executions/{{DurableExecutionArn}}?IncludeExecutionData={{IncludeExecutionData}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDurableExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DurableExecutionArn](#API_GetDurableExecution_RequestSyntax) **   <a name="lambda-GetDurableExecution-request-uri-DurableExecutionArn"></a>
The Amazon Resource Name (ARN) of the durable execution.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:([a-zA-Z0-9-]+):lambda:([a-zA-Z0-9-]+):(\d{12}):function:([a-zA-Z0-9_-]+):(\$LATEST(?:\.PUBLISHED)?|[0-9]+)/durable-execution/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_-]+)`
Required: Yes

 ** [IncludeExecutionData](#API_GetDurableExecution_RequestSyntax) **   <a name="lambda-GetDurableExecution-request-uri-IncludeExecutionData"></a>
Specifies whether to include execution data such as input payload, result, and error information in the response. Set to `false` for a more compact response that includes only execution metadata. The default value is set to `true`.

## Request Body
<a name="API_GetDurableExecution_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDurableExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DurableConfig": {
      "ExecutionTimeout": number,
      "KMSKeyArn": "string",
      "RetentionPeriodInDays": number
   },
   "DurableExecutionArn": "string",
   "DurableExecutionName": "string",
   "EndTimestamp": number,
   "Error": {
      "ErrorData": "string",
      "ErrorMessage": "string",
      "ErrorType": "string",
      "StackTrace": [ "string" ]
   },
   "ExecutionDataIncluded": boolean,
   "FunctionArn": "string",
   "InputPayload": "string",
   "Result": "string",
   "StartTimestamp": number,
   "Status": "string",
   "TraceHeader": {
      "XAmznTraceId": "string"
   },
   "Version": "string"
}
```

## Response Elements
<a name="API_GetDurableExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DurableConfig](#API_GetDurableExecution_ResponseSyntax) **   <a name="lambda-GetDurableExecution-response-DurableConfig"></a>
Configuration settings for the durable execution, including execution timeout, retention period for execution history, and an optional ARN of the AWS Key Management Service (AWS KMS) customer managed key that is used to encrypt your durable execution's payload data, including input, output, and error payloads.
Type: [DurableConfig](API_DurableConfig.md) object

 ** [DurableExecutionArn](#API_GetDurableExecution_ResponseSyntax) **   <a name="lambda-GetDurableExecution-response-DurableExecutionArn"></a>
The Amazon Resource Name (ARN) of the durable execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:([a-zA-Z0-9-]+):lambda:([a-zA-Z0-9-]+):(\d{12}):function:([a-zA-Z0-9_-]+):(\$LATEST(?:\.PUBLISHED)?|[0-9]+)/durable-execution/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_-]+)`

 ** [DurableExecutionName](#API_GetDurableExecution_ResponseSyntax) **   <a name="lambda-GetDurableExecution-response-DurableExecutionName"></a>
The name of the durable execution. This is either the name you provided when invoking the function, or a system-generated unique identifier if no name was provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`

 ** [EndTimestamp](#API_GetDurableExecution_ResponseSyntax) **   <a name="lambda-GetDurableExecution-response-EndTimestamp"></a>
The date and time when the durable execution ended, in Unix timestamp format. This field is only present if the execution has completed (status is `SUCCEEDED`, `FAILED`, `TIMED_OUT`, or `STOPPED`).
Type: Timestamp

 ** [Error](#API_GetDurableExecution_ResponseSyntax) **   <a name="lambda-GetDurableExecution-response-Error"></a>
Error information if the durable execution failed. This field is only present when the execution status is `FAILED`, `TIMED_OUT`, or `STOPPED`. The combined size of all error fields is limited to 256 KB.
Type: [ErrorObject](API_ErrorObject.md) object

 ** [ExecutionDataIncluded](#API_GetDurableExecution_ResponseSyntax) **   <a name="lambda-GetDurableExecution-response-ExecutionDataIncluded"></a>
Indicates whether execution data is included in this response. Returns `false` when `IncludeExecutionData` is set to `false` in the request.
Type: Boolean

 ** [FunctionArn](#API_GetDurableExecution_ResponseSyntax) **   <a name="lambda-GetDurableExecution-response-FunctionArn"></a>
The Amazon Resource Name (ARN) of the Lambda function that was invoked to start this durable execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`

 ** [InputPayload](#API_GetDurableExecution_ResponseSyntax) **   <a name="lambda-GetDurableExecution-response-InputPayload"></a>
The JSON input payload that was provided when the durable execution was started. For asynchronous invocations, this is limited to 256 KB. For synchronous invocations, this can be up to 6 MB.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 6291456.

 ** [Result](#API_GetDurableExecution_ResponseSyntax) **   <a name="lambda-GetDurableExecution-response-Result"></a>
The JSON result returned by the durable execution if it completed successfully. This field is only present when the execution status is `SUCCEEDED`. The result is limited to 256 KB.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 6291456.

 ** [StartTimestamp](#API_GetDurableExecution_ResponseSyntax) **   <a name="lambda-GetDurableExecution-response-StartTimestamp"></a>
The date and time when the durable execution started, in Unix timestamp format.
Type: Timestamp

 ** [Status](#API_GetDurableExecution_ResponseSyntax) **   <a name="lambda-GetDurableExecution-response-Status"></a>
The current status of the durable execution. Valid values are `RUNNING`, `SUCCEEDED`, `FAILED`, `TIMED_OUT`, and `STOPPED`.
Type: String
Valid Values: `RUNNING | SUCCEEDED | FAILED | TIMED_OUT | STOPPED`

 ** [TraceHeader](#API_GetDurableExecution_ResponseSyntax) **   <a name="lambda-GetDurableExecution-response-TraceHeader"></a>
The trace headers associated with the durable execution.
Type: [TraceHeader](API_TraceHeader.md) object

 ** [Version](#API_GetDurableExecution_ResponseSyntax) **   <a name="lambda-GetDurableExecution-response-Version"></a>
The version of the Lambda function that was invoked for this durable execution. This ensures that all replays during the execution use the same function version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(\$LATEST(\.PUBLISHED)?|[0-9]+)`

## Errors
<a name="API_GetDurableExecution_Errors"></a>

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
<a name="API_GetDurableExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/GetDurableExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/GetDurableExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/GetDurableExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/GetDurableExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/GetDurableExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/GetDurableExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/GetDurableExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/GetDurableExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/GetDurableExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/GetDurableExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
