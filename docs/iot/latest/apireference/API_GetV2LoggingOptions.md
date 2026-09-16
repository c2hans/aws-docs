---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_GetV2LoggingOptions.html
---

# GetV2LoggingOptions
<a name="API_GetV2LoggingOptions"></a>

Gets the fine grained logging options.

Requires permission to access the [GetV2LoggingOptions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_GetV2LoggingOptions_RequestSyntax"></a>

```
GET /v2LoggingOptions?verbose={{verbose}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetV2LoggingOptions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [verbose](#API_GetV2LoggingOptions_RequestSyntax) **   <a name="iot-GetV2LoggingOptions-request-uri-verbose"></a>
 The flag is used to get all the event types and their respective configuration that event-based logging supports.

## Request Body
<a name="API_GetV2LoggingOptions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetV2LoggingOptions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "defaultLogLevel": "string",
   "disableAllLogs": boolean,
   "eventConfigurations": [
      {
         "eventType": "string",
         "logDestination": "string",
         "logLevel": "string"
      }
   ],
   "roleArn": "string"
}
```

## Response Elements
<a name="API_GetV2LoggingOptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [defaultLogLevel](#API_GetV2LoggingOptions_ResponseSyntax) **   <a name="iot-GetV2LoggingOptions-response-defaultLogLevel"></a>
The default log level.
Type: String
Valid Values: `DEBUG | INFO | ERROR | WARN | DISABLED`

 ** [disableAllLogs](#API_GetV2LoggingOptions_ResponseSyntax) **   <a name="iot-GetV2LoggingOptions-response-disableAllLogs"></a>
Disables all logs.
Type: Boolean

 ** [eventConfigurations](#API_GetV2LoggingOptions_ResponseSyntax) **   <a name="iot-GetV2LoggingOptions-response-eventConfigurations"></a>
 The list of event configurations that override account-level logging.
Type: Array of [LogEventConfiguration](API_LogEventConfiguration.md) objects

 ** [roleArn](#API_GetV2LoggingOptions_ResponseSyntax) **   <a name="iot-GetV2LoggingOptions-response-roleArn"></a>
The IAM role ARN AWS IoT uses to write to your CloudWatch logs.
Type: String

## Errors
<a name="API_GetV2LoggingOptions_Errors"></a>

 ** InternalException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** NotConfiguredException **
The resource is not configured.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

## See Also
<a name="API_GetV2LoggingOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/GetV2LoggingOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/GetV2LoggingOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/GetV2LoggingOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/GetV2LoggingOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/GetV2LoggingOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/GetV2LoggingOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/GetV2LoggingOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/GetV2LoggingOptions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/GetV2LoggingOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/GetV2LoggingOptions)
