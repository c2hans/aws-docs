---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-createcolumnsoperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet CreateColumnsOperation
<a name="aws-properties-quicksight-dataset-createcolumnsoperation"></a>

A transform operation that creates calculated columns. Columns created in one such operation form a lexical closure.

## Syntax
<a name="aws-properties-quicksight-dataset-createcolumnsoperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-createcolumnsoperation-syntax.json"></a>

```
{
  "[Alias](#cfn-quicksight-dataset-createcolumnsoperation-alias)" : {{String}},
  "[Columns](#cfn-quicksight-dataset-createcolumnsoperation-columns)" : {{[ CalculatedColumn, ... ]}},
  "[Source](#cfn-quicksight-dataset-createcolumnsoperation-source)" : {{TransformOperationSource}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-createcolumnsoperation-syntax.yaml"></a>

```
  [Alias](#cfn-quicksight-dataset-createcolumnsoperation-alias): {{String}}
  [Columns](#cfn-quicksight-dataset-createcolumnsoperation-columns): {{
    - CalculatedColumn}}
  [Source](#cfn-quicksight-dataset-createcolumnsoperation-source): {{
    TransformOperationSource}}
```

## Properties
<a name="aws-properties-quicksight-dataset-createcolumnsoperation-properties"></a>

`Alias`  <a name="cfn-quicksight-dataset-createcolumnsoperation-alias"></a>
Alias for this operation.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Columns`  <a name="cfn-quicksight-dataset-createcolumnsoperation-columns"></a>
Calculated columns to create.
*Required*: Yes
*Type*: Array of [CalculatedColumn](aws-properties-quicksight-dataset-calculatedcolumn.md)
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-quicksight-dataset-createcolumnsoperation-source"></a>
The source transform operation that provides input data for creating new calculated columns.
*Required*: No
*Type*: [TransformOperationSource](aws-properties-quicksight-dataset-transformoperationsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
