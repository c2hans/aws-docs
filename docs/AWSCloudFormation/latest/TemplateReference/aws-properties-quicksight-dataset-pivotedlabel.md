---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-pivotedlabel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet PivotedLabel
<a name="aws-properties-quicksight-dataset-pivotedlabel"></a>

Specifies a label value to be pivoted into a separate column, including the new column name and identifier.

## Syntax
<a name="aws-properties-quicksight-dataset-pivotedlabel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-pivotedlabel-syntax.json"></a>

```
{
  "[LabelName](#cfn-quicksight-dataset-pivotedlabel-labelname)" : {{String}},
  "[NewColumnId](#cfn-quicksight-dataset-pivotedlabel-newcolumnid)" : {{String}},
  "[NewColumnName](#cfn-quicksight-dataset-pivotedlabel-newcolumnname)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-pivotedlabel-syntax.yaml"></a>

```
  [LabelName](#cfn-quicksight-dataset-pivotedlabel-labelname): {{String}}
  [NewColumnId](#cfn-quicksight-dataset-pivotedlabel-newcolumnid): {{String}}
  [NewColumnName](#cfn-quicksight-dataset-pivotedlabel-newcolumnname): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-pivotedlabel-properties"></a>

`LabelName`  <a name="cfn-quicksight-dataset-pivotedlabel-labelname"></a>
The label value from the source data to be pivoted.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `2047`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NewColumnId`  <a name="cfn-quicksight-dataset-pivotedlabel-newcolumnid"></a>
A unique identifier for the new column created from this pivoted label.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NewColumnName`  <a name="cfn-quicksight-dataset-pivotedlabel-newcolumnname"></a>
The name for the new column created from this pivoted label.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
