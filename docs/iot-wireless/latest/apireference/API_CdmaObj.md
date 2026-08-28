---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CdmaObj.html
---

# CdmaObj
<a name="API_CdmaObj"></a>

CDMA (Code-division multiple access) object.

## Contents
<a name="API_CdmaObj_Contents"></a>

 ** BaseStationId **   <a name="iotwireless-Type-CdmaObj-BaseStationId"></a>
CDMA base station ID (BSID).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: Yes

 ** NetworkId **   <a name="iotwireless-Type-CdmaObj-NetworkId"></a>
CDMA network ID (NID).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: Yes

 ** SystemId **   <a name="iotwireless-Type-CdmaObj-SystemId"></a>
CDMA system ID (SID).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 32767.
Required: Yes

 ** BaseLat **   <a name="iotwireless-Type-CdmaObj-BaseLat"></a>
CDMA base station latitude in degrees.
Type: Float
Valid Range: Minimum value of -90. Maximum value of 90.
Required: No

 ** BaseLng **   <a name="iotwireless-Type-CdmaObj-BaseLng"></a>
CDMA base station longitude in degrees.
Type: Float
Valid Range: Minimum value of -180. Maximum value of 180.
Required: No

 ** CdmaLocalId **   <a name="iotwireless-Type-CdmaObj-CdmaLocalId"></a>
CDMA local identification (local ID) parameters.
Type: [CdmaLocalId](API_CdmaLocalId.md) object
Required: No

 ** CdmaNmr **   <a name="iotwireless-Type-CdmaObj-CdmaNmr"></a>
CDMA network measurement reports.
Type: Array of [CdmaNmrObj](API_CdmaNmrObj.md) objects
Array Members: Minimum number of 1 item. Maximum number of 32 items.
Required: No

 ** PilotPower **   <a name="iotwireless-Type-CdmaObj-PilotPower"></a>
Transmit power level of the pilot signal, measured in dBm (decibel-milliwatts).
Type: Integer
Valid Range: Minimum value of -142. Maximum value of -49.
Required: No

 ** RegistrationZone **   <a name="iotwireless-Type-CdmaObj-RegistrationZone"></a>
CDMA registration zone (RZ).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 4095.
Required: No

## See Also
<a name="API_CdmaObj_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/CdmaObj)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/CdmaObj)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/CdmaObj)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
