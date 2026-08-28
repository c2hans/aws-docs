---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_GetDurableExecutionState.html
---

# GetDurableExecutionState
<a name="API_GetDurableExecutionState"></a>

Retrieves the current execution state required for the replay process during [durable function](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html) execution. This API is used by the Lambda durable functions SDK to get state information needed for replay. You typically don't need to call this API directly as the SDK handles state management automatically.

The response contains operations ordered by start sequence number in ascending order. Completed operations with children don't include child operation details since they don't need to be replayed.

## Request Syntax
<a name="API_GetDurableExecutionState_RequestSyntax"></a>

```
GET /2025-12-01/durable-executions/{{DurableExecutionArn}}/state?CheckpointToken={{CheckpointToken}}&Marker={{Marker}}&MaxItems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDurableExecutionState_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CheckpointToken](#API_GetDurableExecutionState_RequestSyntax) **   <a name="lambda-GetDurableExecutionState-request-uri-CheckpointToken"></a>
A checkpoint token that identifies the current state of the execution. This token is provided by the Lambda runtime and ensures that state retrieval is consistent with the current execution context.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[A-Za-z0-9+/]+={0,2}`
Required: Yes

 ** [DurableExecutionArn](#API_GetDurableExecutionState_RequestSyntax) **   <a name="lambda-GetDurableExecutionState-request-uri-DurableExecutionArn"></a>
The Amazon Resource Name (ARN) of the durable execution.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:([a-zA-Z0-9-]+):lambda:([a-zA-Z0-9-]+):(\d{12}):function:([a-zA-Z0-9_-]+):(\$LATEST(?:\.PUBLISHED)?|[0-9]+)/durable-execution/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_-]+)`
Required: Yes

 ** [Marker](#API_GetDurableExecutionState_RequestSyntax) **   <a name="lambda-GetDurableExecutionState-request-uri-Marker"></a>
If `NextMarker` was returned from a previous request, use this value to retrieve the next page of operations. Each pagination token expires after 24 hours.

 ** [MaxItems](#API_GetDurableExecutionState_RequestSyntax) **   <a name="lambda-GetDurableExecutionState-request-uri-MaxItems"></a>
The maximum number of operations to return per call. You can use `Marker` to retrieve additional pages of results. The default is 100 and the maximum allowed is 1000. A value of 0 uses the default.
Valid Range: Minimum value of 0. Maximum value of 1000.

## Request Body
<a name="API_GetDurableExecutionState_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDurableExecutionState_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextMarker": "string",
   "Operations": [
      {
         "CallbackDetails": {
            "CallbackId": "string",
            "Error": {
               "ErrorData": "string",
               "ErrorMessage": "string",
               "ErrorType": "string",
               "StackTrace": [ "string" ]
            },
            "Result": "string"
         },
         "ChainedInvokeDetails": {
            "Error": {
               "ErrorData": "string",
               "ErrorMessage": "string",
               "ErrorType": "string",
               "StackTrace": [ "string" ]
            },
            "Result": "string"
         },
         "ContextDetails": {
            "Error": {
               "ErrorData": "string",
               "ErrorMessage": "string",
               "ErrorType": "string",
               "StackTrace": [ "string" ]
            },
            "ReplayChildren": boolean,
            "Result": "string"
         },
         "EndTimestamp": number,
         "ExecutionDetails": {
            "InputPayload": "string"
         },
         "Id": "string",
         "Name": "string",
         "ParentId": "string",
         "StartTimestamp": number,
         "Status": "string",
         "StepDetails": {
            "Attempt": number,
            "Error": {
               "ErrorData": "string",
               "ErrorMessage": "string",
               "ErrorType": "string",
               "StackTrace": [ "string" ]
            },
            "NextAttemptTimestamp": number,
            "Result": "string"
         },
         "SubType": "string",
         "Type": "string",
         "WaitDetails": {
            "ScheduledEndTimestamp": number
         }
      }
   ]
}
```

## Response Elements
<a name="API_GetDurableExecutionState_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextMarker](#API_GetDurableExecutionState_ResponseSyntax) **   <a name="lambda-GetDurableExecutionState-response-NextMarker"></a>
If present, indicates that more operations are available. Use this value as the `Marker` parameter in a subsequent request to retrieve the next page of results.
Type: String

 ** [Operations](#API_GetDurableExecutionState_ResponseSyntax) **   <a name="lambda-GetDurableExecutionState-response-Operations"></a>
An array of operations that represent the current state of the durable execution. Operations are ordered by their start sequence number in ascending order and include information needed for replay processing.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_GetDurableExecutionState_Errors"></a>

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

 ** ServiceException **
The AWS Lambda service encountered an internal error.
HTTP Status Code: 500

 ** TooManyRequestsException **
The request throughput limit was exceeded. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests).
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 429

## See Also
<a name="API_GetDurableExecutionState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/GetDurableExecutionState)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/GetDurableExecutionState)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/GetDurableExecutionState)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/GetDurableExecutionState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/GetDurableExecutionState)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/GetDurableExecutionState)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/GetDurableExecutionState)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/GetDurableExecutionState)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/GetDurableExecutionState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/GetDurableExecutionState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
