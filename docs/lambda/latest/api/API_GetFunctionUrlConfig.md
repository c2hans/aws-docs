---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_GetFunctionUrlConfig.html
---

# GetFunctionUrlConfig
<a name="API_GetFunctionUrlConfig"></a>

Returns details about a Lambda function URL.

## Request Syntax
<a name="API_GetFunctionUrlConfig_RequestSyntax"></a>

```
GET /2021-10-31/functions/{{FunctionName}}/url?Qualifier={{Qualifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetFunctionUrlConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FunctionName](#API_GetFunctionUrlConfig_RequestSyntax) **   <a name="lambda-GetFunctionUrlConfig-request-uri-FunctionName"></a>
The name or ARN of the Lambda function.

**Name formats**
+  **Function name** – `my-function`.
+  **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
+  **Partial ARN** – `123456789012:function:my-function`.
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]{1,64})(:((?!\d+$)[0-9a-zA-Z-_]+))?`
Required: Yes

 ** [Qualifier](#API_GetFunctionUrlConfig_RequestSyntax) **   <a name="lambda-GetFunctionUrlConfig-request-uri-Qualifier"></a>
The alias name.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `((?!^\d+$)^[0-9a-zA-Z-_]+$)`

## Request Body
<a name="API_GetFunctionUrlConfig_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetFunctionUrlConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AuthType": "string",
   "Cors": {
      "AllowCredentials": boolean,
      "AllowHeaders": [ "string" ],
      "AllowMethods": [ "string" ],
      "AllowOrigins": [ "string" ],
      "ExposeHeaders": [ "string" ],
      "MaxAge": number
   },
   "CreationTime": "string",
   "FunctionArn": "string",
   "FunctionUrl": "string",
   "InvokeMode": "string",
   "LastModifiedTime": "string"
}
```

## Response Elements
<a name="API_GetFunctionUrlConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthType](#API_GetFunctionUrlConfig_ResponseSyntax) **   <a name="lambda-GetFunctionUrlConfig-response-AuthType"></a>
The type of authentication that your function URL uses. Set to `AWS_IAM` if you want to restrict access to authenticated users only. Set to `NONE` if you want to bypass IAM authentication to create a public endpoint. For more information, see [Control access to Lambda function URLs](https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html).
Type: String
Valid Values: `NONE | AWS_IAM`

 ** [Cors](#API_GetFunctionUrlConfig_ResponseSyntax) **   <a name="lambda-GetFunctionUrlConfig-response-Cors"></a>
The [cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) settings for your function URL.
Type: [Cors](API_Cors.md) object

 ** [CreationTime](#API_GetFunctionUrlConfig_ResponseSyntax) **   <a name="lambda-GetFunctionUrlConfig-response-CreationTime"></a>
When the function URL was created, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).
Type: String

 ** [FunctionArn](#API_GetFunctionUrlConfig_ResponseSyntax) **   <a name="lambda-GetFunctionUrlConfig-response-FunctionArn"></a>
The Amazon Resource Name (ARN) of your function.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`

 ** [FunctionUrl](#API_GetFunctionUrlConfig_ResponseSyntax) **   <a name="lambda-GetFunctionUrlConfig-response-FunctionUrl"></a>
The HTTP URL endpoint for your function.
Type: String
Length Constraints: Minimum length of 40. Maximum length of 100.

 ** [InvokeMode](#API_GetFunctionUrlConfig_ResponseSyntax) **   <a name="lambda-GetFunctionUrlConfig-response-InvokeMode"></a>
Use one of the following options:
+  `BUFFERED` – This is the default option. Lambda invokes your function using the `Invoke` API operation. Invocation results are available when the payload is complete. The maximum payload size is 6 MB.
+  `RESPONSE_STREAM` – Your function streams payload results as they become available. Lambda invokes your function using the `InvokeWithResponseStream` API operation. The maximum response payload size is 200 MB.
Type: String
Valid Values: `BUFFERED | RESPONSE_STREAM`

 ** [LastModifiedTime](#API_GetFunctionUrlConfig_ResponseSyntax) **   <a name="lambda-GetFunctionUrlConfig-response-LastModifiedTime"></a>
When the function URL configuration was last updated, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).
Type: String

## Errors
<a name="API_GetFunctionUrlConfig_Errors"></a>

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
<a name="API_GetFunctionUrlConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/GetFunctionUrlConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/GetFunctionUrlConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/GetFunctionUrlConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/GetFunctionUrlConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/GetFunctionUrlConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/GetFunctionUrlConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/GetFunctionUrlConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/GetFunctionUrlConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/GetFunctionUrlConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/GetFunctionUrlConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
