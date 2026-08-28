---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-scheduler-schedule-sagemakerpipelineparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Scheduler::Schedule SageMakerPipelineParameter
<a name="aws-properties-scheduler-schedule-sagemakerpipelineparameter"></a>

The name and value pair of a parameter to use to start execution of a SageMaker Model Building Pipeline.

## Syntax
<a name="aws-properties-scheduler-schedule-sagemakerpipelineparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-scheduler-schedule-sagemakerpipelineparameter-syntax.json"></a>

```
{
  "[Name](#cfn-scheduler-schedule-sagemakerpipelineparameter-name)" : {{String}},
  "[Value](#cfn-scheduler-schedule-sagemakerpipelineparameter-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-scheduler-schedule-sagemakerpipelineparameter-syntax.yaml"></a>

```
  [Name](#cfn-scheduler-schedule-sagemakerpipelineparameter-name): {{String}}
  [Value](#cfn-scheduler-schedule-sagemakerpipelineparameter-value): {{String}}
```

## Properties
<a name="aws-properties-scheduler-schedule-sagemakerpipelineparameter-properties"></a>

`Name`  <a name="cfn-scheduler-schedule-sagemakerpipelineparameter-name"></a>
Name of parameter to start execution of a SageMaker Model Building Pipeline.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9\-_]*$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-scheduler-schedule-sagemakerpipelineparameter-value"></a>
Value of parameter to start execution of a SageMaker Model Building Pipeline.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
