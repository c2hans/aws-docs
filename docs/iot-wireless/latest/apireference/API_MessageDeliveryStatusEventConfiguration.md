---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_MessageDeliveryStatusEventConfiguration.html
---

# MessageDeliveryStatusEventConfiguration
<a name="API_MessageDeliveryStatusEventConfiguration"></a>

Message delivery status event configuration object for enabling and disabling relevant topics.

## Contents
<a name="API_MessageDeliveryStatusEventConfiguration_Contents"></a>

 ** Sidewalk **   <a name="iotwireless-Type-MessageDeliveryStatusEventConfiguration-Sidewalk"></a>
 `SidewalkEventNotificationConfigurations` object, which is the event configuration object for Sidewalk-related event topics.
Type: [SidewalkEventNotificationConfigurations](API_SidewalkEventNotificationConfigurations.md) object
Required: No

 ** WirelessDeviceIdEventTopic **   <a name="iotwireless-Type-MessageDeliveryStatusEventConfiguration-WirelessDeviceIdEventTopic"></a>
Denotes whether the wireless device ID message delivery status event topic is enabled or disabled.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

## See Also
<a name="API_MessageDeliveryStatusEventConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/MessageDeliveryStatusEventConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/MessageDeliveryStatusEventConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/MessageDeliveryStatusEventConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
