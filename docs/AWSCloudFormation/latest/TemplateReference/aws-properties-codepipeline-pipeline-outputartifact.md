---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-outputartifact.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Pipeline OutputArtifact
<a name="aws-properties-codepipeline-pipeline-outputartifact"></a>

Represents information about the output of an action.

## Syntax
<a name="aws-properties-codepipeline-pipeline-outputartifact-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-pipeline-outputartifact-syntax.json"></a>

```
{
  "[Files](#cfn-codepipeline-pipeline-outputartifact-files)" : {{[ String, ... ]}},
  "[Name](#cfn-codepipeline-pipeline-outputartifact-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-codepipeline-pipeline-outputartifact-syntax.yaml"></a>

```
  [Files](#cfn-codepipeline-pipeline-outputartifact-files): {{
    - String}}
  [Name](#cfn-codepipeline-pipeline-outputartifact-name): {{String}}
```

## Properties
<a name="aws-properties-codepipeline-pipeline-outputartifact-properties"></a>

`Files`  <a name="cfn-codepipeline-pipeline-outputartifact-files"></a>
The files that you want to associate with the output artifact that will be exported from the compute action.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-codepipeline-pipeline-outputartifact-name"></a>
The name of the output of an artifact, such as "My App".
The output artifact name must exactly match the input artifact declared for a downstream action. However, the downstream action's input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
Output artifact names must be unique within a pipeline.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9_\-]+`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
