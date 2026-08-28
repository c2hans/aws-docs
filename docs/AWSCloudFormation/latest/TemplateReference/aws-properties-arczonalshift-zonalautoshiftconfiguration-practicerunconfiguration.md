---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCZonalShift::ZonalAutoshiftConfiguration PracticeRunConfiguration
<a name="aws-properties-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration"></a>

A practice run configuration for a resource includes the Amazon CloudWatch alarms that you've specified for a practice run, as well as any blocked dates or blocked windows for the practice run.

When a resource has a practice run configuation, ARC starts weekly zonal shifts for the resource, to shift traffic away from an Availability Zone. Weekly practice runs help you to make sure that your application can continue to operate normally with the loss of one Availability Zone.

You can update or delete a practice run configuration. When you delete a practice run configuration, zonal autoshift is disabled for the resource. A practice run configuration is required when zonal autoshift is enabled.

## Syntax
<a name="aws-properties-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-syntax.json"></a>

```
{
  "[BlockedDates](#cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-blockeddates)" : {{[ String, ... ]}},
  "[BlockedWindows](#cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-blockedwindows)" : {{[ String, ... ]}},
  "[BlockingAlarms](#cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-blockingalarms)" : {{[ ControlCondition, ... ]}},
  "[OutcomeAlarms](#cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-outcomealarms)" : {{[ ControlCondition, ... ]}}
}
```

### YAML
<a name="aws-properties-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-syntax.yaml"></a>

```
  [BlockedDates](#cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-blockeddates): {{
    - String}}
  [BlockedWindows](#cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-blockedwindows): {{
    - String}}
  [BlockingAlarms](#cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-blockingalarms): {{
    - ControlCondition}}
  [OutcomeAlarms](#cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-outcomealarms): {{
    - ControlCondition}}
```

## Properties
<a name="aws-properties-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-properties"></a>

`BlockedDates`  <a name="cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-blockeddates"></a>
An array of one or more dates that you can specify when AWS does not start practice runs for a resource. Dates are in UTC.
Specify blocked dates in the format `YYYY-MM-DD`, separated by spaces.
*Required*: No
*Type*: Array of String
*Minimum*: `10 | 0`
*Maximum*: `10 | 15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BlockedWindows`  <a name="cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-blockedwindows"></a>
An array of one or more days and times that you can specify when ARC does not start practice runs for a resource. Days and times are in UTC.
Specify blocked windows in the format `DAY:HH:MM-DAY:HH:MM`, separated by spaces. For example, `MON:18:30-MON:19:30 TUE:18:30-TUE:19:30`.
Blocked windows have to start and end on the same day. Windows that span multiple days aren't supported.
*Required*: No
*Type*: Array of String
*Minimum*: `19 | 0`
*Maximum*: `19 | 15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BlockingAlarms`  <a name="cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-blockingalarms"></a>
An optional alarm that you can specify that blocks practice runs when the alarm is in an `ALARM` state. When a blocking alarm goes into an `ALARM` state, it prevents practice runs from being started, and ends practice runs that are in progress.
*Required*: No
*Type*: Array of [ControlCondition](aws-properties-arczonalshift-zonalautoshiftconfiguration-controlcondition.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutcomeAlarms`  <a name="cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-outcomealarms"></a>
The alarm that you specify to monitor the health of your application during practice runs. When the outcome alarm goes into an `ALARM` state, the practice run is ended and the outcome is set to `FAILED`.
*Required*: Yes
*Type*: Array of [ControlCondition](aws-properties-arczonalshift-zonalautoshiftconfiguration-controlcondition.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
