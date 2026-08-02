---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-funnelchartvisual.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template FunnelChartVisual
<a name="aws-properties-quicksight-template-funnelchartvisual"></a>

A funnel chart.

For more information, see [Using funnel charts](https://docs.aws.amazon.com/quicksight/latest/user/funnel-visual-content.html) in the *Amazon Quick Suite User Guide*.

## Syntax
<a name="aws-properties-quicksight-template-funnelchartvisual-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-funnelchartvisual-syntax.json"></a>

```
{
  "[Actions](#cfn-quicksight-template-funnelchartvisual-actions)" : {{[ VisualCustomAction, ... ]}},
  "[ChartConfiguration](#cfn-quicksight-template-funnelchartvisual-chartconfiguration)" : {{FunnelChartConfiguration}},
  "[ColumnHierarchies](#cfn-quicksight-template-funnelchartvisual-columnhierarchies)" : {{[ ColumnHierarchy, ... ]}},
  "[Subtitle](#cfn-quicksight-template-funnelchartvisual-subtitle)" : {{VisualSubtitleLabelOptions}},
  "[Title](#cfn-quicksight-template-funnelchartvisual-title)" : {{VisualTitleLabelOptions}},
  "[VisualContentAltText](#cfn-quicksight-template-funnelchartvisual-visualcontentalttext)" : {{String}},
  "[VisualId](#cfn-quicksight-template-funnelchartvisual-visualid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-funnelchartvisual-syntax.yaml"></a>

```
  [Actions](#cfn-quicksight-template-funnelchartvisual-actions): {{
    - VisualCustomAction}}
  [ChartConfiguration](#cfn-quicksight-template-funnelchartvisual-chartconfiguration): {{
    FunnelChartConfiguration}}
  [ColumnHierarchies](#cfn-quicksight-template-funnelchartvisual-columnhierarchies): {{
    - ColumnHierarchy}}
  [Subtitle](#cfn-quicksight-template-funnelchartvisual-subtitle): {{
    VisualSubtitleLabelOptions}}
  [Title](#cfn-quicksight-template-funnelchartvisual-title): {{
    VisualTitleLabelOptions}}
  [VisualContentAltText](#cfn-quicksight-template-funnelchartvisual-visualcontentalttext): {{String}}
  [VisualId](#cfn-quicksight-template-funnelchartvisual-visualid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-funnelchartvisual-properties"></a>

`Actions`  <a name="cfn-quicksight-template-funnelchartvisual-actions"></a>
The list of custom actions that are configured for a visual.
*Required*: No
*Type*: Array of [VisualCustomAction](aws-properties-quicksight-template-visualcustomaction.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ChartConfiguration`  <a name="cfn-quicksight-template-funnelchartvisual-chartconfiguration"></a>
The configuration of a `FunnelChartVisual`.
*Required*: No
*Type*: [FunnelChartConfiguration](aws-properties-quicksight-template-funnelchartconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnHierarchies`  <a name="cfn-quicksight-template-funnelchartvisual-columnhierarchies"></a>
The column hierarchy that is used during drill-downs and drill-ups.
*Required*: No
*Type*: Array of [ColumnHierarchy](aws-properties-quicksight-template-columnhierarchy.md)
*Minimum*: `0`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subtitle`  <a name="cfn-quicksight-template-funnelchartvisual-subtitle"></a>
The subtitle that is displayed on the visual.
*Required*: No
*Type*: [VisualSubtitleLabelOptions](aws-properties-quicksight-template-visualsubtitlelabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-template-funnelchartvisual-title"></a>
The title that is displayed on the visual.
*Required*: No
*Type*: [VisualTitleLabelOptions](aws-properties-quicksight-template-visualtitlelabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualContentAltText`  <a name="cfn-quicksight-template-funnelchartvisual-visualcontentalttext"></a>
The alt text for the visual.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualId`  <a name="cfn-quicksight-template-funnelchartvisual-visualid"></a>
The unique identifier of a visual. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have visuals with the same identifiers..
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
