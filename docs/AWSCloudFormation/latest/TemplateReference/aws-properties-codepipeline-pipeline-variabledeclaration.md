---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-variabledeclaration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Pipeline VariableDeclaration
<a name="aws-properties-codepipeline-pipeline-variabledeclaration"></a>

A variable declared at the pipeline level.

## Syntax
<a name="aws-properties-codepipeline-pipeline-variabledeclaration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-pipeline-variabledeclaration-syntax.json"></a>

```
{
  "[DefaultValue](#cfn-codepipeline-pipeline-variabledeclaration-defaultvalue)" : {{String}},
  "[Description](#cfn-codepipeline-pipeline-variabledeclaration-description)" : {{String}},
  "[Name](#cfn-codepipeline-pipeline-variabledeclaration-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-codepipeline-pipeline-variabledeclaration-syntax.yaml"></a>

```
  [DefaultValue](#cfn-codepipeline-pipeline-variabledeclaration-defaultvalue): {{String}}
  [Description](#cfn-codepipeline-pipeline-variabledeclaration-description): {{String}}
  [Name](#cfn-codepipeline-pipeline-variabledeclaration-name): {{String}}
```

## Properties
<a name="aws-properties-codepipeline-pipeline-variabledeclaration-properties"></a>

`DefaultValue`  <a name="cfn-codepipeline-pipeline-variabledeclaration-defaultvalue"></a>
The value of a pipeline-level variable.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-codepipeline-pipeline-variabledeclaration-description"></a>
The description of a pipeline-level variable. It's used to add additional context about the variable, and not being used at time when pipeline executes.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-codepipeline-pipeline-variabledeclaration-name"></a>
The name of a pipeline-level variable.
*Required*: Yes
*Type*: String
*Pattern*: `[A-Za-z0-9@\-_]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
