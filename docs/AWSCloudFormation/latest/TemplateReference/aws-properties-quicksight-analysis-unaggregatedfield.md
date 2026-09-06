---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-unaggregatedfield.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis UnaggregatedField
<a name="aws-properties-quicksight-analysis-unaggregatedfield"></a>

The unaggregated field for a table.

## Syntax
<a name="aws-properties-quicksight-analysis-unaggregatedfield-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-unaggregatedfield-syntax.json"></a>

```
{
  "[Column](#cfn-quicksight-analysis-unaggregatedfield-column)" : {{ColumnIdentifier}},
  "[FieldId](#cfn-quicksight-analysis-unaggregatedfield-fieldid)" : {{String}},
  "[FormatConfiguration](#cfn-quicksight-analysis-unaggregatedfield-formatconfiguration)" : {{FormatConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-unaggregatedfield-syntax.yaml"></a>

```
  [Column](#cfn-quicksight-analysis-unaggregatedfield-column): {{
    ColumnIdentifier}}
  [FieldId](#cfn-quicksight-analysis-unaggregatedfield-fieldid): {{String}}
  [FormatConfiguration](#cfn-quicksight-analysis-unaggregatedfield-formatconfiguration): {{
    FormatConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-analysis-unaggregatedfield-properties"></a>

`Column`  <a name="cfn-quicksight-analysis-unaggregatedfield-column"></a>
The column that is used in the `UnaggregatedField`.
*Required*: Yes
*Type*: [ColumnIdentifier](aws-properties-quicksight-analysis-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldId`  <a name="cfn-quicksight-analysis-unaggregatedfield-fieldid"></a>
The custom field ID.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FormatConfiguration`  <a name="cfn-quicksight-analysis-unaggregatedfield-formatconfiguration"></a>
The format configuration of the field.
*Required*: No
*Type*: [FormatConfiguration](aws-properties-quicksight-analysis-formatconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
