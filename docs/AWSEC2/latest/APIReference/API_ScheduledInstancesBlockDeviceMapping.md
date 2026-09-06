---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ScheduledInstancesBlockDeviceMapping.html
---

# ScheduledInstancesBlockDeviceMapping
<a name="API_ScheduledInstancesBlockDeviceMapping"></a>

Describes a block device mapping for a Scheduled Instance.

## Contents
<a name="API_ScheduledInstancesBlockDeviceMapping_Contents"></a>

 ** DeviceName **
The device name (for example, `/dev/sdh` or `xvdh`).
Type: String
Required: No

 ** Ebs **
Parameters used to set up EBS volumes automatically when the instance is launched.
Type: [ScheduledInstancesEbs](API_ScheduledInstancesEbs.md) object
Required: No

 ** NoDevice **
To omit the device from the block device mapping, specify an empty string.
Type: String
Required: No

 ** VirtualName **
The virtual device name (`ephemeral`N). Instance store volumes are numbered starting from 0. An instance type with two available instance store volumes can specify mappings for `ephemeral0` and `ephemeral1`. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.
Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.
Type: String
Required: No

## See Also
<a name="API_ScheduledInstancesBlockDeviceMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ScheduledInstancesBlockDeviceMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ScheduledInstancesBlockDeviceMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ScheduledInstancesBlockDeviceMapping)
