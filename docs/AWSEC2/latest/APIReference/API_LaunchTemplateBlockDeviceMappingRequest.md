---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateBlockDeviceMappingRequest.html
---

# LaunchTemplateBlockDeviceMappingRequest
<a name="API_LaunchTemplateBlockDeviceMappingRequest"></a>

Describes a block device mapping.

## Contents
<a name="API_LaunchTemplateBlockDeviceMappingRequest_Contents"></a>

 ** DeviceName **
The device name (for example, /dev/sdh or xvdh).
Type: String
Required: No

 ** Ebs **
Parameters used to automatically set up EBS volumes when the instance is launched.
Type: [LaunchTemplateEbsBlockDeviceRequest](API_LaunchTemplateEbsBlockDeviceRequest.md) object
Required: No

 ** NoDevice **
To omit the device from the block device mapping, specify an empty string.
Type: String
Required: No

 ** VirtualName **
The virtual device name (ephemeralN). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for ephemeral0 and ephemeral1. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.
Type: String
Required: No

## See Also
<a name="API_LaunchTemplateBlockDeviceMappingRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LaunchTemplateBlockDeviceMappingRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LaunchTemplateBlockDeviceMappingRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LaunchTemplateBlockDeviceMappingRequest)
