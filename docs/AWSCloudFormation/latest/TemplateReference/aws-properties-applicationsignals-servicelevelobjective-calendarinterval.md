---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-servicelevelobjective-calendarinterval.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::ServiceLevelObjective CalendarInterval
<a name="aws-properties-applicationsignals-servicelevelobjective-calendarinterval"></a>

If the interval for this service level objective is a calendar interval, this structure contains the interval specifications.

## Syntax
<a name="aws-properties-applicationsignals-servicelevelobjective-calendarinterval-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-servicelevelobjective-calendarinterval-syntax.json"></a>

```
{
  "[Duration](#cfn-applicationsignals-servicelevelobjective-calendarinterval-duration)" : {{Integer}},
  "[DurationUnit](#cfn-applicationsignals-servicelevelobjective-calendarinterval-durationunit)" : {{String}},
  "[StartTime](#cfn-applicationsignals-servicelevelobjective-calendarinterval-starttime)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-applicationsignals-servicelevelobjective-calendarinterval-syntax.yaml"></a>

```
  [Duration](#cfn-applicationsignals-servicelevelobjective-calendarinterval-duration): {{Integer}}
  [DurationUnit](#cfn-applicationsignals-servicelevelobjective-calendarinterval-durationunit): {{String}}
  [StartTime](#cfn-applicationsignals-servicelevelobjective-calendarinterval-starttime): {{Integer}}
```

## Properties
<a name="aws-properties-applicationsignals-servicelevelobjective-calendarinterval-properties"></a>

`Duration`  <a name="cfn-applicationsignals-servicelevelobjective-calendarinterval-duration"></a>
Specifies the duration of each calendar interval. For example, if `Duration` is `1` and `DurationUnit` is `MONTH`, each interval is one month, aligned with the calendar.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DurationUnit`  <a name="cfn-applicationsignals-servicelevelobjective-calendarinterval-durationunit"></a>
Specifies the calendar interval unit.
*Required*: Yes
*Type*: String
*Allowed values*: `MINUTE | HOUR | DAY | MONTH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartTime`  <a name="cfn-applicationsignals-servicelevelobjective-calendarinterval-starttime"></a>
The date and time when you want the first interval to start. Be sure to choose a time that configures the intervals the way that you want. For example, if you want weekly intervals starting on Mondays at 6 a.m., be sure to specify a start time that is a Monday at 6 a.m.
When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: `1698778057`
As soon as one calendar interval ends, another automatically begins.
*Required*: Yes
*Type*: Integer
*Minimum*: `946684800`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
