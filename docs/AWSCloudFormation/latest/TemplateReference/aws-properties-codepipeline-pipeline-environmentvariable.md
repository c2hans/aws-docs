---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-environmentvariable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Pipeline EnvironmentVariable
<a name="aws-properties-codepipeline-pipeline-environmentvariable"></a>

The environment variables for the action.

## Syntax
<a name="aws-properties-codepipeline-pipeline-environmentvariable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-pipeline-environmentvariable-syntax.json"></a>

```
{
  "[Name](#cfn-codepipeline-pipeline-environmentvariable-name)" : {{String}},
  "[Type](#cfn-codepipeline-pipeline-environmentvariable-type)" : {{String}},
  "[Value](#cfn-codepipeline-pipeline-environmentvariable-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-codepipeline-pipeline-environmentvariable-syntax.yaml"></a>

```
  [Name](#cfn-codepipeline-pipeline-environmentvariable-name): {{String}}
  [Type](#cfn-codepipeline-pipeline-environmentvariable-type): {{String}}
  [Value](#cfn-codepipeline-pipeline-environmentvariable-value): {{String}}
```

## Properties
<a name="aws-properties-codepipeline-pipeline-environmentvariable-properties"></a>

`Name`  <a name="cfn-codepipeline-pipeline-environmentvariable-name"></a>
The environment variable name in the key-value pair.
*Required*: Yes
*Type*: String
*Pattern*: `[A-Za-z0-9_]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-codepipeline-pipeline-environmentvariable-type"></a>
Specifies the type of use for the environment variable value. The value can be either `PLAINTEXT` or `SECRETS_MANAGER`. If the value is `SECRETS_MANAGER`, provide the Secrets reference in the EnvironmentVariable value.
*Required*: No
*Type*: String
*Allowed values*: `PLAINTEXT | SECRETS_MANAGER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-codepipeline-pipeline-environmentvariable-value"></a>
The environment variable value in the key-value pair.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Minimum*: `1`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
