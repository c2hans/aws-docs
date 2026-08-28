---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-pivottabletotaloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template PivotTableTotalOptions
<a name="aws-properties-quicksight-template-pivottabletotaloptions"></a>

The total options for a pivot table visual.

## Syntax
<a name="aws-properties-quicksight-template-pivottabletotaloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-pivottabletotaloptions-syntax.json"></a>

```
{
  "[ColumnSubtotalOptions](#cfn-quicksight-template-pivottabletotaloptions-columnsubtotaloptions)" : {{SubtotalOptions}},
  "[ColumnTotalOptions](#cfn-quicksight-template-pivottabletotaloptions-columntotaloptions)" : {{PivotTotalOptions}},
  "[RowSubtotalOptions](#cfn-quicksight-template-pivottabletotaloptions-rowsubtotaloptions)" : {{SubtotalOptions}},
  "[RowTotalOptions](#cfn-quicksight-template-pivottabletotaloptions-rowtotaloptions)" : {{PivotTotalOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-template-pivottabletotaloptions-syntax.yaml"></a>

```
  [ColumnSubtotalOptions](#cfn-quicksight-template-pivottabletotaloptions-columnsubtotaloptions): {{
    SubtotalOptions}}
  [ColumnTotalOptions](#cfn-quicksight-template-pivottabletotaloptions-columntotaloptions): {{
    PivotTotalOptions}}
  [RowSubtotalOptions](#cfn-quicksight-template-pivottabletotaloptions-rowsubtotaloptions): {{
    SubtotalOptions}}
  [RowTotalOptions](#cfn-quicksight-template-pivottabletotaloptions-rowtotaloptions): {{
    PivotTotalOptions}}
```

## Properties
<a name="aws-properties-quicksight-template-pivottabletotaloptions-properties"></a>

`ColumnSubtotalOptions`  <a name="cfn-quicksight-template-pivottabletotaloptions-columnsubtotaloptions"></a>
The column subtotal options.
*Required*: No
*Type*: [SubtotalOptions](aws-properties-quicksight-template-subtotaloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnTotalOptions`  <a name="cfn-quicksight-template-pivottabletotaloptions-columntotaloptions"></a>
The column total options.
*Required*: No
*Type*: [PivotTotalOptions](aws-properties-quicksight-template-pivottotaloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RowSubtotalOptions`  <a name="cfn-quicksight-template-pivottabletotaloptions-rowsubtotaloptions"></a>
The row subtotal options.
*Required*: No
*Type*: [SubtotalOptions](aws-properties-quicksight-template-subtotaloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RowTotalOptions`  <a name="cfn-quicksight-template-pivottabletotaloptions-rowtotaloptions"></a>
The row total options.
*Required*: No
*Type*: [PivotTotalOptions](aws-properties-quicksight-template-pivottotaloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
