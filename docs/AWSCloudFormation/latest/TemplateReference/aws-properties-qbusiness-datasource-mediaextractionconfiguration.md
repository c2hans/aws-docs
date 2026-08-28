---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-datasource-mediaextractionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::DataSource MediaExtractionConfiguration
<a name="aws-properties-qbusiness-datasource-mediaextractionconfiguration"></a>

The configuration for extracting information from media in documents.

## Syntax
<a name="aws-properties-qbusiness-datasource-mediaextractionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-datasource-mediaextractionconfiguration-syntax.json"></a>

```
{
  "[AudioExtractionConfiguration](#cfn-qbusiness-datasource-mediaextractionconfiguration-audioextractionconfiguration)" : {{AudioExtractionConfiguration}},
  "[ImageExtractionConfiguration](#cfn-qbusiness-datasource-mediaextractionconfiguration-imageextractionconfiguration)" : {{ImageExtractionConfiguration}},
  "[VideoExtractionConfiguration](#cfn-qbusiness-datasource-mediaextractionconfiguration-videoextractionconfiguration)" : {{VideoExtractionConfiguration}}
}
```

### YAML
<a name="aws-properties-qbusiness-datasource-mediaextractionconfiguration-syntax.yaml"></a>

```
  [AudioExtractionConfiguration](#cfn-qbusiness-datasource-mediaextractionconfiguration-audioextractionconfiguration): {{
    AudioExtractionConfiguration}}
  [ImageExtractionConfiguration](#cfn-qbusiness-datasource-mediaextractionconfiguration-imageextractionconfiguration): {{
    ImageExtractionConfiguration}}
  [VideoExtractionConfiguration](#cfn-qbusiness-datasource-mediaextractionconfiguration-videoextractionconfiguration): {{
    VideoExtractionConfiguration}}
```

## Properties
<a name="aws-properties-qbusiness-datasource-mediaextractionconfiguration-properties"></a>

`AudioExtractionConfiguration`  <a name="cfn-qbusiness-datasource-mediaextractionconfiguration-audioextractionconfiguration"></a>
Configuration settings for extracting and processing audio content from media files.
*Required*: No
*Type*: [AudioExtractionConfiguration](aws-properties-qbusiness-datasource-audioextractionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageExtractionConfiguration`  <a name="cfn-qbusiness-datasource-mediaextractionconfiguration-imageextractionconfiguration"></a>
The configuration for extracting semantic meaning from images in documents. For more information, see [Extracting semantic meaning from images and visuals](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/extracting-meaning-from-images.html).
*Required*: No
*Type*: [ImageExtractionConfiguration](aws-properties-qbusiness-datasource-imageextractionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VideoExtractionConfiguration`  <a name="cfn-qbusiness-datasource-mediaextractionconfiguration-videoextractionconfiguration"></a>
Configuration settings for extracting and processing video content from media files.
*Required*: No
*Type*: [VideoExtractionConfiguration](aws-properties-qbusiness-datasource-videoextractionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
