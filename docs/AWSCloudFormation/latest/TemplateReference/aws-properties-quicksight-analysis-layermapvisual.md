---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-layermapvisual.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis LayerMapVisual
<a name="aws-properties-quicksight-analysis-layermapvisual"></a>

A layer map visual.

## Syntax
<a name="aws-properties-quicksight-analysis-layermapvisual-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-layermapvisual-syntax.json"></a>

```
{
  "[ChartConfiguration](#cfn-quicksight-analysis-layermapvisual-chartconfiguration)" : {{GeospatialLayerMapConfiguration}},
  "[DataSetIdentifier](#cfn-quicksight-analysis-layermapvisual-datasetidentifier)" : {{String}},
  "[Subtitle](#cfn-quicksight-analysis-layermapvisual-subtitle)" : {{VisualSubtitleLabelOptions}},
  "[Title](#cfn-quicksight-analysis-layermapvisual-title)" : {{VisualTitleLabelOptions}},
  "[VisualContentAltText](#cfn-quicksight-analysis-layermapvisual-visualcontentalttext)" : {{String}},
  "[VisualId](#cfn-quicksight-analysis-layermapvisual-visualid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-layermapvisual-syntax.yaml"></a>

```
  [ChartConfiguration](#cfn-quicksight-analysis-layermapvisual-chartconfiguration): {{
    GeospatialLayerMapConfiguration}}
  [DataSetIdentifier](#cfn-quicksight-analysis-layermapvisual-datasetidentifier): {{String}}
  [Subtitle](#cfn-quicksight-analysis-layermapvisual-subtitle): {{
    VisualSubtitleLabelOptions}}
  [Title](#cfn-quicksight-analysis-layermapvisual-title): {{
    VisualTitleLabelOptions}}
  [VisualContentAltText](#cfn-quicksight-analysis-layermapvisual-visualcontentalttext): {{String}}
  [VisualId](#cfn-quicksight-analysis-layermapvisual-visualid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-layermapvisual-properties"></a>

`ChartConfiguration`  <a name="cfn-quicksight-analysis-layermapvisual-chartconfiguration"></a>
The configuration settings of the visual.
*Required*: No
*Type*: [GeospatialLayerMapConfiguration](aws-properties-quicksight-analysis-geospatiallayermapconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetIdentifier`  <a name="cfn-quicksight-analysis-layermapvisual-datasetidentifier"></a>
The dataset that is used to create the layer map visual. You can't create a visual without a dataset or a topic.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subtitle`  <a name="cfn-quicksight-analysis-layermapvisual-subtitle"></a>
Property description not available.
*Required*: No
*Type*: [VisualSubtitleLabelOptions](aws-properties-quicksight-analysis-visualsubtitlelabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-analysis-layermapvisual-title"></a>
Property description not available.
*Required*: No
*Type*: [VisualTitleLabelOptions](aws-properties-quicksight-analysis-visualtitlelabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualContentAltText`  <a name="cfn-quicksight-analysis-layermapvisual-visualcontentalttext"></a>
The alt text for the visual.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualId`  <a name="cfn-quicksight-analysis-layermapvisual-visualid"></a>
The ID of the visual.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
