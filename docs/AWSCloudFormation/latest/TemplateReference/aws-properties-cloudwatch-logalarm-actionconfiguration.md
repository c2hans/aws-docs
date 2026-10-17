---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-logalarm-actionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::LogAlarm ActionConfiguration
<a name="aws-properties-cloudwatch-logalarm-actionconfiguration"></a>

Settings that change the content of the notifications and events that the alarm sends when its state changes.

## Syntax
<a name="aws-properties-cloudwatch-logalarm-actionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-logalarm-actionconfiguration-syntax.json"></a>

```
{
  "[AlarmTagsPropagation](#cfn-cloudwatch-logalarm-actionconfiguration-alarmtagspropagation)" : {{AlarmTagsPropagation}}
}
```

### YAML
<a name="aws-properties-cloudwatch-logalarm-actionconfiguration-syntax.yaml"></a>

```
  [AlarmTagsPropagation](#cfn-cloudwatch-logalarm-actionconfiguration-alarmtagspropagation): {{
    AlarmTagsPropagation}}
```

## Properties
<a name="aws-properties-cloudwatch-logalarm-actionconfiguration-properties"></a>

`AlarmTagsPropagation`  <a name="cfn-cloudwatch-logalarm-actionconfiguration-alarmtagspropagation"></a>
Settings for including the alarm's tags in its action notifications and state-change events.
*Required*: No
*Type*: [AlarmTagsPropagation](aws-properties-cloudwatch-logalarm-alarmtagspropagation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
