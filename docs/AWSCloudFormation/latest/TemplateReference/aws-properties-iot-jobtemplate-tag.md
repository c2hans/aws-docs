---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-jobtemplate-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::JobTemplate Tag
<a name="aws-properties-iot-jobtemplate-tag"></a>

A set of key/value pairs that are used to manage the resource.

## Syntax
<a name="aws-properties-iot-jobtemplate-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-jobtemplate-tag-syntax.json"></a>

```
{
  "[Key](#cfn-iot-jobtemplate-tag-key)" : {{String}},
  "[Value](#cfn-iot-jobtemplate-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-jobtemplate-tag-syntax.yaml"></a>

```
  [Key](#cfn-iot-jobtemplate-tag-key): {{String}}
  [Value](#cfn-iot-jobtemplate-tag-value): {{String}}
```

## Properties
<a name="aws-properties-iot-jobtemplate-tag-properties"></a>

`Key`  <a name="cfn-iot-jobtemplate-tag-key"></a>
The tag's key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-iot-jobtemplate-tag-value"></a>
The tag's value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
