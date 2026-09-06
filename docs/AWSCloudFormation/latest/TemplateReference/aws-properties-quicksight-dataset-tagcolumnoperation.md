---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-tagcolumnoperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet TagColumnOperation
<a name="aws-properties-quicksight-dataset-tagcolumnoperation"></a>

A transform operation that tags a column with additional information.

## Syntax
<a name="aws-properties-quicksight-dataset-tagcolumnoperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-tagcolumnoperation-syntax.json"></a>

```
{
  "[ColumnName](#cfn-quicksight-dataset-tagcolumnoperation-columnname)" : {{String}},
  "[Tags](#cfn-quicksight-dataset-tagcolumnoperation-tags)" : {{[ ColumnTag, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-tagcolumnoperation-syntax.yaml"></a>

```
  [ColumnName](#cfn-quicksight-dataset-tagcolumnoperation-columnname): {{String}}
  [Tags](#cfn-quicksight-dataset-tagcolumnoperation-tags): {{
    - ColumnTag}}
```

## Properties
<a name="aws-properties-quicksight-dataset-tagcolumnoperation-properties"></a>

`ColumnName`  <a name="cfn-quicksight-dataset-tagcolumnoperation-columnname"></a>
The column that this operation acts on.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-quicksight-dataset-tagcolumnoperation-tags"></a>
The dataset column tag, currently only used for geospatial type tagging.
This is not tags for the AWS tagging feature.
*Required*: Yes
*Type*: Array of [ColumnTag](aws-properties-quicksight-dataset-columntag.md)
*Minimum*: `1`
*Maximum*: `16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
