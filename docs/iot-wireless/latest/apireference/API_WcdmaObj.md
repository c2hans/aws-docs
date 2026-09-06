---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_WcdmaObj.html
---

# WcdmaObj
<a name="API_WcdmaObj"></a>

WCDMA.

## Contents
<a name="API_WcdmaObj_Contents"></a>

 ** Mcc **   <a name="iotwireless-Type-WcdmaObj-Mcc"></a>
Mobile Country Code.
Type: Integer
Valid Range: Minimum value of 200. Maximum value of 999.
Required: Yes

 ** Mnc **   <a name="iotwireless-Type-WcdmaObj-Mnc"></a>
Mobile Network Code.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 999.
Required: Yes

 ** UtranCid **   <a name="iotwireless-Type-WcdmaObj-UtranCid"></a>
UTRAN (UMTS Terrestrial Radio Access Network) Cell Global Identifier.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 268435455.
Required: Yes

 ** Lac **   <a name="iotwireless-Type-WcdmaObj-Lac"></a>
Location Area Code.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** PathLoss **   <a name="iotwireless-Type-WcdmaObj-PathLoss"></a>
Path loss, or path attenuation, is the reduction in power density of an electromagnetic wave as it propagates through space.
Type: Integer
Valid Range: Minimum value of 46. Maximum value of 158.
Required: No

 ** Rscp **   <a name="iotwireless-Type-WcdmaObj-Rscp"></a>
Received Signal Code Power (signal power) (dBm).
Type: Integer
Valid Range: Minimum value of -120. Maximum value of -25.
Required: No

 ** WcdmaLocalId **   <a name="iotwireless-Type-WcdmaObj-WcdmaLocalId"></a>
WCDMA local ID information.
Type: [WcdmaLocalId](API_WcdmaLocalId.md) object
Required: No

 ** WcdmaNmr **   <a name="iotwireless-Type-WcdmaObj-WcdmaNmr"></a>
WCDMA object for network measurement reports.
Type: Array of [WcdmaNmrObj](API_WcdmaNmrObj.md) objects
Array Members: Minimum number of 1 item. Maximum number of 32 items.
Required: No

## See Also
<a name="API_WcdmaObj_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/WcdmaObj)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/WcdmaObj)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/WcdmaObj)
