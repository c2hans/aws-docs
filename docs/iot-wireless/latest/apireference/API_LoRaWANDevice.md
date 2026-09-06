---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_LoRaWANDevice.html
---

# LoRaWANDevice
<a name="API_LoRaWANDevice"></a>

LoRaWAN object for create functions.

## Contents
<a name="API_LoRaWANDevice_Contents"></a>

 ** AbpV1\_0\_x **   <a name="iotwireless-Type-LoRaWANDevice-AbpV1_0_x"></a>
LoRaWAN object for create APIs
Type: [AbpV1\_0\_x](API_AbpV1_0_x.md) object
Required: No

 ** AbpV1\_1 **   <a name="iotwireless-Type-LoRaWANDevice-AbpV1_1"></a>
ABP device object for create APIs for v1.1
Type: [AbpV1\_1](API_AbpV1_1.md) object
Required: No

 ** DevEui **   <a name="iotwireless-Type-LoRaWANDevice-DevEui"></a>
The DevEUI value.
Type: String
Pattern: `[a-fA-F0-9]{16}`
Required: No

 ** DeviceProfileId **   <a name="iotwireless-Type-LoRaWANDevice-DeviceProfileId"></a>
The ID of the device profile for the new wireless device.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** FPorts **   <a name="iotwireless-Type-LoRaWANDevice-FPorts"></a>
List of FPort assigned for different LoRaWAN application packages to use
Type: [FPorts](API_FPorts.md) object
Required: No

 ** OtaaV1\_0\_x **   <a name="iotwireless-Type-LoRaWANDevice-OtaaV1_0_x"></a>
OTAA device object for create APIs for v1.0.x
Type: [OtaaV1\_0\_x](API_OtaaV1_0_x.md) object
Required: No

 ** OtaaV1\_1 **   <a name="iotwireless-Type-LoRaWANDevice-OtaaV1_1"></a>
OTAA device object for v1.1 for create APIs
Type: [OtaaV1\_1](API_OtaaV1_1.md) object
Required: No

 ** ServiceProfileId **   <a name="iotwireless-Type-LoRaWANDevice-ServiceProfileId"></a>
The ID of the service profile.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_LoRaWANDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/LoRaWANDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/LoRaWANDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/LoRaWANDevice)
