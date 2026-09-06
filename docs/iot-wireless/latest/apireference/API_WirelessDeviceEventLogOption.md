---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_WirelessDeviceEventLogOption.html
---

# WirelessDeviceEventLogOption
<a name="API_WirelessDeviceEventLogOption"></a>

The log options for a wireless device event and can be used to set log levels for a specific wireless device event.

For a LoRaWAN device, possible events for a log messsage are: `Join`, `Rejoin`, `Downlink_Data`, and `Uplink_Data`. For a Sidewalk device, possible events for a log message are `Registration`, `Downlink_Data`, and `Uplink_Data`.

## Contents
<a name="API_WirelessDeviceEventLogOption_Contents"></a>

 ** Event **   <a name="iotwireless-Type-WirelessDeviceEventLogOption-Event"></a>
The event for a log message, if the log message is tied to a wireless device.
Type: String
Valid Values: `Join | Rejoin | Uplink_Data | Downlink_Data | Registration`
Required: Yes

 ** LogLevel **   <a name="iotwireless-Type-WirelessDeviceEventLogOption-LogLevel"></a>
The log level for a log message. The log levels can be disabled, or set to `ERROR` to display less verbose logs containing only error information, or to `INFO` for more detailed logs.
Type: String
Valid Values: `INFO | ERROR | DISABLED`
Required: Yes

## See Also
<a name="API_WirelessDeviceEventLogOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/WirelessDeviceEventLogOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/WirelessDeviceEventLogOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/WirelessDeviceEventLogOption)
