---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-topicconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TopicConfiguration
<a name="aws-properties-quicksight-template-topicconfiguration"></a>

The configuration of a topic.

## Syntax
<a name="aws-properties-quicksight-template-topicconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-topicconfiguration-syntax.json"></a>

```
{
  "[ColumnGroupSchemaList](#cfn-quicksight-template-topicconfiguration-columngroupschemalist)" : {{[ ColumnGroupSchema, ... ]}},
  "[DataSetSchema](#cfn-quicksight-template-topicconfiguration-datasetschema)" : {{DataSetSchema}},
  "[Placeholder](#cfn-quicksight-template-topicconfiguration-placeholder)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-topicconfiguration-syntax.yaml"></a>

```
  [ColumnGroupSchemaList](#cfn-quicksight-template-topicconfiguration-columngroupschemalist): {{
    - ColumnGroupSchema}}
  [DataSetSchema](#cfn-quicksight-template-topicconfiguration-datasetschema): {{
    DataSetSchema}}
  [Placeholder](#cfn-quicksight-template-topicconfiguration-placeholder): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-topicconfiguration-properties"></a>

`ColumnGroupSchemaList`  <a name="cfn-quicksight-template-topicconfiguration-columngroupschemalist"></a>
The list of column group schemas in the topic configuration.
*Required*: No
*Type*: Array of [ColumnGroupSchema](aws-properties-quicksight-template-columngroupschema.md)
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetSchema`  <a name="cfn-quicksight-template-topicconfiguration-datasetschema"></a>
Topic schema.
*Required*: No
*Type*: [DataSetSchema](aws-properties-quicksight-template-datasetschema.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Placeholder`  <a name="cfn-quicksight-template-topicconfiguration-placeholder"></a>
The placeholder for the topic configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
