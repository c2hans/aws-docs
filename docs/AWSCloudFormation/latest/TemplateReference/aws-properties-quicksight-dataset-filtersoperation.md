---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-filtersoperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet FiltersOperation
<a name="aws-properties-quicksight-dataset-filtersoperation"></a>

A transform operation that applies one or more filter conditions.

## Syntax
<a name="aws-properties-quicksight-dataset-filtersoperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-filtersoperation-syntax.json"></a>

```
{
  "[Alias](#cfn-quicksight-dataset-filtersoperation-alias)" : {{String}},
  "[FilterOperations](#cfn-quicksight-dataset-filtersoperation-filteroperations)" : {{[ FilterOperation, ... ]}},
  "[Source](#cfn-quicksight-dataset-filtersoperation-source)" : {{TransformOperationSource}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-filtersoperation-syntax.yaml"></a>

```
  [Alias](#cfn-quicksight-dataset-filtersoperation-alias): {{String}}
  [FilterOperations](#cfn-quicksight-dataset-filtersoperation-filteroperations): {{
    - FilterOperation}}
  [Source](#cfn-quicksight-dataset-filtersoperation-source): {{
    TransformOperationSource}}
```

## Properties
<a name="aws-properties-quicksight-dataset-filtersoperation-properties"></a>

`Alias`  <a name="cfn-quicksight-dataset-filtersoperation-alias"></a>
Alias for this operation.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterOperations`  <a name="cfn-quicksight-dataset-filtersoperation-filteroperations"></a>
The list of filter operations to apply.
*Required*: Yes
*Type*: Array of [FilterOperation](aws-properties-quicksight-dataset-filteroperation.md)
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-quicksight-dataset-filtersoperation-source"></a>
The source transform operation that provides input data for filtering.
*Required*: Yes
*Type*: [TransformOperationSource](aws-properties-quicksight-dataset-transformoperationsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
