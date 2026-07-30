---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-gitconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Pipeline GitConfiguration
<a name="aws-properties-codepipeline-pipeline-gitconfiguration"></a>

A type of trigger configuration for Git-based source actions.

**Note**
You can specify the Git configuration trigger type for all third-party Git-based source actions that are supported by the `CodeStarSourceConnection` action type.

## Syntax
<a name="aws-properties-codepipeline-pipeline-gitconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-pipeline-gitconfiguration-syntax.json"></a>

```
{
  "[PullRequest](#cfn-codepipeline-pipeline-gitconfiguration-pullrequest)" : {{[ GitPullRequestFilter, ... ]}},
  "[Push](#cfn-codepipeline-pipeline-gitconfiguration-push)" : {{[ GitPushFilter, ... ]}},
  "[SourceActionName](#cfn-codepipeline-pipeline-gitconfiguration-sourceactionname)" : {{String}}
}
```

### YAML
<a name="aws-properties-codepipeline-pipeline-gitconfiguration-syntax.yaml"></a>

```
  [PullRequest](#cfn-codepipeline-pipeline-gitconfiguration-pullrequest): {{
    - GitPullRequestFilter}}
  [Push](#cfn-codepipeline-pipeline-gitconfiguration-push): {{
    - GitPushFilter}}
  [SourceActionName](#cfn-codepipeline-pipeline-gitconfiguration-sourceactionname): {{String}}
```

## Properties
<a name="aws-properties-codepipeline-pipeline-gitconfiguration-properties"></a>

`PullRequest`  <a name="cfn-codepipeline-pipeline-gitconfiguration-pullrequest"></a>
The field where the repository event that will start the pipeline is specified as pull requests.
*Required*: No
*Type*: Array of [GitPullRequestFilter](aws-properties-codepipeline-pipeline-gitpullrequestfilter.md)
*Minimum*: `1`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Push`  <a name="cfn-codepipeline-pipeline-gitconfiguration-push"></a>
The field where the repository event that will start the pipeline, such as pushing Git tags, is specified with details.
*Required*: No
*Type*: Array of [GitPushFilter](aws-properties-codepipeline-pipeline-gitpushfilter.md)
*Minimum*: `1`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceActionName`  <a name="cfn-codepipeline-pipeline-gitconfiguration-sourceactionname"></a>
The name of the pipeline source action where the trigger configuration, such as Git tags, is specified. The trigger configuration will start the pipeline upon the specified change only.
You can only specify one trigger configuration per source action.
*Required*: Yes
*Type*: String
*Pattern*: `[A-Za-z0-9.@\-_]+`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
