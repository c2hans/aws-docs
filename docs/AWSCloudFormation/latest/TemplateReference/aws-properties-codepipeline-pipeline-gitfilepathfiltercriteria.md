---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-gitfilepathfiltercriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Pipeline GitFilePathFilterCriteria
<a name="aws-properties-codepipeline-pipeline-gitfilepathfiltercriteria"></a>

The Git repository file paths specified as filter criteria to start the pipeline.

## Syntax
<a name="aws-properties-codepipeline-pipeline-gitfilepathfiltercriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-pipeline-gitfilepathfiltercriteria-syntax.json"></a>

```
{
  "[Excludes](#cfn-codepipeline-pipeline-gitfilepathfiltercriteria-excludes)" : {{[ String, ... ]}},
  "[Includes](#cfn-codepipeline-pipeline-gitfilepathfiltercriteria-includes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-codepipeline-pipeline-gitfilepathfiltercriteria-syntax.yaml"></a>

```
  [Excludes](#cfn-codepipeline-pipeline-gitfilepathfiltercriteria-excludes): {{
    - String}}
  [Includes](#cfn-codepipeline-pipeline-gitfilepathfiltercriteria-includes): {{
    - String}}
```

## Properties
<a name="aws-properties-codepipeline-pipeline-gitfilepathfiltercriteria-properties"></a>

`Excludes`  <a name="cfn-codepipeline-pipeline-gitfilepathfiltercriteria-excludes"></a>
The list of patterns of Git repository file paths that, when a commit is pushed, are to be excluded from starting the pipeline.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `8`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Includes`  <a name="cfn-codepipeline-pipeline-gitfilepathfiltercriteria-includes"></a>
The list of patterns of Git repository file paths that, when a commit is pushed, are to be included as criteria that starts the pipeline.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `8`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
