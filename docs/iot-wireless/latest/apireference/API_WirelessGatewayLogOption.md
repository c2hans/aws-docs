---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_WirelessGatewayLogOption.html
---

# WirelessGatewayLogOption
<a name="API_WirelessGatewayLogOption"></a>

The log options for wireless gateways and can be used to set log levels for a specific type of wireless gateway.

## Contents
<a name="API_WirelessGatewayLogOption_Contents"></a>

 ** LogLevel **   <a name="iotwireless-Type-WirelessGatewayLogOption-LogLevel"></a>
The log level for a log message. The log levels can be disabled, or set to `ERROR` to display less verbose logs containing only error information, or to `INFO` for more detailed logs.
Type: String
Valid Values: `INFO | ERROR | DISABLED`
Required: Yes

 ** Type **   <a name="iotwireless-Type-WirelessGatewayLogOption-Type"></a>
The wireless gateway type.
Type: String
Valid Values: `LoRaWAN`
Required: Yes

 ** Events **   <a name="iotwireless-Type-WirelessGatewayLogOption-Events"></a>
The list of wireless gateway event log options.
Type: Array of [WirelessGatewayEventLogOption](API_WirelessGatewayEventLogOption.md) objects
Required: No

## See Also
<a name="API_WirelessGatewayLogOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/WirelessGatewayLogOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/WirelessGatewayLogOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/WirelessGatewayLogOption)
