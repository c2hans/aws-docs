---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-alert-rule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Alert Rule
<a name="aws-properties-cloudwatch-alert-rule"></a>

Defines the schedule configuration for an alarm mute rule.

The rule contains a schedule that specifies when and how long alarms should be muted. The schedule can be a recurring pattern using cron expressions or a one-time mute window using at expressions.

## Syntax
<a name="aws-properties-cloudwatch-alert-rule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-alert-rule-syntax.json"></a>

```
{
  "[TelemetryRule](#cfn-cloudwatch-alert-rule-telemetryrule)" : {{TelemetryRule}}
}
```

### YAML
<a name="aws-properties-cloudwatch-alert-rule-syntax.yaml"></a>

```
  [TelemetryRule](#cfn-cloudwatch-alert-rule-telemetryrule): {{
    TelemetryRule}}
```

## Properties
<a name="aws-properties-cloudwatch-alert-rule-properties"></a>

`TelemetryRule`  <a name="cfn-cloudwatch-alert-rule-telemetryrule"></a>
Property description not available.
*Required*: Yes
*Type*: [TelemetryRule](aws-properties-cloudwatch-alert-telemetryrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
