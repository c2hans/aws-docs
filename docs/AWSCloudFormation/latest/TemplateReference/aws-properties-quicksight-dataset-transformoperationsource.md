---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-transformoperationsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet TransformOperationSource
<a name="aws-properties-quicksight-dataset-transformoperationsource"></a>

Specifies the source of data for a transform operation, including the source operation and column mappings.

## Syntax
<a name="aws-properties-quicksight-dataset-transformoperationsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-transformoperationsource-syntax.json"></a>

```
{
  "[ColumnIdMappings](#cfn-quicksight-dataset-transformoperationsource-columnidmappings)" : {{[ DataSetColumnIdMapping, ... ]}},
  "[TransformOperationId](#cfn-quicksight-dataset-transformoperationsource-transformoperationid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-transformoperationsource-syntax.yaml"></a>

```
  [ColumnIdMappings](#cfn-quicksight-dataset-transformoperationsource-columnidmappings): {{
    - DataSetColumnIdMapping}}
  [TransformOperationId](#cfn-quicksight-dataset-transformoperationsource-transformoperationid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-transformoperationsource-properties"></a>

`ColumnIdMappings`  <a name="cfn-quicksight-dataset-transformoperationsource-columnidmappings"></a>
The mappings between source column identifiers and target column identifiers for this transformation.
*Required*: No
*Type*: Array of [DataSetColumnIdMapping](aws-properties-quicksight-dataset-datasetcolumnidmapping.md)
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransformOperationId`  <a name="cfn-quicksight-dataset-transformoperationsource-transformoperationid"></a>
The identifier of the transform operation that provides input data.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-zA-Z-]*$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
