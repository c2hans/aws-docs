---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-layermapvisual.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template LayerMapVisual
<a name="aws-properties-quicksight-template-layermapvisual"></a>

A layer map visual.

## Syntax
<a name="aws-properties-quicksight-template-layermapvisual-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-layermapvisual-syntax.json"></a>

```
{
  "[ChartConfiguration](#cfn-quicksight-template-layermapvisual-chartconfiguration)" : {{GeospatialLayerMapConfiguration}},
  "[DataSetIdentifier](#cfn-quicksight-template-layermapvisual-datasetidentifier)" : {{String}},
  "[Subtitle](#cfn-quicksight-template-layermapvisual-subtitle)" : {{VisualSubtitleLabelOptions}},
  "[Title](#cfn-quicksight-template-layermapvisual-title)" : {{VisualTitleLabelOptions}},
  "[TopicIdentifier](#cfn-quicksight-template-layermapvisual-topicidentifier)" : {{String}},
  "[VisualContentAltText](#cfn-quicksight-template-layermapvisual-visualcontentalttext)" : {{String}},
  "[VisualId](#cfn-quicksight-template-layermapvisual-visualid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-layermapvisual-syntax.yaml"></a>

```
  [ChartConfiguration](#cfn-quicksight-template-layermapvisual-chartconfiguration): {{
    GeospatialLayerMapConfiguration}}
  [DataSetIdentifier](#cfn-quicksight-template-layermapvisual-datasetidentifier): {{String}}
  [Subtitle](#cfn-quicksight-template-layermapvisual-subtitle): {{
    VisualSubtitleLabelOptions}}
  [Title](#cfn-quicksight-template-layermapvisual-title): {{
    VisualTitleLabelOptions}}
  [TopicIdentifier](#cfn-quicksight-template-layermapvisual-topicidentifier): {{String}}
  [VisualContentAltText](#cfn-quicksight-template-layermapvisual-visualcontentalttext): {{String}}
  [VisualId](#cfn-quicksight-template-layermapvisual-visualid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-layermapvisual-properties"></a>

`ChartConfiguration`  <a name="cfn-quicksight-template-layermapvisual-chartconfiguration"></a>
The configuration settings of the visual.
*Required*: No
*Type*: [GeospatialLayerMapConfiguration](aws-properties-quicksight-template-geospatiallayermapconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetIdentifier`  <a name="cfn-quicksight-template-layermapvisual-datasetidentifier"></a>
The dataset that is used to create the layer map visual. You can't create a visual without a dataset or a topic.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subtitle`  <a name="cfn-quicksight-template-layermapvisual-subtitle"></a>
Property description not available.
*Required*: No
*Type*: [VisualSubtitleLabelOptions](aws-properties-quicksight-template-visualsubtitlelabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-template-layermapvisual-title"></a>
Property description not available.
*Required*: No
*Type*: [VisualTitleLabelOptions](aws-properties-quicksight-template-visualtitlelabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicIdentifier`  <a name="cfn-quicksight-template-layermapvisual-topicidentifier"></a>
The topic that is used in the layer map visual. You can't create a visual without a dataset or a topic.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualContentAltText`  <a name="cfn-quicksight-template-layermapvisual-visualcontentalttext"></a>
The alt text for the visual.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualId`  <a name="cfn-quicksight-template-layermapvisual-visualid"></a>
The ID of the visual.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
