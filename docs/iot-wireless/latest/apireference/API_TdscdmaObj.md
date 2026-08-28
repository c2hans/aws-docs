---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_TdscdmaObj.html
---

# TdscdmaObj
<a name="API_TdscdmaObj"></a>

TD-SCDMA object.

## Contents
<a name="API_TdscdmaObj_Contents"></a>

 ** Mcc **   <a name="iotwireless-Type-TdscdmaObj-Mcc"></a>
Mobile Country Code.
Type: Integer
Valid Range: Minimum value of 200. Maximum value of 999.
Required: Yes

 ** Mnc **   <a name="iotwireless-Type-TdscdmaObj-Mnc"></a>
Mobile Network Code.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 999.
Required: Yes

 ** UtranCid **   <a name="iotwireless-Type-TdscdmaObj-UtranCid"></a>
UTRAN (UMTS Terrestrial Radio Access Network) Cell Global Identifier.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 268435455.
Required: Yes

 ** Lac **   <a name="iotwireless-Type-TdscdmaObj-Lac"></a>
Location Area Code.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** PathLoss **   <a name="iotwireless-Type-TdscdmaObj-PathLoss"></a>
Path loss, or path attenuation, is the reduction in power density of an electromagnetic wave as it propagates through space.
Type: Integer
Valid Range: Minimum value of 46. Maximum value of 158.
Required: No

 ** Rscp **   <a name="iotwireless-Type-TdscdmaObj-Rscp"></a>
Signal power of the received signal (Received Signal Code Power), measured in decibel-milliwatts (dBm).
Type: Integer
Valid Range: Minimum value of -120. Maximum value of -25.
Required: No

 ** TdscdmaLocalId **   <a name="iotwireless-Type-TdscdmaObj-TdscdmaLocalId"></a>
TD-SCDMA local identification (local ID) information.
Type: [TdscdmaLocalId](API_TdscdmaLocalId.md) object
Required: No

 ** TdscdmaNmr **   <a name="iotwireless-Type-TdscdmaObj-TdscdmaNmr"></a>
TD-SCDMA object for network measurement reports.
Type: Array of [TdscdmaNmrObj](API_TdscdmaNmrObj.md) objects
Array Members: Minimum number of 1 item. Maximum number of 32 items.
Required: No

 ** TdscdmaTimingAdvance **   <a name="iotwireless-Type-TdscdmaObj-TdscdmaTimingAdvance"></a>
TD-SCDMA Timing advance.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1530.
Required: No

## See Also
<a name="API_TdscdmaObj_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/TdscdmaObj)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/TdscdmaObj)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/TdscdmaObj)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
