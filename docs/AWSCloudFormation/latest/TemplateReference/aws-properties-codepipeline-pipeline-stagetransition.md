---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-stagetransition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Pipeline StageTransition
<a name="aws-properties-codepipeline-pipeline-stagetransition"></a>

The name of the pipeline in which you want to disable the flow of artifacts from one stage to another.

## Syntax
<a name="aws-properties-codepipeline-pipeline-stagetransition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-pipeline-stagetransition-syntax.json"></a>

```
{
  "[Reason](#cfn-codepipeline-pipeline-stagetransition-reason)" : {{String}},
  "[StageName](#cfn-codepipeline-pipeline-stagetransition-stagename)" : {{String}}
}
```

### YAML
<a name="aws-properties-codepipeline-pipeline-stagetransition-syntax.yaml"></a>

```
  [Reason](#cfn-codepipeline-pipeline-stagetransition-reason): {{String}}
  [StageName](#cfn-codepipeline-pipeline-stagetransition-stagename): {{String}}
```

## Properties
<a name="aws-properties-codepipeline-pipeline-stagetransition-properties"></a>

`Reason`  <a name="cfn-codepipeline-pipeline-stagetransition-reason"></a>
The reason given to the user that a stage is disabled, such as waiting for manual approval or manual tests. This message is displayed in the pipeline console UI.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9!@ \(\)\.\*\?\-]+`
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StageName`  <a name="cfn-codepipeline-pipeline-stagetransition-stagename"></a>
The name of the stage where you want to disable the inbound or outbound transition of artifacts.
*Required*: Yes
*Type*: String
*Pattern*: `[A-Za-z0-9.@\-_]+`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
