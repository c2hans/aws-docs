---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-querygenerationcontext.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase QueryGenerationContext
<a name="aws-properties-bedrock-knowledgebase-querygenerationcontext"></a>

>Contains configurations for context to use during query generation.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-querygenerationcontext-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-querygenerationcontext-syntax.json"></a>

```
{
  "[CuratedQueries](#cfn-bedrock-knowledgebase-querygenerationcontext-curatedqueries)" : {{[ CuratedQuery, ... ]}},
  "[Tables](#cfn-bedrock-knowledgebase-querygenerationcontext-tables)" : {{[ QueryGenerationTable, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-querygenerationcontext-syntax.yaml"></a>

```
  [CuratedQueries](#cfn-bedrock-knowledgebase-querygenerationcontext-curatedqueries): {{
    - CuratedQuery}}
  [Tables](#cfn-bedrock-knowledgebase-querygenerationcontext-tables): {{
    - QueryGenerationTable}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-querygenerationcontext-properties"></a>

`CuratedQueries`  <a name="cfn-bedrock-knowledgebase-querygenerationcontext-curatedqueries"></a>
An array of objects, each of which defines information about example queries to help the query engine generate appropriate SQL queries.
*Required*: No
*Type*: Array of [CuratedQuery](aws-properties-bedrock-knowledgebase-curatedquery.md)
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tables`  <a name="cfn-bedrock-knowledgebase-querygenerationcontext-tables"></a>
An array of objects, each of which defines information about a table in the database.
*Required*: No
*Type*: Array of [QueryGenerationTable](aws-properties-bedrock-knowledgebase-querygenerationtable.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
