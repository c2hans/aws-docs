---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-tablecellstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TableCellStyle
<a name="aws-properties-quicksight-template-tablecellstyle"></a>

The table cell style for a cell in pivot table or table visual.

## Syntax
<a name="aws-properties-quicksight-template-tablecellstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-tablecellstyle-syntax.json"></a>

```
{
  "[BackgroundColor](#cfn-quicksight-template-tablecellstyle-backgroundcolor)" : {{String}},
  "[Border](#cfn-quicksight-template-tablecellstyle-border)" : {{GlobalTableBorderOptions}},
  "[FontConfiguration](#cfn-quicksight-template-tablecellstyle-fontconfiguration)" : {{FontConfiguration}},
  "[Height](#cfn-quicksight-template-tablecellstyle-height)" : {{Number}},
  "[HorizontalTextAlignment](#cfn-quicksight-template-tablecellstyle-horizontaltextalignment)" : {{String}},
  "[TextWrap](#cfn-quicksight-template-tablecellstyle-textwrap)" : {{String}},
  "[VerticalTextAlignment](#cfn-quicksight-template-tablecellstyle-verticaltextalignment)" : {{String}},
  "[Visibility](#cfn-quicksight-template-tablecellstyle-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-tablecellstyle-syntax.yaml"></a>

```
  [BackgroundColor](#cfn-quicksight-template-tablecellstyle-backgroundcolor): {{String}}
  [Border](#cfn-quicksight-template-tablecellstyle-border): {{
    GlobalTableBorderOptions}}
  [FontConfiguration](#cfn-quicksight-template-tablecellstyle-fontconfiguration): {{
    FontConfiguration}}
  [Height](#cfn-quicksight-template-tablecellstyle-height): {{Number}}
  [HorizontalTextAlignment](#cfn-quicksight-template-tablecellstyle-horizontaltextalignment): {{String}}
  [TextWrap](#cfn-quicksight-template-tablecellstyle-textwrap): {{String}}
  [VerticalTextAlignment](#cfn-quicksight-template-tablecellstyle-verticaltextalignment): {{String}}
  [Visibility](#cfn-quicksight-template-tablecellstyle-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-tablecellstyle-properties"></a>

`BackgroundColor`  <a name="cfn-quicksight-template-tablecellstyle-backgroundcolor"></a>
The background color for the table cells.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Border`  <a name="cfn-quicksight-template-tablecellstyle-border"></a>
The borders for the table cells.
*Required*: No
*Type*: [GlobalTableBorderOptions](aws-properties-quicksight-template-globaltableborderoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FontConfiguration`  <a name="cfn-quicksight-template-tablecellstyle-fontconfiguration"></a>
The font configuration of the table cells.
*Required*: No
*Type*: [FontConfiguration](aws-properties-quicksight-template-fontconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Height`  <a name="cfn-quicksight-template-tablecellstyle-height"></a>
The height color for the table cells.
*Required*: No
*Type*: Number
*Minimum*: `8`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HorizontalTextAlignment`  <a name="cfn-quicksight-template-tablecellstyle-horizontaltextalignment"></a>
The horizontal text alignment (left, center, right, auto) for the table cells.
*Required*: No
*Type*: String
*Allowed values*: `LEFT | CENTER | RIGHT | AUTO`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextWrap`  <a name="cfn-quicksight-template-tablecellstyle-textwrap"></a>
The text wrap (none, wrap) for the table cells.
*Required*: No
*Type*: String
*Allowed values*: `NONE | WRAP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VerticalTextAlignment`  <a name="cfn-quicksight-template-tablecellstyle-verticaltextalignment"></a>
The vertical text alignment (top, middle, bottom) for the table cells.
*Required*: No
*Type*: String
*Allowed values*: `TOP | MIDDLE | BOTTOM | AUTO`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-template-tablecellstyle-visibility"></a>
The visibility of the table cells.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
