---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudtrail-dashboard-refreshschedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudTrail::Dashboard RefreshSchedule
<a name="aws-properties-cloudtrail-dashboard-refreshschedule"></a>

 The schedule for a dashboard refresh.

## Syntax
<a name="aws-properties-cloudtrail-dashboard-refreshschedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudtrail-dashboard-refreshschedule-syntax.json"></a>

```
{
  "[Frequency](#cfn-cloudtrail-dashboard-refreshschedule-frequency)" : {{Frequency}},
  "[Status](#cfn-cloudtrail-dashboard-refreshschedule-status)" : {{String}},
  "[TimeOfDay](#cfn-cloudtrail-dashboard-refreshschedule-timeofday)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudtrail-dashboard-refreshschedule-syntax.yaml"></a>

```
  [Frequency](#cfn-cloudtrail-dashboard-refreshschedule-frequency): {{
    Frequency}}
  [Status](#cfn-cloudtrail-dashboard-refreshschedule-status): {{String}}
  [TimeOfDay](#cfn-cloudtrail-dashboard-refreshschedule-timeofday): {{String}}
```

## Properties
<a name="aws-properties-cloudtrail-dashboard-refreshschedule-properties"></a>

`Frequency`  <a name="cfn-cloudtrail-dashboard-refreshschedule-frequency"></a>
 The frequency at which you want the dashboard refreshed.
*Required*: No
*Type*: [Frequency](aws-properties-cloudtrail-dashboard-frequency.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-cloudtrail-dashboard-refreshschedule-status"></a>
 Specifies whether the refresh schedule is enabled. Set the value to `ENABLED` to enable the refresh schedule, or to `DISABLED` to turn off the refresh schedule.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeOfDay`  <a name="cfn-cloudtrail-dashboard-refreshschedule-timeofday"></a>
 The time of day in UTC to run the schedule; for hourly only refer to minutes; default is 00:00.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{2}:[0-9]{2}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
