---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_LoRaWANDeviceMetadata.html
---

# LoRaWANDeviceMetadata
<a name="API_LoRaWANDeviceMetadata"></a>

LoRaWAN device metatdata.

## Contents
<a name="API_LoRaWANDeviceMetadata_Contents"></a>

 ** DataRate **   <a name="iotwireless-Type-LoRaWANDeviceMetadata-DataRate"></a>
The DataRate value.
Type: Integer
Required: No

 ** DevEui **   <a name="iotwireless-Type-LoRaWANDeviceMetadata-DevEui"></a>
The DevEUI value.
Type: String
Pattern: `[a-fA-F0-9]{16}`
Required: No

 ** FPort **   <a name="iotwireless-Type-LoRaWANDeviceMetadata-FPort"></a>
The FPort value.
Type: Integer
Required: No

 ** Frequency **   <a name="iotwireless-Type-LoRaWANDeviceMetadata-Frequency"></a>
The device's channel frequency in Hz.
Type: Integer
Required: No

 ** Gateways **   <a name="iotwireless-Type-LoRaWANDeviceMetadata-Gateways"></a>
Information about the gateways accessed by the device.
Type: Array of [LoRaWANGatewayMetadata](API_LoRaWANGatewayMetadata.md) objects
Required: No

 ** PublicGateways **   <a name="iotwireless-Type-LoRaWANDeviceMetadata-PublicGateways"></a>
Information about the LoRaWAN public network accessed by the device.
Type: Array of [LoRaWANPublicGatewayMetadata](API_LoRaWANPublicGatewayMetadata.md) objects
Required: No

 ** Timestamp **   <a name="iotwireless-Type-LoRaWANDeviceMetadata-Timestamp"></a>
The date and time of the metadata.
Type: String
Pattern: `^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$`
Required: No

## See Also
<a name="API_LoRaWANDeviceMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/LoRaWANDeviceMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/LoRaWANDeviceMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/LoRaWANDeviceMetadata)
