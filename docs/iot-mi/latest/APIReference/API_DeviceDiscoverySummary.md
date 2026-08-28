---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_DeviceDiscoverySummary.html
---

# DeviceDiscoverySummary
<a name="API_DeviceDiscoverySummary"></a>

Structure containing summary information about a device discovery job, including its identifier, type, and status.

## Contents
<a name="API_DeviceDiscoverySummary_Contents"></a>

 ** DiscoveryType **   <a name="managedintegrations-Type-DeviceDiscoverySummary-DiscoveryType"></a>
The type of discovery process used to find devices.
Type: String
Valid Values: `ZWAVE | ZIGBEE | CLOUD | CUSTOM | CONTROLLER_CAPABILITY_REDISCOVERY`
Required: No

 ** Id **   <a name="managedintegrations-Type-DeviceDiscoverySummary-Id"></a>
The unique identifier of the device discovery job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[A-Za-z0-9]+`
Required: No

 ** Status **   <a name="managedintegrations-Type-DeviceDiscoverySummary-Status"></a>
The current status of the device discovery job.
Type: String
Valid Values: `RUNNING | SUCCEEDED | FAILED | TIMED_OUT`
Required: No

## See Also
<a name="API_DeviceDiscoverySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/DeviceDiscoverySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/DeviceDiscoverySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/DeviceDiscoverySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
