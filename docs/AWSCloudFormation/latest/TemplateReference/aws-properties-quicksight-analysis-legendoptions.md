---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-legendoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis LegendOptions
<a name="aws-properties-quicksight-analysis-legendoptions"></a>

The options for the legend setup of a visual.

## Syntax
<a name="aws-properties-quicksight-analysis-legendoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-legendoptions-syntax.json"></a>

```
{
  "[Height](#cfn-quicksight-analysis-legendoptions-height)" : {{String}},
  "[Position](#cfn-quicksight-analysis-legendoptions-position)" : {{String}},
  "[Title](#cfn-quicksight-analysis-legendoptions-title)" : {{LabelOptions}},
  "[ValueFontConfiguration](#cfn-quicksight-analysis-legendoptions-valuefontconfiguration)" : {{FontConfiguration}},
  "[Visibility](#cfn-quicksight-analysis-legendoptions-visibility)" : {{String}},
  "[Width](#cfn-quicksight-analysis-legendoptions-width)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-legendoptions-syntax.yaml"></a>

```
  [Height](#cfn-quicksight-analysis-legendoptions-height): {{String}}
  [Position](#cfn-quicksight-analysis-legendoptions-position): {{String}}
  [Title](#cfn-quicksight-analysis-legendoptions-title): {{
    LabelOptions}}
  [ValueFontConfiguration](#cfn-quicksight-analysis-legendoptions-valuefontconfiguration): {{
    FontConfiguration}}
  [Visibility](#cfn-quicksight-analysis-legendoptions-visibility): {{String}}
  [Width](#cfn-quicksight-analysis-legendoptions-width): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-legendoptions-properties"></a>

`Height`  <a name="cfn-quicksight-analysis-legendoptions-height"></a>
The height of the legend. If this value is omitted, a default height is used when rendering.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Position`  <a name="cfn-quicksight-analysis-legendoptions-position"></a>
The positions for the legend. Choose one of the following options:
+  `AUTO`
+  `RIGHT`
+  `BOTTOM`
+  `LEFT`
*Required*: No
*Type*: String
*Allowed values*: `AUTO | RIGHT | BOTTOM | TOP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-analysis-legendoptions-title"></a>
The custom title for the legend.
*Required*: No
*Type*: [LabelOptions](aws-properties-quicksight-analysis-labeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueFontConfiguration`  <a name="cfn-quicksight-analysis-legendoptions-valuefontconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [FontConfiguration](aws-properties-quicksight-analysis-fontconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-analysis-legendoptions-visibility"></a>
Determines whether or not the legend is visible.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Width`  <a name="cfn-quicksight-analysis-legendoptions-width"></a>
The width of the legend. If this value is omitted, a default width is used when rendering.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
