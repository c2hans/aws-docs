---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_PutFunctionConcurrency.html
---

# PutFunctionConcurrency
<a name="API_PutFunctionConcurrency"></a>

Sets the maximum number of simultaneous executions for a function, and reserves capacity for that concurrency level.

Concurrency settings apply to the function as a whole, including all published versions and the unpublished version. Reserving concurrency both ensures that your function has capacity to process the specified number of events simultaneously, and prevents it from scaling beyond that level. Use [GetFunction](API_GetFunction.md) to see the current setting for a function.

Use [GetAccountSettings](API_GetAccountSettings.md) to see your Regional concurrency limit. You can reserve concurrency for as many functions as you like, as long as you leave at least 100 simultaneous executions unreserved for functions that aren't configured with a per-function limit. For more information, see [Lambda function scaling](https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html).

## Request Syntax
<a name="API_PutFunctionConcurrency_RequestSyntax"></a>

```
PUT /2017-10-31/functions/{{FunctionName}}/concurrency HTTP/1.1
Content-type: application/json

{
   "ReservedConcurrentExecutions": {{number}}
}
```

## URI Request Parameters
<a name="API_PutFunctionConcurrency_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FunctionName](#API_PutFunctionConcurrency_RequestSyntax) **   <a name="lambda-PutFunctionConcurrency-request-uri-FunctionName"></a>
The name or ARN of the Lambda function.

**Name formats**
+  **Function name** – `my-function`.
+  **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
+  **Partial ARN** – `123456789012:function:my-function`.
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?`
Required: Yes

## Request Body
<a name="API_PutFunctionConcurrency_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ReservedConcurrentExecutions](#API_PutFunctionConcurrency_RequestSyntax) **   <a name="lambda-PutFunctionConcurrency-request-ReservedConcurrentExecutions"></a>
The number of simultaneous executions to reserve for the function.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

## Response Syntax
<a name="API_PutFunctionConcurrency_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ReservedConcurrentExecutions": number
}
```

## Response Elements
<a name="API_PutFunctionConcurrency_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReservedConcurrentExecutions](#API_PutFunctionConcurrency_ResponseSyntax) **   <a name="lambda-PutFunctionConcurrency-response-ReservedConcurrentExecutions"></a>
The number of concurrent executions that are reserved for this function. For more information, see [Managing Lambda reserved concurrency](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html).
Type: Integer
Valid Range: Minimum value of 0.

## Errors
<a name="API_PutFunctionConcurrency_Errors"></a>

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
<a name="API_PutFunctionConcurrency_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/PutFunctionConcurrency)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/PutFunctionConcurrency)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/PutFunctionConcurrency)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/PutFunctionConcurrency)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/PutFunctionConcurrency)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/PutFunctionConcurrency)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/PutFunctionConcurrency)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/PutFunctionConcurrency)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/PutFunctionConcurrency)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/PutFunctionConcurrency)
