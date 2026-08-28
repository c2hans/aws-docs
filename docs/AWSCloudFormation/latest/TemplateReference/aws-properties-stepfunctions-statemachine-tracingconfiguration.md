---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-stepfunctions-statemachine-tracingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::StepFunctions::StateMachine TracingConfiguration
<a name="aws-properties-stepfunctions-statemachine-tracingconfiguration"></a>

Selects whether or not the state machine's AWS X-Ray tracing is enabled. To configure your state machine to send trace data to X-Ray, set `Enabled` to `true`.

## Syntax
<a name="aws-properties-stepfunctions-statemachine-tracingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-stepfunctions-statemachine-tracingconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-stepfunctions-statemachine-tracingconfiguration-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-stepfunctions-statemachine-tracingconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-stepfunctions-statemachine-tracingconfiguration-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-stepfunctions-statemachine-tracingconfiguration-properties"></a>

`Enabled`  <a name="cfn-stepfunctions-statemachine-tracingconfiguration-enabled"></a>
When set to `true`, X-Ray tracing is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
