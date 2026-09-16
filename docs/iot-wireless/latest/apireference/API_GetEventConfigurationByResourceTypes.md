---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetEventConfigurationByResourceTypes.html
---

# GetEventConfigurationByResourceTypes
<a name="API_GetEventConfigurationByResourceTypes"></a>

Get the event configuration based on resource types.

## Request Syntax
<a name="API_GetEventConfigurationByResourceTypes_RequestSyntax"></a>

```
GET /event-configurations-resource-types HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEventConfigurationByResourceTypes_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetEventConfigurationByResourceTypes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEventConfigurationByResourceTypes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConnectionStatus": {
      "LoRaWAN": {
         "WirelessGatewayEventTopic": "string"
      }
   },
   "DeviceRegistrationState": {
      "Sidewalk": {
         "WirelessDeviceEventTopic": "string"
      }
   },
   "Join": {
      "LoRaWAN": {
         "WirelessDeviceEventTopic": "string"
      }
   },
   "MessageDeliveryStatus": {
      "Sidewalk": {
         "WirelessDeviceEventTopic": "string"
      }
   },
   "Proximity": {
      "Sidewalk": {
         "WirelessDeviceEventTopic": "string"
      }
   }
}
```

## Response Elements
<a name="API_GetEventConfigurationByResourceTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectionStatus](#API_GetEventConfigurationByResourceTypes_ResponseSyntax) **   <a name="iotwireless-GetEventConfigurationByResourceTypes-response-ConnectionStatus"></a>
Resource type event configuration for the connection status event.
Type: [ConnectionStatusResourceTypeEventConfiguration](API_ConnectionStatusResourceTypeEventConfiguration.md) object

 ** [DeviceRegistrationState](#API_GetEventConfigurationByResourceTypes_ResponseSyntax) **   <a name="iotwireless-GetEventConfigurationByResourceTypes-response-DeviceRegistrationState"></a>
Resource type event configuration for the device registration state event.
Type: [DeviceRegistrationStateResourceTypeEventConfiguration](API_DeviceRegistrationStateResourceTypeEventConfiguration.md) object

 ** [Join](#API_GetEventConfigurationByResourceTypes_ResponseSyntax) **   <a name="iotwireless-GetEventConfigurationByResourceTypes-response-Join"></a>
Resource type event configuration for the join event.
Type: [JoinResourceTypeEventConfiguration](API_JoinResourceTypeEventConfiguration.md) object

 ** [MessageDeliveryStatus](#API_GetEventConfigurationByResourceTypes_ResponseSyntax) **   <a name="iotwireless-GetEventConfigurationByResourceTypes-response-MessageDeliveryStatus"></a>
Resource type event configuration object for the message delivery status event.
Type: [MessageDeliveryStatusResourceTypeEventConfiguration](API_MessageDeliveryStatusResourceTypeEventConfiguration.md) object

 ** [Proximity](#API_GetEventConfigurationByResourceTypes_ResponseSyntax) **   <a name="iotwireless-GetEventConfigurationByResourceTypes-response-Proximity"></a>
Resource type event configuration for the proximity event.
Type: [ProximityResourceTypeEventConfiguration](API_ProximityResourceTypeEventConfiguration.md) object

## Errors
<a name="API_GetEventConfigurationByResourceTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing a request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied because it exceeded the allowed API request rate.
HTTP Status Code: 429

## See Also
<a name="API_GetEventConfigurationByResourceTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/GetEventConfigurationByResourceTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/GetEventConfigurationByResourceTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GetEventConfigurationByResourceTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/GetEventConfigurationByResourceTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GetEventConfigurationByResourceTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/GetEventConfigurationByResourceTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/GetEventConfigurationByResourceTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/GetEventConfigurationByResourceTypes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/GetEventConfigurationByResourceTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GetEventConfigurationByResourceTypes)
