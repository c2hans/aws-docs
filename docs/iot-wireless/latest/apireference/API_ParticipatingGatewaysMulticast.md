---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ParticipatingGatewaysMulticast.html
---

# ParticipatingGatewaysMulticast
<a name="API_ParticipatingGatewaysMulticast"></a>

Specify the list of gateways to which you want to send the multicast downlink messages. The multicast message will be sent to each gateway in the list, with the transmission interval as the time interval between each message.

## Contents
<a name="API_ParticipatingGatewaysMulticast_Contents"></a>

 ** GatewayList **   <a name="iotwireless-Type-ParticipatingGatewaysMulticast-GatewayList"></a>
The list of gateways that you want to use for sending the multicast downlink message. Each downlink message will be sent to all the gateways in the list in the order that you provided. If the gateway list is empty, then AWS IoT Core for LoRaWAN chooses the gateways that were most recently used by the devices to send an uplink message.
Type: Array of strings
Array Members: Maximum number of 20 items.
Length Constraints: Maximum length of 256.
Required: No

 ** TransmissionInterval **   <a name="iotwireless-Type-ParticipatingGatewaysMulticast-TransmissionInterval"></a>
The duration of time in milliseconds for which AWS IoT Core for LoRaWAN will wait before transmitting the multicast payload to the next gateway in the list.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 60000.
Required: No

## See Also
<a name="API_ParticipatingGatewaysMulticast_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/ParticipatingGatewaysMulticast)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/ParticipatingGatewaysMulticast)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/ParticipatingGatewaysMulticast)
