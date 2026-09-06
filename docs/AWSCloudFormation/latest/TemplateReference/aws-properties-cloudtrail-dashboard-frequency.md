---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudtrail-dashboard-frequency.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudTrail::Dashboard Frequency
<a name="aws-properties-cloudtrail-dashboard-frequency"></a>

 Specifies the frequency for a dashboard refresh schedule.

 For a custom dashboard, you can schedule a refresh for every 1, 6, 12, or 24 hours, or every day.

## Syntax
<a name="aws-properties-cloudtrail-dashboard-frequency-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudtrail-dashboard-frequency-syntax.json"></a>

```
{
  "[Unit](#cfn-cloudtrail-dashboard-frequency-unit)" : {{String}},
  "[Value](#cfn-cloudtrail-dashboard-frequency-value)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-cloudtrail-dashboard-frequency-syntax.yaml"></a>

```
  [Unit](#cfn-cloudtrail-dashboard-frequency-unit): {{String}}
  [Value](#cfn-cloudtrail-dashboard-frequency-value): {{Integer}}
```

## Properties
<a name="aws-properties-cloudtrail-dashboard-frequency-properties"></a>

`Unit`  <a name="cfn-cloudtrail-dashboard-frequency-unit"></a>
 The unit to use for the refresh.
For custom dashboards, the unit can be `HOURS` or `DAYS`.
For the Highlights dashboard, the `Unit` must be `HOURS`.
*Required*: Yes
*Type*: String
*Allowed values*: `HOURS | DAYS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-cloudtrail-dashboard-frequency-value"></a>
 The value for the refresh schedule.
 For custom dashboards, the following values are valid when the unit is `HOURS`: `1`, `6`, `12`, `24`
For custom dashboards, the only valid value when the unit is `DAYS` is `1`.
For the Highlights dashboard, the `Value` must be `6`.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
