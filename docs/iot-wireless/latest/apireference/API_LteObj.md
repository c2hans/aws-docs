---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_LteObj.html
---

# LteObj
<a name="API_LteObj"></a>

LTE object.

## Contents
<a name="API_LteObj_Contents"></a>

 ** EutranCid **   <a name="iotwireless-Type-LteObj-EutranCid"></a>
E-UTRAN (Evolved Universal Terrestrial Radio Access Network) Cell Global Identifier.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 268435455.
Required: Yes

 ** Mcc **   <a name="iotwireless-Type-LteObj-Mcc"></a>
Mobile Country Code.
Type: Integer
Valid Range: Minimum value of 200. Maximum value of 999.
Required: Yes

 ** Mnc **   <a name="iotwireless-Type-LteObj-Mnc"></a>
Mobile Network Code.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 999.
Required: Yes

 ** LteLocalId **   <a name="iotwireless-Type-LteObj-LteLocalId"></a>
LTE local identification (local ID) information.
Type: [LteLocalId](API_LteLocalId.md) object
Required: No

 ** LteNmr **   <a name="iotwireless-Type-LteObj-LteNmr"></a>
LTE object for network measurement reports.
Type: Array of [LteNmrObj](API_LteNmrObj.md) objects
Array Members: Minimum number of 1 item. Maximum number of 32 items.
Required: No

 ** LteTimingAdvance **   <a name="iotwireless-Type-LteObj-LteTimingAdvance"></a>
LTE timing advance.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1282.
Required: No

 ** NrCapable **   <a name="iotwireless-Type-LteObj-NrCapable"></a>
Parameter that determines whether the LTE object is capable of supporting NR (new radio).
Type: Boolean
Required: No

 ** Rsrp **   <a name="iotwireless-Type-LteObj-Rsrp"></a>
Signal power of the reference signal received, measured in dBm (decibel-milliwatts).
Type: Integer
Valid Range: Minimum value of -140. Maximum value of -44.
Required: No

 ** Rsrq **   <a name="iotwireless-Type-LteObj-Rsrq"></a>
Signal quality of the reference Signal received, measured in decibels (dB).
Type: Float
Valid Range: Minimum value of -19.5. Maximum value of -3.
Required: No

 ** Tac **   <a name="iotwireless-Type-LteObj-Tac"></a>
LTE tracking area code.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

## See Also
<a name="API_LteObj_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/LteObj)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/LteObj)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/LteObj)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
