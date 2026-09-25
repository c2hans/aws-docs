---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-monthlyschedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource MonthlySchedule
<a name="aws-properties-bedrock-datasource-monthlyschedule"></a>

A monthly sync on a specified day of the month.

## Syntax
<a name="aws-properties-bedrock-datasource-monthlyschedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-monthlyschedule-syntax.json"></a>

```
{
  "[DayOfMonth](#cfn-bedrock-datasource-monthlyschedule-dayofmonth)" : {{DayOfMonth}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-monthlyschedule-syntax.yaml"></a>

```
  [DayOfMonth](#cfn-bedrock-datasource-monthlyschedule-dayofmonth): {{
    DayOfMonth}}
```

## Properties
<a name="aws-properties-bedrock-datasource-monthlyschedule-properties"></a>

`DayOfMonth`  <a name="cfn-bedrock-datasource-monthlyschedule-dayofmonth"></a>
The day of the month on which the monthly sync runs.
*Required*: Yes
*Type*: [DayOfMonth](aws-properties-bedrock-datasource-dayofmonth.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
