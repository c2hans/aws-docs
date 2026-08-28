---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_SidewalkDeviceMetadata.html
---

# SidewalkDeviceMetadata
<a name="API_SidewalkDeviceMetadata"></a>

MetaData for Sidewalk device.

## Contents
<a name="API_SidewalkDeviceMetadata_Contents"></a>

 ** BatteryLevel **   <a name="iotwireless-Type-SidewalkDeviceMetadata-BatteryLevel"></a>
Sidewalk device battery level.
Type: String
Valid Values: `normal | low | critical`
Required: No

 ** DeviceState **   <a name="iotwireless-Type-SidewalkDeviceMetadata-DeviceState"></a>
Device state defines the device status of sidewalk device.
Type: String
Valid Values: `Provisioned | RegisteredNotSeen | RegisteredReachable | RegisteredUnreachable`
Required: No

 ** Event **   <a name="iotwireless-Type-SidewalkDeviceMetadata-Event"></a>
Sidewalk device status notification.
Type: String
Valid Values: `discovered | lost | ack | nack | passthrough`
Required: No

 ** Rssi **   <a name="iotwireless-Type-SidewalkDeviceMetadata-Rssi"></a>
The RSSI value.
Type: Integer
Required: No

## See Also
<a name="API_SidewalkDeviceMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/SidewalkDeviceMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/SidewalkDeviceMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/SidewalkDeviceMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
