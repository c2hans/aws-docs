---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-inputcolumn.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet InputColumn
<a name="aws-properties-quicksight-dataset-inputcolumn"></a>

Metadata for a column that is used as the input of a transform operation.

## Syntax
<a name="aws-properties-quicksight-dataset-inputcolumn-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-inputcolumn-syntax.json"></a>

```
{
  "[Id](#cfn-quicksight-dataset-inputcolumn-id)" : {{String}},
  "[Name](#cfn-quicksight-dataset-inputcolumn-name)" : {{String}},
  "[SubType](#cfn-quicksight-dataset-inputcolumn-subtype)" : {{String}},
  "[Type](#cfn-quicksight-dataset-inputcolumn-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-inputcolumn-syntax.yaml"></a>

```
  [Id](#cfn-quicksight-dataset-inputcolumn-id): {{String}}
  [Name](#cfn-quicksight-dataset-inputcolumn-name): {{String}}
  [SubType](#cfn-quicksight-dataset-inputcolumn-subtype): {{String}}
  [Type](#cfn-quicksight-dataset-inputcolumn-type): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-inputcolumn-properties"></a>

`Id`  <a name="cfn-quicksight-dataset-inputcolumn-id"></a>
A unique identifier for the input column.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-dataset-inputcolumn-name"></a>
The name of this column in the underlying data source.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubType`  <a name="cfn-quicksight-dataset-inputcolumn-subtype"></a>
The sub data type of the column. Sub types are only available for decimal columns that are part of a SPICE dataset.
*Required*: No
*Type*: String
*Allowed values*: `FLOAT | FIXED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-dataset-inputcolumn-type"></a>
The data type of the column.
**Note:**`SEMISTRUCT` represents Athena's map, row, and struct data types. It is supported when using the new data preparation experience.
*Required*: Yes
*Type*: String
*Allowed values*: `STRING | INTEGER | DECIMAL | DATETIME | BIT | BOOLEAN | JSON | SEMISTRUCT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
