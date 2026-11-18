---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_DeleteDurableExecution.html
---

# DeleteDurableExecution
<a name="API_DeleteDurableExecution"></a>

Deletes a completed Lambda [durable execution](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html) and its data. The execution must be in a terminal state (`SUCCEEDED`, `FAILED`, `STOPPED`, or `TIMED_OUT`). Otherwise, this operation returns a `ResourceConflictException`.

The execution has `DELETING` status until the deletion finishes. For more information, see [Deleting durable executions](https://docs.aws.amazon.com/lambda/latest/dg/durable-delete.html).

## Request Syntax
<a name="API_DeleteDurableExecution_RequestSyntax"></a>

```
DELETE /2025-12-01/durable-executions/{{DurableExecutionArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteDurableExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DurableExecutionArn](#API_DeleteDurableExecution_RequestSyntax) **   <a name="lambda-DeleteDurableExecution-request-uri-DurableExecutionArn"></a>
The Amazon Resource Name (ARN) of the durable execution.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:([a-zA-Z0-9-]+):lambda:([a-zA-Z0-9-]+):(\d{12}):function:([a-zA-Z0-9_-]+):(\$LATEST(?:\.PUBLISHED)?|[0-9]+)/durable-execution/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_DeleteDurableExecution_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteDurableExecution_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "DeletionRequestTimestamp": number
}
```

## Response Elements
<a name="API_DeleteDurableExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [DeletionRequestTimestamp](#API_DeleteDurableExecution_ResponseSyntax) **   <a name="lambda-DeleteDurableExecution-response-DeletionRequestTimestamp"></a>
The timestamp when Lambda accepted the deletion request (ISO 8601 format).
Type: Timestamp

## Errors
<a name="API_DeleteDurableExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

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
<a name="API_DeleteDurableExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/DeleteDurableExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/DeleteDurableExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/DeleteDurableExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/DeleteDurableExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/DeleteDurableExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/DeleteDurableExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/DeleteDurableExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/DeleteDurableExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/DeleteDurableExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/DeleteDurableExecution)
