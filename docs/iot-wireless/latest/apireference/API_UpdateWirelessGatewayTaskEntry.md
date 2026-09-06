---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateWirelessGatewayTaskEntry.html
---

# UpdateWirelessGatewayTaskEntry
<a name="API_UpdateWirelessGatewayTaskEntry"></a>

UpdateWirelessGatewayTaskEntry object.

## Contents
<a name="API_UpdateWirelessGatewayTaskEntry_Contents"></a>

 ** Arn **   <a name="iotwireless-Type-UpdateWirelessGatewayTaskEntry-Arn"></a>
The Amazon Resource Name of the resource.
Type: String
Required: No

 ** Id **   <a name="iotwireless-Type-UpdateWirelessGatewayTaskEntry-Id"></a>
The ID of the new wireless gateway task entry.
Type: String
Length Constraints: Maximum length of 36.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`
Required: No

 ** LoRaWAN **   <a name="iotwireless-Type-UpdateWirelessGatewayTaskEntry-LoRaWAN"></a>
The properties that relate to the LoRaWAN wireless gateway.
Type: [LoRaWANUpdateGatewayTaskEntry](API_LoRaWANUpdateGatewayTaskEntry.md) object
Required: No

## See Also
<a name="API_UpdateWirelessGatewayTaskEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/UpdateWirelessGatewayTaskEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/UpdateWirelessGatewayTaskEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/UpdateWirelessGatewayTaskEntry)
