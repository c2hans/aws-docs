---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_FunctionUrlConfig.html
---

# FunctionUrlConfig
<a name="API_FunctionUrlConfig"></a>

Details about a Lambda function URL.

## Contents
<a name="API_FunctionUrlConfig_Contents"></a>

 ** AuthType **   <a name="lambda-Type-FunctionUrlConfig-AuthType"></a>
The type of authentication that your function URL uses. Set to `AWS_IAM` if you want to restrict access to authenticated users only. Set to `NONE` if you want to bypass IAM authentication to create a public endpoint. For more information, see [Security and auth model for Lambda function URLs](https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html).
Type: String
Valid Values: `NONE | AWS_IAM`
Required: Yes

 ** CreationTime **   <a name="lambda-Type-FunctionUrlConfig-CreationTime"></a>
When the function URL was created, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).
Type: String
Required: Yes

 ** FunctionArn **   <a name="lambda-Type-FunctionUrlConfig-FunctionArn"></a>
The Amazon Resource Name (ARN) of your function.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`
Required: Yes

 ** FunctionUrl **   <a name="lambda-Type-FunctionUrlConfig-FunctionUrl"></a>
The HTTP URL endpoint for your function.
Type: String
Length Constraints: Minimum length of 40. Maximum length of 100.
Required: Yes

 ** LastModifiedTime **   <a name="lambda-Type-FunctionUrlConfig-LastModifiedTime"></a>
When the function URL configuration was last updated, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).
Type: String
Required: Yes

 ** Cors **   <a name="lambda-Type-FunctionUrlConfig-Cors"></a>
The [cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) settings for your function URL.
Type: [Cors](API_Cors.md) object
Required: No

 ** InvokeMode **   <a name="lambda-Type-FunctionUrlConfig-InvokeMode"></a>
Use one of the following options:
+  `BUFFERED` – This is the default option. Lambda invokes your function using the `Invoke` API operation. Invocation results are available when the payload is complete. The maximum payload size is 6 MB.
+  `RESPONSE_STREAM` – Your function streams payload results as they become available. Lambda invokes your function using the `InvokeWithResponseStream` API operation. The maximum response payload size is 200 MB.
Type: String
Valid Values: `BUFFERED | RESPONSE_STREAM`
Required: No

## See Also
<a name="API_FunctionUrlConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/FunctionUrlConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/FunctionUrlConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/FunctionUrlConfig)
