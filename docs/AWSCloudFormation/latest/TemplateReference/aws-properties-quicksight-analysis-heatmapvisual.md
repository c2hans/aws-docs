---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-heatmapvisual.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis HeatMapVisual
<a name="aws-properties-quicksight-analysis-heatmapvisual"></a>

A heat map.

For more information, see [Using heat maps](https://docs.aws.amazon.com/quicksight/latest/user/heat-map.html) in the *Amazon Quick Suite User Guide*.

## Syntax
<a name="aws-properties-quicksight-analysis-heatmapvisual-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-heatmapvisual-syntax.json"></a>

```
{
  "[Actions](#cfn-quicksight-analysis-heatmapvisual-actions)" : {{[ VisualCustomAction, ... ]}},
  "[ChartConfiguration](#cfn-quicksight-analysis-heatmapvisual-chartconfiguration)" : {{HeatMapConfiguration}},
  "[ColumnHierarchies](#cfn-quicksight-analysis-heatmapvisual-columnhierarchies)" : {{[ ColumnHierarchy, ... ]}},
  "[Subtitle](#cfn-quicksight-analysis-heatmapvisual-subtitle)" : {{VisualSubtitleLabelOptions}},
  "[Title](#cfn-quicksight-analysis-heatmapvisual-title)" : {{VisualTitleLabelOptions}},
  "[VisualContentAltText](#cfn-quicksight-analysis-heatmapvisual-visualcontentalttext)" : {{String}},
  "[VisualId](#cfn-quicksight-analysis-heatmapvisual-visualid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-heatmapvisual-syntax.yaml"></a>

```
  [Actions](#cfn-quicksight-analysis-heatmapvisual-actions): {{
    - VisualCustomAction}}
  [ChartConfiguration](#cfn-quicksight-analysis-heatmapvisual-chartconfiguration): {{
    HeatMapConfiguration}}
  [ColumnHierarchies](#cfn-quicksight-analysis-heatmapvisual-columnhierarchies): {{
    - ColumnHierarchy}}
  [Subtitle](#cfn-quicksight-analysis-heatmapvisual-subtitle): {{
    VisualSubtitleLabelOptions}}
  [Title](#cfn-quicksight-analysis-heatmapvisual-title): {{
    VisualTitleLabelOptions}}
  [VisualContentAltText](#cfn-quicksight-analysis-heatmapvisual-visualcontentalttext): {{String}}
  [VisualId](#cfn-quicksight-analysis-heatmapvisual-visualid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-heatmapvisual-properties"></a>

`Actions`  <a name="cfn-quicksight-analysis-heatmapvisual-actions"></a>
The list of custom actions that are configured for a visual.
*Required*: No
*Type*: Array of [VisualCustomAction](aws-properties-quicksight-analysis-visualcustomaction.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ChartConfiguration`  <a name="cfn-quicksight-analysis-heatmapvisual-chartconfiguration"></a>
The configuration of a heat map.
*Required*: No
*Type*: [HeatMapConfiguration](aws-properties-quicksight-analysis-heatmapconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnHierarchies`  <a name="cfn-quicksight-analysis-heatmapvisual-columnhierarchies"></a>
The column hierarchy that is used during drill-downs and drill-ups.
*Required*: No
*Type*: Array of [ColumnHierarchy](aws-properties-quicksight-analysis-columnhierarchy.md)
*Minimum*: `0`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subtitle`  <a name="cfn-quicksight-analysis-heatmapvisual-subtitle"></a>
The subtitle that is displayed on the visual.
*Required*: No
*Type*: [VisualSubtitleLabelOptions](aws-properties-quicksight-analysis-visualsubtitlelabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-analysis-heatmapvisual-title"></a>
The title that is displayed on the visual.
*Required*: No
*Type*: [VisualTitleLabelOptions](aws-properties-quicksight-analysis-visualtitlelabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualContentAltText`  <a name="cfn-quicksight-analysis-heatmapvisual-visualcontentalttext"></a>
The alt text for the visual.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualId`  <a name="cfn-quicksight-analysis-heatmapvisual-visualid"></a>
The unique identifier of a visual. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have visuals with the same identifiers.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
