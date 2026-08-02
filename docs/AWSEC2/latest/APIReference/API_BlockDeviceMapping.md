---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BlockDeviceMapping.html
---

# BlockDeviceMapping
<a name="API_BlockDeviceMapping"></a>

Describes a block device mapping, which defines the EBS volumes and instance store volumes to attach to an instance at launch.

## Contents
<a name="API_BlockDeviceMapping_Contents"></a>

 ** DeviceName ** (request), ** deviceName ** (response)
The device name. For available device names, see [Device names for volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html).
Type: String
Required: No

 ** Ebs ** (request), ** ebs ** (response)
Parameters used to automatically set up EBS volumes when the instance is launched.
Type: [EbsBlockDevice](API_EbsBlockDevice.md) object
Required: No

 ** NoDevice ** (request), ** noDevice ** (response)
To omit the device from the block device mapping, specify an empty string. When this property is specified, the device is removed from the block device mapping regardless of the assigned value.
Type: String
Required: No

 ** VirtualName ** (request), ** virtualName ** (response)
The virtual device name (`ephemeral`N). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for `ephemeral0` and `ephemeral1`. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.
NVMe instance store volumes are automatically enumerated and assigned a device name. Including them in your block device mapping has no effect.
Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.
Type: String
Required: No

## See Also
<a name="API_BlockDeviceMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/BlockDeviceMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/BlockDeviceMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/BlockDeviceMapping)
