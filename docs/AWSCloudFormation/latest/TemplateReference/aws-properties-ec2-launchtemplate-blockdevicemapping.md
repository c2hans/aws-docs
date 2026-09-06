---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-launchtemplate-blockdevicemapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate BlockDeviceMapping
<a name="aws-properties-ec2-launchtemplate-blockdevicemapping"></a>

Specifies a block device mapping for a launch template. You must specify `DeviceName` plus exactly one of the following properties: `Ebs`, `NoDevice`, or `VirtualName`.

`BlockDeviceMapping` is a property of [ AWS::EC2::LaunchTemplate LaunchTemplateData](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html).

## Syntax
<a name="aws-properties-ec2-launchtemplate-blockdevicemapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-launchtemplate-blockdevicemapping-syntax.json"></a>

```
{
  "[DeviceName](#cfn-ec2-launchtemplate-blockdevicemapping-devicename)" : {{String}},
  "[Ebs](#cfn-ec2-launchtemplate-blockdevicemapping-ebs)" : {{Ebs}},
  "[NoDevice](#cfn-ec2-launchtemplate-blockdevicemapping-nodevice)" : {{String}},
  "[VirtualName](#cfn-ec2-launchtemplate-blockdevicemapping-virtualname)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-launchtemplate-blockdevicemapping-syntax.yaml"></a>

```
  [DeviceName](#cfn-ec2-launchtemplate-blockdevicemapping-devicename): {{String}}
  [Ebs](#cfn-ec2-launchtemplate-blockdevicemapping-ebs): {{
    Ebs}}
  [NoDevice](#cfn-ec2-launchtemplate-blockdevicemapping-nodevice): {{String}}
  [VirtualName](#cfn-ec2-launchtemplate-blockdevicemapping-virtualname): {{String}}
```

## Properties
<a name="aws-properties-ec2-launchtemplate-blockdevicemapping-properties"></a>

`DeviceName`  <a name="cfn-ec2-launchtemplate-blockdevicemapping-devicename"></a>
The device name (for example, /dev/sdh or xvdh).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ebs`  <a name="cfn-ec2-launchtemplate-blockdevicemapping-ebs"></a>
Parameters used to automatically set up EBS volumes when the instance is launched.
*Required*: No
*Type*: [Ebs](aws-properties-ec2-launchtemplate-ebs.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NoDevice`  <a name="cfn-ec2-launchtemplate-blockdevicemapping-nodevice"></a>
To omit the device from the block device mapping, specify an empty string.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VirtualName`  <a name="cfn-ec2-launchtemplate-blockdevicemapping-virtualname"></a>
The virtual device name (ephemeralN). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for ephemeral0 and ephemeral1. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ec2-launchtemplate-blockdevicemapping--seealso"></a>
+ [ Block device mappings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html) in the *Amazon EC2 User Guide*.
