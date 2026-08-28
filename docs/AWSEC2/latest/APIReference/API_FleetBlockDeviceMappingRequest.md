---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_FleetBlockDeviceMappingRequest.html
---

# FleetBlockDeviceMappingRequest
<a name="API_FleetBlockDeviceMappingRequest"></a>

Describes a block device mapping, which defines the EBS volumes and instance store volumes to attach to an instance at launch.

To override a block device mapping specified in the launch template:
+ Specify the exact same `DeviceName` here as specified in the launch template.
+ Only specify the parameters you want to change.
+ Any parameters you don't specify here will keep their original launch template values.

To add a new block device mapping:
+ Specify a `DeviceName` that doesn't exist in the launch template.
+ Specify all desired parameters here.

## Contents
<a name="API_FleetBlockDeviceMappingRequest_Contents"></a>

 ** DeviceName **
The device name (for example, `/dev/sdh` or `xvdh`).
Type: String
Required: No

 ** Ebs **
Parameters used to automatically set up EBS volumes when the instance is launched.
Type: [FleetEbsBlockDeviceRequest](API_FleetEbsBlockDeviceRequest.md) object
Required: No

 ** NoDevice **
To omit the device from the block device mapping, specify an empty string. When this property is specified, the device is removed from the block device mapping regardless of the assigned value.
Type: String
Required: No

 ** VirtualName **
The virtual device name (`ephemeralN`). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for `ephemeral0` and `ephemeral1`. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.
NVMe instance store volumes are automatically enumerated and assigned a device name. Including them in your block device mapping has no effect.
Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.
Type: String
Required: No

## See Also
<a name="API_FleetBlockDeviceMappingRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/FleetBlockDeviceMappingRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/FleetBlockDeviceMappingRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/FleetBlockDeviceMappingRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
