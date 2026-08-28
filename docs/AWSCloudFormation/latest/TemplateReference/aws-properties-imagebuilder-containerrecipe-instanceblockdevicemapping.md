---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::ContainerRecipe InstanceBlockDeviceMapping
<a name="aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping"></a>

Defines block device mappings for the instance used to configure your image.

## Syntax
<a name="aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping-syntax.json"></a>

```
{
  "[DeviceName](#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-devicename)" : {{String}},
  "[Ebs](#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-ebs)" : {{EbsInstanceBlockDeviceSpecification}},
  "[NoDevice](#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-nodevice)" : {{String}},
  "[VirtualName](#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-virtualname)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping-syntax.yaml"></a>

```
  [DeviceName](#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-devicename): {{String}}
  [Ebs](#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-ebs): {{
    EbsInstanceBlockDeviceSpecification}}
  [NoDevice](#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-nodevice): {{String}}
  [VirtualName](#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-virtualname): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping-properties"></a>

`DeviceName`  <a name="cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-devicename"></a>
The device to which these mappings apply.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ebs`  <a name="cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-ebs"></a>
Use to manage Amazon EBS-specific configuration for this mapping.
*Required*: No
*Type*: [EbsInstanceBlockDeviceSpecification](aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NoDevice`  <a name="cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-nodevice"></a>
Use to remove a mapping from the base image.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `0`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VirtualName`  <a name="cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-virtualname"></a>
Use to manage instance ephemeral devices.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
