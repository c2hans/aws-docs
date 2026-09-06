---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-ec2fleet-blockdevicemapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::EC2Fleet BlockDeviceMapping
<a name="aws-properties-ec2-ec2fleet-blockdevicemapping"></a>

Describes a block device mapping, which defines the EBS volumes and instance store volumes to attach to an instance at launch.

## Syntax
<a name="aws-properties-ec2-ec2fleet-blockdevicemapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-ec2fleet-blockdevicemapping-syntax.json"></a>

```
{
  "[DeviceName](#cfn-ec2-ec2fleet-blockdevicemapping-devicename)" : {{String}},
  "[Ebs](#cfn-ec2-ec2fleet-blockdevicemapping-ebs)" : {{EbsBlockDevice}},
  "[NoDevice](#cfn-ec2-ec2fleet-blockdevicemapping-nodevice)" : {{String}},
  "[VirtualName](#cfn-ec2-ec2fleet-blockdevicemapping-virtualname)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-ec2fleet-blockdevicemapping-syntax.yaml"></a>

```
  [DeviceName](#cfn-ec2-ec2fleet-blockdevicemapping-devicename): {{String}}
  [Ebs](#cfn-ec2-ec2fleet-blockdevicemapping-ebs): {{
    EbsBlockDevice}}
  [NoDevice](#cfn-ec2-ec2fleet-blockdevicemapping-nodevice): {{String}}
  [VirtualName](#cfn-ec2-ec2fleet-blockdevicemapping-virtualname): {{String}}
```

## Properties
<a name="aws-properties-ec2-ec2fleet-blockdevicemapping-properties"></a>

`DeviceName`  <a name="cfn-ec2-ec2fleet-blockdevicemapping-devicename"></a>
The device name. For available device names, see [Device names for volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html).
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ebs`  <a name="cfn-ec2-ec2fleet-blockdevicemapping-ebs"></a>
Parameters used to automatically set up EBS volumes when the instance is launched.
*Required*: No
*Type*: [EbsBlockDevice](aws-properties-ec2-ec2fleet-ebsblockdevice.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NoDevice`  <a name="cfn-ec2-ec2fleet-blockdevicemapping-nodevice"></a>
To omit the device from the block device mapping, specify an empty string. When this property is specified, the device is removed from the block device mapping regardless of the assigned value.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VirtualName`  <a name="cfn-ec2-ec2fleet-blockdevicemapping-virtualname"></a>
The virtual device name (`ephemeral`N). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for `ephemeral0` and `ephemeral1`. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.
NVMe instance store volumes are automatically enumerated and assigned a device name. Including them in your block device mapping has no effect.
Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
