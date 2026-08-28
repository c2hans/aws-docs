---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-successconditions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Pipeline SuccessConditions
<a name="aws-properties-codepipeline-pipeline-successconditions"></a>

The conditions for making checks that, if met, succeed a stage. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html).

## Syntax
<a name="aws-properties-codepipeline-pipeline-successconditions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-pipeline-successconditions-syntax.json"></a>

```
{
  "[Conditions](#cfn-codepipeline-pipeline-successconditions-conditions)" : {{[ Condition, ... ]}}
}
```

### YAML
<a name="aws-properties-codepipeline-pipeline-successconditions-syntax.yaml"></a>

```
  [Conditions](#cfn-codepipeline-pipeline-successconditions-conditions): {{
    - Condition}}
```

## Properties
<a name="aws-properties-codepipeline-pipeline-successconditions-properties"></a>

`Conditions`  <a name="cfn-codepipeline-pipeline-successconditions-conditions"></a>
The conditions that are success conditions.
*Required*: No
*Type*: Array of [Condition](aws-properties-codepipeline-pipeline-condition.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
