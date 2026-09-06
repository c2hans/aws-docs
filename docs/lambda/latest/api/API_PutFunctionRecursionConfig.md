---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_PutFunctionRecursionConfig.html
---

# PutFunctionRecursionConfig
<a name="API_PutFunctionRecursionConfig"></a>

Sets your function's [recursive loop detection](https://docs.aws.amazon.com/lambda/latest/dg/invocation-recursion.html) configuration.

When you configure a Lambda function to output to the same service or resource that invokes the function, it's possible to create an infinite recursive loop. For example, a Lambda function might write a message to an Amazon Simple Queue Service (Amazon SQS) queue, which then invokes the same function. This invocation causes the function to write another message to the queue, which in turn invokes the function again.

Lambda can detect certain types of recursive loops shortly after they occur. When Lambda detects a recursive loop and your function's recursive loop detection configuration is set to `Terminate`, it stops your function being invoked and notifies you.

## Request Syntax
<a name="API_PutFunctionRecursionConfig_RequestSyntax"></a>

```
PUT /2024-08-31/functions/{{FunctionName}}/recursion-config HTTP/1.1
Content-type: application/json

{
   "RecursiveLoop": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutFunctionRecursionConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FunctionName](#API_PutFunctionRecursionConfig_RequestSyntax) **   <a name="lambda-PutFunctionRecursionConfig-request-uri-FunctionName"></a>
The name or ARN of the Lambda function.

**Name formats**
+  **Function name** – `my-function`.
+  **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
+  **Partial ARN** – `123456789012:function:my-function`.
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)`
Required: Yes

## Request Body
<a name="API_PutFunctionRecursionConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [RecursiveLoop](#API_PutFunctionRecursionConfig_RequestSyntax) **   <a name="lambda-PutFunctionRecursionConfig-request-RecursiveLoop"></a>
If you set your function's recursive loop detection configuration to `Allow`, Lambda doesn't take any action when it detects your function being invoked as part of a recursive loop. We recommend that you only use this setting if your design intentionally uses a Lambda function to write data back to the same AWS resource that invokes it.
If you set your function's recursive loop detection configuration to `Terminate`, Lambda stops your function being invoked and notifies you when it detects your function being invoked as part of a recursive loop.
By default, Lambda sets your function's configuration to `Terminate`.
If your design intentionally uses a Lambda function to write data back to the same AWS resource that invokes the function, then use caution and implement suitable guard rails to prevent unexpected charges being billed to your AWS account. To learn more about best practices for using recursive invocation patterns, see [Recursive patterns that cause run-away Lambda functions](https://serverlessland.com/content/service/lambda/guides/aws-lambda-operator-guide/recursive-runaway) in Serverless Land.
Type: String
Valid Values: `Allow | Terminate`
Required: Yes

## Response Syntax
<a name="API_PutFunctionRecursionConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RecursiveLoop": "string"
}
```

## Response Elements
<a name="API_PutFunctionRecursionConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RecursiveLoop](#API_PutFunctionRecursionConfig_ResponseSyntax) **   <a name="lambda-PutFunctionRecursionConfig-response-RecursiveLoop"></a>
The status of your function's recursive loop detection configuration.
When this value is set to `Allow`and Lambda detects your function being invoked as part of a recursive loop, it doesn't take any action.
When this value is set to `Terminate` and Lambda detects your function being invoked as part of a recursive loop, it stops your function being invoked and notifies you.
Type: String
Valid Values: `Allow | Terminate`

## Errors
<a name="API_PutFunctionRecursionConfig_Errors"></a>

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
<a name="API_PutFunctionRecursionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/PutFunctionRecursionConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/PutFunctionRecursionConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/PutFunctionRecursionConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/PutFunctionRecursionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/PutFunctionRecursionConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/PutFunctionRecursionConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/PutFunctionRecursionConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/PutFunctionRecursionConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/PutFunctionRecursionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/PutFunctionRecursionConfig)
