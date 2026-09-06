---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DownlinkQueueMessage.html
---

# DownlinkQueueMessage
<a name="API_DownlinkQueueMessage"></a>

The message in the downlink queue.

## Contents
<a name="API_DownlinkQueueMessage_Contents"></a>

 ** LoRaWAN **   <a name="iotwireless-Type-DownlinkQueueMessage-LoRaWAN"></a>
LoRaWAN router info.
Type: [LoRaWANSendDataToDevice](API_LoRaWANSendDataToDevice.md) object
Required: No

 ** MessageId **   <a name="iotwireless-Type-DownlinkQueueMessage-MessageId"></a>
 The message ID assigned by IoT Wireless to each downlink message, which helps identify the message.
Type: String
Required: No

 ** ReceivedAt **   <a name="iotwireless-Type-DownlinkQueueMessage-ReceivedAt"></a>
The time at which Iot Wireless received the downlink message.
Type: String
Pattern: `^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$`
Required: No

 ** TransmitMode **   <a name="iotwireless-Type-DownlinkQueueMessage-TransmitMode"></a>
The transmit mode to use for sending data to the wireless device. This can be `0` for UM (unacknowledge mode) or `1` for AM (acknowledge mode).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

## See Also
<a name="API_DownlinkQueueMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/DownlinkQueueMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/DownlinkQueueMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/DownlinkQueueMessage)
