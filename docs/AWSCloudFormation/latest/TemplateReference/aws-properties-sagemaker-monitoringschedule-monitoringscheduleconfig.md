---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::MonitoringSchedule MonitoringScheduleConfig
<a name="aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig"></a>

Configures the monitoring schedule and defines the monitoring job.

## Syntax
<a name="aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig-syntax.json"></a>

```
{
  "[MonitoringJobDefinition](#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-monitoringjobdefinition)" : {{MonitoringJobDefinition}},
  "[MonitoringJobDefinitionName](#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-monitoringjobdefinitionname)" : {{String}},
  "[MonitoringType](#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-monitoringtype)" : {{String}},
  "[ScheduleConfig](#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-scheduleconfig)" : {{ScheduleConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig-syntax.yaml"></a>

```
  [MonitoringJobDefinition](#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-monitoringjobdefinition): {{
    MonitoringJobDefinition}}
  [MonitoringJobDefinitionName](#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-monitoringjobdefinitionname): {{String}}
  [MonitoringType](#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-monitoringtype): {{String}}
  [ScheduleConfig](#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-scheduleconfig): {{
    ScheduleConfig}}
```

## Properties
<a name="aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig-properties"></a>

`MonitoringJobDefinition`  <a name="cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-monitoringjobdefinition"></a>
Defines the monitoring job.
*Required*: No
*Type*: [MonitoringJobDefinition](aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MonitoringJobDefinitionName`  <a name="cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-monitoringjobdefinitionname"></a>
The name of the monitoring job definition to schedule.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MonitoringType`  <a name="cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-monitoringtype"></a>
The type of the monitoring job definition to schedule.
*Required*: No
*Type*: String
*Allowed values*: `DataQuality | ModelQuality | ModelBias | ModelExplainability`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleConfig`  <a name="cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-scheduleconfig"></a>
Configures the monitoring schedule.
*Required*: No
*Type*: [ScheduleConfig](aws-properties-sagemaker-monitoringschedule-scheduleconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
