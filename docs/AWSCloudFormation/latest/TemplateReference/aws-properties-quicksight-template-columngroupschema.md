---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-columngroupschema.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template ColumnGroupSchema
<a name="aws-properties-quicksight-template-columngroupschema"></a>

The column group schema.

## Syntax
<a name="aws-properties-quicksight-template-columngroupschema-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-columngroupschema-syntax.json"></a>

```
{
  "[ColumnGroupColumnSchemaList](#cfn-quicksight-template-columngroupschema-columngroupcolumnschemalist)" : {{[ ColumnGroupColumnSchema, ... ]}},
  "[Name](#cfn-quicksight-template-columngroupschema-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-columngroupschema-syntax.yaml"></a>

```
  [ColumnGroupColumnSchemaList](#cfn-quicksight-template-columngroupschema-columngroupcolumnschemalist): {{
    - ColumnGroupColumnSchema}}
  [Name](#cfn-quicksight-template-columngroupschema-name): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-columngroupschema-properties"></a>

`ColumnGroupColumnSchemaList`  <a name="cfn-quicksight-template-columngroupschema-columngroupcolumnschemalist"></a>
A structure containing the list of schemas for column group columns.
*Required*: No
*Type*: Array of [ColumnGroupColumnSchema](aws-properties-quicksight-template-columngroupcolumnschema.md)
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-template-columngroupschema-name"></a>
The name of the column group schema.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
