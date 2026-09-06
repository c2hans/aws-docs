---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-querygenerationtable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase QueryGenerationTable
<a name="aws-properties-bedrock-knowledgebase-querygenerationtable"></a>

Contains information about a table for the query engine to consider.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-querygenerationtable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-querygenerationtable-syntax.json"></a>

```
{
  "[Columns](#cfn-bedrock-knowledgebase-querygenerationtable-columns)" : {{[ QueryGenerationColumn, ... ]}},
  "[Description](#cfn-bedrock-knowledgebase-querygenerationtable-description)" : {{String}},
  "[Inclusion](#cfn-bedrock-knowledgebase-querygenerationtable-inclusion)" : {{String}},
  "[Name](#cfn-bedrock-knowledgebase-querygenerationtable-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-querygenerationtable-syntax.yaml"></a>

```
  [Columns](#cfn-bedrock-knowledgebase-querygenerationtable-columns): {{
    - QueryGenerationColumn}}
  [Description](#cfn-bedrock-knowledgebase-querygenerationtable-description): {{String}}
  [Inclusion](#cfn-bedrock-knowledgebase-querygenerationtable-inclusion): {{String}}
  [Name](#cfn-bedrock-knowledgebase-querygenerationtable-name): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-querygenerationtable-properties"></a>

`Columns`  <a name="cfn-bedrock-knowledgebase-querygenerationtable-columns"></a>
An array of objects, each of which defines information about a column in the table.
*Required*: No
*Type*: Array of [QueryGenerationColumn](aws-properties-bedrock-knowledgebase-querygenerationcolumn.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-bedrock-knowledgebase-querygenerationtable-description"></a>
A description of the table that helps the query engine understand the contents of the table.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Inclusion`  <a name="cfn-bedrock-knowledgebase-querygenerationtable-inclusion"></a>
Specifies whether to include or exclude the table during query generation. If you specify `EXCLUDE`, the table will be ignored. If you specify `INCLUDE`, all other tables will be ignored.
*Required*: No
*Type*: String
*Allowed values*: `INCLUDE | EXCLUDE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrock-knowledgebase-querygenerationtable-name"></a>
The name of the table for which the other fields in this object apply.
*Required*: Yes
*Type*: String
*Pattern*: `^.*\..*\..*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
