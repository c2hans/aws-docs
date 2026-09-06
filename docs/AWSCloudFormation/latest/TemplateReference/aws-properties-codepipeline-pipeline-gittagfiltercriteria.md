---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-gittagfiltercriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Pipeline GitTagFilterCriteria
<a name="aws-properties-codepipeline-pipeline-gittagfiltercriteria"></a>

The Git tags specified as filter criteria for whether a Git tag repository event will start the pipeline.

## Syntax
<a name="aws-properties-codepipeline-pipeline-gittagfiltercriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-pipeline-gittagfiltercriteria-syntax.json"></a>

```
{
  "[Excludes](#cfn-codepipeline-pipeline-gittagfiltercriteria-excludes)" : {{[ String, ... ]}},
  "[Includes](#cfn-codepipeline-pipeline-gittagfiltercriteria-includes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-codepipeline-pipeline-gittagfiltercriteria-syntax.yaml"></a>

```
  [Excludes](#cfn-codepipeline-pipeline-gittagfiltercriteria-excludes): {{
    - String}}
  [Includes](#cfn-codepipeline-pipeline-gittagfiltercriteria-includes): {{
    - String}}
```

## Properties
<a name="aws-properties-codepipeline-pipeline-gittagfiltercriteria-properties"></a>

`Excludes`  <a name="cfn-codepipeline-pipeline-gittagfiltercriteria-excludes"></a>
The list of patterns of Git tags that, when pushed, are to be excluded from starting the pipeline.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `8`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Includes`  <a name="cfn-codepipeline-pipeline-gittagfiltercriteria-includes"></a>
The list of patterns of Git tags that, when pushed, are to be included as criteria that starts the pipeline.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `8`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
