---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-querygenerationcolumn.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase QueryGenerationColumn
<a name="aws-properties-bedrock-knowledgebase-querygenerationcolumn"></a>

Contains information about a column in the current table for the query engine to consider.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-querygenerationcolumn-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-querygenerationcolumn-syntax.json"></a>

```
{
  "[Description](#cfn-bedrock-knowledgebase-querygenerationcolumn-description)" : {{String}},
  "[Inclusion](#cfn-bedrock-knowledgebase-querygenerationcolumn-inclusion)" : {{String}},
  "[Name](#cfn-bedrock-knowledgebase-querygenerationcolumn-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-querygenerationcolumn-syntax.yaml"></a>

```
  [Description](#cfn-bedrock-knowledgebase-querygenerationcolumn-description): {{String}}
  [Inclusion](#cfn-bedrock-knowledgebase-querygenerationcolumn-inclusion): {{String}}
  [Name](#cfn-bedrock-knowledgebase-querygenerationcolumn-name): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-querygenerationcolumn-properties"></a>

`Description`  <a name="cfn-bedrock-knowledgebase-querygenerationcolumn-description"></a>
A description of the column that helps the query engine understand the contents of the column.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Inclusion`  <a name="cfn-bedrock-knowledgebase-querygenerationcolumn-inclusion"></a>
Specifies whether to include or exclude the column during query generation. If you specify `EXCLUDE`, the column will be ignored. If you specify `INCLUDE`, all other columns in the table will be ignored.
*Required*: No
*Type*: String
*Allowed values*: `INCLUDE | EXCLUDE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrock-knowledgebase-querygenerationcolumn-name"></a>
The name of the column for which the other fields in this object apply.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
