---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_PutProvisionedConcurrencyConfig.html
---

# PutProvisionedConcurrencyConfig
<a name="API_PutProvisionedConcurrencyConfig"></a>

Adds a provisioned concurrency configuration to a function's alias or version.

## Request Syntax
<a name="API_PutProvisionedConcurrencyConfig_RequestSyntax"></a>

```
PUT /2019-09-30/functions/{{FunctionName}}/provisioned-concurrency?Qualifier={{Qualifier}} HTTP/1.1
Content-type: application/json

{
   "ProvisionedConcurrentExecutions": {{number}}
}
```

## URI Request Parameters
<a name="API_PutProvisionedConcurrencyConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FunctionName](#API_PutProvisionedConcurrencyConfig_RequestSyntax) **   <a name="lambda-PutProvisionedConcurrencyConfig-request-uri-FunctionName"></a>
The name or ARN of the Lambda function.

**Name formats**
+  **Function name** – `my-function`.
+  **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
+  **Partial ARN** – `123456789012:function:my-function`.
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?`
Required: Yes

 ** [Qualifier](#API_PutProvisionedConcurrencyConfig_RequestSyntax) **   <a name="lambda-PutProvisionedConcurrencyConfig-request-uri-Qualifier"></a>
The version number or alias name.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(|[a-zA-Z0-9$_-]+)`
Required: Yes

## Request Body
<a name="API_PutProvisionedConcurrencyConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ProvisionedConcurrentExecutions](#API_PutProvisionedConcurrencyConfig_RequestSyntax) **   <a name="lambda-PutProvisionedConcurrencyConfig-request-ProvisionedConcurrentExecutions"></a>
The amount of provisioned concurrency to allocate for the version or alias.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

## Response Syntax
<a name="API_PutProvisionedConcurrencyConfig_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "AllocatedProvisionedConcurrentExecutions": number,
   "AvailableProvisionedConcurrentExecutions": number,
   "LastModified": "string",
   "RequestedProvisionedConcurrentExecutions": number,
   "Status": "string",
   "StatusReason": "string"
}
```

## Response Elements
<a name="API_PutProvisionedConcurrencyConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [AllocatedProvisionedConcurrentExecutions](#API_PutProvisionedConcurrencyConfig_ResponseSyntax) **   <a name="lambda-PutProvisionedConcurrencyConfig-response-AllocatedProvisionedConcurrentExecutions"></a>
The amount of provisioned concurrency allocated. When a weighted alias is used during linear and canary deployments, this value fluctuates depending on the amount of concurrency that is provisioned for the function versions.
Type: Integer
Valid Range: Minimum value of 0.

 ** [AvailableProvisionedConcurrentExecutions](#API_PutProvisionedConcurrencyConfig_ResponseSyntax) **   <a name="lambda-PutProvisionedConcurrencyConfig-response-AvailableProvisionedConcurrentExecutions"></a>
The amount of provisioned concurrency available.
Type: Integer
Valid Range: Minimum value of 0.

 ** [LastModified](#API_PutProvisionedConcurrencyConfig_ResponseSyntax) **   <a name="lambda-PutProvisionedConcurrencyConfig-response-LastModified"></a>
The date and time that a user last updated the configuration, in [ISO 8601 format](https://www.iso.org/iso-8601-date-and-time-format.html).
Type: String

 ** [RequestedProvisionedConcurrentExecutions](#API_PutProvisionedConcurrencyConfig_ResponseSyntax) **   <a name="lambda-PutProvisionedConcurrencyConfig-response-RequestedProvisionedConcurrentExecutions"></a>
The amount of provisioned concurrency requested.
Type: Integer
Valid Range: Minimum value of 1.

 ** [Status](#API_PutProvisionedConcurrencyConfig_ResponseSyntax) **   <a name="lambda-PutProvisionedConcurrencyConfig-response-Status"></a>
The status of the allocation process.
Type: String
Valid Values: `IN_PROGRESS | READY | FAILED`

 ** [StatusReason](#API_PutProvisionedConcurrencyConfig_ResponseSyntax) **   <a name="lambda-PutProvisionedConcurrencyConfig-response-StatusReason"></a>
For failed allocations, the reason that provisioned concurrency could not be allocated.
Type: String

## Errors
<a name="API_PutProvisionedConcurrencyConfig_Errors"></a>

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
<a name="API_PutProvisionedConcurrencyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/PutProvisionedConcurrencyConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/PutProvisionedConcurrencyConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/PutProvisionedConcurrencyConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/PutProvisionedConcurrencyConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/PutProvisionedConcurrencyConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/PutProvisionedConcurrencyConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/PutProvisionedConcurrencyConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/PutProvisionedConcurrencyConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/PutProvisionedConcurrencyConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/PutProvisionedConcurrencyConfig)
