---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotwireless-fuotatask-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::FuotaTask Tag
<a name="aws-properties-iotwireless-fuotatask-tag"></a>

The tags to attach to the FUOTA task. Tags are metadata that you can use to manage a resource.

## Syntax
<a name="aws-properties-iotwireless-fuotatask-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotwireless-fuotatask-tag-syntax.json"></a>

```
{
  "[Key](#cfn-iotwireless-fuotatask-tag-key)" : {{String}},
  "[Value](#cfn-iotwireless-fuotatask-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotwireless-fuotatask-tag-syntax.yaml"></a>

```
  [Key](#cfn-iotwireless-fuotatask-tag-key): {{String}}
  [Value](#cfn-iotwireless-fuotatask-tag-value): {{String}}
```

## Properties
<a name="aws-properties-iotwireless-fuotatask-tag-properties"></a>

`Key`  <a name="cfn-iotwireless-fuotatask-tag-key"></a>
The tag's key value.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-iotwireless-fuotatask-tag-value"></a>
The tag's value.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
