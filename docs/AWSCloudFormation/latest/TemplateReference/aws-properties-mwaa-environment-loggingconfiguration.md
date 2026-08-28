---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mwaa-environment-loggingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MWAA::Environment LoggingConfiguration
<a name="aws-properties-mwaa-environment-loggingconfiguration"></a>

The type of Apache Airflow logs to send to CloudWatch Logs.

## Syntax
<a name="aws-properties-mwaa-environment-loggingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mwaa-environment-loggingconfiguration-syntax.json"></a>

```
{
  "[DagProcessingLogs](#cfn-mwaa-environment-loggingconfiguration-dagprocessinglogs)" : {{ModuleLoggingConfiguration}},
  "[SchedulerLogs](#cfn-mwaa-environment-loggingconfiguration-schedulerlogs)" : {{ModuleLoggingConfiguration}},
  "[TaskLogs](#cfn-mwaa-environment-loggingconfiguration-tasklogs)" : {{ModuleLoggingConfiguration}},
  "[WebserverLogs](#cfn-mwaa-environment-loggingconfiguration-webserverlogs)" : {{ModuleLoggingConfiguration}},
  "[WorkerLogs](#cfn-mwaa-environment-loggingconfiguration-workerlogs)" : {{ModuleLoggingConfiguration}}
}
```

### YAML
<a name="aws-properties-mwaa-environment-loggingconfiguration-syntax.yaml"></a>

```
  [DagProcessingLogs](#cfn-mwaa-environment-loggingconfiguration-dagprocessinglogs): {{
    ModuleLoggingConfiguration}}
  [SchedulerLogs](#cfn-mwaa-environment-loggingconfiguration-schedulerlogs): {{
    ModuleLoggingConfiguration}}
  [TaskLogs](#cfn-mwaa-environment-loggingconfiguration-tasklogs): {{
    ModuleLoggingConfiguration}}
  [WebserverLogs](#cfn-mwaa-environment-loggingconfiguration-webserverlogs): {{
    ModuleLoggingConfiguration}}
  [WorkerLogs](#cfn-mwaa-environment-loggingconfiguration-workerlogs): {{
    ModuleLoggingConfiguration}}
```

## Properties
<a name="aws-properties-mwaa-environment-loggingconfiguration-properties"></a>

`DagProcessingLogs`  <a name="cfn-mwaa-environment-loggingconfiguration-dagprocessinglogs"></a>
Defines the processing logs sent to CloudWatch Logs and the logging level to send.
*Required*: No
*Type*: [ModuleLoggingConfiguration](aws-properties-mwaa-environment-moduleloggingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchedulerLogs`  <a name="cfn-mwaa-environment-loggingconfiguration-schedulerlogs"></a>
Defines the scheduler logs sent to CloudWatch Logs and the logging level to send.
*Required*: No
*Type*: [ModuleLoggingConfiguration](aws-properties-mwaa-environment-moduleloggingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TaskLogs`  <a name="cfn-mwaa-environment-loggingconfiguration-tasklogs"></a>
Defines the task logs sent to CloudWatch Logs and the logging level to send.
*Required*: No
*Type*: [ModuleLoggingConfiguration](aws-properties-mwaa-environment-moduleloggingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WebserverLogs`  <a name="cfn-mwaa-environment-loggingconfiguration-webserverlogs"></a>
Defines the web server logs sent to CloudWatch Logs and the logging level to send.
*Required*: No
*Type*: [ModuleLoggingConfiguration](aws-properties-mwaa-environment-moduleloggingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkerLogs`  <a name="cfn-mwaa-environment-loggingconfiguration-workerlogs"></a>
Defines the worker logs sent to CloudWatch Logs and the logging level to send.
*Required*: No
*Type*: [ModuleLoggingConfiguration](aws-properties-mwaa-environment-moduleloggingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
