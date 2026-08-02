---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-castcolumntypesoperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet CastColumnTypesOperation
<a name="aws-properties-quicksight-dataset-castcolumntypesoperation"></a>

A transform operation that changes the data types of one or more columns in the dataset.

## Syntax
<a name="aws-properties-quicksight-dataset-castcolumntypesoperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-castcolumntypesoperation-syntax.json"></a>

```
{
  "[Alias](#cfn-quicksight-dataset-castcolumntypesoperation-alias)" : {{String}},
  "[CastColumnTypeOperations](#cfn-quicksight-dataset-castcolumntypesoperation-castcolumntypeoperations)" : {{[ CastColumnTypeOperation, ... ]}},
  "[Source](#cfn-quicksight-dataset-castcolumntypesoperation-source)" : {{TransformOperationSource}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-castcolumntypesoperation-syntax.yaml"></a>

```
  [Alias](#cfn-quicksight-dataset-castcolumntypesoperation-alias): {{String}}
  [CastColumnTypeOperations](#cfn-quicksight-dataset-castcolumntypesoperation-castcolumntypeoperations): {{
    - CastColumnTypeOperation}}
  [Source](#cfn-quicksight-dataset-castcolumntypesoperation-source): {{
    TransformOperationSource}}
```

## Properties
<a name="aws-properties-quicksight-dataset-castcolumntypesoperation-properties"></a>

`Alias`  <a name="cfn-quicksight-dataset-castcolumntypesoperation-alias"></a>
Alias for this operation.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CastColumnTypeOperations`  <a name="cfn-quicksight-dataset-castcolumntypesoperation-castcolumntypeoperations"></a>
The list of column type casting operations to perform.
*Required*: Yes
*Type*: Array of [CastColumnTypeOperation](aws-properties-quicksight-dataset-castcolumntypeoperation.md)
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-quicksight-dataset-castcolumntypesoperation-source"></a>
The source transform operation that provides input data for the type casting.
*Required*: Yes
*Type*: [TransformOperationSource](aws-properties-quicksight-dataset-transformoperationsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
