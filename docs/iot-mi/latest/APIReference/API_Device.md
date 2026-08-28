---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_Device.html
---

# Device
<a name="API_Device"></a>

Describe the device using the relevant metadata and supported clusters for device discovery.

## Contents
<a name="API_Device_Contents"></a>

 ** CapabilityReport **   <a name="managedintegrations-Type-Device-CapabilityReport"></a>
The capability report for the device.
Type: [MatterCapabilityReport](API_MatterCapabilityReport.md) object
Required: Yes

 ** ConnectorDeviceId **   <a name="managedintegrations-Type-Device-ConnectorDeviceId"></a>
The device id as defined by the connector.
This parameter is used for cloud-to-cloud devices only.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.,@-]+`
Required: Yes

 ** CapabilitySchemas **   <a name="managedintegrations-Type-Device-CapabilitySchemas"></a>
Report of all capabilities supported by the device.
Type: Array of [CapabilitySchemaItem](API_CapabilitySchemaItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 40 items.
Required: No

 ** ConnectorDeviceName **   <a name="managedintegrations-Type-Device-ConnectorDeviceName"></a>
The name of the device as defined by the connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}\p{N} ._-]+`
Required: No

 ** DeviceMetadata **   <a name="managedintegrations-Type-Device-DeviceMetadata"></a>
The metadata attributes for a device.
Type: JSON value
Required: No

## See Also
<a name="API_Device_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/Device)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/Device)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/Device)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
