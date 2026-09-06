---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_DiscoveredDeviceSummary.html
---

# DiscoveredDeviceSummary
<a name="API_DiscoveredDeviceSummary"></a>

Structure containing summary information about a device discovered during a device discovery job.

## Contents
<a name="API_DiscoveredDeviceSummary_Contents"></a>

 ** AuthenticationMaterial **   <a name="managedintegrations-Type-DiscoveredDeviceSummary-AuthenticationMaterial"></a>
The authentication material required for connecting to the discovered device, such as credentials or tokens.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[0-9A-Za-z!#$%&()*\+\-;<=>?@^_`{|}~\/: {},\\"]+`
Required: No

 ** Brand **   <a name="managedintegrations-Type-DiscoveredDeviceSummary-Brand"></a>
The brand of the discovered device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

 ** ConnectorDeviceId **   <a name="managedintegrations-Type-DiscoveredDeviceSummary-ConnectorDeviceId"></a>
The third-party device identifier as defined by the connector. This identifier must not contain personal identifiable information (PII).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.,@-]+`
Required: No

 ** ConnectorDeviceName **   <a name="managedintegrations-Type-DiscoveredDeviceSummary-ConnectorDeviceName"></a>
The name of the device as defined by the connector or third-party system.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}\p{N} ._-]+`
Required: No

 ** DeviceTypes **   <a name="managedintegrations-Type-DiscoveredDeviceSummary-DeviceTypes"></a>
The list of device types or categories that the discovered device belongs to.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9=_. ,@\+\-/]+`
Required: No

 ** DiscoveredAt **   <a name="managedintegrations-Type-DiscoveredDeviceSummary-DiscoveredAt"></a>
The timestamp indicating when the device was discovered.
Type: Timestamp
Required: No

 ** ManagedThingId **   <a name="managedintegrations-Type-DiscoveredDeviceSummary-ManagedThingId"></a>
The identifier of the managed thing created for this discovered device, if one exists.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`
Required: No

 ** Model **   <a name="managedintegrations-Type-DiscoveredDeviceSummary-Model"></a>
The model of the discovered device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

 ** Modification **   <a name="managedintegrations-Type-DiscoveredDeviceSummary-Modification"></a>
The status of the discovered device, indicating whether it has been added, removed, or modified since the last discovery.
Type: String
Valid Values: `DISCOVERED | UPDATED | NO_CHANGE`
Required: No

## See Also
<a name="API_DiscoveredDeviceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/DiscoveredDeviceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/DiscoveredDeviceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/DiscoveredDeviceSummary)
