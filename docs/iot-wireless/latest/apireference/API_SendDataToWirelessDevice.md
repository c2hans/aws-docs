---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_SendDataToWirelessDevice.html
---

# SendDataToWirelessDevice
<a name="API_SendDataToWirelessDevice"></a>

Sends a decrypted application data frame to a device.

## Request Syntax
<a name="API_SendDataToWirelessDevice_RequestSyntax"></a>

```
POST /wireless-devices/{{Id}}/data HTTP/1.1
Content-type: application/json

{
   "PayloadData": "{{string}}",
   "TransmitMode": {{number}},
   "WirelessMetadata": {
      "LoRaWAN": {
         "FPort": {{number}},
         "ParticipatingGateways": {
            "DownlinkMode": "{{string}}",
            "GatewayList": [
               {
                  "DownlinkFrequency": {{number}},
                  "GatewayId": "{{string}}"
               }
            ],
            "TransmissionInterval": {{number}}
         }
      },
      "Sidewalk": {
         "AckModeRetryDurationSecs": {{number}},
         "MessageType": "{{string}}",
         "Seq": {{number}}
      }
   }
}
```

## URI Request Parameters
<a name="API_SendDataToWirelessDevice_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_SendDataToWirelessDevice_RequestSyntax) **   <a name="iotwireless-SendDataToWirelessDevice-request-uri-Id"></a>
The ID of the wireless device to receive the data.
Length Constraints: Maximum length of 256.
Required: Yes

## Request Body
<a name="API_SendDataToWirelessDevice_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [PayloadData](#API_SendDataToWirelessDevice_RequestSyntax) **   <a name="iotwireless-SendDataToWirelessDevice-request-PayloadData"></a>
The binary to be sent to the end device, encoded in base64.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$`
Required: Yes

 ** [TransmitMode](#API_SendDataToWirelessDevice_RequestSyntax) **   <a name="iotwireless-SendDataToWirelessDevice-request-TransmitMode"></a>
The transmit mode to use to send data to the wireless device. Can be: `0` for UM (unacknowledge mode) or `1` for AM (acknowledge mode).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1.
Required: Yes

 ** [WirelessMetadata](#API_SendDataToWirelessDevice_RequestSyntax) **   <a name="iotwireless-SendDataToWirelessDevice-request-WirelessMetadata"></a>
Metadata about the message request.
Type: [WirelessMetadata](API_WirelessMetadata.md) object
Required: No

## Response Syntax
<a name="API_SendDataToWirelessDevice_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "MessageId": "string"
}
```

## Response Elements
<a name="API_SendDataToWirelessDevice_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [MessageId](#API_SendDataToWirelessDevice_ResponseSyntax) **   <a name="iotwireless-SendDataToWirelessDevice-response-MessageId"></a>
The ID of the message sent to the wireless device.
Type: String

## Errors
<a name="API_SendDataToWirelessDevice_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_SendDataToWirelessDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/SendDataToWirelessDevice)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/SendDataToWirelessDevice)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/SendDataToWirelessDevice)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/SendDataToWirelessDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/SendDataToWirelessDevice)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/SendDataToWirelessDevice)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/SendDataToWirelessDevice)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/SendDataToWirelessDevice)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/SendDataToWirelessDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/SendDataToWirelessDevice)
