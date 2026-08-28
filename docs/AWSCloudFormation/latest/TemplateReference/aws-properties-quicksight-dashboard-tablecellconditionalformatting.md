---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-tablecellconditionalformatting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard TableCellConditionalFormatting
<a name="aws-properties-quicksight-dashboard-tablecellconditionalformatting"></a>

The cell conditional formatting option for a table.

## Syntax
<a name="aws-properties-quicksight-dashboard-tablecellconditionalformatting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-tablecellconditionalformatting-syntax.json"></a>

```
{
  "[FieldId](#cfn-quicksight-dashboard-tablecellconditionalformatting-fieldid)" : {{String}},
  "[TextFormat](#cfn-quicksight-dashboard-tablecellconditionalformatting-textformat)" : {{TextConditionalFormat}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-tablecellconditionalformatting-syntax.yaml"></a>

```
  [FieldId](#cfn-quicksight-dashboard-tablecellconditionalformatting-fieldid): {{String}}
  [TextFormat](#cfn-quicksight-dashboard-tablecellconditionalformatting-textformat): {{
    TextConditionalFormat}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-tablecellconditionalformatting-properties"></a>

`FieldId`  <a name="cfn-quicksight-dashboard-tablecellconditionalformatting-fieldid"></a>
The field ID of the cell for conditional formatting.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextFormat`  <a name="cfn-quicksight-dashboard-tablecellconditionalformatting-textformat"></a>
The text format of the cell for conditional formatting.
*Required*: No
*Type*: [TextConditionalFormat](aws-properties-quicksight-dashboard-textconditionalformat.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
