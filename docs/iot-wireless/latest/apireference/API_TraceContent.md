---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_TraceContent.html
---

# TraceContent
<a name="API_TraceContent"></a>

Trace content for your wireless devices, gateways, and multicast groups.

## Contents
<a name="API_TraceContent_Contents"></a>

 ** LogLevel **   <a name="iotwireless-Type-TraceContent-LogLevel"></a>
The log level for a log message. The log levels can be disabled, or set to `ERROR` to display less verbose logs containing only error information, or to `INFO` for more detailed logs.
Type: String
Valid Values: `INFO | ERROR | DISABLED`
Required: No

 ** MulticastFrameInfo **   <a name="iotwireless-Type-TraceContent-MulticastFrameInfo"></a>
 `FrameInfo` of your multicast group resources for the trace content. Use FrameInfo to debug the multicast communication between your multicast groups and the network server.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** WirelessDeviceFrameInfo **   <a name="iotwireless-Type-TraceContent-WirelessDeviceFrameInfo"></a>
 `FrameInfo` of your wireless device resources for the trace content. Use FrameInfo to debug the communication between your LoRaWAN end devices and the network server.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_TraceContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/TraceContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/TraceContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/TraceContent)
