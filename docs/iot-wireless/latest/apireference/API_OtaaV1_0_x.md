---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_OtaaV1_0_x.html
---

# OtaaV1\_0\_x
<a name="API_OtaaV1_0_x"></a>

OTAA device object for v1.0.x

## Contents
<a name="API_OtaaV1_0_x_Contents"></a>

 ** AppEui **   <a name="iotwireless-Type-OtaaV1_0_x-AppEui"></a>
The AppEUI value. You specify this value when using LoRaWAN versions v1.0.2 or v1.0.3.
Type: String
Pattern: `[a-fA-F0-9]{16}`
Required: No

 ** AppKey **   <a name="iotwireless-Type-OtaaV1_0_x-AppKey"></a>
The AppKey value.
Type: String
Pattern: `[a-fA-F0-9]{32}`
Required: No

 ** GenAppKey **   <a name="iotwireless-Type-OtaaV1_0_x-GenAppKey"></a>
The GenAppKey value.
Type: String
Pattern: `[a-fA-F0-9]{32}`
Required: No

 ** JoinEui **   <a name="iotwireless-Type-OtaaV1_0_x-JoinEui"></a>
The JoinEUI value. You specify this value instead of the AppEUI when using LoRaWAN version v1.0.4.
Type: String
Pattern: `[a-fA-F0-9]{16}`
Required: No

## See Also
<a name="API_OtaaV1_0_x_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/OtaaV1_0_x)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/OtaaV1_0_x)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/OtaaV1_0_x)
