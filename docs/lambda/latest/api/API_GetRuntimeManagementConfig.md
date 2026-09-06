---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_GetRuntimeManagementConfig.html
---

# GetRuntimeManagementConfig
<a name="API_GetRuntimeManagementConfig"></a>

Retrieves the runtime management configuration for a function's version. If the runtime update mode is **Manual**, this includes the ARN of the runtime version and the runtime update mode. If the runtime update mode is **Auto** or **Function update**, this includes the runtime update mode and `null` is returned for the ARN. For more information, see [Runtime updates](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html).

## Request Syntax
<a name="API_GetRuntimeManagementConfig_RequestSyntax"></a>

```
GET /2021-07-20/functions/{{FunctionName}}/runtime-management-config?Qualifier={{Qualifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRuntimeManagementConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FunctionName](#API_GetRuntimeManagementConfig_RequestSyntax) **   <a name="lambda-GetRuntimeManagementConfig-request-uri-FunctionName"></a>
The name or ARN of the Lambda function.

**Name formats**
+  **Function name** – `my-function`.
+  **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
+  **Partial ARN** – `123456789012:function:my-function`.
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_\.]+)(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`
Required: Yes

 ** [Qualifier](#API_GetRuntimeManagementConfig_RequestSyntax) **   <a name="lambda-GetRuntimeManagementConfig-request-uri-Qualifier"></a>
Specify a version of the function. This can be `$LATEST` or a published version number. If no value is specified, the configuration for the `$LATEST` version is returned.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\$(LATEST(\.PUBLISHED)?)|[a-zA-Z0-9-_$]+`

## Request Body
<a name="API_GetRuntimeManagementConfig_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRuntimeManagementConfig_ResponseSyntax"></a>

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
<a name="API_GetRuntimeManagementConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FunctionArn](#API_GetRuntimeManagementConfig_ResponseSyntax) **   <a name="lambda-GetRuntimeManagementConfig-response-FunctionArn"></a>
The Amazon Resource Name (ARN) of your function.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`

 ** [RuntimeVersionArn](#API_GetRuntimeManagementConfig_ResponseSyntax) **   <a name="lambda-GetRuntimeManagementConfig-response-RuntimeVersionArn"></a>
The ARN of the runtime the function is configured to use. If the runtime update mode is **Manual**, the ARN is returned, otherwise `null` is returned.
Type: String
Length Constraints: Minimum length of 26. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*):lambda:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}::runtime:.+`

 ** [UpdateRuntimeOn](#API_GetRuntimeManagementConfig_ResponseSyntax) **   <a name="lambda-GetRuntimeManagementConfig-response-UpdateRuntimeOn"></a>
The current runtime update mode of the function.
Type: String
Valid Values: `Auto | Manual | FunctionUpdate`

## Errors
<a name="API_GetRuntimeManagementConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_GetRuntimeManagementConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/GetRuntimeManagementConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/GetRuntimeManagementConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/GetRuntimeManagementConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/GetRuntimeManagementConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/GetRuntimeManagementConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/GetRuntimeManagementConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/GetRuntimeManagementConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/GetRuntimeManagementConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/GetRuntimeManagementConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/GetRuntimeManagementConfig)
