---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-transposedtableoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis TransposedTableOption
<a name="aws-properties-quicksight-analysis-transposedtableoption"></a>

The column option of the transposed table.

## Syntax
<a name="aws-properties-quicksight-analysis-transposedtableoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-transposedtableoption-syntax.json"></a>

```
{
  "[ColumnIndex](#cfn-quicksight-analysis-transposedtableoption-columnindex)" : {{Number}},
  "[ColumnType](#cfn-quicksight-analysis-transposedtableoption-columntype)" : {{String}},
  "[ColumnWidth](#cfn-quicksight-analysis-transposedtableoption-columnwidth)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-transposedtableoption-syntax.yaml"></a>

```
  [ColumnIndex](#cfn-quicksight-analysis-transposedtableoption-columnindex): {{Number}}
  [ColumnType](#cfn-quicksight-analysis-transposedtableoption-columntype): {{String}}
  [ColumnWidth](#cfn-quicksight-analysis-transposedtableoption-columnwidth): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-transposedtableoption-properties"></a>

`ColumnIndex`  <a name="cfn-quicksight-analysis-transposedtableoption-columnindex"></a>
The index of a columns in a transposed table. The index range is 0-9999.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `9999`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnType`  <a name="cfn-quicksight-analysis-transposedtableoption-columntype"></a>
The column type of the column in a transposed table. Choose one of the following options:
+ `ROW_HEADER_COLUMN`: Refers to the leftmost column of the row header in the transposed table.
+ `VALUE_COLUMN`: Refers to all value columns in the transposed table.
*Required*: Yes
*Type*: String
*Allowed values*: `ROW_HEADER_COLUMN | VALUE_COLUMN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnWidth`  <a name="cfn-quicksight-analysis-transposedtableoption-columnwidth"></a>
The width of a column in a transposed table.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
