---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-tablevisual.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TableVisual
<a name="aws-properties-quicksight-template-tablevisual"></a>

A table visual.

For more information, see [Using tables as visuals](https://docs.aws.amazon.com/quicksight/latest/user/tabular.html) in the *Amazon Quick Suite User Guide*.

## Syntax
<a name="aws-properties-quicksight-template-tablevisual-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-tablevisual-syntax.json"></a>

```
{
  "[Actions](#cfn-quicksight-template-tablevisual-actions)" : {{[ VisualCustomAction, ... ]}},
  "[ChartConfiguration](#cfn-quicksight-template-tablevisual-chartconfiguration)" : {{TableConfiguration}},
  "[ConditionalFormatting](#cfn-quicksight-template-tablevisual-conditionalformatting)" : {{TableConditionalFormatting}},
  "[Subtitle](#cfn-quicksight-template-tablevisual-subtitle)" : {{VisualSubtitleLabelOptions}},
  "[Title](#cfn-quicksight-template-tablevisual-title)" : {{VisualTitleLabelOptions}},
  "[VisualContentAltText](#cfn-quicksight-template-tablevisual-visualcontentalttext)" : {{String}},
  "[VisualId](#cfn-quicksight-template-tablevisual-visualid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-tablevisual-syntax.yaml"></a>

```
  [Actions](#cfn-quicksight-template-tablevisual-actions): {{
    - VisualCustomAction}}
  [ChartConfiguration](#cfn-quicksight-template-tablevisual-chartconfiguration): {{
    TableConfiguration}}
  [ConditionalFormatting](#cfn-quicksight-template-tablevisual-conditionalformatting): {{
    TableConditionalFormatting}}
  [Subtitle](#cfn-quicksight-template-tablevisual-subtitle): {{
    VisualSubtitleLabelOptions}}
  [Title](#cfn-quicksight-template-tablevisual-title): {{
    VisualTitleLabelOptions}}
  [VisualContentAltText](#cfn-quicksight-template-tablevisual-visualcontentalttext): {{String}}
  [VisualId](#cfn-quicksight-template-tablevisual-visualid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-tablevisual-properties"></a>

`Actions`  <a name="cfn-quicksight-template-tablevisual-actions"></a>
The list of custom actions that are configured for a visual.
*Required*: No
*Type*: Array of [VisualCustomAction](aws-properties-quicksight-template-visualcustomaction.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ChartConfiguration`  <a name="cfn-quicksight-template-tablevisual-chartconfiguration"></a>
The configuration settings of the visual.
*Required*: No
*Type*: [TableConfiguration](aws-properties-quicksight-template-tableconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConditionalFormatting`  <a name="cfn-quicksight-template-tablevisual-conditionalformatting"></a>
The conditional formatting for a `PivotTableVisual`.
*Required*: No
*Type*: [TableConditionalFormatting](aws-properties-quicksight-template-tableconditionalformatting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subtitle`  <a name="cfn-quicksight-template-tablevisual-subtitle"></a>
The subtitle that is displayed on the visual.
*Required*: No
*Type*: [VisualSubtitleLabelOptions](aws-properties-quicksight-template-visualsubtitlelabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-template-tablevisual-title"></a>
The title that is displayed on the visual.
*Required*: No
*Type*: [VisualTitleLabelOptions](aws-properties-quicksight-template-visualtitlelabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualContentAltText`  <a name="cfn-quicksight-template-tablevisual-visualcontentalttext"></a>
The alt text for the visual.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualId`  <a name="cfn-quicksight-template-tablevisual-visualid"></a>
The unique identifier of a visual. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have visuals with the same identifiers..
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
