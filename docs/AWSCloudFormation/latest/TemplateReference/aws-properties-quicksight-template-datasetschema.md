---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-datasetschema.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template DataSetSchema
<a name="aws-properties-quicksight-template-datasetschema"></a>

Dataset schema.

## Syntax
<a name="aws-properties-quicksight-template-datasetschema-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-datasetschema-syntax.json"></a>

```
{
  "[ColumnSchemaList](#cfn-quicksight-template-datasetschema-columnschemalist)" : {{[ ColumnSchema, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-datasetschema-syntax.yaml"></a>

```
  [ColumnSchemaList](#cfn-quicksight-template-datasetschema-columnschemalist): {{
    - ColumnSchema}}
```

## Properties
<a name="aws-properties-quicksight-template-datasetschema-properties"></a>

`ColumnSchemaList`  <a name="cfn-quicksight-template-datasetschema-columnschemalist"></a>
A structure containing the list of column schemas.
*Required*: No
*Type*: Array of [ColumnSchema](aws-properties-quicksight-template-columnschema.md)
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
