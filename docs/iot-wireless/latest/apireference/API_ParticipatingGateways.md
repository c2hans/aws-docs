---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ParticipatingGateways.html
---

# ParticipatingGateways
<a name="API_ParticipatingGateways"></a>

Specify the list of gateways to which you want to send downlink data traffic when the wireless device is running in class B or class C mode.

## Contents
<a name="API_ParticipatingGateways_Contents"></a>

 ** DownlinkMode **   <a name="iotwireless-Type-ParticipatingGateways-DownlinkMode"></a>
Indicates whether to send the downlink message in sequential mode or concurrent mode, or to use only the chosen gateways from the previous uplink message transmission.
Type: String
Valid Values: `SEQUENTIAL | CONCURRENT | USING_UPLINK_GATEWAY`
Required: Yes

 ** GatewayList **   <a name="iotwireless-Type-ParticipatingGateways-GatewayList"></a>
The list of gateways that you want to use for sending the downlink data traffic.
Type: Array of [GatewayListItem](API_GatewayListItem.md) objects
Required: Yes

 ** TransmissionInterval **   <a name="iotwireless-Type-ParticipatingGateways-TransmissionInterval"></a>
The duration of time for which AWS IoT Core for LoRaWAN will wait before transmitting the payload to the next gateway.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 604800.
Required: Yes

## See Also
<a name="API_ParticipatingGateways_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/ParticipatingGateways)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/ParticipatingGateways)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/ParticipatingGateways)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
