---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-hoursofoperation-recurrenceconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::HoursOfOperation RecurrenceConfig
<a name="aws-properties-connect-hoursofoperation-recurrenceconfig"></a>

Defines the recurrence configuration for overrides. This configuration uses a recurrence pattern to specify when and how frequently an event should repeat.

## Syntax
<a name="aws-properties-connect-hoursofoperation-recurrenceconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-hoursofoperation-recurrenceconfig-syntax.json"></a>

```
{
  "[RecurrencePattern](#cfn-connect-hoursofoperation-recurrenceconfig-recurrencepattern)" : {{RecurrencePattern}}
}
```

### YAML
<a name="aws-properties-connect-hoursofoperation-recurrenceconfig-syntax.yaml"></a>

```
  [RecurrencePattern](#cfn-connect-hoursofoperation-recurrenceconfig-recurrencepattern): {{
    RecurrencePattern}}
```

## Properties
<a name="aws-properties-connect-hoursofoperation-recurrenceconfig-properties"></a>

`RecurrencePattern`  <a name="cfn-connect-hoursofoperation-recurrenceconfig-recurrencepattern"></a>
The recurrence pattern that defines how the event repeats. Example: Frequency, Interval, ByMonth, ByMonthDay, ByWeekdayOccurrence
*Required*: Yes
*Type*: [RecurrencePattern](aws-properties-connect-hoursofoperation-recurrencepattern.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
