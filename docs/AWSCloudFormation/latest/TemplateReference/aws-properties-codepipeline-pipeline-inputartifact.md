---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-inputartifact.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Pipeline InputArtifact
<a name="aws-properties-codepipeline-pipeline-inputartifact"></a>

Represents information about an artifact to be worked on, such as a test or build artifact.

## Syntax
<a name="aws-properties-codepipeline-pipeline-inputartifact-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-pipeline-inputartifact-syntax.json"></a>

```
{
  "[Name](#cfn-codepipeline-pipeline-inputartifact-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-codepipeline-pipeline-inputartifact-syntax.yaml"></a>

```
  [Name](#cfn-codepipeline-pipeline-inputartifact-name): {{String}}
```

## Properties
<a name="aws-properties-codepipeline-pipeline-inputartifact-properties"></a>

`Name`  <a name="cfn-codepipeline-pipeline-inputartifact-name"></a>
The name of the artifact to be worked on (for example, "My App").
Artifacts are the files that are worked on by actions in the pipeline. See the action configuration for each action for details about artifact parameters. For example, the S3 source action input artifact is a file name (or file path), and the files are generally provided as a ZIP file. Example artifact name: SampleApp\_Windows.zip
The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9_\-]+`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
