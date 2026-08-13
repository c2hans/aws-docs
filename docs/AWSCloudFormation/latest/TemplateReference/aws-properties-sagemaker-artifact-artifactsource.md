---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-artifact-artifactsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Artifact ArtifactSource
<a name="aws-properties-sagemaker-artifact-artifactsource"></a>

A structure describing the source of an artifact.

## Syntax
<a name="aws-properties-sagemaker-artifact-artifactsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-artifact-artifactsource-syntax.json"></a>

```
{
  "[SourceTypes](#cfn-sagemaker-artifact-artifactsource-sourcetypes)" : {{[ ArtifactSourceType, ... ]}},
  "[SourceUri](#cfn-sagemaker-artifact-artifactsource-sourceuri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-artifact-artifactsource-syntax.yaml"></a>

```
  [SourceTypes](#cfn-sagemaker-artifact-artifactsource-sourcetypes): {{
    - ArtifactSourceType}}
  [SourceUri](#cfn-sagemaker-artifact-artifactsource-sourceuri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-artifact-artifactsource-properties"></a>

`SourceTypes`  <a name="cfn-sagemaker-artifact-artifactsource-sourcetypes"></a>
A list of source types.
*Required*: No
*Type*: Array of [ArtifactSourceType](aws-properties-sagemaker-artifact-artifactsourcetype.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceUri`  <a name="cfn-sagemaker-artifact-artifactsource-sourceuri"></a>
The URI of the source.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
