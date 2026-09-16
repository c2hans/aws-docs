---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateWirelessDevice.html
---

# UpdateWirelessDevice
<a name="API_UpdateWirelessDevice"></a>

Updates properties of a wireless device.

## Request Syntax
<a name="API_UpdateWirelessDevice_RequestSyntax"></a>

```
PATCH /wireless-devices/{{Id}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "DestinationName": "{{string}}",
   "LoRaWAN": {
      "AbpV1\_0\_x": {
         "FCntStart": {{number}}
      },
      "AbpV1\_1": {
         "FCntStart": {{number}}
      },
      "DeviceProfileId": "{{string}}",
      "FPorts": {
         "Applications": [
            {
               "DestinationName": "{{string}}",
               "FPort": {{number}},
               "Type": "{{string}}"
            }
         ],
         "Positioning": {
            "ClockSync": {{number}},
            "Gnss": {{number}},
            "Stream": {{number}}
         }
      },
      "ServiceProfileId": "{{string}}"
   },
   "Name": "{{string}}",
   "Positioning": "{{string}}",
   "Sidewalk": {
      "Positioning": {
         "DestinationName": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_UpdateWirelessDevice_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_UpdateWirelessDevice_RequestSyntax) **   <a name="iotwireless-UpdateWirelessDevice-request-uri-Id"></a>
The ID of the resource to update.
Length Constraints: Maximum length of 256.
Required: Yes

## Request Body
<a name="API_UpdateWirelessDevice_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateWirelessDevice_RequestSyntax) **   <a name="iotwireless-UpdateWirelessDevice-request-Description"></a>
A new description of the resource.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [DestinationName](#API_UpdateWirelessDevice_RequestSyntax) **   <a name="iotwireless-UpdateWirelessDevice-request-DestinationName"></a>
The name of the new destination for the device.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

 ** [LoRaWAN](#API_UpdateWirelessDevice_RequestSyntax) **   <a name="iotwireless-UpdateWirelessDevice-request-LoRaWAN"></a>
The updated wireless device's configuration.
Type: [LoRaWANUpdateDevice](API_LoRaWANUpdateDevice.md) object
Required: No

 ** [Name](#API_UpdateWirelessDevice_RequestSyntax) **   <a name="iotwireless-UpdateWirelessDevice-request-Name"></a>
The new name of the resource.
The following special characters aren't accepted: `<>^#~$`
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [Positioning](#API_UpdateWirelessDevice_RequestSyntax) **   <a name="iotwireless-UpdateWirelessDevice-request-Positioning"></a>
The integration status of the Device Location feature for LoRaWAN and Sidewalk devices.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

 ** [Sidewalk](#API_UpdateWirelessDevice_RequestSyntax) **   <a name="iotwireless-UpdateWirelessDevice-request-Sidewalk"></a>
The updated sidewalk properties.
Type: [SidewalkUpdateWirelessDevice](API_SidewalkUpdateWirelessDevice.md) object
Required: No

## Response Syntax
<a name="API_UpdateWirelessDevice_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_UpdateWirelessDevice_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_UpdateWirelessDevice_Errors"></a>

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
<a name="API_UpdateWirelessDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/UpdateWirelessDevice)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/UpdateWirelessDevice)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/UpdateWirelessDevice)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/UpdateWirelessDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/UpdateWirelessDevice)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/UpdateWirelessDevice)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/UpdateWirelessDevice)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/UpdateWirelessDevice)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/UpdateWirelessDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/UpdateWirelessDevice)
