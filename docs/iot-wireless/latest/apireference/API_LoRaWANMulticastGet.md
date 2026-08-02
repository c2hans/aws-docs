---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_LoRaWANMulticastGet.html
---

# LoRaWANMulticastGet
<a name="API_LoRaWANMulticastGet"></a>

The LoRaWAN information that is to be returned from getting multicast group information.

## Contents
<a name="API_LoRaWANMulticastGet_Contents"></a>

 ** DefaultSessionParameters **   <a name="iotwireless-Type-LoRaWANMulticastGet-DefaultSessionParameters"></a>
The default session parameters for the multicast group.
Type: [DefaultSessionParametersMulticast](API_DefaultSessionParametersMulticast.md) object
Required: No

 ** DlClass **   <a name="iotwireless-Type-LoRaWANMulticastGet-DlClass"></a>
DlClass for LoRaWAM, valid values are ClassB and ClassC.
Type: String
Length Constraints: Maximum length of 256.
Valid Values: `ClassB | ClassC`
Required: No

 ** NumberOfDevicesInGroup **   <a name="iotwireless-Type-LoRaWANMulticastGet-NumberOfDevicesInGroup"></a>
Number of devices that are associated to the multicast group.
Type: Integer
Required: No

 ** NumberOfDevicesRequested **   <a name="iotwireless-Type-LoRaWANMulticastGet-NumberOfDevicesRequested"></a>
Number of devices that are requested to be associated with the multicast group.
Type: Integer
Required: No

 ** ParticipatingGateways **   <a name="iotwireless-Type-LoRaWANMulticastGet-ParticipatingGateways"></a>
Specify the list of gateways to which you want to send the multicast downlink messages. The multicast message will be sent to each gateway in the list, with the transmission interval as the time interval between each message.
Type: [ParticipatingGatewaysMulticast](API_ParticipatingGatewaysMulticast.md) object
Required: No

 ** RfRegion **   <a name="iotwireless-Type-LoRaWANMulticastGet-RfRegion"></a>
Supported RfRegions
Type: String
Valid Values: `EU868 | US915 | AU915 | AS923-1 | AS923-2 | AS923-3 | AS923-4 | EU433 | CN470 | CN779 | RU864 | KR920 | IN865`
Required: No

## See Also
<a name="API_LoRaWANMulticastGet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/LoRaWANMulticastGet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/LoRaWANMulticastGet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/LoRaWANMulticastGet)
