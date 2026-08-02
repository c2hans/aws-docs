---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-projectoperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet ProjectOperation
<a name="aws-properties-quicksight-dataset-projectoperation"></a>

A transform operation that projects columns. Operations that come after a projection can only refer to projected columns.

## Syntax
<a name="aws-properties-quicksight-dataset-projectoperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-projectoperation-syntax.json"></a>

```
{
  "[Alias](#cfn-quicksight-dataset-projectoperation-alias)" : {{String}},
  "[ProjectedColumns](#cfn-quicksight-dataset-projectoperation-projectedcolumns)" : {{[ String, ... ]}},
  "[Source](#cfn-quicksight-dataset-projectoperation-source)" : {{TransformOperationSource}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-projectoperation-syntax.yaml"></a>

```
  [Alias](#cfn-quicksight-dataset-projectoperation-alias): {{String}}
  [ProjectedColumns](#cfn-quicksight-dataset-projectoperation-projectedcolumns): {{
    - String}}
  [Source](#cfn-quicksight-dataset-projectoperation-source): {{
    TransformOperationSource}}
```

## Properties
<a name="aws-properties-quicksight-dataset-projectoperation-properties"></a>

`Alias`  <a name="cfn-quicksight-dataset-projectoperation-alias"></a>
Alias for this operation.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProjectedColumns`  <a name="cfn-quicksight-dataset-projectoperation-projectedcolumns"></a>
Projected columns.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-quicksight-dataset-projectoperation-source"></a>
The source transform operation that provides input data for column projection.
*Required*: No
*Type*: [TransformOperationSource](aws-properties-quicksight-dataset-transformoperationsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
