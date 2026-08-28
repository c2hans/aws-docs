---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_GetLoggingOptions.html
---

# GetLoggingOptions
<a name="API_GetLoggingOptions"></a>

Gets the logging options.

NOTE: use of this command is not recommended. Use `GetV2LoggingOptions` instead.

Requires permission to access the [GetLoggingOptions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_GetLoggingOptions_RequestSyntax"></a>

```
GET /loggingOptions HTTP/1.1
```

## URI Request Parameters
<a name="API_GetLoggingOptions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetLoggingOptions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetLoggingOptions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "logLevel": "string",
   "roleArn": "string"
}
```

## Response Elements
<a name="API_GetLoggingOptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [logLevel](#API_GetLoggingOptions_ResponseSyntax) **   <a name="iot-GetLoggingOptions-response-logLevel"></a>
The logging level.
Type: String
Valid Values: `DEBUG | INFO | ERROR | WARN | DISABLED`

 ** [roleArn](#API_GetLoggingOptions_ResponseSyntax) **   <a name="iot-GetLoggingOptions-response-roleArn"></a>
The ARN of the IAM role that grants access.
Type: String

## Errors
<a name="API_GetLoggingOptions_Errors"></a>

 ** InternalException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

## See Also
<a name="API_GetLoggingOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/GetLoggingOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/GetLoggingOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/GetLoggingOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/GetLoggingOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/GetLoggingOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/GetLoggingOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/GetLoggingOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/GetLoggingOptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/GetLoggingOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/GetLoggingOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
