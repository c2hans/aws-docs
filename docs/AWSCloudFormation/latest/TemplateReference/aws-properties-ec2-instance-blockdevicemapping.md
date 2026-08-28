---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instance-blockdevicemapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::Instance BlockDeviceMapping
<a name="aws-properties-ec2-instance-blockdevicemapping"></a>

Specifies a block device mapping for an instance. You must specify exactly one of the following properties: `VirtualName`, `Ebs`, or `NoDevice`.

`BlockDeviceMapping` is a property of the [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html) resource.

**Important**
After the instance is running, you can modify only the `DeleteOnTermination` parameter for the attached volumes without interrupting the instance. Modifying any other parameter results in instance [ replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement).

## Syntax
<a name="aws-properties-ec2-instance-blockdevicemapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-instance-blockdevicemapping-syntax.json"></a>

```
{
  "[DeviceName](#cfn-ec2-instance-blockdevicemapping-devicename)" : {{String}},
  "[Ebs](#cfn-ec2-instance-blockdevicemapping-ebs)" : {{Ebs}},
  "[NoDevice](#cfn-ec2-instance-blockdevicemapping-nodevice)" : {{Json}},
  "[VirtualName](#cfn-ec2-instance-blockdevicemapping-virtualname)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-instance-blockdevicemapping-syntax.yaml"></a>

```
  [DeviceName](#cfn-ec2-instance-blockdevicemapping-devicename): {{String}}
  [Ebs](#cfn-ec2-instance-blockdevicemapping-ebs): {{
    Ebs}}
  [NoDevice](#cfn-ec2-instance-blockdevicemapping-nodevice): {{Json}}
  [VirtualName](#cfn-ec2-instance-blockdevicemapping-virtualname): {{String}}
```

## Properties
<a name="aws-properties-ec2-instance-blockdevicemapping-properties"></a>

`DeviceName`  <a name="cfn-ec2-instance-blockdevicemapping-devicename"></a>
The device name. For available device names, see [Device names for volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html).
After the instance is running, this parameter is used to specify the device name of the block device mapping to update.
*Required*: Yes
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Ebs`  <a name="cfn-ec2-instance-blockdevicemapping-ebs"></a>
Parameters used to automatically set up EBS volumes when the instance is launched.
After the instance is running, you can modify only the `DeleteOnTermination` parameter for the attached volumes without interrupting the instance. Modifying any other parameter results in instance [ replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt).
*Required*: Conditional
*Type*: [Ebs](aws-properties-ec2-instance-ebs.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`NoDevice`  <a name="cfn-ec2-instance-blockdevicemapping-nodevice"></a>
To omit the device from the block device mapping, specify an empty string.
After the instance is running, modifying this parameter results in instance [ replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement).
*Required*: Conditional
*Type*: Json
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`VirtualName`  <a name="cfn-ec2-instance-blockdevicemapping-virtualname"></a>
The virtual device name (`ephemeral`N). The name must be in the form `ephemeral`*X* where *X* is a number starting from zero (0). For example, an instance type with 2 available instance store volumes can specify mappings for `ephemeral0` and `ephemeral1`. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.
NVMe instance store volumes are automatically enumerated and assigned a device name. Including them in your block device mapping has no effect.
*Constraints*: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.
After the instance is running, modifying this parameter results in instance [ replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement).
*Required*: Conditional
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## Examples
<a name="aws-properties-ec2-instance-blockdevicemapping--examples"></a>

**Topics**
+ [Block device mapping with two EBS volumes](#aws-properties-ec2-instance-blockdevicemapping--examples--Block_device_mapping_with_two_EBS_volumes)
+ [Unmap an AMI-defined device](#aws-properties-ec2-instance-blockdevicemapping--examples--Unmap_an_AMI-defined_device)

### Block device mapping with two EBS volumes
<a name="aws-properties-ec2-instance-blockdevicemapping--examples--Block_device_mapping_with_two_EBS_volumes"></a>

This example sets the size of an EBS-backed root device to 50 GiB and adds another EBS volume that is 100 GiB in size. The supported device names depend on the AMI for the instance. The volume names in this example are supported for Nitro-based Windows instances.

#### JSON
<a name="aws-properties-ec2-instance-blockdevicemapping--examples--Block_device_mapping_with_two_EBS_volumes--json"></a>

```
"BlockDeviceMappings" : [
   {
      "DeviceName" : "/dev/sda1",
      "Ebs" : { "VolumeSize" : "50" }
   },
   {
      "DeviceName" : "xvdbm",
      "Ebs" : { "VolumeSize" : "100" }
   }
]
```

#### YAML
<a name="aws-properties-ec2-instance-blockdevicemapping--examples--Block_device_mapping_with_two_EBS_volumes--yaml"></a>

```
BlockDeviceMappings:
  - DeviceName: /dev/sda1
    Ebs:
      VolumeSize: 50
  - DeviceName: xvdbm
    Ebs:
      VolumeSize: 100
```

### Unmap an AMI-defined device
<a name="aws-properties-ec2-instance-blockdevicemapping--examples--Unmap_an_AMI-defined_device"></a>

To unmap a device defined in the AMI, set the `NoDevice` property to an empty map, as shown here:

#### JSON
<a name="aws-properties-ec2-instance-blockdevicemapping--examples--Unmap_an_AMI-defined_device--json"></a>

```
"BlockDeviceMappings" : [
   {
      "DeviceName":"/dev/sde",
      "NoDevice": {}
   }
]
```

#### YAML
<a name="aws-properties-ec2-instance-blockdevicemapping--examples--Unmap_an_AMI-defined_device--yaml"></a>

```
BlockDeviceMappings:
  - DeviceName: /dev/sde
    NoDevice: {}
```

## See also
<a name="aws-properties-ec2-instance-blockdevicemapping--seealso"></a>
+ [ Block device mappings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html) in the *Amazon EC2 User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
