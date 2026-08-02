---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-tablecellconditionalformatting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis TableCellConditionalFormatting
<a name="aws-properties-quicksight-analysis-tablecellconditionalformatting"></a>

The cell conditional formatting option for a table.

## Syntax
<a name="aws-properties-quicksight-analysis-tablecellconditionalformatting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-tablecellconditionalformatting-syntax.json"></a>

```
{
  "[FieldId](#cfn-quicksight-analysis-tablecellconditionalformatting-fieldid)" : {{String}},
  "[TextFormat](#cfn-quicksight-analysis-tablecellconditionalformatting-textformat)" : {{TextConditionalFormat}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-tablecellconditionalformatting-syntax.yaml"></a>

```
  [FieldId](#cfn-quicksight-analysis-tablecellconditionalformatting-fieldid): {{String}}
  [TextFormat](#cfn-quicksight-analysis-tablecellconditionalformatting-textformat): {{
    TextConditionalFormat}}
```

## Properties
<a name="aws-properties-quicksight-analysis-tablecellconditionalformatting-properties"></a>

`FieldId`  <a name="cfn-quicksight-analysis-tablecellconditionalformatting-fieldid"></a>
The field ID of the cell for conditional formatting.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextFormat`  <a name="cfn-quicksight-analysis-tablecellconditionalformatting-textformat"></a>
The text format of the cell for conditional formatting.
*Required*: No
*Type*: [TextConditionalFormat](aws-properties-quicksight-analysis-textconditionalformat.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
