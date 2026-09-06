---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-outputcolumn.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet OutputColumn
<a name="aws-properties-quicksight-dataset-outputcolumn"></a>

Output column.

## Syntax
<a name="aws-properties-quicksight-dataset-outputcolumn-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-outputcolumn-syntax.json"></a>

```
{
  "[Description](#cfn-quicksight-dataset-outputcolumn-description)" : {{String}},
  "[Id](#cfn-quicksight-dataset-outputcolumn-id)" : {{String}},
  "[Name](#cfn-quicksight-dataset-outputcolumn-name)" : {{String}},
  "[SubType](#cfn-quicksight-dataset-outputcolumn-subtype)" : {{String}},
  "[Type](#cfn-quicksight-dataset-outputcolumn-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-outputcolumn-syntax.yaml"></a>

```
  [Description](#cfn-quicksight-dataset-outputcolumn-description): {{String}}
  [Id](#cfn-quicksight-dataset-outputcolumn-id): {{String}}
  [Name](#cfn-quicksight-dataset-outputcolumn-name): {{String}}
  [SubType](#cfn-quicksight-dataset-outputcolumn-subtype): {{String}}
  [Type](#cfn-quicksight-dataset-outputcolumn-type): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-outputcolumn-properties"></a>

`Description`  <a name="cfn-quicksight-dataset-outputcolumn-description"></a>
A description for a column.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-quicksight-dataset-outputcolumn-id"></a>
A unique identifier for the output column.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-dataset-outputcolumn-name"></a>
The display name of the column..
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubType`  <a name="cfn-quicksight-dataset-outputcolumn-subtype"></a>
The sub data type of the column.
*Required*: No
*Type*: String
*Allowed values*: `FLOAT | FIXED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-dataset-outputcolumn-type"></a>
The data type of the column.
*Required*: No
*Type*: String
*Allowed values*: `STRING | INTEGER | DECIMAL | DATETIME`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
