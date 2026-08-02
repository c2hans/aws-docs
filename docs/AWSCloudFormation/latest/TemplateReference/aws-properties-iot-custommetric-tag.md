---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-custommetric-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::CustomMetric Tag
<a name="aws-properties-iot-custommetric-tag"></a>

A set of key/value pairs that are used to manage the resource.

## Syntax
<a name="aws-properties-iot-custommetric-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-custommetric-tag-syntax.json"></a>

```
{
  "[Key](#cfn-iot-custommetric-tag-key)" : {{String}},
  "[Value](#cfn-iot-custommetric-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-custommetric-tag-syntax.yaml"></a>

```
  [Key](#cfn-iot-custommetric-tag-key): {{String}}
  [Value](#cfn-iot-custommetric-tag-value): {{String}}
```

## Properties
<a name="aws-properties-iot-custommetric-tag-properties"></a>

`Key`  <a name="cfn-iot-custommetric-tag-key"></a>
The tag's key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-iot-custommetric-tag-value"></a>
The tag's value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
