---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_SetV2LoggingOptions.html
---

# SetV2LoggingOptions
<a name="API_SetV2LoggingOptions"></a>

Sets the logging options for the V2 logging service.

Requires permission to access the [SetV2LoggingOptions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_SetV2LoggingOptions_RequestSyntax"></a>

```
POST /v2LoggingOptions HTTP/1.1
Content-type: application/json

{
   "defaultLogLevel": "{{string}}",
   "disableAllLogs": {{boolean}},
   "eventConfigurations": [
      {
         "eventType": "{{string}}",
         "logDestination": "{{string}}",
         "logLevel": "{{string}}"
      }
   ],
   "roleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SetV2LoggingOptions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SetV2LoggingOptions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [defaultLogLevel](#API_SetV2LoggingOptions_RequestSyntax) **   <a name="iot-SetV2LoggingOptions-request-defaultLogLevel"></a>
The default logging level.
Type: String
Valid Values: `DEBUG | INFO | ERROR | WARN | DISABLED`
Required: No

 ** [disableAllLogs](#API_SetV2LoggingOptions_RequestSyntax) **   <a name="iot-SetV2LoggingOptions-request-disableAllLogs"></a>
If true all logs are disabled. The default is false.
Type: Boolean
Required: No

 ** [eventConfigurations](#API_SetV2LoggingOptions_RequestSyntax) **   <a name="iot-SetV2LoggingOptions-request-eventConfigurations"></a>
 The list of event configurations that override account-level logging.
Type: Array of [LogEventConfiguration](API_LogEventConfiguration.md) objects
Required: No

 ** [roleArn](#API_SetV2LoggingOptions_RequestSyntax) **   <a name="iot-SetV2LoggingOptions-request-roleArn"></a>
The ARN of the role that allows IoT to write to Cloudwatch logs.
Type: String
Required: No

## Response Syntax
<a name="API_SetV2LoggingOptions_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_SetV2LoggingOptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SetV2LoggingOptions_Errors"></a>

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
<a name="API_SetV2LoggingOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/SetV2LoggingOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/SetV2LoggingOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/SetV2LoggingOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/SetV2LoggingOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/SetV2LoggingOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/SetV2LoggingOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/SetV2LoggingOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/SetV2LoggingOptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/SetV2LoggingOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/SetV2LoggingOptions)
