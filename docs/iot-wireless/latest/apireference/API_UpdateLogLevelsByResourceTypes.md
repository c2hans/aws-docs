---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateLogLevelsByResourceTypes.html
---

# UpdateLogLevelsByResourceTypes
<a name="API_UpdateLogLevelsByResourceTypes"></a>

Set default log level, or log levels by resource types. This can be for wireless device, wireless gateway, or FUOTA task log options, and is used to control the log messages that'll be displayed in CloudWatch.

## Request Syntax
<a name="API_UpdateLogLevelsByResourceTypes_RequestSyntax"></a>

```
POST /log-levels HTTP/1.1
Content-type: application/json

{
   "DefaultLogLevel": "{{string}}",
   "FuotaTaskLogOptions": [
      {
         "Events": [
            {
               "Event": "{{string}}",
               "LogLevel": "{{string}}"
            }
         ],
         "LogLevel": "{{string}}",
         "Type": "{{string}}"
      }
   ],
   "WirelessDeviceLogOptions": [
      {
         "Events": [
            {
               "Event": "{{string}}",
               "LogLevel": "{{string}}"
            }
         ],
         "LogLevel": "{{string}}",
         "Type": "{{string}}"
      }
   ],
   "WirelessGatewayLogOptions": [
      {
         "Events": [
            {
               "Event": "{{string}}",
               "LogLevel": "{{string}}"
            }
         ],
         "LogLevel": "{{string}}",
         "Type": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateLogLevelsByResourceTypes_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateLogLevelsByResourceTypes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DefaultLogLevel](#API_UpdateLogLevelsByResourceTypes_RequestSyntax) **   <a name="iotwireless-UpdateLogLevelsByResourceTypes-request-DefaultLogLevel"></a>
The log level for a log message. The log levels can be disabled, or set to `ERROR` to display less verbose logs containing only error information, or to `INFO` for more detailed logs.
Type: String
Valid Values: `INFO | ERROR | DISABLED`
Required: No

 ** [FuotaTaskLogOptions](#API_UpdateLogLevelsByResourceTypes_RequestSyntax) **   <a name="iotwireless-UpdateLogLevelsByResourceTypes-request-FuotaTaskLogOptions"></a>
The list of FUOTA task log options.
Type: Array of [FuotaTaskLogOption](API_FuotaTaskLogOption.md) objects
Required: No

 ** [WirelessDeviceLogOptions](#API_UpdateLogLevelsByResourceTypes_RequestSyntax) **   <a name="iotwireless-UpdateLogLevelsByResourceTypes-request-WirelessDeviceLogOptions"></a>
The list of wireless device log options.
Type: Array of [WirelessDeviceLogOption](API_WirelessDeviceLogOption.md) objects
Required: No

 ** [WirelessGatewayLogOptions](#API_UpdateLogLevelsByResourceTypes_RequestSyntax) **   <a name="iotwireless-UpdateLogLevelsByResourceTypes-request-WirelessGatewayLogOptions"></a>
The list of wireless gateway log options.
Type: Array of [WirelessGatewayLogOption](API_WirelessGatewayLogOption.md) objects
Required: No

## Response Syntax
<a name="API_UpdateLogLevelsByResourceTypes_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateLogLevelsByResourceTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateLogLevelsByResourceTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Adding, updating, or deleting the resource can cause an inconsistent state.
 ** ResourceId **
Id of the resource in the conflicting operation.
 ** ResourceType **
Type of the resource in the conflicting operation.
HTTP Status Code: 409

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
<a name="API_UpdateLogLevelsByResourceTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/UpdateLogLevelsByResourceTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/UpdateLogLevelsByResourceTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/UpdateLogLevelsByResourceTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/UpdateLogLevelsByResourceTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/UpdateLogLevelsByResourceTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/UpdateLogLevelsByResourceTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/UpdateLogLevelsByResourceTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/UpdateLogLevelsByResourceTypes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/UpdateLogLevelsByResourceTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/UpdateLogLevelsByResourceTypes)
