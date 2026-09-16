---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_GetDurableExecutionHistory.html
---

# GetDurableExecutionHistory
<a name="API_GetDurableExecutionHistory"></a>

Retrieves the execution history for a [durable execution](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html), showing all the steps, callbacks, and events that occurred during the execution. This provides a detailed audit trail of the execution's progress over time.

The history is available while the execution is running and for a retention period after it completes (1-90 days, default 30 days). You can control whether to include execution data such as step results and callback payloads.

## Request Syntax
<a name="API_GetDurableExecutionHistory_RequestSyntax"></a>

```
GET /2025-12-01/durable-executions/{{DurableExecutionArn}}/history?IncludeExecutionData={{IncludeExecutionData}}&Marker={{Marker}}&MaxItems={{MaxItems}}&ReverseOrder={{ReverseOrder}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDurableExecutionHistory_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DurableExecutionArn](#API_GetDurableExecutionHistory_RequestSyntax) **   <a name="lambda-GetDurableExecutionHistory-request-uri-DurableExecutionArn"></a>
The Amazon Resource Name (ARN) of the durable execution.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:([a-zA-Z0-9-]+):lambda:([a-zA-Z0-9-]+):(\d{12}):function:([a-zA-Z0-9_-]+):(\$LATEST(?:\.PUBLISHED)?|[0-9]+)/durable-execution/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_-]+)`
Required: Yes

 ** [IncludeExecutionData](#API_GetDurableExecutionHistory_RequestSyntax) **   <a name="lambda-GetDurableExecutionHistory-request-uri-IncludeExecutionData"></a>
Specifies whether to include execution data such as step results and callback payloads in the history events. Set to `true` to include data, or `false` to exclude it for a more compact response. The default is `true`.

 ** [Marker](#API_GetDurableExecutionHistory_RequestSyntax) **   <a name="lambda-GetDurableExecutionHistory-request-uri-Marker"></a>
If `NextMarker` was returned from a previous request, use this value to retrieve the next page of results. Each pagination token expires after 24 hours.

 ** [MaxItems](#API_GetDurableExecutionHistory_RequestSyntax) **   <a name="lambda-GetDurableExecutionHistory-request-uri-MaxItems"></a>
The maximum number of history events to return per call. You can use `Marker` to retrieve additional pages of results. The default is 100 and the maximum allowed is 1000. A value of 0 uses the default.
Valid Range: Minimum value of 0. Maximum value of 1000.

 ** [ReverseOrder](#API_GetDurableExecutionHistory_RequestSyntax) **   <a name="lambda-GetDurableExecutionHistory-request-uri-ReverseOrder"></a>
When set to `true`, returns the history events in reverse chronological order (newest first). By default, events are returned in chronological order (oldest first).

## Request Body
<a name="API_GetDurableExecutionHistory_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDurableExecutionHistory_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Events": [
      {
         "CallbackFailedDetails": {
            "Error": {
               "Payload": {
                  "ErrorData": "string",
                  "ErrorMessage": "string",
                  "ErrorType": "string",
                  "StackTrace": [ "string" ]
               },
               "Truncated": boolean
            }
         },
         "CallbackStartedDetails": {
            "CallbackId": "string",
            "HeartbeatTimeout": number,
            "Timeout": number
         },
         "CallbackSucceededDetails": {
            "Result": {
               "Payload": "string",
               "Truncated": boolean
            }
         },
         "CallbackTimedOutDetails": {
            "Error": {
               "Payload": {
                  "ErrorData": "string",
                  "ErrorMessage": "string",
                  "ErrorType": "string",
                  "StackTrace": [ "string" ]
               },
               "Truncated": boolean
            }
         },
         "ChainedInvokeFailedDetails": {
            "Error": {
               "Payload": {
                  "ErrorData": "string",
                  "ErrorMessage": "string",
                  "ErrorType": "string",
                  "StackTrace": [ "string" ]
               },
               "Truncated": boolean
            }
         },
         "ChainedInvokeStartedDetails": {
            "DurableExecutionArn": "string",
            "ExecutedVersion": "string",
            "FunctionName": "string",
            "Input": {
               "Payload": "string",
               "Truncated": boolean
            },
            "TenantId": "string"
         },
         "ChainedInvokeStoppedDetails": {
            "Error": {
               "Payload": {
                  "ErrorData": "string",
                  "ErrorMessage": "string",
                  "ErrorType": "string",
                  "StackTrace": [ "string" ]
               },
               "Truncated": boolean
            }
         },
         "ChainedInvokeSucceededDetails": {
            "Result": {
               "Payload": "string",
               "Truncated": boolean
            }
         },
         "ChainedInvokeTimedOutDetails": {
            "Error": {
               "Payload": {
                  "ErrorData": "string",
                  "ErrorMessage": "string",
                  "ErrorType": "string",
                  "StackTrace": [ "string" ]
               },
               "Truncated": boolean
            }
         },
         "ContextFailedDetails": {
            "Error": {
               "Payload": {
                  "ErrorData": "string",
                  "ErrorMessage": "string",
                  "ErrorType": "string",
                  "StackTrace": [ "string" ]
               },
               "Truncated": boolean
            }
         },
         "ContextStartedDetails": {
         },
         "ContextSucceededDetails": {
            "Result": {
               "Payload": "string",
               "Truncated": boolean
            }
         },
         "EventId": number,
         "EventTimestamp": number,
         "EventType": "string",
         "ExecutionFailedDetails": {
            "Error": {
               "Payload": {
                  "ErrorData": "string",
                  "ErrorMessage": "string",
                  "ErrorType": "string",
                  "StackTrace": [ "string" ]
               },
               "Truncated": boolean
            }
         },
         "ExecutionStartedDetails": {
            "ExecutionTimeout": number,
            "Input": {
               "Payload": "string",
               "Truncated": boolean
            }
         },
         "ExecutionStoppedDetails": {
            "Error": {
               "Payload": {
                  "ErrorData": "string",
                  "ErrorMessage": "string",
                  "ErrorType": "string",
                  "StackTrace": [ "string" ]
               },
               "Truncated": boolean
            }
         },
         "ExecutionSucceededDetails": {
            "Result": {
               "Payload": "string",
               "Truncated": boolean
            }
         },
         "ExecutionTimedOutDetails": {
            "Error": {
               "Payload": {
                  "ErrorData": "string",
                  "ErrorMessage": "string",
                  "ErrorType": "string",
                  "StackTrace": [ "string" ]
               },
               "Truncated": boolean
            }
         },
         "Id": "string",
         "InvocationCompletedDetails": {
            "EndTimestamp": number,
            "Error": {
               "Payload": {
                  "ErrorData": "string",
                  "ErrorMessage": "string",
                  "ErrorType": "string",
                  "StackTrace": [ "string" ]
               },
               "Truncated": boolean
            },
            "RequestId": "string",
            "StartTimestamp": number
         },
         "Name": "string",
         "ParentId": "string",
         "StepFailedDetails": {
            "Error": {
               "Payload": {
                  "ErrorData": "string",
                  "ErrorMessage": "string",
                  "ErrorType": "string",
                  "StackTrace": [ "string" ]
               },
               "Truncated": boolean
            },
            "RetryDetails": {
               "CurrentAttempt": number,
               "NextAttemptDelaySeconds": number
            }
         },
         "StepStartedDetails": {
         },
         "StepSucceededDetails": {
            "Result": {
               "Payload": "string",
               "Truncated": boolean
            },
            "RetryDetails": {
               "CurrentAttempt": number,
               "NextAttemptDelaySeconds": number
            }
         },
         "SubType": "string",
         "WaitCancelledDetails": {
            "Error": {
               "Payload": {
                  "ErrorData": "string",
                  "ErrorMessage": "string",
                  "ErrorType": "string",
                  "StackTrace": [ "string" ]
               },
               "Truncated": boolean
            }
         },
         "WaitStartedDetails": {
            "Duration": number,
            "ScheduledEndTimestamp": number
         },
         "WaitSucceededDetails": {
            "Duration": number
         }
      }
   ],
   "NextMarker": "string"
}
```

## Response Elements
<a name="API_GetDurableExecutionHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Events](#API_GetDurableExecutionHistory_ResponseSyntax) **   <a name="lambda-GetDurableExecutionHistory-response-Events"></a>
An array of execution history events, ordered chronologically unless `ReverseOrder` is set to `true`. Each event represents a significant occurrence during the execution, such as step completion or callback resolution.
Type: Array of [Event](API_Event.md) objects

 ** [NextMarker](#API_GetDurableExecutionHistory_ResponseSyntax) **   <a name="lambda-GetDurableExecutionHistory-response-NextMarker"></a>
If present, indicates that more history events are available. Use this value as the `Marker` parameter in a subsequent request to retrieve the next page of results.
Type: String

## Errors
<a name="API_GetDurableExecutionHistory_Errors"></a>

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
<a name="API_GetDurableExecutionHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/GetDurableExecutionHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/GetDurableExecutionHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/GetDurableExecutionHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/GetDurableExecutionHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/GetDurableExecutionHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/GetDurableExecutionHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/GetDurableExecutionHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/GetDurableExecutionHistory)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/GetDurableExecutionHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/GetDurableExecutionHistory)
