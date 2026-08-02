---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_CheckpointDurableExecution.html
---

# CheckpointDurableExecution
<a name="API_CheckpointDurableExecution"></a>

Saves the progress of a [durable function](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html) execution during runtime. This API is used by the Lambda durable functions SDK to checkpoint completed steps and schedule asynchronous operations. You typically don't need to call this API directly as the SDK handles checkpointing automatically.

Each checkpoint operation consumes the current checkpoint token and returns a new one for the next checkpoint. This ensures that checkpoints are applied in the correct order and prevents duplicate or out-of-order state updates.

## Request Syntax
<a name="API_CheckpointDurableExecution_RequestSyntax"></a>

```
POST /2025-12-01/durable-executions/{{DurableExecutionArn}}/checkpoint HTTP/1.1
Content-type: application/json

{
   "CheckpointToken": "{{string}}",
   "ClientToken": "{{string}}",
   "Updates": [
      {
         "Action": "{{string}}",
         "CallbackOptions": {
            "HeartbeatTimeoutSeconds": {{number}},
            "TimeoutSeconds": {{number}}
         },
         "ChainedInvokeOptions": {
            "FunctionName": "{{string}}",
            "TenantId": "{{string}}"
         },
         "ContextOptions": {
            "ReplayChildren": {{boolean}}
         },
         "Error": {
            "ErrorData": "{{string}}",
            "ErrorMessage": "{{string}}",
            "ErrorType": "{{string}}",
            "StackTrace": [ "{{string}}" ]
         },
         "Id": "{{string}}",
         "Name": "{{string}}",
         "ParentId": "{{string}}",
         "Payload": "{{string}}",
         "StepOptions": {
            "NextAttemptDelaySeconds": {{number}}
         },
         "SubType": "{{string}}",
         "Type": "{{string}}",
         "WaitOptions": {
            "WaitSeconds": {{number}}
         }
      }
   ]
}
```

## URI Request Parameters
<a name="API_CheckpointDurableExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DurableExecutionArn](#API_CheckpointDurableExecution_RequestSyntax) **   <a name="lambda-CheckpointDurableExecution-request-uri-DurableExecutionArn"></a>
The Amazon Resource Name (ARN) of the durable execution.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:([a-zA-Z0-9-]+):lambda:([a-zA-Z0-9-]+):(\d{12}):function:([a-zA-Z0-9_-]+):(\$LATEST(?:\.PUBLISHED)?|[0-9]+)/durable-execution/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_CheckpointDurableExecution_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CheckpointToken](#API_CheckpointDurableExecution_RequestSyntax) **   <a name="lambda-CheckpointDurableExecution-request-CheckpointToken"></a>
A unique token that identifies the current checkpoint state. This token is provided by the Lambda runtime and must be used to ensure checkpoints are applied in the correct order. Each checkpoint operation consumes this token and returns a new one.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[A-Za-z0-9+/]+={0,2}`
Required: Yes

 ** [ClientToken](#API_CheckpointDurableExecution_RequestSyntax) **   <a name="lambda-CheckpointDurableExecution-request-ClientToken"></a>
An optional idempotency token to ensure that duplicate checkpoint requests are handled correctly. If provided, Lambda uses this token to detect and handle duplicate requests within a 15-minute window.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [Updates](#API_CheckpointDurableExecution_RequestSyntax) **   <a name="lambda-CheckpointDurableExecution-request-Updates"></a>
An array of state updates to apply during this checkpoint. Each update represents a change to the execution state, such as completing a step, starting a callback, or scheduling a timer. Updates are applied atomically as part of the checkpoint operation.
Type: Array of [OperationUpdate](API_OperationUpdate.md) objects
Required: No

## Response Syntax
<a name="API_CheckpointDurableExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CheckpointToken": "string",
   "NewExecutionState": {
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
}
```

## Response Elements
<a name="API_CheckpointDurableExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CheckpointToken](#API_CheckpointDurableExecution_ResponseSyntax) **   <a name="lambda-CheckpointDurableExecution-response-CheckpointToken"></a>
A new checkpoint token to use for the next checkpoint operation. This token replaces the one provided in the request and must be used for subsequent checkpoints to maintain proper ordering.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[A-Za-z0-9+/]+={0,2}`

 ** [NewExecutionState](#API_CheckpointDurableExecution_ResponseSyntax) **   <a name="lambda-CheckpointDurableExecution-response-NewExecutionState"></a>
Updated execution state information that includes any changes that occurred since the last checkpoint, such as completed callbacks or expired timers. This allows the SDK to update its internal state during replay.
Type: [CheckpointUpdatedExecutionState](API_CheckpointUpdatedExecutionState.md) object

## Errors
<a name="API_CheckpointDurableExecution_Errors"></a>

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
<a name="API_CheckpointDurableExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/CheckpointDurableExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/CheckpointDurableExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/CheckpointDurableExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/CheckpointDurableExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/CheckpointDurableExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/CheckpointDurableExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/CheckpointDurableExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/CheckpointDurableExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/CheckpointDurableExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/CheckpointDurableExecution)
