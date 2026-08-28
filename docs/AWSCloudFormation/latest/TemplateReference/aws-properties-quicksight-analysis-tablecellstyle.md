---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-tablecellstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis TableCellStyle
<a name="aws-properties-quicksight-analysis-tablecellstyle"></a>

The table cell style for a cell in pivot table or table visual.

## Syntax
<a name="aws-properties-quicksight-analysis-tablecellstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-tablecellstyle-syntax.json"></a>

```
{
  "[BackgroundColor](#cfn-quicksight-analysis-tablecellstyle-backgroundcolor)" : {{String}},
  "[Border](#cfn-quicksight-analysis-tablecellstyle-border)" : {{GlobalTableBorderOptions}},
  "[FontConfiguration](#cfn-quicksight-analysis-tablecellstyle-fontconfiguration)" : {{FontConfiguration}},
  "[Height](#cfn-quicksight-analysis-tablecellstyle-height)" : {{Number}},
  "[HorizontalTextAlignment](#cfn-quicksight-analysis-tablecellstyle-horizontaltextalignment)" : {{String}},
  "[TextWrap](#cfn-quicksight-analysis-tablecellstyle-textwrap)" : {{String}},
  "[VerticalTextAlignment](#cfn-quicksight-analysis-tablecellstyle-verticaltextalignment)" : {{String}},
  "[Visibility](#cfn-quicksight-analysis-tablecellstyle-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-tablecellstyle-syntax.yaml"></a>

```
  [BackgroundColor](#cfn-quicksight-analysis-tablecellstyle-backgroundcolor): {{String}}
  [Border](#cfn-quicksight-analysis-tablecellstyle-border): {{
    GlobalTableBorderOptions}}
  [FontConfiguration](#cfn-quicksight-analysis-tablecellstyle-fontconfiguration): {{
    FontConfiguration}}
  [Height](#cfn-quicksight-analysis-tablecellstyle-height): {{Number}}
  [HorizontalTextAlignment](#cfn-quicksight-analysis-tablecellstyle-horizontaltextalignment): {{String}}
  [TextWrap](#cfn-quicksight-analysis-tablecellstyle-textwrap): {{String}}
  [VerticalTextAlignment](#cfn-quicksight-analysis-tablecellstyle-verticaltextalignment): {{String}}
  [Visibility](#cfn-quicksight-analysis-tablecellstyle-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-tablecellstyle-properties"></a>

`BackgroundColor`  <a name="cfn-quicksight-analysis-tablecellstyle-backgroundcolor"></a>
The background color for the table cells.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Border`  <a name="cfn-quicksight-analysis-tablecellstyle-border"></a>
The borders for the table cells.
*Required*: No
*Type*: [GlobalTableBorderOptions](aws-properties-quicksight-analysis-globaltableborderoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FontConfiguration`  <a name="cfn-quicksight-analysis-tablecellstyle-fontconfiguration"></a>
The font configuration of the table cells.
*Required*: No
*Type*: [FontConfiguration](aws-properties-quicksight-analysis-fontconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Height`  <a name="cfn-quicksight-analysis-tablecellstyle-height"></a>
The height color for the table cells.
*Required*: No
*Type*: Number
*Minimum*: `8`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HorizontalTextAlignment`  <a name="cfn-quicksight-analysis-tablecellstyle-horizontaltextalignment"></a>
The horizontal text alignment (left, center, right, auto) for the table cells.
*Required*: No
*Type*: String
*Allowed values*: `LEFT | CENTER | RIGHT | AUTO`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextWrap`  <a name="cfn-quicksight-analysis-tablecellstyle-textwrap"></a>
The text wrap (none, wrap) for the table cells.
*Required*: No
*Type*: String
*Allowed values*: `NONE | WRAP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VerticalTextAlignment`  <a name="cfn-quicksight-analysis-tablecellstyle-verticaltextalignment"></a>
The vertical text alignment (top, middle, bottom) for the table cells.
*Required*: No
*Type*: String
*Allowed values*: `TOP | MIDDLE | BOTTOM | AUTO`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-analysis-tablecellstyle-visibility"></a>
The visibility of the table cells.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
