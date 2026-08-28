---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotevents-alarmmodel-alarmrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTEvents::AlarmModel AlarmRule
<a name="aws-properties-iotevents-alarmmodel-alarmrule"></a>

Defines when your alarm is invoked.

## Syntax
<a name="aws-properties-iotevents-alarmmodel-alarmrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotevents-alarmmodel-alarmrule-syntax.json"></a>

```
{
  "[SimpleRule](#cfn-iotevents-alarmmodel-alarmrule-simplerule)" : {{SimpleRule}}
}
```

### YAML
<a name="aws-properties-iotevents-alarmmodel-alarmrule-syntax.yaml"></a>

```
  [SimpleRule](#cfn-iotevents-alarmmodel-alarmrule-simplerule): {{
    SimpleRule}}
```

## Properties
<a name="aws-properties-iotevents-alarmmodel-alarmrule-properties"></a>

`SimpleRule`  <a name="cfn-iotevents-alarmmodel-alarmrule-simplerule"></a>
A rule that compares an input property value to a threshold value with a comparison operator.
*Required*: No
*Type*: [SimpleRule](aws-properties-iotevents-alarmmodel-simplerule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
