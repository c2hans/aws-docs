---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetLogLevelsByResourceTypes.html
---

# GetLogLevelsByResourceTypes
<a name="API_GetLogLevelsByResourceTypes"></a>

Returns current default log levels or log levels by resource types. Based on the resource type, log levels can be returned for wireless device, wireless gateway, or FUOTA task log options.

## Request Syntax
<a name="API_GetLogLevelsByResourceTypes_RequestSyntax"></a>

```
GET /log-levels HTTP/1.1
```

## URI Request Parameters
<a name="API_GetLogLevelsByResourceTypes_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetLogLevelsByResourceTypes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetLogLevelsByResourceTypes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DefaultLogLevel": "string",
   "FuotaTaskLogOptions": [
      {
         "Events": [
            {
               "Event": "string",
               "LogLevel": "string"
            }
         ],
         "LogLevel": "string",
         "Type": "string"
      }
   ],
   "WirelessDeviceLogOptions": [
      {
         "Events": [
            {
               "Event": "string",
               "LogLevel": "string"
            }
         ],
         "LogLevel": "string",
         "Type": "string"
      }
   ],
   "WirelessGatewayLogOptions": [
      {
         "Events": [
            {
               "Event": "string",
               "LogLevel": "string"
            }
         ],
         "LogLevel": "string",
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetLogLevelsByResourceTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DefaultLogLevel](#API_GetLogLevelsByResourceTypes_ResponseSyntax) **   <a name="iotwireless-GetLogLevelsByResourceTypes-response-DefaultLogLevel"></a>
The log level for a log message. The log levels can be disabled, or set to `ERROR` to display less verbose logs containing only error information, or to `INFO` for more detailed logs.
Type: String
Valid Values: `INFO | ERROR | DISABLED`

 ** [FuotaTaskLogOptions](#API_GetLogLevelsByResourceTypes_ResponseSyntax) **   <a name="iotwireless-GetLogLevelsByResourceTypes-response-FuotaTaskLogOptions"></a>
The list of FUOTA task log options.
Type: Array of [FuotaTaskLogOption](API_FuotaTaskLogOption.md) objects

 ** [WirelessDeviceLogOptions](#API_GetLogLevelsByResourceTypes_ResponseSyntax) **   <a name="iotwireless-GetLogLevelsByResourceTypes-response-WirelessDeviceLogOptions"></a>
The list of wireless device log options.
Type: Array of [WirelessDeviceLogOption](API_WirelessDeviceLogOption.md) objects

 ** [WirelessGatewayLogOptions](#API_GetLogLevelsByResourceTypes_ResponseSyntax) **   <a name="iotwireless-GetLogLevelsByResourceTypes-response-WirelessGatewayLogOptions"></a>
The list of wireless gateway log options.
Type: Array of [WirelessGatewayLogOption](API_WirelessGatewayLogOption.md) objects

## Errors
<a name="API_GetLogLevelsByResourceTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource does not exist.
 ** ResourceId **
Id of the not found resource.
 ** ResourceType **
Type of the font found resource.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because it exceeded the allowed API request rate.
HTTP Status Code: 429

 ** ValidationException **
The input did not meet the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_GetLogLevelsByResourceTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/GetLogLevelsByResourceTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/GetLogLevelsByResourceTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GetLogLevelsByResourceTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/GetLogLevelsByResourceTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GetLogLevelsByResourceTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/GetLogLevelsByResourceTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/GetLogLevelsByResourceTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/GetLogLevelsByResourceTypes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/GetLogLevelsByResourceTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GetLogLevelsByResourceTypes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
