---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-mediaextractionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource MediaExtractionConfiguration
<a name="aws-properties-bedrock-datasource-mediaextractionconfiguration"></a>

Configuration for media extraction settings.

## Syntax
<a name="aws-properties-bedrock-datasource-mediaextractionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-mediaextractionconfiguration-syntax.json"></a>

```
{
  "[AudioExtractionConfiguration](#cfn-bedrock-datasource-mediaextractionconfiguration-audioextractionconfiguration)" : {{AudioExtractionConfiguration}},
  "[ImageExtractionConfiguration](#cfn-bedrock-datasource-mediaextractionconfiguration-imageextractionconfiguration)" : {{ImageExtractionConfiguration}},
  "[VideoExtractionConfiguration](#cfn-bedrock-datasource-mediaextractionconfiguration-videoextractionconfiguration)" : {{VideoExtractionConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-mediaextractionconfiguration-syntax.yaml"></a>

```
  [AudioExtractionConfiguration](#cfn-bedrock-datasource-mediaextractionconfiguration-audioextractionconfiguration): {{
    AudioExtractionConfiguration}}
  [ImageExtractionConfiguration](#cfn-bedrock-datasource-mediaextractionconfiguration-imageextractionconfiguration): {{
    ImageExtractionConfiguration}}
  [VideoExtractionConfiguration](#cfn-bedrock-datasource-mediaextractionconfiguration-videoextractionconfiguration): {{
    VideoExtractionConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-datasource-mediaextractionconfiguration-properties"></a>

`AudioExtractionConfiguration`  <a name="cfn-bedrock-datasource-mediaextractionconfiguration-audioextractionconfiguration"></a>
Configuration for audio extraction.
*Required*: No
*Type*: [AudioExtractionConfiguration](aws-properties-bedrock-datasource-audioextractionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageExtractionConfiguration`  <a name="cfn-bedrock-datasource-mediaextractionconfiguration-imageextractionconfiguration"></a>
Configuration for image extraction.
*Required*: No
*Type*: [ImageExtractionConfiguration](aws-properties-bedrock-datasource-imageextractionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VideoExtractionConfiguration`  <a name="cfn-bedrock-datasource-mediaextractionconfiguration-videoextractionconfiguration"></a>
Configuration for video extraction.
*Required*: No
*Type*: [VideoExtractionConfiguration](aws-properties-bedrock-datasource-videoextractionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
