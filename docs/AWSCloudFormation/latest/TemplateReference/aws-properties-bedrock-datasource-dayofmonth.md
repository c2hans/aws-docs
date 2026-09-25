---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-dayofmonth.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource DayOfMonth
<a name="aws-properties-bedrock-datasource-dayofmonth"></a>

The day of the month on which a monthly sync runs. Specify exactly one of `dayNumber` or `lastDayOfMonth`.

## Syntax
<a name="aws-properties-bedrock-datasource-dayofmonth-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-dayofmonth-syntax.json"></a>

```
{
  "[DayNumber](#cfn-bedrock-datasource-dayofmonth-daynumber)" : {{Integer}},
  "[LastDayOfMonth](#cfn-bedrock-datasource-dayofmonth-lastdayofmonth)" : {{Json}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-dayofmonth-syntax.yaml"></a>

```
  [DayNumber](#cfn-bedrock-datasource-dayofmonth-daynumber): {{Integer}}
  [LastDayOfMonth](#cfn-bedrock-datasource-dayofmonth-lastdayofmonth): {{Json}}
```

## Properties
<a name="aws-properties-bedrock-datasource-dayofmonth-properties"></a>

`DayNumber`  <a name="cfn-bedrock-datasource-dayofmonth-daynumber"></a>
A specific day of the month, from 1 to 28. Values are capped at 28, so a monthly sync runs in every month, including February.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `28`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LastDayOfMonth`  <a name="cfn-bedrock-datasource-dayofmonth-lastdayofmonth"></a>
Set this option to run the monthly sync on the last calendar day of each month.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
