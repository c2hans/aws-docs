---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateFPorts.html
---

# UpdateFPorts
<a name="API_UpdateFPorts"></a>

Object for updating the FPorts information.

## Contents
<a name="API_UpdateFPorts_Contents"></a>

 ** Applications **   <a name="iotwireless-Type-UpdateFPorts-Applications"></a>
LoRaWAN application, which can be used for geolocation by activating positioning.
Type: Array of [ApplicationConfig](API_ApplicationConfig.md) objects
Required: No

 ** Positioning **   <a name="iotwireless-Type-UpdateFPorts-Positioning"></a>
Positioning FPorts for the ClockSync, Stream, and GNSS functions.
Type: [Positioning](API_Positioning.md) object
Required: No

## See Also
<a name="API_UpdateFPorts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/UpdateFPorts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/UpdateFPorts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/UpdateFPorts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
