---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-layermapvisual.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard LayerMapVisual
<a name="aws-properties-quicksight-dashboard-layermapvisual"></a>

A layer map visual.

## Syntax
<a name="aws-properties-quicksight-dashboard-layermapvisual-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-layermapvisual-syntax.json"></a>

```
{
  "[ChartConfiguration](#cfn-quicksight-dashboard-layermapvisual-chartconfiguration)" : {{GeospatialLayerMapConfiguration}},
  "[DataSetIdentifier](#cfn-quicksight-dashboard-layermapvisual-datasetidentifier)" : {{String}},
  "[Subtitle](#cfn-quicksight-dashboard-layermapvisual-subtitle)" : {{VisualSubtitleLabelOptions}},
  "[Title](#cfn-quicksight-dashboard-layermapvisual-title)" : {{VisualTitleLabelOptions}},
  "[VisualContentAltText](#cfn-quicksight-dashboard-layermapvisual-visualcontentalttext)" : {{String}},
  "[VisualId](#cfn-quicksight-dashboard-layermapvisual-visualid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-layermapvisual-syntax.yaml"></a>

```
  [ChartConfiguration](#cfn-quicksight-dashboard-layermapvisual-chartconfiguration): {{
    GeospatialLayerMapConfiguration}}
  [DataSetIdentifier](#cfn-quicksight-dashboard-layermapvisual-datasetidentifier): {{String}}
  [Subtitle](#cfn-quicksight-dashboard-layermapvisual-subtitle): {{
    VisualSubtitleLabelOptions}}
  [Title](#cfn-quicksight-dashboard-layermapvisual-title): {{
    VisualTitleLabelOptions}}
  [VisualContentAltText](#cfn-quicksight-dashboard-layermapvisual-visualcontentalttext): {{String}}
  [VisualId](#cfn-quicksight-dashboard-layermapvisual-visualid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-layermapvisual-properties"></a>

`ChartConfiguration`  <a name="cfn-quicksight-dashboard-layermapvisual-chartconfiguration"></a>
The configuration settings of the visual.
*Required*: No
*Type*: [GeospatialLayerMapConfiguration](aws-properties-quicksight-dashboard-geospatiallayermapconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetIdentifier`  <a name="cfn-quicksight-dashboard-layermapvisual-datasetidentifier"></a>
The dataset that is used to create the layer map visual. You can't create a visual without a dataset or a topic.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subtitle`  <a name="cfn-quicksight-dashboard-layermapvisual-subtitle"></a>
Property description not available.
*Required*: No
*Type*: [VisualSubtitleLabelOptions](aws-properties-quicksight-dashboard-visualsubtitlelabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-dashboard-layermapvisual-title"></a>
Property description not available.
*Required*: No
*Type*: [VisualTitleLabelOptions](aws-properties-quicksight-dashboard-visualtitlelabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualContentAltText`  <a name="cfn-quicksight-dashboard-layermapvisual-visualcontentalttext"></a>
The alt text for the visual.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualId`  <a name="cfn-quicksight-dashboard-layermapvisual-visualid"></a>
The ID of the visual.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
