---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_InvokeAsync.html
---

# InvokeAsync
<a name="API_InvokeAsync"></a>

 *This action has been deprecated.*

**Note**
For asynchronous function invocation, use [Invoke](API_Invoke.md).

Invokes a function asynchronously.

**Note**
The payload limit is 256KB. For larger payloads, for up to 1MB, use [Invoke](API_Invoke.md).

**Note**
If you do use the InvokeAsync action, note that it doesn't support the use of X-Ray active tracing. Trace ID is not propagated to the function, even if X-Ray active tracing is turned on.

## Request Syntax
<a name="API_InvokeAsync_RequestSyntax"></a>

```
POST /2014-11-13/functions/{{FunctionName}}/invoke-async HTTP/1.1

{{InvokeArgs}}
```

## URI Request Parameters
<a name="API_InvokeAsync_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FunctionName](#API_InvokeAsync_RequestSyntax) **   <a name="lambda-InvokeAsync-request-uri-FunctionName"></a>
The name or ARN of the Lambda function.

**Name formats**
+  **Function name** – `my-function`.
+  **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
+  **Partial ARN** – `123456789012:function:my-function`.
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_\.]+)(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`
Required: Yes

## Request Body
<a name="API_InvokeAsync_RequestBody"></a>

The request accepts the following binary data.

 ** [InvokeArgs](#API_InvokeAsync_RequestSyntax) **   <a name="lambda-InvokeAsync-request-InvokeArgs"></a>
The JSON that you want to provide to your Lambda function as input.
Required: Yes

## Response Syntax
<a name="API_InvokeAsync_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
```

## Response Elements
<a name="API_InvokeAsync_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_InvokeAsync_ResponseSyntax) **   <a name="lambda-InvokeAsync-response-Status"></a>
The status code.

## Errors
<a name="API_InvokeAsync_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestContentException **
The request body could not be parsed as JSON, or a request header is invalid. For example, the 'x-amzn-RequestId' header is not a valid UUID string.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** InvalidRuntimeException **
The runtime or runtime version specified is not supported.
HTTP Status Code: 502

 ** ModeNotSupportedException **
The Lambda function doesn't support the invocation mode requested. For example, calling `Invoke` with `InvocationType=RequestResponse` on a function configured for asynchronous-only invocation, or vice versa. For more information about invocation types, see [Invoking Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/invocation-options.html).
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

 ** ServiceQuotaExceededException **
The request would exceed a service quota. For more information about Lambda service quotas, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html). To request a quota increase, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.
 ** Message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 402

 ** SnapStartRegenerationFailureException **
Lambda couldn't regenerate the SnapStart snapshot for the function. SnapStart-enabled functions periodically regenerate snapshots when their underlying runtime or dependencies change; this regeneration failed. Wait for Lambda to retry, or update the function's configuration to trigger a new snapshot. For more information, see [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html).
 ** Message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 409

## See Also
<a name="API_InvokeAsync_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/InvokeAsync)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/InvokeAsync)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/InvokeAsync)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/InvokeAsync)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/InvokeAsync)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/InvokeAsync)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/InvokeAsync)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/InvokeAsync)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/InvokeAsync)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/InvokeAsync)
