---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-stepfunctions-statemachine-loggingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::StepFunctions::StateMachine LoggingConfiguration
<a name="aws-properties-stepfunctions-statemachine-loggingconfiguration"></a>

Defines what execution history events are logged and where they are logged.

Step Functions provides the log levels — `OFF`, `ALL`, `ERROR`, and `FATAL`. No event types log when set to `OFF` and all event types do when set to `ALL`.

**Note**
By default, the `level` is set to `OFF`. For more information see [Log Levels](https://docs.aws.amazon.com/step-functions/latest/dg/cloudwatch-log-level.html) in the AWS Step Functions User Guide.

## Syntax
<a name="aws-properties-stepfunctions-statemachine-loggingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-stepfunctions-statemachine-loggingconfiguration-syntax.json"></a>

```
{
  "[Destinations](#cfn-stepfunctions-statemachine-loggingconfiguration-destinations)" : {{[ LogDestination, ... ]}},
  "[IncludeExecutionData](#cfn-stepfunctions-statemachine-loggingconfiguration-includeexecutiondata)" : {{Boolean}},
  "[Level](#cfn-stepfunctions-statemachine-loggingconfiguration-level)" : {{String}}
}
```

### YAML
<a name="aws-properties-stepfunctions-statemachine-loggingconfiguration-syntax.yaml"></a>

```
  [Destinations](#cfn-stepfunctions-statemachine-loggingconfiguration-destinations): {{
    - LogDestination}}
  [IncludeExecutionData](#cfn-stepfunctions-statemachine-loggingconfiguration-includeexecutiondata): {{Boolean}}
  [Level](#cfn-stepfunctions-statemachine-loggingconfiguration-level): {{String}}
```

## Properties
<a name="aws-properties-stepfunctions-statemachine-loggingconfiguration-properties"></a>

`Destinations`  <a name="cfn-stepfunctions-statemachine-loggingconfiguration-destinations"></a>
An array of objects that describes where your execution history events will be logged. Limited to size 1. Required, if your log level is not set to `OFF`.
*Required*: No
*Type*: Array of [LogDestination](aws-properties-stepfunctions-statemachine-logdestination.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludeExecutionData`  <a name="cfn-stepfunctions-statemachine-loggingconfiguration-includeexecutiondata"></a>
Determines whether execution data is included in your log. When set to `false`, data is excluded.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Level`  <a name="cfn-stepfunctions-statemachine-loggingconfiguration-level"></a>
Defines which category of execution history events are logged.
*Required*: No
*Type*: String
*Allowed values*: `ALL | ERROR | FATAL | OFF`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
