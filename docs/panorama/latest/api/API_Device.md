---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_Device.html
---

# Device
<a name="API_Device"></a>

A device.

## Contents
<a name="API_Device_Contents"></a>

 ** Brand **   <a name="panorama-Type-Device-Brand"></a>
The device's maker.
Type: String
Valid Values: `AWS_PANORAMA | LENOVO`
Required: No

 ** CreatedTime **   <a name="panorama-Type-Device-CreatedTime"></a>
When the device was created.
Type: Timestamp
Required: No

 ** CurrentSoftware **   <a name="panorama-Type-Device-CurrentSoftware"></a>
A device's current software.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Description **   <a name="panorama-Type-Device-Description"></a>
A description for the device.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

 ** DeviceAggregatedStatus **   <a name="panorama-Type-Device-DeviceAggregatedStatus"></a>
A device's aggregated status. Including the device's connection status, provisioning status, and lease status.
Type: String
Valid Values: `ERROR | AWAITING_PROVISIONING | PENDING | FAILED | DELETING | ONLINE | OFFLINE | LEASE_EXPIRED | UPDATE_NEEDED | REBOOTING`
Required: No

 ** DeviceId **   <a name="panorama-Type-Device-DeviceId"></a>
The device's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: No

 ** LastUpdatedTime **   <a name="panorama-Type-Device-LastUpdatedTime"></a>
When the device was updated.
Type: Timestamp
Required: No

 ** LatestDeviceJob **   <a name="panorama-Type-Device-LatestDeviceJob"></a>
A device's latest job. Includes the target image version, and the update job status.
Type: [LatestDeviceJob](API_LatestDeviceJob.md) object
Required: No

 ** LeaseExpirationTime **   <a name="panorama-Type-Device-LeaseExpirationTime"></a>
The device's lease expiration time.
Type: Timestamp
Required: No

 ** Name **   <a name="panorama-Type-Device-Name"></a>
The device's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: No

 ** ProvisioningStatus **   <a name="panorama-Type-Device-ProvisioningStatus"></a>
The device's provisioning status.
Type: String
Valid Values: `AWAITING_PROVISIONING | PENDING | SUCCEEDED | FAILED | ERROR | DELETING`
Required: No

 ** Tags **   <a name="panorama-Type-Device-Tags"></a>
The device's tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `.+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*`
Required: No

 ** Type **   <a name="panorama-Type-Device-Type"></a>
The device's type.
Type: String
Valid Values: `PANORAMA_APPLIANCE_DEVELOPER_KIT | PANORAMA_APPLIANCE`
Required: No

## See Also
<a name="API_Device_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/Device)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/Device)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/Device)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
