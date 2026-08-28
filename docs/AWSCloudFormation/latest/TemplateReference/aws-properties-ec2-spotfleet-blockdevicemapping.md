---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-blockdevicemapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SpotFleet BlockDeviceMapping
<a name="aws-properties-ec2-spotfleet-blockdevicemapping"></a>

Specifies a block device mapping.

You can specify `Ebs` or `VirtualName`, but not both.

## Syntax
<a name="aws-properties-ec2-spotfleet-blockdevicemapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-spotfleet-blockdevicemapping-syntax.json"></a>

```
{
  "[DeviceName](#cfn-ec2-spotfleet-blockdevicemapping-devicename)" : {{String}},
  "[Ebs](#cfn-ec2-spotfleet-blockdevicemapping-ebs)" : {{EbsBlockDevice}},
  "[NoDevice](#cfn-ec2-spotfleet-blockdevicemapping-nodevice)" : {{String}},
  "[VirtualName](#cfn-ec2-spotfleet-blockdevicemapping-virtualname)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-spotfleet-blockdevicemapping-syntax.yaml"></a>

```
  [DeviceName](#cfn-ec2-spotfleet-blockdevicemapping-devicename): {{String}}
  [Ebs](#cfn-ec2-spotfleet-blockdevicemapping-ebs): {{
    EbsBlockDevice}}
  [NoDevice](#cfn-ec2-spotfleet-blockdevicemapping-nodevice): {{String}}
  [VirtualName](#cfn-ec2-spotfleet-blockdevicemapping-virtualname): {{String}}
```

## Properties
<a name="aws-properties-ec2-spotfleet-blockdevicemapping-properties"></a>

`DeviceName`  <a name="cfn-ec2-spotfleet-blockdevicemapping-devicename"></a>
The device name. For available device names, see [Device names for volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html).
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ebs`  <a name="cfn-ec2-spotfleet-blockdevicemapping-ebs"></a>
Parameters used to automatically set up EBS volumes when the instance is launched.
*Required*: Conditional
*Type*: [EbsBlockDevice](aws-properties-ec2-spotfleet-ebsblockdevice.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NoDevice`  <a name="cfn-ec2-spotfleet-blockdevicemapping-nodevice"></a>
To omit the device from the block device mapping, specify an empty string. When this property is specified, the device is removed from the block device mapping regardless of the assigned value.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VirtualName`  <a name="cfn-ec2-spotfleet-blockdevicemapping-virtualname"></a>
The virtual device name (`ephemeral`N). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for `ephemeral0` and `ephemeral1`. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.
NVMe instance store volumes are automatically enumerated and assigned a device name. Including them in your block device mapping has no effect.
Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.
*Required*: Conditional
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
