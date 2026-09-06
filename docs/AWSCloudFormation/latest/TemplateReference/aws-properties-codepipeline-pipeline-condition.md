---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-condition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Pipeline Condition
<a name="aws-properties-codepipeline-pipeline-condition"></a>

The condition for the stage. A condition is made up of the rules and the result for the condition. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html).. For more information about rules, see the [AWS CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html).

## Syntax
<a name="aws-properties-codepipeline-pipeline-condition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-pipeline-condition-syntax.json"></a>

```
{
  "[Result](#cfn-codepipeline-pipeline-condition-result)" : {{String}},
  "[Rules](#cfn-codepipeline-pipeline-condition-rules)" : {{[ RuleDeclaration, ... ]}}
}
```

### YAML
<a name="aws-properties-codepipeline-pipeline-condition-syntax.yaml"></a>

```
  [Result](#cfn-codepipeline-pipeline-condition-result): {{String}}
  [Rules](#cfn-codepipeline-pipeline-condition-rules): {{
    - RuleDeclaration}}
```

## Properties
<a name="aws-properties-codepipeline-pipeline-condition-properties"></a>

`Result`  <a name="cfn-codepipeline-pipeline-condition-result"></a>
The action to be done when the condition is met. For example, rolling back an execution for a failure condition.
*Required*: No
*Type*: String
*Allowed values*: `ROLLBACK | FAIL | RETRY | SKIP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rules`  <a name="cfn-codepipeline-pipeline-condition-rules"></a>
The rules that make up the condition.
*Required*: No
*Type*: Array of [RuleDeclaration](aws-properties-codepipeline-pipeline-ruledeclaration.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
