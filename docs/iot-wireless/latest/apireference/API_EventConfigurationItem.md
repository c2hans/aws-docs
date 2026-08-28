---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_EventConfigurationItem.html
---

# EventConfigurationItem
<a name="API_EventConfigurationItem"></a>

Event configuration object for a single resource.

## Contents
<a name="API_EventConfigurationItem_Contents"></a>

 ** Events **   <a name="iotwireless-Type-EventConfigurationItem-Events"></a>
Object of all event configurations and the status of the event topics.
Type: [EventNotificationItemConfigurations](API_EventNotificationItemConfigurations.md) object
Required: No

 ** Identifier **   <a name="iotwireless-Type-EventConfigurationItem-Identifier"></a>
Resource identifier opted in for event messaging.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** IdentifierType **   <a name="iotwireless-Type-EventConfigurationItem-IdentifierType"></a>
Identifier type of the particular resource identifier for event configuration.
Type: String
Valid Values: `PartnerAccountId | DevEui | GatewayEui | WirelessDeviceId | WirelessGatewayId`
Required: No

 ** PartnerType **   <a name="iotwireless-Type-EventConfigurationItem-PartnerType"></a>
Partner type of the resource if the identifier type is PartnerAccountId.
Type: String
Valid Values: `Sidewalk`
Required: No

## See Also
<a name="API_EventConfigurationItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/EventConfigurationItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/EventConfigurationItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/EventConfigurationItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
