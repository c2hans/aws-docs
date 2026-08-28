---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-ruledeclaration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Pipeline RuleDeclaration
<a name="aws-properties-codepipeline-pipeline-ruledeclaration"></a>

Represents information about the rule to be created for an associated condition. An example would be creating a new rule for an entry condition, such as a rule that checks for a test result before allowing the run to enter the deployment stage. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html). For more information about rules, see the [AWS CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html).

## Syntax
<a name="aws-properties-codepipeline-pipeline-ruledeclaration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-pipeline-ruledeclaration-syntax.json"></a>

```
{
  "[Commands](#cfn-codepipeline-pipeline-ruledeclaration-commands)" : {{[ String, ... ]}},
  "[Configuration](#cfn-codepipeline-pipeline-ruledeclaration-configuration)" : {{Json}},
  "[InputArtifacts](#cfn-codepipeline-pipeline-ruledeclaration-inputartifacts)" : {{[ InputArtifact, ... ]}},
  "[Name](#cfn-codepipeline-pipeline-ruledeclaration-name)" : {{String}},
  "[Region](#cfn-codepipeline-pipeline-ruledeclaration-region)" : {{String}},
  "[RoleArn](#cfn-codepipeline-pipeline-ruledeclaration-rolearn)" : {{String}},
  "[RuleTypeId](#cfn-codepipeline-pipeline-ruledeclaration-ruletypeid)" : {{RuleTypeId}}
}
```

### YAML
<a name="aws-properties-codepipeline-pipeline-ruledeclaration-syntax.yaml"></a>

```
  [Commands](#cfn-codepipeline-pipeline-ruledeclaration-commands): {{
    - String}}
  [Configuration](#cfn-codepipeline-pipeline-ruledeclaration-configuration): {{Json}}
  [InputArtifacts](#cfn-codepipeline-pipeline-ruledeclaration-inputartifacts): {{
    - InputArtifact}}
  [Name](#cfn-codepipeline-pipeline-ruledeclaration-name): {{String}}
  [Region](#cfn-codepipeline-pipeline-ruledeclaration-region): {{String}}
  [RoleArn](#cfn-codepipeline-pipeline-ruledeclaration-rolearn): {{String}}
  [RuleTypeId](#cfn-codepipeline-pipeline-ruledeclaration-ruletypeid): {{
    RuleTypeId}}
```

## Properties
<a name="aws-properties-codepipeline-pipeline-ruledeclaration-properties"></a>

`Commands`  <a name="cfn-codepipeline-pipeline-ruledeclaration-commands"></a>
The shell commands to run with your commands rule in CodePipeline. All commands are supported except multi-line formats. While CodeBuild logs and permissions are used, you do not need to create any resources in CodeBuild.
Using compute time for this action will incur separate charges in AWS CodeBuild.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Configuration`  <a name="cfn-codepipeline-pipeline-ruledeclaration-configuration"></a>
The action configuration fields for the rule.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputArtifacts`  <a name="cfn-codepipeline-pipeline-ruledeclaration-inputartifacts"></a>
The input artifacts fields for the rule, such as specifying an input file for the rule.
*Required*: No
*Type*: Array of [InputArtifact](aws-properties-codepipeline-pipeline-inputartifact.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-codepipeline-pipeline-ruledeclaration-name"></a>
The name of the rule that is created for the condition, such as `VariableCheck`.
*Required*: No
*Type*: String
*Pattern*: `[A-Za-z0-9.@\-_]+`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-codepipeline-pipeline-ruledeclaration-region"></a>
The Region for the condition associated with the rule.
*Required*: No
*Type*: String
*Minimum*: `4`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-codepipeline-pipeline-ruledeclaration-rolearn"></a>
The pipeline role ARN associated with the rule.
*Required*: No
*Type*: String
*Pattern*: `arn:aws(-[\w]+)*:iam::[0-9]{12}:role/.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleTypeId`  <a name="cfn-codepipeline-pipeline-ruledeclaration-ruletypeid"></a>
The ID for the rule type, which is made up of the combined values for category, owner, provider, and version.
*Required*: No
*Type*: [RuleTypeId](aws-properties-codepipeline-pipeline-ruletypeid.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
