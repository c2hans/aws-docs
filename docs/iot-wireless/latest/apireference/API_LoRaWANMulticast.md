---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_LoRaWANMulticast.html
---

# LoRaWANMulticast
<a name="API_LoRaWANMulticast"></a>

The LoRaWAN information that is to be used with the multicast group.

## Contents
<a name="API_LoRaWANMulticast_Contents"></a>

 ** DefaultSessionParameters **   <a name="iotwireless-Type-LoRaWANMulticast-DefaultSessionParameters"></a>
The default session parameters for the multicast group.
Type: [DefaultSessionParametersMulticast](API_DefaultSessionParametersMulticast.md) object
Required: No

 ** DlClass **   <a name="iotwireless-Type-LoRaWANMulticast-DlClass"></a>
DlClass for LoRaWAM, valid values are ClassB and ClassC.
Type: String
Length Constraints: Maximum length of 256.
Valid Values: `ClassB | ClassC`
Required: No

 ** ParticipatingGateways **   <a name="iotwireless-Type-LoRaWANMulticast-ParticipatingGateways"></a>
Specify the list of gateways to which you want to send the multicast downlink messages. The multicast message will be sent to each gateway in the list, with the transmission interval as the time interval between each message.
Type: [ParticipatingGatewaysMulticast](API_ParticipatingGatewaysMulticast.md) object
Required: No

 ** RfRegion **   <a name="iotwireless-Type-LoRaWANMulticast-RfRegion"></a>
Supported RfRegions
Type: String
Valid Values: `EU868 | US915 | AU915 | AS923-1 | AS923-2 | AS923-3 | AS923-4 | EU433 | CN470 | CN779 | RU864 | KR920 | IN865`
Required: No

## See Also
<a name="API_LoRaWANMulticast_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/LoRaWANMulticast)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/LoRaWANMulticast)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/LoRaWANMulticast)
