---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-failureconditions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Pipeline FailureConditions
<a name="aws-properties-codepipeline-pipeline-failureconditions"></a>

The configuration that specifies the result, such as rollback, to occur upon stage failure. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html).

## Syntax
<a name="aws-properties-codepipeline-pipeline-failureconditions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-pipeline-failureconditions-syntax.json"></a>

```
{
  "[Conditions](#cfn-codepipeline-pipeline-failureconditions-conditions)" : {{[ Condition, ... ]}},
  "[Result](#cfn-codepipeline-pipeline-failureconditions-result)" : {{String}},
  "[RetryConfiguration](#cfn-codepipeline-pipeline-failureconditions-retryconfiguration)" : {{RetryConfiguration}}
}
```

### YAML
<a name="aws-properties-codepipeline-pipeline-failureconditions-syntax.yaml"></a>

```
  [Conditions](#cfn-codepipeline-pipeline-failureconditions-conditions): {{
    - Condition}}
  [Result](#cfn-codepipeline-pipeline-failureconditions-result): {{String}}
  [RetryConfiguration](#cfn-codepipeline-pipeline-failureconditions-retryconfiguration): {{
    RetryConfiguration}}
```

## Properties
<a name="aws-properties-codepipeline-pipeline-failureconditions-properties"></a>

`Conditions`  <a name="cfn-codepipeline-pipeline-failureconditions-conditions"></a>
The conditions that are configured as failure conditions. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html).
*Required*: No
*Type*: Array of [Condition](aws-properties-codepipeline-pipeline-condition.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Result`  <a name="cfn-codepipeline-pipeline-failureconditions-result"></a>
The specified result for when the failure conditions are met, such as rolling back the stage.
*Required*: No
*Type*: String
*Allowed values*: `ROLLBACK | RETRY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetryConfiguration`  <a name="cfn-codepipeline-pipeline-failureconditions-retryconfiguration"></a>
The retry configuration specifies automatic retry for a failed stage, along with the configured retry mode.
*Required*: No
*Type*: [RetryConfiguration](aws-properties-codepipeline-pipeline-retryconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
