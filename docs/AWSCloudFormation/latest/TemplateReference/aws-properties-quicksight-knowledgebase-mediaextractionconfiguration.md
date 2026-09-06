---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-knowledgebase-mediaextractionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::KnowledgeBase MediaExtractionConfiguration
<a name="aws-properties-quicksight-knowledgebase-mediaextractionconfiguration"></a>

The configuration for media extraction from knowledge base documents.

## Syntax
<a name="aws-properties-quicksight-knowledgebase-mediaextractionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-knowledgebase-mediaextractionconfiguration-syntax.json"></a>

```
{
  "[AudioExtractionConfiguration](#cfn-quicksight-knowledgebase-mediaextractionconfiguration-audioextractionconfiguration)" : {{AudioExtractionConfiguration}},
  "[ImageExtractionConfiguration](#cfn-quicksight-knowledgebase-mediaextractionconfiguration-imageextractionconfiguration)" : {{ImageExtractionConfiguration}},
  "[VideoExtractionConfiguration](#cfn-quicksight-knowledgebase-mediaextractionconfiguration-videoextractionconfiguration)" : {{VideoExtractionConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-knowledgebase-mediaextractionconfiguration-syntax.yaml"></a>

```
  [AudioExtractionConfiguration](#cfn-quicksight-knowledgebase-mediaextractionconfiguration-audioextractionconfiguration): {{
    AudioExtractionConfiguration}}
  [ImageExtractionConfiguration](#cfn-quicksight-knowledgebase-mediaextractionconfiguration-imageextractionconfiguration): {{
    ImageExtractionConfiguration}}
  [VideoExtractionConfiguration](#cfn-quicksight-knowledgebase-mediaextractionconfiguration-videoextractionconfiguration): {{
    VideoExtractionConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-knowledgebase-mediaextractionconfiguration-properties"></a>

`AudioExtractionConfiguration`  <a name="cfn-quicksight-knowledgebase-mediaextractionconfiguration-audioextractionconfiguration"></a>
The configuration for audio extraction.
*Required*: No
*Type*: [AudioExtractionConfiguration](aws-properties-quicksight-knowledgebase-audioextractionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageExtractionConfiguration`  <a name="cfn-quicksight-knowledgebase-mediaextractionconfiguration-imageextractionconfiguration"></a>
The configuration for image extraction.
*Required*: No
*Type*: [ImageExtractionConfiguration](aws-properties-quicksight-knowledgebase-imageextractionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VideoExtractionConfiguration`  <a name="cfn-quicksight-knowledgebase-mediaextractionconfiguration-videoextractionconfiguration"></a>
The configuration for video extraction.
*Required*: No
*Type*: [VideoExtractionConfiguration](aws-properties-quicksight-knowledgebase-videoextractionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
