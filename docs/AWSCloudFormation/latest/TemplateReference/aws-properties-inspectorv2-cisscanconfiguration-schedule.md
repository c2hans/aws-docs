---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-cisscanconfiguration-schedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::CisScanConfiguration Schedule
<a name="aws-properties-inspectorv2-cisscanconfiguration-schedule"></a>

The schedule the CIS scan configuration runs on. Each CIS scan configuration has exactly one type of schedule.

## Syntax
<a name="aws-properties-inspectorv2-cisscanconfiguration-schedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-cisscanconfiguration-schedule-syntax.json"></a>

```
{
  "[Daily](#cfn-inspectorv2-cisscanconfiguration-schedule-daily)" : {{DailySchedule}},
  "[Monthly](#cfn-inspectorv2-cisscanconfiguration-schedule-monthly)" : {{MonthlySchedule}},
  "[OneTime](#cfn-inspectorv2-cisscanconfiguration-schedule-onetime)" : {{Json}},
  "[Weekly](#cfn-inspectorv2-cisscanconfiguration-schedule-weekly)" : {{WeeklySchedule}}
}
```

### YAML
<a name="aws-properties-inspectorv2-cisscanconfiguration-schedule-syntax.yaml"></a>

```
  [Daily](#cfn-inspectorv2-cisscanconfiguration-schedule-daily): {{
    DailySchedule}}
  [Monthly](#cfn-inspectorv2-cisscanconfiguration-schedule-monthly): {{
    MonthlySchedule}}
  [OneTime](#cfn-inspectorv2-cisscanconfiguration-schedule-onetime): {{Json}}
  [Weekly](#cfn-inspectorv2-cisscanconfiguration-schedule-weekly): {{
    WeeklySchedule}}
```

## Properties
<a name="aws-properties-inspectorv2-cisscanconfiguration-schedule-properties"></a>

`Daily`  <a name="cfn-inspectorv2-cisscanconfiguration-schedule-daily"></a>
A daily schedule.
*Required*: No
*Type*: [DailySchedule](aws-properties-inspectorv2-cisscanconfiguration-dailyschedule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Monthly`  <a name="cfn-inspectorv2-cisscanconfiguration-schedule-monthly"></a>
A monthly schedule.
*Required*: No
*Type*: [MonthlySchedule](aws-properties-inspectorv2-cisscanconfiguration-monthlyschedule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OneTime`  <a name="cfn-inspectorv2-cisscanconfiguration-schedule-onetime"></a>
A one time schedule.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weekly`  <a name="cfn-inspectorv2-cisscanconfiguration-schedule-weekly"></a>
A weekly schedule.
*Required*: No
*Type*: [WeeklySchedule](aws-properties-inspectorv2-cisscanconfiguration-weeklyschedule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
