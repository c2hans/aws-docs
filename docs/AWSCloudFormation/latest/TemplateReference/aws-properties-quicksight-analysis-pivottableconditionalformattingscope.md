---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-pivottableconditionalformattingscope.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis PivotTableConditionalFormattingScope
<a name="aws-properties-quicksight-analysis-pivottableconditionalformattingscope"></a>

The scope of the cell for conditional formatting.

## Syntax
<a name="aws-properties-quicksight-analysis-pivottableconditionalformattingscope-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-pivottableconditionalformattingscope-syntax.json"></a>

```
{
  "[Role](#cfn-quicksight-analysis-pivottableconditionalformattingscope-role)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-pivottableconditionalformattingscope-syntax.yaml"></a>

```
  [Role](#cfn-quicksight-analysis-pivottableconditionalformattingscope-role): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-pivottableconditionalformattingscope-properties"></a>

`Role`  <a name="cfn-quicksight-analysis-pivottableconditionalformattingscope-role"></a>
The role (field, field total, grand total) of the cell for conditional formatting.
*Required*: No
*Type*: String
*Allowed values*: `FIELD | FIELD_TOTAL | GRAND_TOTAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
