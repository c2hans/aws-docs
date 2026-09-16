---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_SetLoggingOptions.html
---

# SetLoggingOptions
<a name="API_SetLoggingOptions"></a>

Sets the logging options.

NOTE: use of this command is not recommended. Use `SetV2LoggingOptions` instead.

Requires permission to access the [SetLoggingOptions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_SetLoggingOptions_RequestSyntax"></a>

```
POST /loggingOptions HTTP/1.1
Content-type: application/json

{
   "logLevel": "{{string}}",
   "roleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SetLoggingOptions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SetLoggingOptions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [logLevel](#API_SetLoggingOptions_RequestSyntax) **   <a name="iot-SetLoggingOptions-request-logLevel"></a>
The log level.
Type: String
Valid Values: `DEBUG | INFO | ERROR | WARN | DISABLED`
Required: No

 ** [roleArn](#API_SetLoggingOptions_RequestSyntax) **   <a name="iot-SetLoggingOptions-request-roleArn"></a>
The ARN of the IAM role that grants access.
Type: String
Required: Yes

## Response Syntax
<a name="API_SetLoggingOptions_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_SetLoggingOptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SetLoggingOptions_Errors"></a>

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
<a name="API_SetLoggingOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/SetLoggingOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/SetLoggingOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/SetLoggingOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/SetLoggingOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/SetLoggingOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/SetLoggingOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/SetLoggingOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/SetLoggingOptions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/SetLoggingOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/SetLoggingOptions)
