---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-analysistemplate-analysistemplateartifacts.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::AnalysisTemplate AnalysisTemplateArtifacts
<a name="aws-properties-cleanrooms-analysistemplate-analysistemplateartifacts"></a>

The analysis template artifacts.

## Syntax
<a name="aws-properties-cleanrooms-analysistemplate-analysistemplateartifacts-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-analysistemplate-analysistemplateartifacts-syntax.json"></a>

```
{
  "[AdditionalArtifacts](#cfn-cleanrooms-analysistemplate-analysistemplateartifacts-additionalartifacts)" : {{[ AnalysisTemplateArtifact, ... ]}},
  "[EntryPoint](#cfn-cleanrooms-analysistemplate-analysistemplateartifacts-entrypoint)" : {{AnalysisTemplateArtifact}},
  "[RoleArn](#cfn-cleanrooms-analysistemplate-analysistemplateartifacts-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-analysistemplate-analysistemplateartifacts-syntax.yaml"></a>

```
  [AdditionalArtifacts](#cfn-cleanrooms-analysistemplate-analysistemplateartifacts-additionalartifacts): {{
    - AnalysisTemplateArtifact}}
  [EntryPoint](#cfn-cleanrooms-analysistemplate-analysistemplateartifacts-entrypoint): {{
    AnalysisTemplateArtifact}}
  [RoleArn](#cfn-cleanrooms-analysistemplate-analysistemplateartifacts-rolearn): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-analysistemplate-analysistemplateartifacts-properties"></a>

`AdditionalArtifacts`  <a name="cfn-cleanrooms-analysistemplate-analysistemplateartifacts-additionalartifacts"></a>
 Additional artifacts for the analysis template.
*Required*: No
*Type*: Array of [AnalysisTemplateArtifact](aws-properties-cleanrooms-analysistemplate-analysistemplateartifact.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EntryPoint`  <a name="cfn-cleanrooms-analysistemplate-analysistemplateartifacts-entrypoint"></a>
 The entry point for the analysis template artifacts.
*Required*: Yes
*Type*: [AnalysisTemplateArtifact](aws-properties-cleanrooms-analysistemplate-analysistemplateartifact.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-cleanrooms-analysistemplate-analysistemplateartifacts-rolearn"></a>
 The role ARN for the analysis template artifacts.
*Required*: Yes
*Type*: String
*Minimum*: `32`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
