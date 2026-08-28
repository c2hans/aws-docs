---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-tableoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TableOptions
<a name="aws-properties-quicksight-template-tableoptions"></a>

The table options for a table visual.

## Syntax
<a name="aws-properties-quicksight-template-tableoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-tableoptions-syntax.json"></a>

```
{
  "[CellStyle](#cfn-quicksight-template-tableoptions-cellstyle)" : {{TableCellStyle}},
  "[HeaderStyle](#cfn-quicksight-template-tableoptions-headerstyle)" : {{TableCellStyle}},
  "[Orientation](#cfn-quicksight-template-tableoptions-orientation)" : {{String}},
  "[RowAlternateColorOptions](#cfn-quicksight-template-tableoptions-rowalternatecoloroptions)" : {{RowAlternateColorOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-template-tableoptions-syntax.yaml"></a>

```
  [CellStyle](#cfn-quicksight-template-tableoptions-cellstyle): {{
    TableCellStyle}}
  [HeaderStyle](#cfn-quicksight-template-tableoptions-headerstyle): {{
    TableCellStyle}}
  [Orientation](#cfn-quicksight-template-tableoptions-orientation): {{String}}
  [RowAlternateColorOptions](#cfn-quicksight-template-tableoptions-rowalternatecoloroptions): {{
    RowAlternateColorOptions}}
```

## Properties
<a name="aws-properties-quicksight-template-tableoptions-properties"></a>

`CellStyle`  <a name="cfn-quicksight-template-tableoptions-cellstyle"></a>
The table cell style of table cells.
*Required*: No
*Type*: [TableCellStyle](aws-properties-quicksight-template-tablecellstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HeaderStyle`  <a name="cfn-quicksight-template-tableoptions-headerstyle"></a>
The table cell style of a table header.
*Required*: No
*Type*: [TableCellStyle](aws-properties-quicksight-template-tablecellstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Orientation`  <a name="cfn-quicksight-template-tableoptions-orientation"></a>
The orientation (vertical, horizontal) for a table.
*Required*: No
*Type*: String
*Allowed values*: `VERTICAL | HORIZONTAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RowAlternateColorOptions`  <a name="cfn-quicksight-template-tableoptions-rowalternatecoloroptions"></a>
The row alternate color options (widget status, row alternate colors) for a table.
*Required*: No
*Type*: [RowAlternateColorOptions](aws-properties-quicksight-template-rowalternatecoloroptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
