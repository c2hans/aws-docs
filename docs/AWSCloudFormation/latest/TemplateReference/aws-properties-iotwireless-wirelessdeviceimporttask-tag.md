---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotwireless-wirelessdeviceimporttask-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::WirelessDeviceImportTask Tag
<a name="aws-properties-iotwireless-wirelessdeviceimporttask-tag"></a>

The tags to attach to the wireless device. Tags are metadata that you can use to manage a resource.

## Syntax
<a name="aws-properties-iotwireless-wirelessdeviceimporttask-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotwireless-wirelessdeviceimporttask-tag-syntax.json"></a>

```
{
  "[Key](#cfn-iotwireless-wirelessdeviceimporttask-tag-key)" : {{String}},
  "[Value](#cfn-iotwireless-wirelessdeviceimporttask-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotwireless-wirelessdeviceimporttask-tag-syntax.yaml"></a>

```
  [Key](#cfn-iotwireless-wirelessdeviceimporttask-tag-key): {{String}}
  [Value](#cfn-iotwireless-wirelessdeviceimporttask-tag-value): {{String}}
```

## Properties
<a name="aws-properties-iotwireless-wirelessdeviceimporttask-tag-properties"></a>

`Key`  <a name="cfn-iotwireless-wirelessdeviceimporttask-tag-key"></a>
The tag's key value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-iotwireless-wirelessdeviceimporttask-tag-value"></a>
The tag's value.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
