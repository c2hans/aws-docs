---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_TdscdmaNmrObj.html
---

# TdscdmaNmrObj
<a name="API_TdscdmaNmrObj"></a>

TD-SCDMA object for network measurement reports.

## Contents
<a name="API_TdscdmaNmrObj_Contents"></a>

 ** CellParams **   <a name="iotwireless-Type-TdscdmaNmrObj-CellParams"></a>
Cell parameters for TD-SCDMA network measurement reports object.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 127.
Required: Yes

 ** Uarfcn **   <a name="iotwireless-Type-TdscdmaNmrObj-Uarfcn"></a>
TD-SCDMA UTRA (Universal Terrestrial Radio Access Network) absolute RF channel number.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 16383.
Required: Yes

 ** PathLoss **   <a name="iotwireless-Type-TdscdmaNmrObj-PathLoss"></a>
Path loss, or path attenuation, is the reduction in power density of an electromagnetic wave as it propagates through space.
Type: Integer
Valid Range: Minimum value of 46. Maximum value of 158.
Required: No

 ** Rscp **   <a name="iotwireless-Type-TdscdmaNmrObj-Rscp"></a>
Code power of the received signal, measured in decibel-milliwatts (dBm).
Type: Integer
Valid Range: Minimum value of -120. Maximum value of -25.
Required: No

 ** UtranCid **   <a name="iotwireless-Type-TdscdmaNmrObj-UtranCid"></a>
UTRAN (UMTS Terrestrial Radio Access Network) cell global identifier.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 268435455.
Required: No

## See Also
<a name="API_TdscdmaNmrObj_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/TdscdmaNmrObj)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/TdscdmaNmrObj)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/TdscdmaNmrObj)
