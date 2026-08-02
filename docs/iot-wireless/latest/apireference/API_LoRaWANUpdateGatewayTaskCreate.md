---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_LoRaWANUpdateGatewayTaskCreate.html
---

# LoRaWANUpdateGatewayTaskCreate
<a name="API_LoRaWANUpdateGatewayTaskCreate"></a>

LoRaWANUpdateGatewayTaskCreate object.

## Contents
<a name="API_LoRaWANUpdateGatewayTaskCreate_Contents"></a>

 ** CurrentVersion **   <a name="iotwireless-Type-LoRaWANUpdateGatewayTaskCreate-CurrentVersion"></a>
The version of the gateways that should receive the update.
Type: [LoRaWANGatewayVersion](API_LoRaWANGatewayVersion.md) object
Required: No

 ** SigKeyCrc **   <a name="iotwireless-Type-LoRaWANUpdateGatewayTaskCreate-SigKeyCrc"></a>
The CRC of the signature private key to check.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 4294967295.
Required: No

 ** UpdateSignature **   <a name="iotwireless-Type-LoRaWANUpdateGatewayTaskCreate-UpdateSignature"></a>
The signature used to verify the update firmware.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** UpdateVersion **   <a name="iotwireless-Type-LoRaWANUpdateGatewayTaskCreate-UpdateVersion"></a>
The firmware version to update the gateway to.
Type: [LoRaWANGatewayVersion](API_LoRaWANGatewayVersion.md) object
Required: No

## See Also
<a name="API_LoRaWANUpdateGatewayTaskCreate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/LoRaWANUpdateGatewayTaskCreate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/LoRaWANUpdateGatewayTaskCreate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/LoRaWANUpdateGatewayTaskCreate)
