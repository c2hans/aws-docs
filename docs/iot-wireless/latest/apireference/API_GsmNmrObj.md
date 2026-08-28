---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GsmNmrObj.html
---

# GsmNmrObj
<a name="API_GsmNmrObj"></a>

GSM object for network measurement reports.

## Contents
<a name="API_GsmNmrObj_Contents"></a>

 ** Bcch **   <a name="iotwireless-Type-GsmNmrObj-Bcch"></a>
GSM broadcast control channel.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1023.
Required: Yes

 ** Bsic **   <a name="iotwireless-Type-GsmNmrObj-Bsic"></a>
GSM base station identity code (BSIC).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 63.
Required: Yes

 ** GlobalIdentity **   <a name="iotwireless-Type-GsmNmrObj-GlobalIdentity"></a>
Global identity information of the GSM object.
Type: [GlobalIdentity](API_GlobalIdentity.md) object
Required: No

 ** RxLevel **   <a name="iotwireless-Type-GsmNmrObj-RxLevel"></a>
Rx level, which is the received signal power, measured in dBm (decibel-milliwatts).
Type: Integer
Valid Range: Minimum value of -110. Maximum value of -25.
Required: No

## See Also
<a name="API_GsmNmrObj_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GsmNmrObj)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GsmNmrObj)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GsmNmrObj)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
