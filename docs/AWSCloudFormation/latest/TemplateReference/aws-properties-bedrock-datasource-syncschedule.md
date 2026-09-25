---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-syncschedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource SyncSchedule
<a name="aws-properties-bedrock-datasource-syncschedule"></a>

The recurring schedule on which a managed knowledge base connector automatically syncs its data source. Specify exactly one of `daily`, `weekly`, or `monthly`.

## Syntax
<a name="aws-properties-bedrock-datasource-syncschedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-syncschedule-syntax.json"></a>

```
{
  "[Daily](#cfn-bedrock-datasource-syncschedule-daily)" : {{Json}},
  "[Monthly](#cfn-bedrock-datasource-syncschedule-monthly)" : {{MonthlySchedule}},
  "[Weekly](#cfn-bedrock-datasource-syncschedule-weekly)" : {{WeeklySchedule}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-syncschedule-syntax.yaml"></a>

```
  [Daily](#cfn-bedrock-datasource-syncschedule-daily): {{Json}}
  [Monthly](#cfn-bedrock-datasource-syncschedule-monthly): {{
    MonthlySchedule}}
  [Weekly](#cfn-bedrock-datasource-syncschedule-weekly): {{
    WeeklySchedule}}
```

## Properties
<a name="aws-properties-bedrock-datasource-syncschedule-properties"></a>

`Daily`  <a name="cfn-bedrock-datasource-syncschedule-daily"></a>
A daily sync that runs once a day at a system-chosen off-peak time. The run time is not configurable.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Monthly`  <a name="cfn-bedrock-datasource-syncschedule-monthly"></a>
A monthly sync that runs once a month on the specified day of the month.
*Required*: No
*Type*: [MonthlySchedule](aws-properties-bedrock-datasource-monthlyschedule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weekly`  <a name="cfn-bedrock-datasource-syncschedule-weekly"></a>
A weekly sync that runs once a week on the specified day of the week.
*Required*: No
*Type*: [WeeklySchedule](aws-properties-bedrock-datasource-weeklyschedule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
