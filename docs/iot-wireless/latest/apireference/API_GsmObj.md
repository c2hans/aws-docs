---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GsmObj.html
---

# GsmObj
<a name="API_GsmObj"></a>

GSM object.

## Contents
<a name="API_GsmObj_Contents"></a>

 ** GeranCid **   <a name="iotwireless-Type-GsmObj-GeranCid"></a>
GERAN (GSM EDGE Radio Access Network) Cell Global Identifier.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: Yes

 ** Lac **   <a name="iotwireless-Type-GsmObj-Lac"></a>
Location area code.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: Yes

 ** Mcc **   <a name="iotwireless-Type-GsmObj-Mcc"></a>
Mobile Country Code.
Type: Integer
Valid Range: Minimum value of 200. Maximum value of 999.
Required: Yes

 ** Mnc **   <a name="iotwireless-Type-GsmObj-Mnc"></a>
Mobile Network Code.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 999.
Required: Yes

 ** GsmLocalId **   <a name="iotwireless-Type-GsmObj-GsmLocalId"></a>
GSM local identification (local ID) information.
Type: [GsmLocalId](API_GsmLocalId.md) object
Required: No

 ** GsmNmr **   <a name="iotwireless-Type-GsmObj-GsmNmr"></a>
GSM object for network measurement reports.
Type: Array of [GsmNmrObj](API_GsmNmrObj.md) objects
Array Members: Minimum number of 1 item. Maximum number of 32 items.
Required: No

 ** GsmTimingAdvance **   <a name="iotwireless-Type-GsmObj-GsmTimingAdvance"></a>
Timing advance value, which corresponds to the length of time a signal takes to reach the base station from a mobile phone.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 63.
Required: No

 ** RxLevel **   <a name="iotwireless-Type-GsmObj-RxLevel"></a>
Rx level, which is the received signal power, measured in dBm (decibel-milliwatts).
Type: Integer
Valid Range: Minimum value of -110. Maximum value of -25.
Required: No

## See Also
<a name="API_GsmObj_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GsmObj)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GsmObj)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GsmObj)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
