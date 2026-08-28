---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-knowledgebase-vectoringestionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::KnowledgeBase VectorIngestionConfiguration
<a name="aws-properties-wisdom-knowledgebase-vectoringestionconfiguration"></a>

Contains details about how to ingest the documents in a data source.

## Syntax
<a name="aws-properties-wisdom-knowledgebase-vectoringestionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-knowledgebase-vectoringestionconfiguration-syntax.json"></a>

```
{
  "[ChunkingConfiguration](#cfn-wisdom-knowledgebase-vectoringestionconfiguration-chunkingconfiguration)" : {{ChunkingConfiguration}},
  "[ParsingConfiguration](#cfn-wisdom-knowledgebase-vectoringestionconfiguration-parsingconfiguration)" : {{ParsingConfiguration}}
}
```

### YAML
<a name="aws-properties-wisdom-knowledgebase-vectoringestionconfiguration-syntax.yaml"></a>

```
  [ChunkingConfiguration](#cfn-wisdom-knowledgebase-vectoringestionconfiguration-chunkingconfiguration): {{
    ChunkingConfiguration}}
  [ParsingConfiguration](#cfn-wisdom-knowledgebase-vectoringestionconfiguration-parsingconfiguration): {{
    ParsingConfiguration}}
```

## Properties
<a name="aws-properties-wisdom-knowledgebase-vectoringestionconfiguration-properties"></a>

`ChunkingConfiguration`  <a name="cfn-wisdom-knowledgebase-vectoringestionconfiguration-chunkingconfiguration"></a>
Details about how to chunk the documents in the data source. A chunk refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried.
*Required*: No
*Type*: [ChunkingConfiguration](aws-properties-wisdom-knowledgebase-chunkingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParsingConfiguration`  <a name="cfn-wisdom-knowledgebase-vectoringestionconfiguration-parsingconfiguration"></a>
A custom parser for data source documents.
*Required*: No
*Type*: [ParsingConfiguration](aws-properties-wisdom-knowledgebase-parsingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
