---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetResourceEventConfiguration.html
---

# GetResourceEventConfiguration
<a name="API_GetResourceEventConfiguration"></a>

Get the event configuration for a particular resource identifier.

## Request Syntax
<a name="API_GetResourceEventConfiguration_RequestSyntax"></a>

```
GET /event-configurations/{{Identifier}}?identifierType={{IdentifierType}}&partnerType={{PartnerType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetResourceEventConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_GetResourceEventConfiguration_RequestSyntax) **   <a name="iotwireless-GetResourceEventConfiguration-request-uri-Identifier"></a>
Resource identifier to opt in for event messaging.
Length Constraints: Maximum length of 256.
Required: Yes

 ** [IdentifierType](#API_GetResourceEventConfiguration_RequestSyntax) **   <a name="iotwireless-GetResourceEventConfiguration-request-uri-IdentifierType"></a>
Identifier type of the particular resource identifier for event configuration.
Valid Values: `PartnerAccountId | DevEui | GatewayEui | WirelessDeviceId | WirelessGatewayId`
Required: Yes

 ** [PartnerType](#API_GetResourceEventConfiguration_RequestSyntax) **   <a name="iotwireless-GetResourceEventConfiguration-request-uri-PartnerType"></a>
Partner type of the resource if the identifier type is `PartnerAccountId`.
Valid Values: `Sidewalk`

## Request Body
<a name="API_GetResourceEventConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetResourceEventConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConnectionStatus": {
      "LoRaWAN": {
         "GatewayEuiEventTopic": "string"
      },
      "WirelessGatewayIdEventTopic": "string"
   },
   "DeviceRegistrationState": {
      "Sidewalk": {
         "AmazonIdEventTopic": "string"
      },
      "WirelessDeviceIdEventTopic": "string"
   },
   "Join": {
      "LoRaWAN": {
         "DevEuiEventTopic": "string"
      },
      "WirelessDeviceIdEventTopic": "string"
   },
   "MessageDeliveryStatus": {
      "Sidewalk": {
         "AmazonIdEventTopic": "string"
      },
      "WirelessDeviceIdEventTopic": "string"
   },
   "Proximity": {
      "Sidewalk": {
         "AmazonIdEventTopic": "string"
      },
      "WirelessDeviceIdEventTopic": "string"
   }
}
```

## Response Elements
<a name="API_GetResourceEventConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectionStatus](#API_GetResourceEventConfiguration_ResponseSyntax) **   <a name="iotwireless-GetResourceEventConfiguration-response-ConnectionStatus"></a>
Event configuration for the connection status event.
Type: [ConnectionStatusEventConfiguration](API_ConnectionStatusEventConfiguration.md) object

 ** [DeviceRegistrationState](#API_GetResourceEventConfiguration_ResponseSyntax) **   <a name="iotwireless-GetResourceEventConfiguration-response-DeviceRegistrationState"></a>
Event configuration for the device registration state event.
Type: [DeviceRegistrationStateEventConfiguration](API_DeviceRegistrationStateEventConfiguration.md) object

 ** [Join](#API_GetResourceEventConfiguration_ResponseSyntax) **   <a name="iotwireless-GetResourceEventConfiguration-response-Join"></a>
Event configuration for the join event.
Type: [JoinEventConfiguration](API_JoinEventConfiguration.md) object

 ** [MessageDeliveryStatus](#API_GetResourceEventConfiguration_ResponseSyntax) **   <a name="iotwireless-GetResourceEventConfiguration-response-MessageDeliveryStatus"></a>
Event configuration for the message delivery status event.
Type: [MessageDeliveryStatusEventConfiguration](API_MessageDeliveryStatusEventConfiguration.md) object

 ** [Proximity](#API_GetResourceEventConfiguration_ResponseSyntax) **   <a name="iotwireless-GetResourceEventConfiguration-response-Proximity"></a>
Event configuration for the proximity event.
Type: [ProximityEventConfiguration](API_ProximityEventConfiguration.md) object

## Errors
<a name="API_GetResourceEventConfiguration_Errors"></a>

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
<a name="API_GetResourceEventConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/GetResourceEventConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/GetResourceEventConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GetResourceEventConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/GetResourceEventConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GetResourceEventConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/GetResourceEventConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/GetResourceEventConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/GetResourceEventConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/GetResourceEventConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GetResourceEventConfiguration)
