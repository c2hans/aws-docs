---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_PutRuntimeManagementConfig.html
---

# PutRuntimeManagementConfig
<a name="API_PutRuntimeManagementConfig"></a>

Sets the runtime management configuration for a function's version. For more information, see [Runtime updates](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html).

## Request Syntax
<a name="API_PutRuntimeManagementConfig_RequestSyntax"></a>

```
PUT /2021-07-20/functions/{{FunctionName}}/runtime-management-config?Qualifier={{Qualifier}} HTTP/1.1
Content-type: application/json

{
   "RuntimeVersionArn": "{{string}}",
   "UpdateRuntimeOn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutRuntimeManagementConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FunctionName](#API_PutRuntimeManagementConfig_RequestSyntax) **   <a name="lambda-PutRuntimeManagementConfig-request-uri-FunctionName"></a>
The name or ARN of the Lambda function.

**Name formats**
+  **Function name** – `my-function`.
+  **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
+  **Partial ARN** – `123456789012:function:my-function`.
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_\.]+)(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`
Required: Yes

 ** [Qualifier](#API_PutRuntimeManagementConfig_RequestSyntax) **   <a name="lambda-PutRuntimeManagementConfig-request-uri-Qualifier"></a>
Specify a version of the function. This can be `$LATEST` or a published version number. If no value is specified, the configuration for the `$LATEST` version is returned.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\$(LATEST(\.PUBLISHED)?)|[a-zA-Z0-9-_$]+`

## Request Body
<a name="API_PutRuntimeManagementConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [RuntimeVersionArn](#API_PutRuntimeManagementConfig_RequestSyntax) **   <a name="lambda-PutRuntimeManagementConfig-request-RuntimeVersionArn"></a>
The ARN of the runtime version you want the function to use.
This is only required if you're using the **Manual** runtime update mode.
Type: String
Length Constraints: Minimum length of 26. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*):lambda:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}::runtime:.+`
Required: No

 ** [UpdateRuntimeOn](#API_PutRuntimeManagementConfig_RequestSyntax) **   <a name="lambda-PutRuntimeManagementConfig-request-UpdateRuntimeOn"></a>
Specify the runtime update mode.
+  **Auto (default)** - Automatically update to the most recent and secure runtime version using a [Two-phase runtime version rollout](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html#runtime-management-two-phase). This is the best choice for most customers to ensure they always benefit from runtime updates.
+  **Function update** - Lambda updates the runtime of your function to the most recent and secure runtime version when you update your function. This approach synchronizes runtime updates with function deployments, giving you control over when runtime updates are applied and allowing you to detect and mitigate rare runtime update incompatibilities early. When using this setting, you need to regularly update your functions to keep their runtime up-to-date.
+  **Manual** - You specify a runtime version in your function configuration. The function will use this runtime version indefinitely. In the rare case where a new runtime version is incompatible with an existing function, this allows you to roll back your function to an earlier runtime version. For more information, see [Roll back a runtime version](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html#runtime-management-rollback).
Type: String
Valid Values: `Auto | Manual | FunctionUpdate`
Required: Yes

## Response Syntax
<a name="API_PutRuntimeManagementConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "FunctionArn": "string",
   "RuntimeVersionArn": "string",
   "UpdateRuntimeOn": "string"
}
```

## Response Elements
<a name="API_PutRuntimeManagementConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FunctionArn](#API_PutRuntimeManagementConfig_ResponseSyntax) **   <a name="lambda-PutRuntimeManagementConfig-response-FunctionArn"></a>
The ARN of the function
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`

 ** [RuntimeVersionArn](#API_PutRuntimeManagementConfig_ResponseSyntax) **   <a name="lambda-PutRuntimeManagementConfig-response-RuntimeVersionArn"></a>
The ARN of the runtime the function is configured to use. If the runtime update mode is **manual**, the ARN is returned, otherwise `null` is returned.
Type: String
Length Constraints: Minimum length of 26. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*):lambda:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}::runtime:.+`

 ** [UpdateRuntimeOn](#API_PutRuntimeManagementConfig_ResponseSyntax) **   <a name="lambda-PutRuntimeManagementConfig-response-UpdateRuntimeOn"></a>
The runtime update mode.
Type: String
Valid Values: `Auto | Manual | FunctionUpdate`

## Errors
<a name="API_PutRuntimeManagementConfig_Errors"></a>

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
<a name="API_PutRuntimeManagementConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/PutRuntimeManagementConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/PutRuntimeManagementConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/PutRuntimeManagementConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/PutRuntimeManagementConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/PutRuntimeManagementConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/PutRuntimeManagementConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/PutRuntimeManagementConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/PutRuntimeManagementConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/PutRuntimeManagementConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/PutRuntimeManagementConfig)
