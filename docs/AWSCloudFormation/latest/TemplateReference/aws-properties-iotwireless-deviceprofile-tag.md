---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotwireless-deviceprofile-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::DeviceProfile Tag
<a name="aws-properties-iotwireless-deviceprofile-tag"></a>

The tags to attach to the device profile. Tags are metadata that you can use to manage a resource.

## Syntax
<a name="aws-properties-iotwireless-deviceprofile-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotwireless-deviceprofile-tag-syntax.json"></a>

```
{
  "[Key](#cfn-iotwireless-deviceprofile-tag-key)" : {{String}},
  "[Value](#cfn-iotwireless-deviceprofile-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotwireless-deviceprofile-tag-syntax.yaml"></a>

```
  [Key](#cfn-iotwireless-deviceprofile-tag-key): {{String}}
  [Value](#cfn-iotwireless-deviceprofile-tag-value): {{String}}
```

## Properties
<a name="aws-properties-iotwireless-deviceprofile-tag-properties"></a>

`Key`  <a name="cfn-iotwireless-deviceprofile-tag-key"></a>
The tag's key value.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-iotwireless-deviceprofile-tag-value"></a>
The tag's value.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
