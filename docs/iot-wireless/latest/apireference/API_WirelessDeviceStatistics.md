---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_WirelessDeviceStatistics.html
---

# WirelessDeviceStatistics
<a name="API_WirelessDeviceStatistics"></a>

Information about a wireless device's operation.

## Contents
<a name="API_WirelessDeviceStatistics_Contents"></a>

 ** Arn **   <a name="iotwireless-Type-WirelessDeviceStatistics-Arn"></a>
The Amazon Resource Name of the resource.
Type: String
Required: No

 ** DestinationName **   <a name="iotwireless-Type-WirelessDeviceStatistics-DestinationName"></a>
The name of the destination to which the device is assigned.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

 ** FuotaDeviceStatus **   <a name="iotwireless-Type-WirelessDeviceStatistics-FuotaDeviceStatus"></a>
The status of a wireless device in a FUOTA task.
Type: String
Valid Values: `Initial | Package_Not_Supported | FragAlgo_unsupported | Not_enough_memory | FragIndex_unsupported | Wrong_descriptor | SessionCnt_replay | MissingFrag | MemoryError | MICError | Successful | Device_exist_in_conflict_fuota_task`
Required: No

 ** Id **   <a name="iotwireless-Type-WirelessDeviceStatistics-Id"></a>
The ID of the wireless device reporting the data.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** LastUplinkReceivedAt **   <a name="iotwireless-Type-WirelessDeviceStatistics-LastUplinkReceivedAt"></a>
The date and time when the most recent uplink was received.
Theis value is only valid for 3 months.
Type: String
Pattern: `^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$`
Required: No

 ** LoRaWAN **   <a name="iotwireless-Type-WirelessDeviceStatistics-LoRaWAN"></a>
LoRaWAN device info.
Type: [LoRaWANListDevice](API_LoRaWANListDevice.md) object
Required: No

 ** McGroupId **   <a name="iotwireless-Type-WirelessDeviceStatistics-McGroupId"></a>
Id of the multicast group.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 256.
Required: No

 ** MulticastDeviceStatus **   <a name="iotwireless-Type-WirelessDeviceStatistics-MulticastDeviceStatus"></a>
The status of the wireless device in the multicast group.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** Name **   <a name="iotwireless-Type-WirelessDeviceStatistics-Name"></a>
The name of the resource.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** Positioning **   <a name="iotwireless-Type-WirelessDeviceStatistics-Positioning"></a>
The integration status of the Device Location feature for LoRaWAN and Amazon Sidewalk enabled devices.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

 ** Sidewalk **   <a name="iotwireless-Type-WirelessDeviceStatistics-Sidewalk"></a>
The Sidewalk account credentials.
Type: [SidewalkListDevice](API_SidewalkListDevice.md) object
Required: No

 ** Type **   <a name="iotwireless-Type-WirelessDeviceStatistics-Type"></a>
The wireless device type.
Type: String
Valid Values: `Sidewalk | LoRaWAN`
Required: No

## See Also
<a name="API_WirelessDeviceStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/WirelessDeviceStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/WirelessDeviceStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/WirelessDeviceStatistics)
