---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_LoRaWANPublicGatewayMetadata.html
---

# LoRaWANPublicGatewayMetadata
<a name="API_LoRaWANPublicGatewayMetadata"></a>

LoRaWAN public gateway metadata.

## Contents
<a name="API_LoRaWANPublicGatewayMetadata_Contents"></a>

 ** DlAllowed **   <a name="iotwireless-Type-LoRaWANPublicGatewayMetadata-DlAllowed"></a>
Boolean that indicates whether downlink is allowed using the network.
Type: Boolean
Required: No

 ** Id **   <a name="iotwireless-Type-LoRaWANPublicGatewayMetadata-Id"></a>
The ID of the gateways that are operated by the network provider.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** ProviderNetId **   <a name="iotwireless-Type-LoRaWANPublicGatewayMetadata-ProviderNetId"></a>
The ID of the LoRaWAN public network provider.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** RfRegion **   <a name="iotwireless-Type-LoRaWANPublicGatewayMetadata-RfRegion"></a>
The frequency band (RFRegion) value.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** Rssi **   <a name="iotwireless-Type-LoRaWANPublicGatewayMetadata-Rssi"></a>
The RSSI (received signal strength indicator) value.
Type: Double
Required: No

 ** Snr **   <a name="iotwireless-Type-LoRaWANPublicGatewayMetadata-Snr"></a>
The SNR (signal to noise ratio) value.
Type: Double
Required: No

## See Also
<a name="API_LoRaWANPublicGatewayMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/LoRaWANPublicGatewayMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/LoRaWANPublicGatewayMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/LoRaWANPublicGatewayMetadata)
