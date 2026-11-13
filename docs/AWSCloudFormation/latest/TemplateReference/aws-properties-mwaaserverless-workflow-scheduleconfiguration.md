---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mwaaserverless-workflow-scheduleconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MWAAServerless::Workflow ScheduleConfiguration
<a name="aws-properties-mwaaserverless-workflow-scheduleconfiguration"></a>

Contains the configuration used to schedule automated workflow execution. Only one version of a workflow can have an active schedule at any time.

## Syntax
<a name="aws-properties-mwaaserverless-workflow-scheduleconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mwaaserverless-workflow-scheduleconfiguration-syntax.json"></a>

```
{
  "[CronExpression](#cfn-mwaaserverless-workflow-scheduleconfiguration-cronexpression)" : {{String}}
}
```

### YAML
<a name="aws-properties-mwaaserverless-workflow-scheduleconfiguration-syntax.yaml"></a>

```
  [CronExpression](#cfn-mwaaserverless-workflow-scheduleconfiguration-cronexpression): {{String}}
```

## Properties
<a name="aws-properties-mwaaserverless-workflow-scheduleconfiguration-properties"></a>

`CronExpression`  <a name="cfn-mwaaserverless-workflow-scheduleconfiguration-cronexpression"></a>
The schedule expression that determines when the workflow runs, as specified in the `schedule` parameter of the workflow's YAML definition. You can specify one of the following types of schedule expressions:
+ Apache Airflow cron expression – Five fields, such as `0 12 1 * *`.
+ Apache Airflow schedule preset – `@hourly`, `@daily`, `@weekly`, `@monthly`, `@yearly`, or `@annually`.
+ EventBridge Scheduler rate expression – For example, `rate(5 minutes)`. Supported units are minutes, hours, and days.
+ EventBridge Scheduler cron expression – Six fields, such as `cron(0 12 * * ? *)`.
In a cron expression, specify either a day-of-month or a day-of-week, not both.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
