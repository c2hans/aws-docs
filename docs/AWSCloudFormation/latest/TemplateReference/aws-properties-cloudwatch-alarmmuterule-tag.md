---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-alarmmuterule-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::AlarmMuteRule Tag
<a name="aws-properties-cloudwatch-alarmmuterule-tag"></a>

A key-value pair associated with a CloudWatch resource.

## Syntax
<a name="aws-properties-cloudwatch-alarmmuterule-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-alarmmuterule-tag-syntax.json"></a>

```
{
  "[Key](#cfn-cloudwatch-alarmmuterule-tag-key)" : {{String}},
  "[Value](#cfn-cloudwatch-alarmmuterule-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudwatch-alarmmuterule-tag-syntax.yaml"></a>

```
  [Key](#cfn-cloudwatch-alarmmuterule-tag-key): {{String}}
  [Value](#cfn-cloudwatch-alarmmuterule-tag-value): {{String}}
```

## Properties
<a name="aws-properties-cloudwatch-alarmmuterule-tag-properties"></a>

`Key`  <a name="cfn-cloudwatch-alarmmuterule-tag-key"></a>
A key-value pair associated with a CloudWatch resource.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-cloudwatch-alarmmuterule-tag-value"></a>
A key-value pair associated with a CloudWatch resource.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
