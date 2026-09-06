---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetWirelessDevice.html
---

# GetWirelessDevice
<a name="API_GetWirelessDevice"></a>

Gets information about a wireless device.

## Request Syntax
<a name="API_GetWirelessDevice_RequestSyntax"></a>

```
GET /wireless-devices/{{Identifier}}?identifierType={{IdentifierType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWirelessDevice_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_GetWirelessDevice_RequestSyntax) **   <a name="iotwireless-GetWirelessDevice-request-uri-Identifier"></a>
The identifier of the wireless device to get.
Length Constraints: Maximum length of 256.
Required: Yes

 ** [IdentifierType](#API_GetWirelessDevice_RequestSyntax) **   <a name="iotwireless-GetWirelessDevice-request-uri-IdentifierType"></a>
The type of identifier used in `identifier`.
Valid Values: `WirelessDeviceId | DevEui | ThingName | SidewalkManufacturingSn`
Required: Yes

## Request Body
<a name="API_GetWirelessDevice_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWirelessDevice_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Description": "string",
   "DestinationName": "string",
   "Id": "string",
   "LoRaWAN": {
      "AbpV1\_0\_x": {
         "DevAddr": "string",
         "FCntStart": number,
         "SessionKeys": {
            "AppSKey": "string",
            "NwkSKey": "string"
         }
      },
      "AbpV1\_1": {
         "DevAddr": "string",
         "FCntStart": number,
         "SessionKeys": {
            "AppSKey": "string",
            "FNwkSIntKey": "string",
            "NwkSEncKey": "string",
            "SNwkSIntKey": "string"
         }
      },
      "DevEui": "string",
      "DeviceProfileId": "string",
      "FPorts": {
         "Applications": [
            {
               "DestinationName": "string",
               "FPort": number,
               "Type": "string"
            }
         ],
         "ClockSync": number,
         "Fuota": number,
         "Multicast": number,
         "Positioning": {
            "ClockSync": number,
            "Gnss": number,
            "Stream": number
         }
      },
      "OtaaV1\_0\_x": {
         "AppEui": "string",
         "AppKey": "string",
         "GenAppKey": "string",
         "JoinEui": "string"
      },
      "OtaaV1\_1": {
         "AppKey": "string",
         "JoinEui": "string",
         "NwkKey": "string"
      },
      "ServiceProfileId": "string"
   },
   "Name": "string",
   "Positioning": "string",
   "Sidewalk": {
      "AmazonId": "string",
      "CertificateId": "string",
      "DeviceCertificates": [
         {
            "SigningAlg": "string",
            "Value": "string"
         }
      ],
      "DeviceProfileId": "string",
      "Positioning": {
         "DestinationName": "string"
      },
      "PrivateKeys": [
         {
            "SigningAlg": "string",
            "Value": "string"
         }
      ],
      "SidewalkId": "string",
      "SidewalkManufacturingSn": "string",
      "Status": "string"
   },
   "ThingArn": "string",
   "ThingName": "string",
   "Type": "string"
}
```

## Response Elements
<a name="API_GetWirelessDevice_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetWirelessDevice_ResponseSyntax) **   <a name="iotwireless-GetWirelessDevice-response-Arn"></a>
The Amazon Resource Name of the resource.
Type: String

 ** [Description](#API_GetWirelessDevice_ResponseSyntax) **   <a name="iotwireless-GetWirelessDevice-response-Description"></a>
The description of the resource.
Type: String
Length Constraints: Maximum length of 2048.

 ** [DestinationName](#API_GetWirelessDevice_ResponseSyntax) **   <a name="iotwireless-GetWirelessDevice-response-DestinationName"></a>
The name of the destination to which the device is assigned.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`

 ** [Id](#API_GetWirelessDevice_ResponseSyntax) **   <a name="iotwireless-GetWirelessDevice-response-Id"></a>
The ID of the wireless device.
Type: String
Length Constraints: Maximum length of 256.

 ** [LoRaWAN](#API_GetWirelessDevice_ResponseSyntax) **   <a name="iotwireless-GetWirelessDevice-response-LoRaWAN"></a>
Information about the wireless device.
Type: [LoRaWANDevice](API_LoRaWANDevice.md) object

 ** [Name](#API_GetWirelessDevice_ResponseSyntax) **   <a name="iotwireless-GetWirelessDevice-response-Name"></a>
The name of the resource.
Type: String
Length Constraints: Maximum length of 256.

 ** [Positioning](#API_GetWirelessDevice_ResponseSyntax) **   <a name="iotwireless-GetWirelessDevice-response-Positioning"></a>
The integration status of the Device Location feature for LoRaWAN and Sidewalk devices.
Type: String
Valid Values: `Enabled | Disabled`

 ** [Sidewalk](#API_GetWirelessDevice_ResponseSyntax) **   <a name="iotwireless-GetWirelessDevice-response-Sidewalk"></a>
Sidewalk device object.
Type: [SidewalkDevice](API_SidewalkDevice.md) object

 ** [ThingArn](#API_GetWirelessDevice_ResponseSyntax) **   <a name="iotwireless-GetWirelessDevice-response-ThingArn"></a>
The ARN of the thing associated with the wireless device.
Type: String

 ** [ThingName](#API_GetWirelessDevice_ResponseSyntax) **   <a name="iotwireless-GetWirelessDevice-response-ThingName"></a>
The name of the thing associated with the wireless device. The value is empty if a thing isn't associated with the device.
Type: String

 ** [Type](#API_GetWirelessDevice_ResponseSyntax) **   <a name="iotwireless-GetWirelessDevice-response-Type"></a>
The wireless device type.
Type: String
Valid Values: `Sidewalk | LoRaWAN`

## Errors
<a name="API_GetWirelessDevice_Errors"></a>

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
<a name="API_GetWirelessDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/GetWirelessDevice)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/GetWirelessDevice)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GetWirelessDevice)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/GetWirelessDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GetWirelessDevice)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/GetWirelessDevice)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/GetWirelessDevice)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/GetWirelessDevice)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/GetWirelessDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GetWirelessDevice)
