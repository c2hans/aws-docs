---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_WcdmaNmrObj.html
---

# WcdmaNmrObj
<a name="API_WcdmaNmrObj"></a>

Network Measurement Reports.

## Contents
<a name="API_WcdmaNmrObj_Contents"></a>

 ** Psc **   <a name="iotwireless-Type-WcdmaNmrObj-Psc"></a>
Primary Scrambling Code.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 511.
Required: Yes

 ** Uarfcndl **   <a name="iotwireless-Type-WcdmaNmrObj-Uarfcndl"></a>
WCDMA UTRA Absolute RF Channel Number downlink.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 16383.
Required: Yes

 ** UtranCid **   <a name="iotwireless-Type-WcdmaNmrObj-UtranCid"></a>
UTRAN (UMTS Terrestrial Radio Access Network) Cell Global Identifier.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 268435455.
Required: Yes

 ** PathLoss **   <a name="iotwireless-Type-WcdmaNmrObj-PathLoss"></a>
Path loss, or path attenuation, is the reduction in power density of an electromagnetic wave as it propagates through space.
Type: Integer
Valid Range: Minimum value of 46. Maximum value of 158.
Required: No

 ** Rscp **   <a name="iotwireless-Type-WcdmaNmrObj-Rscp"></a>
Received Signal Code Power (signal power) (dBm)
Type: Integer
Valid Range: Minimum value of -120. Maximum value of -25.
Required: No

## See Also
<a name="API_WcdmaNmrObj_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/WcdmaNmrObj)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/WcdmaNmrObj)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/WcdmaNmrObj)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
