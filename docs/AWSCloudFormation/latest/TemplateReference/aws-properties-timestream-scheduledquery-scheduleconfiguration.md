---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-timestream-scheduledquery-scheduleconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::ScheduledQuery ScheduleConfiguration
<a name="aws-properties-timestream-scheduledquery-scheduleconfiguration"></a>

Configuration of the schedule of the query.

## Syntax
<a name="aws-properties-timestream-scheduledquery-scheduleconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-timestream-scheduledquery-scheduleconfiguration-syntax.json"></a>

```
{
  "[ScheduleExpression](#cfn-timestream-scheduledquery-scheduleconfiguration-scheduleexpression)" : {{String}}
}
```

### YAML
<a name="aws-properties-timestream-scheduledquery-scheduleconfiguration-syntax.yaml"></a>

```
  [ScheduleExpression](#cfn-timestream-scheduledquery-scheduleconfiguration-scheduleexpression): {{String}}
```

## Properties
<a name="aws-properties-timestream-scheduledquery-scheduleconfiguration-properties"></a>

`ScheduleExpression`  <a name="cfn-timestream-scheduledquery-scheduleconfiguration-scheduleexpression"></a>
An expression that denotes when to trigger the scheduled query run. This can be a cron expression or a rate expression.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
