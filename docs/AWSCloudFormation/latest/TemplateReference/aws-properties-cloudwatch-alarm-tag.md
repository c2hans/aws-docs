---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-alarm-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Alarm Tag
<a name="aws-properties-cloudwatch-alarm-tag"></a>

One of the key-value pairs associated with the alarm. Tags can help you organize and categorize your resources.

## Syntax
<a name="aws-properties-cloudwatch-alarm-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-alarm-tag-syntax.json"></a>

```
{
  "[Key](#cfn-cloudwatch-alarm-tag-key)" : {{String}},
  "[Value](#cfn-cloudwatch-alarm-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudwatch-alarm-tag-syntax.yaml"></a>

```
  [Key](#cfn-cloudwatch-alarm-tag-key): {{String}}
  [Value](#cfn-cloudwatch-alarm-tag-value): {{String}}
```

## Properties
<a name="aws-properties-cloudwatch-alarm-tag-properties"></a>

`Key`  <a name="cfn-cloudwatch-alarm-tag-key"></a>
A string that you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-cloudwatch-alarm-tag-value"></a>
The value for the specified tag key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
