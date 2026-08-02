---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mwaaserverless-workflow-scheduleconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MWAAServerless::Workflow ScheduleConfiguration
<a name="aws-properties-mwaaserverless-workflow-scheduleconfiguration"></a>

The configuration to use to schedule automated workflow execution using cron expressions. Amazon Managed Workflows for Apache Airflow Serverless integrates with EventBridge Scheduler to provide cost-effective, timezone-aware scheduling capabilities. The service supports both time-based and event-based scheduling (event-based scheduling available post-GA). When a workflow definition includes scheduling information, Amazon Managed Workflows for Apache Airflow Serverless automatically configures the appropriate triggers and ensures only one version of a workflow has an active schedule at any time.

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
A cron expression that defines when the workflow is automatically executed. Uses standard cron syntax.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
