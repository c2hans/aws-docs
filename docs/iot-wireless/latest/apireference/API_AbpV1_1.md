---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_AbpV1_1.html
---

# AbpV1\_1
<a name="API_AbpV1_1"></a>

ABP device object for LoRaWAN specification v1.1

## Contents
<a name="API_AbpV1_1_Contents"></a>

 ** DevAddr **   <a name="iotwireless-Type-AbpV1_1-DevAddr"></a>
The DevAddr value.
Type: String
Pattern: `[a-fA-F0-9]{8}`
Required: No

 ** FCntStart **   <a name="iotwireless-Type-AbpV1_1-FCntStart"></a>
The FCnt init value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

 ** SessionKeys **   <a name="iotwireless-Type-AbpV1_1-SessionKeys"></a>
Session keys for ABP v1.1
Type: [SessionKeysAbpV1\_1](API_SessionKeysAbpV1_1.md) object
Required: No

## See Also
<a name="API_AbpV1_1_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/AbpV1_1)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/AbpV1_1)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/AbpV1_1)
