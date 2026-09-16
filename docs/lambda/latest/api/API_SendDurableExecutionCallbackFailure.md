---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_SendDurableExecutionCallbackFailure.html
---

# SendDurableExecutionCallbackFailure
<a name="API_SendDurableExecutionCallbackFailure"></a>

Sends a failure response for a callback operation in a durable execution. Use this API when an external system cannot complete a callback operation successfully.

## Request Syntax
<a name="API_SendDurableExecutionCallbackFailure_RequestSyntax"></a>

```
POST /2025-12-01/durable-execution-callbacks/{{CallbackId}}/fail HTTP/1.1
Content-type: application/json

{
   "ErrorData": "{{string}}",
   "ErrorMessage": "{{string}}",
   "ErrorType": "{{string}}",
   "StackTrace": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_SendDurableExecutionCallbackFailure_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CallbackId](#API_SendDurableExecutionCallbackFailure_RequestSyntax) **   <a name="lambda-SendDurableExecutionCallbackFailure-request-uri-CallbackId"></a>
The unique identifier for the callback operation.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[A-Za-z0-9+/]+={0,2}`
Required: Yes

## Request Body
<a name="API_SendDurableExecutionCallbackFailure_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ErrorData](#API_SendDurableExecutionCallbackFailure_RequestSyntax) **   <a name="lambda-SendDurableExecutionCallbackFailure-request-ErrorData"></a>
Machine-readable error data.
Type: String
Required: No

 ** [ErrorMessage](#API_SendDurableExecutionCallbackFailure_RequestSyntax) **   <a name="lambda-SendDurableExecutionCallbackFailure-request-ErrorMessage"></a>
A human-readable error message.
Type: String
Required: No

 ** [ErrorType](#API_SendDurableExecutionCallbackFailure_RequestSyntax) **   <a name="lambda-SendDurableExecutionCallbackFailure-request-ErrorType"></a>
The error type.
Type: String
Required: No

 ** [StackTrace](#API_SendDurableExecutionCallbackFailure_RequestSyntax) **   <a name="lambda-SendDurableExecutionCallbackFailure-request-StackTrace"></a>
Stack trace information for the error.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_SendDurableExecutionCallbackFailure_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_SendDurableExecutionCallbackFailure_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SendDurableExecutionCallbackFailure_Errors"></a>

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
<a name="API_SendDurableExecutionCallbackFailure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/SendDurableExecutionCallbackFailure)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/SendDurableExecutionCallbackFailure)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/SendDurableExecutionCallbackFailure)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/SendDurableExecutionCallbackFailure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/SendDurableExecutionCallbackFailure)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/SendDurableExecutionCallbackFailure)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/SendDurableExecutionCallbackFailure)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/SendDurableExecutionCallbackFailure)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/SendDurableExecutionCallbackFailure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/SendDurableExecutionCallbackFailure)
