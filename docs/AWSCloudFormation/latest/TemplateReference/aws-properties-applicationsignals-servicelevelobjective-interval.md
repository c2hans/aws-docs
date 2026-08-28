---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-servicelevelobjective-interval.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::ServiceLevelObjective Interval
<a name="aws-properties-applicationsignals-servicelevelobjective-interval"></a>

The time period used to evaluate the SLO. It can be either a calendar interval or rolling interval.

## Syntax
<a name="aws-properties-applicationsignals-servicelevelobjective-interval-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-servicelevelobjective-interval-syntax.json"></a>

```
{
  "[CalendarInterval](#cfn-applicationsignals-servicelevelobjective-interval-calendarinterval)" : {{CalendarInterval}},
  "[RollingInterval](#cfn-applicationsignals-servicelevelobjective-interval-rollinginterval)" : {{RollingInterval}}
}
```

### YAML
<a name="aws-properties-applicationsignals-servicelevelobjective-interval-syntax.yaml"></a>

```
  [CalendarInterval](#cfn-applicationsignals-servicelevelobjective-interval-calendarinterval): {{
    CalendarInterval}}
  [RollingInterval](#cfn-applicationsignals-servicelevelobjective-interval-rollinginterval): {{
    RollingInterval}}
```

## Properties
<a name="aws-properties-applicationsignals-servicelevelobjective-interval-properties"></a>

`CalendarInterval`  <a name="cfn-applicationsignals-servicelevelobjective-interval-calendarinterval"></a>
If the interval is a calendar interval, this structure contains the interval specifications.
*Required*: No
*Type*: [CalendarInterval](aws-properties-applicationsignals-servicelevelobjective-calendarinterval.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RollingInterval`  <a name="cfn-applicationsignals-servicelevelobjective-interval-rollinginterval"></a>
If the interval is a rolling interval, this structure contains the interval specifications.
*Required*: No
*Type*: [RollingInterval](aws-properties-applicationsignals-servicelevelobjective-rollinginterval.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
