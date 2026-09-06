---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_LteNmrObj.html
---

# LteNmrObj
<a name="API_LteNmrObj"></a>

LTE object for network measurement reports.

## Contents
<a name="API_LteNmrObj_Contents"></a>

 ** Earfcn **   <a name="iotwireless-Type-LteNmrObj-Earfcn"></a>
E-UTRA (Evolved universal terrestrial Radio Access) absolute radio frequency channel Number (EARFCN).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 262143.
Required: Yes

 ** Pci **   <a name="iotwireless-Type-LteNmrObj-Pci"></a>
Physical cell ID.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 503.
Required: Yes

 ** EutranCid **   <a name="iotwireless-Type-LteNmrObj-EutranCid"></a>
E-UTRAN (Evolved Universal Terrestrial Radio Access Network) cell global identifier (EUTRANCID).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 268435455.
Required: No

 ** Rsrp **   <a name="iotwireless-Type-LteNmrObj-Rsrp"></a>
Signal power of the reference signal received, measured in dBm (decibel-milliwatts).
Type: Integer
Valid Range: Minimum value of -140. Maximum value of -44.
Required: No

 ** Rsrq **   <a name="iotwireless-Type-LteNmrObj-Rsrq"></a>
Signal quality of the reference Signal received, measured in decibels (dB).
Type: Float
Valid Range: Minimum value of -19.5. Maximum value of -3.
Required: No

## See Also
<a name="API_LteNmrObj_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/LteNmrObj)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/LteNmrObj)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/LteNmrObj)
