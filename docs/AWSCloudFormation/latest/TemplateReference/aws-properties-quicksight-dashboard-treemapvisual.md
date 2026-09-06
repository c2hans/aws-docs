---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-treemapvisual.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard TreeMapVisual
<a name="aws-properties-quicksight-dashboard-treemapvisual"></a>

A tree map.

For more information, see [Using tree maps](https://docs.aws.amazon.com/quicksight/latest/user/tree-map.html) in the *Amazon Quick Suite User Guide*.

## Syntax
<a name="aws-properties-quicksight-dashboard-treemapvisual-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-treemapvisual-syntax.json"></a>

```
{
  "[Actions](#cfn-quicksight-dashboard-treemapvisual-actions)" : {{[ VisualCustomAction, ... ]}},
  "[ChartConfiguration](#cfn-quicksight-dashboard-treemapvisual-chartconfiguration)" : {{TreeMapConfiguration}},
  "[ColumnHierarchies](#cfn-quicksight-dashboard-treemapvisual-columnhierarchies)" : {{[ ColumnHierarchy, ... ]}},
  "[Subtitle](#cfn-quicksight-dashboard-treemapvisual-subtitle)" : {{VisualSubtitleLabelOptions}},
  "[Title](#cfn-quicksight-dashboard-treemapvisual-title)" : {{VisualTitleLabelOptions}},
  "[VisualContentAltText](#cfn-quicksight-dashboard-treemapvisual-visualcontentalttext)" : {{String}},
  "[VisualId](#cfn-quicksight-dashboard-treemapvisual-visualid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-treemapvisual-syntax.yaml"></a>

```
  [Actions](#cfn-quicksight-dashboard-treemapvisual-actions): {{
    - VisualCustomAction}}
  [ChartConfiguration](#cfn-quicksight-dashboard-treemapvisual-chartconfiguration): {{
    TreeMapConfiguration}}
  [ColumnHierarchies](#cfn-quicksight-dashboard-treemapvisual-columnhierarchies): {{
    - ColumnHierarchy}}
  [Subtitle](#cfn-quicksight-dashboard-treemapvisual-subtitle): {{
    VisualSubtitleLabelOptions}}
  [Title](#cfn-quicksight-dashboard-treemapvisual-title): {{
    VisualTitleLabelOptions}}
  [VisualContentAltText](#cfn-quicksight-dashboard-treemapvisual-visualcontentalttext): {{String}}
  [VisualId](#cfn-quicksight-dashboard-treemapvisual-visualid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-treemapvisual-properties"></a>

`Actions`  <a name="cfn-quicksight-dashboard-treemapvisual-actions"></a>
The list of custom actions that are configured for a visual.
*Required*: No
*Type*: Array of [VisualCustomAction](aws-properties-quicksight-dashboard-visualcustomaction.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ChartConfiguration`  <a name="cfn-quicksight-dashboard-treemapvisual-chartconfiguration"></a>
The configuration settings of the visual.
*Required*: No
*Type*: [TreeMapConfiguration](aws-properties-quicksight-dashboard-treemapconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnHierarchies`  <a name="cfn-quicksight-dashboard-treemapvisual-columnhierarchies"></a>
The column hierarchy that is used during drill-downs and drill-ups.
*Required*: No
*Type*: Array of [ColumnHierarchy](aws-properties-quicksight-dashboard-columnhierarchy.md)
*Minimum*: `0`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subtitle`  <a name="cfn-quicksight-dashboard-treemapvisual-subtitle"></a>
The subtitle that is displayed on the visual.
*Required*: No
*Type*: [VisualSubtitleLabelOptions](aws-properties-quicksight-dashboard-visualsubtitlelabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-dashboard-treemapvisual-title"></a>
The title that is displayed on the visual.
*Required*: No
*Type*: [VisualTitleLabelOptions](aws-properties-quicksight-dashboard-visualtitlelabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualContentAltText`  <a name="cfn-quicksight-dashboard-treemapvisual-visualcontentalttext"></a>
The alt text for the visual.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualId`  <a name="cfn-quicksight-dashboard-treemapvisual-visualid"></a>
The unique identifier of a visual. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have visuals with the same identifiers..
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
