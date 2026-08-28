---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_LoRaWANUpdateDevice.html
---

# LoRaWANUpdateDevice
<a name="API_LoRaWANUpdateDevice"></a>

LoRaWAN object for update functions.

## Contents
<a name="API_LoRaWANUpdateDevice_Contents"></a>

 ** AbpV1\_0\_x **   <a name="iotwireless-Type-LoRaWANUpdateDevice-AbpV1_0_x"></a>
ABP device object for update APIs for v1.0.x
Type: [UpdateAbpV1\_0\_x](API_UpdateAbpV1_0_x.md) object
Required: No

 ** AbpV1\_1 **   <a name="iotwireless-Type-LoRaWANUpdateDevice-AbpV1_1"></a>
ABP device object for update APIs for v1.1
Type: [UpdateAbpV1\_1](API_UpdateAbpV1_1.md) object
Required: No

 ** DeviceProfileId **   <a name="iotwireless-Type-LoRaWANUpdateDevice-DeviceProfileId"></a>
The ID of the device profile for the wireless device.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** FPorts **   <a name="iotwireless-Type-LoRaWANUpdateDevice-FPorts"></a>
FPorts object for the positioning information of the device.
Type: [UpdateFPorts](API_UpdateFPorts.md) object
Required: No

 ** ServiceProfileId **   <a name="iotwireless-Type-LoRaWANUpdateDevice-ServiceProfileId"></a>
The ID of the service profile.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_LoRaWANUpdateDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/LoRaWANUpdateDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/LoRaWANUpdateDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/LoRaWANUpdateDevice)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
