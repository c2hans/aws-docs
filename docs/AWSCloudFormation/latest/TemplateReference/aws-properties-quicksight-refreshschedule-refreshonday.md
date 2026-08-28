---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-refreshschedule-refreshonday.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::RefreshSchedule RefreshOnDay
<a name="aws-properties-quicksight-refreshschedule-refreshonday"></a>

The day that you want yout dataset to refresh.

## Syntax
<a name="aws-properties-quicksight-refreshschedule-refreshonday-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-refreshschedule-refreshonday-syntax.json"></a>

```
{
  "[DayOfMonth](#cfn-quicksight-refreshschedule-refreshonday-dayofmonth)" : {{String}},
  "[DayOfWeek](#cfn-quicksight-refreshschedule-refreshonday-dayofweek)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-refreshschedule-refreshonday-syntax.yaml"></a>

```
  [DayOfMonth](#cfn-quicksight-refreshschedule-refreshonday-dayofmonth): {{String}}
  [DayOfWeek](#cfn-quicksight-refreshschedule-refreshonday-dayofweek): {{String}}
```

## Properties
<a name="aws-properties-quicksight-refreshschedule-refreshonday-properties"></a>

`DayOfMonth`  <a name="cfn-quicksight-refreshschedule-refreshonday-dayofmonth"></a>
The day of the month that you want your dataset to refresh. This value is required for monthly refresh intervals.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DayOfWeek`  <a name="cfn-quicksight-refreshschedule-refreshonday-dayofweek"></a>
The day of the week that you want to schedule the refresh on. This value is required for weekly and monthly refresh intervals.
*Required*: No
*Type*: String
*Allowed values*: `SUNDAY | MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
