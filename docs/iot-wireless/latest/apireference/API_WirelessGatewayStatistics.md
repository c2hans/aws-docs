---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_WirelessGatewayStatistics.html
---

# WirelessGatewayStatistics
<a name="API_WirelessGatewayStatistics"></a>

Information about a wireless gateway's operation.

## Contents
<a name="API_WirelessGatewayStatistics_Contents"></a>

 ** Arn **   <a name="iotwireless-Type-WirelessGatewayStatistics-Arn"></a>
The Amazon Resource Name of the resource.
Type: String
Required: No

 ** Description **   <a name="iotwireless-Type-WirelessGatewayStatistics-Description"></a>
The description of the resource.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** Id **   <a name="iotwireless-Type-WirelessGatewayStatistics-Id"></a>
The ID of the wireless gateway reporting the data.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** LastUplinkReceivedAt **   <a name="iotwireless-Type-WirelessGatewayStatistics-LastUplinkReceivedAt"></a>
The date and time when the most recent uplink was received.
This value is only valid for 3 months.
Type: String
Pattern: `^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$`
Required: No

 ** LoRaWAN **   <a name="iotwireless-Type-WirelessGatewayStatistics-LoRaWAN"></a>
LoRaWAN gateway info.
Type: [LoRaWANGateway](API_LoRaWANGateway.md) object
Required: No

 ** Name **   <a name="iotwireless-Type-WirelessGatewayStatistics-Name"></a>
The name of the resource.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_WirelessGatewayStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/WirelessGatewayStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/WirelessGatewayStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/WirelessGatewayStatistics)
