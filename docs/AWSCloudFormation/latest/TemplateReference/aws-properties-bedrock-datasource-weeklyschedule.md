---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-weeklyschedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource WeeklySchedule
<a name="aws-properties-bedrock-datasource-weeklyschedule"></a>

A weekly sync on a specified day of the week.

## Syntax
<a name="aws-properties-bedrock-datasource-weeklyschedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-weeklyschedule-syntax.json"></a>

```
{
  "[DayOfWeek](#cfn-bedrock-datasource-weeklyschedule-dayofweek)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-weeklyschedule-syntax.yaml"></a>

```
  [DayOfWeek](#cfn-bedrock-datasource-weeklyschedule-dayofweek): {{String}}
```

## Properties
<a name="aws-properties-bedrock-datasource-weeklyschedule-properties"></a>

`DayOfWeek`  <a name="cfn-bedrock-datasource-weeklyschedule-dayofweek"></a>
The day of the week on which the weekly sync runs.
*Required*: Yes
*Type*: String
*Allowed values*: `SUNDAY | MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
