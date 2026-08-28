---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotevents-alarmmodel-simplerule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTEvents::AlarmModel SimpleRule
<a name="aws-properties-iotevents-alarmmodel-simplerule"></a>

A rule that compares an input property value to a threshold value with a comparison operator.

## Syntax
<a name="aws-properties-iotevents-alarmmodel-simplerule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotevents-alarmmodel-simplerule-syntax.json"></a>

```
{
  "[ComparisonOperator](#cfn-iotevents-alarmmodel-simplerule-comparisonoperator)" : {{String}},
  "[InputProperty](#cfn-iotevents-alarmmodel-simplerule-inputproperty)" : {{String}},
  "[Threshold](#cfn-iotevents-alarmmodel-simplerule-threshold)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotevents-alarmmodel-simplerule-syntax.yaml"></a>

```
  [ComparisonOperator](#cfn-iotevents-alarmmodel-simplerule-comparisonoperator): {{String}}
  [InputProperty](#cfn-iotevents-alarmmodel-simplerule-inputproperty): {{String}}
  [Threshold](#cfn-iotevents-alarmmodel-simplerule-threshold): {{String}}
```

## Properties
<a name="aws-properties-iotevents-alarmmodel-simplerule-properties"></a>

`ComparisonOperator`  <a name="cfn-iotevents-alarmmodel-simplerule-comparisonoperator"></a>
The comparison operator.
*Required*: Yes
*Type*: String
*Allowed values*: `GREATER | GREATER_OR_EQUAL | LESS | LESS_OR_EQUAL | EQUAL | NOT_EQUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputProperty`  <a name="cfn-iotevents-alarmmodel-simplerule-inputproperty"></a>
The value on the left side of the comparison operator. You can specify an AWS IoT Events input attribute as an input property.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Threshold`  <a name="cfn-iotevents-alarmmodel-simplerule-threshold"></a>
The value on the right side of the comparison operator. You can enter a number or specify an AWS IoT Events input attribute.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
