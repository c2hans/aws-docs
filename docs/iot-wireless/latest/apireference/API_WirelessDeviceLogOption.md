---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_WirelessDeviceLogOption.html
---

# WirelessDeviceLogOption
<a name="API_WirelessDeviceLogOption"></a>

The log options for wireless devices and can be used to set log levels for a specific type of wireless device.

## Contents
<a name="API_WirelessDeviceLogOption_Contents"></a>

 ** LogLevel **   <a name="iotwireless-Type-WirelessDeviceLogOption-LogLevel"></a>
The log level for a log message. The log levels can be disabled, or set to `ERROR` to display less verbose logs containing only error information, or to `INFO` for more detailed logs.
Type: String
Valid Values: `INFO | ERROR | DISABLED`
Required: Yes

 ** Type **   <a name="iotwireless-Type-WirelessDeviceLogOption-Type"></a>
The wireless device type.
Type: String
Valid Values: `Sidewalk | LoRaWAN`
Required: Yes

 ** Events **   <a name="iotwireless-Type-WirelessDeviceLogOption-Events"></a>
The list of wireless device event log options.
Type: Array of [WirelessDeviceEventLogOption](API_WirelessDeviceEventLogOption.md) objects
Required: No

## See Also
<a name="API_WirelessDeviceLogOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/WirelessDeviceLogOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/WirelessDeviceLogOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/WirelessDeviceLogOption)
