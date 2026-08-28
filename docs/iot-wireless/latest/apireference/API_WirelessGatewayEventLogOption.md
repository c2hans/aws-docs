---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_WirelessGatewayEventLogOption.html
---

# WirelessGatewayEventLogOption
<a name="API_WirelessGatewayEventLogOption"></a>

The log options for a wireless gateway event and can be used to set log levels for a specific wireless gateway event.

For a LoRaWAN gateway, possible events for a log message are `CUPS_Request` and `Certificate`.

## Contents
<a name="API_WirelessGatewayEventLogOption_Contents"></a>

 ** Event **   <a name="iotwireless-Type-WirelessGatewayEventLogOption-Event"></a>
The event for a log message, if the log message is tied to a wireless gateway.
Type: String
Valid Values: `CUPS_Request | Certificate`
Required: Yes

 ** LogLevel **   <a name="iotwireless-Type-WirelessGatewayEventLogOption-LogLevel"></a>
The log level for a log message. The log levels can be disabled, or set to `ERROR` to display less verbose logs containing only error information, or to `INFO` for more detailed logs.
Type: String
Valid Values: `INFO | ERROR | DISABLED`
Required: Yes

## See Also
<a name="API_WirelessGatewayEventLogOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/WirelessGatewayEventLogOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/WirelessGatewayEventLogOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/WirelessGatewayEventLogOption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
