---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-importtableoperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet ImportTableOperation
<a name="aws-properties-quicksight-dataset-importtableoperation"></a>

A transform operation that imports data from a source table.

## Syntax
<a name="aws-properties-quicksight-dataset-importtableoperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-importtableoperation-syntax.json"></a>

```
{
  "[Alias](#cfn-quicksight-dataset-importtableoperation-alias)" : {{String}},
  "[Source](#cfn-quicksight-dataset-importtableoperation-source)" : {{ImportTableOperationSource}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-importtableoperation-syntax.yaml"></a>

```
  [Alias](#cfn-quicksight-dataset-importtableoperation-alias): {{String}}
  [Source](#cfn-quicksight-dataset-importtableoperation-source): {{
    ImportTableOperationSource}}
```

## Properties
<a name="aws-properties-quicksight-dataset-importtableoperation-properties"></a>

`Alias`  <a name="cfn-quicksight-dataset-importtableoperation-alias"></a>
Alias for this operation.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-quicksight-dataset-importtableoperation-source"></a>
The source configuration that specifies which source table to import and any column mappings.
*Required*: Yes
*Type*: [ImportTableOperationSource](aws-properties-quicksight-dataset-importtableoperationsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
