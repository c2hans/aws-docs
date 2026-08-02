---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotwireless-destination-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::Destination Tag
<a name="aws-properties-iotwireless-destination-tag"></a>

The tags to attach to the destination. Tags are metadata that you can use to manage a resource.

## Syntax
<a name="aws-properties-iotwireless-destination-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotwireless-destination-tag-syntax.json"></a>

```
{
  "[Key](#cfn-iotwireless-destination-tag-key)" : {{String}},
  "[Value](#cfn-iotwireless-destination-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotwireless-destination-tag-syntax.yaml"></a>

```
  [Key](#cfn-iotwireless-destination-tag-key): {{String}}
  [Value](#cfn-iotwireless-destination-tag-value): {{String}}
```

## Properties
<a name="aws-properties-iotwireless-destination-tag-properties"></a>

`Key`  <a name="cfn-iotwireless-destination-tag-key"></a>
The tag's key value.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-iotwireless-destination-tag-value"></a>
The tag's value.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
