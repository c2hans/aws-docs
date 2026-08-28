---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-datasetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template DataSetConfiguration
<a name="aws-properties-quicksight-template-datasetconfiguration"></a>

Dataset configuration.

## Syntax
<a name="aws-properties-quicksight-template-datasetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-datasetconfiguration-syntax.json"></a>

```
{
  "[ColumnGroupSchemaList](#cfn-quicksight-template-datasetconfiguration-columngroupschemalist)" : {{[ ColumnGroupSchema, ... ]}},
  "[DataSetSchema](#cfn-quicksight-template-datasetconfiguration-datasetschema)" : {{DataSetSchema}},
  "[Placeholder](#cfn-quicksight-template-datasetconfiguration-placeholder)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-datasetconfiguration-syntax.yaml"></a>

```
  [ColumnGroupSchemaList](#cfn-quicksight-template-datasetconfiguration-columngroupschemalist): {{
    - ColumnGroupSchema}}
  [DataSetSchema](#cfn-quicksight-template-datasetconfiguration-datasetschema): {{
    DataSetSchema}}
  [Placeholder](#cfn-quicksight-template-datasetconfiguration-placeholder): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-datasetconfiguration-properties"></a>

`ColumnGroupSchemaList`  <a name="cfn-quicksight-template-datasetconfiguration-columngroupschemalist"></a>
A structure containing the list of column group schemas.
*Required*: No
*Type*: Array of [ColumnGroupSchema](aws-properties-quicksight-template-columngroupschema.md)
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetSchema`  <a name="cfn-quicksight-template-datasetconfiguration-datasetschema"></a>
Dataset schema.
*Required*: No
*Type*: [DataSetSchema](aws-properties-quicksight-template-datasetschema.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Placeholder`  <a name="cfn-quicksight-template-datasetconfiguration-placeholder"></a>
Placeholder.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
