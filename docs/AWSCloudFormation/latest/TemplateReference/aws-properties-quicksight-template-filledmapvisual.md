---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-filledmapvisual.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template FilledMapVisual
<a name="aws-properties-quicksight-template-filledmapvisual"></a>

A filled map.

For more information, see [Creating filled maps](https://docs.aws.amazon.com/quicksight/latest/user/filled-maps.html) in the *Amazon Quick Suite User Guide*.

## Syntax
<a name="aws-properties-quicksight-template-filledmapvisual-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-filledmapvisual-syntax.json"></a>

```
{
  "[Actions](#cfn-quicksight-template-filledmapvisual-actions)" : {{[ VisualCustomAction, ... ]}},
  "[ChartConfiguration](#cfn-quicksight-template-filledmapvisual-chartconfiguration)" : {{FilledMapConfiguration}},
  "[ColumnHierarchies](#cfn-quicksight-template-filledmapvisual-columnhierarchies)" : {{[ ColumnHierarchy, ... ]}},
  "[ConditionalFormatting](#cfn-quicksight-template-filledmapvisual-conditionalformatting)" : {{FilledMapConditionalFormatting}},
  "[Subtitle](#cfn-quicksight-template-filledmapvisual-subtitle)" : {{VisualSubtitleLabelOptions}},
  "[Title](#cfn-quicksight-template-filledmapvisual-title)" : {{VisualTitleLabelOptions}},
  "[VisualContentAltText](#cfn-quicksight-template-filledmapvisual-visualcontentalttext)" : {{String}},
  "[VisualId](#cfn-quicksight-template-filledmapvisual-visualid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-filledmapvisual-syntax.yaml"></a>

```
  [Actions](#cfn-quicksight-template-filledmapvisual-actions): {{
    - VisualCustomAction}}
  [ChartConfiguration](#cfn-quicksight-template-filledmapvisual-chartconfiguration): {{
    FilledMapConfiguration}}
  [ColumnHierarchies](#cfn-quicksight-template-filledmapvisual-columnhierarchies): {{
    - ColumnHierarchy}}
  [ConditionalFormatting](#cfn-quicksight-template-filledmapvisual-conditionalformatting): {{
    FilledMapConditionalFormatting}}
  [Subtitle](#cfn-quicksight-template-filledmapvisual-subtitle): {{
    VisualSubtitleLabelOptions}}
  [Title](#cfn-quicksight-template-filledmapvisual-title): {{
    VisualTitleLabelOptions}}
  [VisualContentAltText](#cfn-quicksight-template-filledmapvisual-visualcontentalttext): {{String}}
  [VisualId](#cfn-quicksight-template-filledmapvisual-visualid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-filledmapvisual-properties"></a>

`Actions`  <a name="cfn-quicksight-template-filledmapvisual-actions"></a>
The list of custom actions that are configured for a visual.
*Required*: No
*Type*: Array of [VisualCustomAction](aws-properties-quicksight-template-visualcustomaction.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ChartConfiguration`  <a name="cfn-quicksight-template-filledmapvisual-chartconfiguration"></a>
The configuration settings of the visual.
*Required*: No
*Type*: [FilledMapConfiguration](aws-properties-quicksight-template-filledmapconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnHierarchies`  <a name="cfn-quicksight-template-filledmapvisual-columnhierarchies"></a>
The column hierarchy that is used during drill-downs and drill-ups.
*Required*: No
*Type*: Array of [ColumnHierarchy](aws-properties-quicksight-template-columnhierarchy.md)
*Minimum*: `0`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConditionalFormatting`  <a name="cfn-quicksight-template-filledmapvisual-conditionalformatting"></a>
The conditional formatting of a `FilledMapVisual`.
*Required*: No
*Type*: [FilledMapConditionalFormatting](aws-properties-quicksight-template-filledmapconditionalformatting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subtitle`  <a name="cfn-quicksight-template-filledmapvisual-subtitle"></a>
The subtitle that is displayed on the visual.
*Required*: No
*Type*: [VisualSubtitleLabelOptions](aws-properties-quicksight-template-visualsubtitlelabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-template-filledmapvisual-title"></a>
The title that is displayed on the visual.
*Required*: No
*Type*: [VisualTitleLabelOptions](aws-properties-quicksight-template-visualtitlelabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualContentAltText`  <a name="cfn-quicksight-template-filledmapvisual-visualcontentalttext"></a>
The alt text for the visual.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualId`  <a name="cfn-quicksight-template-filledmapvisual-visualid"></a>
The unique identifier of a visual. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have visuals with the same identifiers..
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
