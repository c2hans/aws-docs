---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_NotificationConfigurationSummary.html
---

# NotificationConfigurationSummary
<a name="API_NotificationConfigurationSummary"></a>

Structure describing a notification configuration.

## Contents
<a name="API_NotificationConfigurationSummary_Contents"></a>

 ** DestinationName **   <a name="managedintegrations-Type-NotificationConfigurationSummary-DestinationName"></a>
The name of the destination for the notification configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{N} ._-]+`
Required: No

 ** EventType **   <a name="managedintegrations-Type-NotificationConfigurationSummary-EventType"></a>
The type of event triggering a device notification to the customer-managed destination.
Type: String
Valid Values: `DEVICE_COMMAND | DEVICE_COMMAND_REQUEST | DEVICE_DISCOVERY_STATUS | DEVICE_EVENT | DEVICE_LIFE_CYCLE | DEVICE_STATE | DEVICE_OTA | DEVICE_WSS | CONNECTOR_ASSOCIATION | ACCOUNT_ASSOCIATION | CONNECTOR_ERROR_REPORT`
Required: No

## See Also
<a name="API_NotificationConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/NotificationConfigurationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/NotificationConfigurationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/NotificationConfigurationSummary)
