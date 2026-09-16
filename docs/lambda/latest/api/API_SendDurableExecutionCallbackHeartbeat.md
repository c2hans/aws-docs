---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_SendDurableExecutionCallbackHeartbeat.html
---

# SendDurableExecutionCallbackHeartbeat
<a name="API_SendDurableExecutionCallbackHeartbeat"></a>

Sends a heartbeat signal for a long-running callback operation to prevent timeout. Use this API to extend the callback timeout period while the external operation is still in progress.

## Request Syntax
<a name="API_SendDurableExecutionCallbackHeartbeat_RequestSyntax"></a>

```
POST /2025-12-01/durable-execution-callbacks/{{CallbackId}}/heartbeat HTTP/1.1
```

## URI Request Parameters
<a name="API_SendDurableExecutionCallbackHeartbeat_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CallbackId](#API_SendDurableExecutionCallbackHeartbeat_RequestSyntax) **   <a name="lambda-SendDurableExecutionCallbackHeartbeat-request-uri-CallbackId"></a>
The unique identifier for the callback operation.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[A-Za-z0-9+/]+={0,2}`
Required: Yes

## Request Body
<a name="API_SendDurableExecutionCallbackHeartbeat_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_SendDurableExecutionCallbackHeartbeat_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_SendDurableExecutionCallbackHeartbeat_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SendDurableExecutionCallbackHeartbeat_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallbackTimeoutException **
The callback ID token has either expired or the callback associated with the token has already been closed.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

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
<a name="API_SendDurableExecutionCallbackHeartbeat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/SendDurableExecutionCallbackHeartbeat)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/SendDurableExecutionCallbackHeartbeat)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/SendDurableExecutionCallbackHeartbeat)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/SendDurableExecutionCallbackHeartbeat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/SendDurableExecutionCallbackHeartbeat)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/SendDurableExecutionCallbackHeartbeat)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/SendDurableExecutionCallbackHeartbeat)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/SendDurableExecutionCallbackHeartbeat)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/SendDurableExecutionCallbackHeartbeat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/SendDurableExecutionCallbackHeartbeat)
