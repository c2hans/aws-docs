---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-imagepipeline-schedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::ImagePipeline Schedule
<a name="aws-properties-imagebuilder-imagepipeline-schedule"></a>

A schedule configures when and how often a pipeline will automatically create a new image.

## Syntax
<a name="aws-properties-imagebuilder-imagepipeline-schedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-imagepipeline-schedule-syntax.json"></a>

```
{
  "[AutoDisablePolicy](#cfn-imagebuilder-imagepipeline-schedule-autodisablepolicy)" : {{AutoDisablePolicy}},
  "[PipelineExecutionStartCondition](#cfn-imagebuilder-imagepipeline-schedule-pipelineexecutionstartcondition)" : {{String}},
  "[ScheduleExpression](#cfn-imagebuilder-imagepipeline-schedule-scheduleexpression)" : {{String}},
  "[Timezone](#cfn-imagebuilder-imagepipeline-schedule-timezone)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-imagepipeline-schedule-syntax.yaml"></a>

```
  [AutoDisablePolicy](#cfn-imagebuilder-imagepipeline-schedule-autodisablepolicy): {{
    AutoDisablePolicy}}
  [PipelineExecutionStartCondition](#cfn-imagebuilder-imagepipeline-schedule-pipelineexecutionstartcondition): {{String}}
  [ScheduleExpression](#cfn-imagebuilder-imagepipeline-schedule-scheduleexpression): {{String}}
  [Timezone](#cfn-imagebuilder-imagepipeline-schedule-timezone): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-imagepipeline-schedule-properties"></a>

`AutoDisablePolicy`  <a name="cfn-imagebuilder-imagepipeline-schedule-autodisablepolicy"></a>
The policy that configures when Image Builder should automatically disable a pipeline that is failing.
*Required*: No
*Type*: [AutoDisablePolicy](aws-properties-imagebuilder-imagepipeline-autodisablepolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PipelineExecutionStartCondition`  <a name="cfn-imagebuilder-imagepipeline-schedule-pipelineexecutionstartcondition"></a>
The start condition configures when the pipeline should trigger a new image build, as follows. If no value is set Image Builder defaults to `EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE`.
+ `EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE` (default) – When you use semantic version filters on the base image or components in your image recipe, EC2 Image Builder builds a new image only when there are new versions of the base image or components in your recipe that match the filter.
**Note**
For semantic version syntax, see [CreateComponent](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateComponent.html).
+ `EXPRESSION_MATCH_ONLY` – This condition builds a new image every time the CRON expression matches the current time.
If the recipe references its base image through an AWS Systems Manager Parameter Store parameter, a change in the parameter's value also counts as an available dependency update.
*Required*: No
*Type*: String
*Allowed values*: `EXPRESSION_MATCH_ONLY | EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleExpression`  <a name="cfn-imagebuilder-imagepipeline-schedule-scheduleexpression"></a>
The expression determines how often EC2 Image Builder evaluates your `pipelineExecutionStartCondition`. You can specify a cron expression, or a rate expression such as `rate(1 day)`.
For information on how to format a cron expression in Image Builder, see [Use cron expressions in EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/image-builder-cron.html).
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timezone`  <a name="cfn-imagebuilder-imagepipeline-schedule-timezone"></a>
The timezone that applies to the scheduling expression. Specify a value in [IANA timezone format](https://www.joda.org/joda-time/timezones.html), for example `Etc/UTC` or `America/Los_Angeles`. If not specified, this defaults to UTC.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]{2,}(?:\/[a-zA-Z0-9\-_+]+)*$`
*Minimum*: `3`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-imagebuilder-imagepipeline-schedule--seealso"></a>
+ [Manage image pipelines](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-pipelines.html) in the *Image Builder User Guide*.
