---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CdmaNmrObj.html
---

# CdmaNmrObj
<a name="API_CdmaNmrObj"></a>

CDMA object for network measurement reports.

## Contents
<a name="API_CdmaNmrObj_Contents"></a>

 ** CdmaChannel **   <a name="iotwireless-Type-CdmaNmrObj-CdmaChannel"></a>
CDMA channel information.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 4095.
Required: Yes

 ** PnOffset **   <a name="iotwireless-Type-CdmaNmrObj-PnOffset"></a>
Pseudo-noise offset, which is a characteristic of the signal from a cell on a radio tower.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 511.
Required: Yes

 ** BaseStationId **   <a name="iotwireless-Type-CdmaNmrObj-BaseStationId"></a>
CDMA base station ID (BSID).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

 ** PilotPower **   <a name="iotwireless-Type-CdmaNmrObj-PilotPower"></a>
Transmit power level of the pilot signal, measured in dBm (decibel-milliwatts).
Type: Integer
Valid Range: Minimum value of -142. Maximum value of -49.
Required: No

## See Also
<a name="API_CdmaNmrObj_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/CdmaNmrObj)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/CdmaNmrObj)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/CdmaNmrObj)
