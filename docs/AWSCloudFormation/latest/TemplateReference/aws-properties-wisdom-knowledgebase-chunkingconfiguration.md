---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-knowledgebase-chunkingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::KnowledgeBase ChunkingConfiguration
<a name="aws-properties-wisdom-knowledgebase-chunkingconfiguration"></a>

Details about how to chunk the documents in the data source. A chunk refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried.

## Syntax
<a name="aws-properties-wisdom-knowledgebase-chunkingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-knowledgebase-chunkingconfiguration-syntax.json"></a>

```
{
  "[ChunkingStrategy](#cfn-wisdom-knowledgebase-chunkingconfiguration-chunkingstrategy)" : {{String}},
  "[FixedSizeChunkingConfiguration](#cfn-wisdom-knowledgebase-chunkingconfiguration-fixedsizechunkingconfiguration)" : {{FixedSizeChunkingConfiguration}},
  "[HierarchicalChunkingConfiguration](#cfn-wisdom-knowledgebase-chunkingconfiguration-hierarchicalchunkingconfiguration)" : {{HierarchicalChunkingConfiguration}},
  "[SemanticChunkingConfiguration](#cfn-wisdom-knowledgebase-chunkingconfiguration-semanticchunkingconfiguration)" : {{SemanticChunkingConfiguration}}
}
```

### YAML
<a name="aws-properties-wisdom-knowledgebase-chunkingconfiguration-syntax.yaml"></a>

```
  [ChunkingStrategy](#cfn-wisdom-knowledgebase-chunkingconfiguration-chunkingstrategy): {{String}}
  [FixedSizeChunkingConfiguration](#cfn-wisdom-knowledgebase-chunkingconfiguration-fixedsizechunkingconfiguration): {{
    FixedSizeChunkingConfiguration}}
  [HierarchicalChunkingConfiguration](#cfn-wisdom-knowledgebase-chunkingconfiguration-hierarchicalchunkingconfiguration): {{
    HierarchicalChunkingConfiguration}}
  [SemanticChunkingConfiguration](#cfn-wisdom-knowledgebase-chunkingconfiguration-semanticchunkingconfiguration): {{
    SemanticChunkingConfiguration}}
```

## Properties
<a name="aws-properties-wisdom-knowledgebase-chunkingconfiguration-properties"></a>

`ChunkingStrategy`  <a name="cfn-wisdom-knowledgebase-chunkingconfiguration-chunkingstrategy"></a>
Knowledge base can split your source data into chunks. A chunk refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried. You have the following options for chunking your data. If you opt for `NONE`, then you may want to pre-process your files by splitting them up such that each file corresponds to a chunk.
*Required*: Yes
*Type*: String
*Allowed values*: `FIXED_SIZE | NONE | HIERARCHICAL | SEMANTIC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FixedSizeChunkingConfiguration`  <a name="cfn-wisdom-knowledgebase-chunkingconfiguration-fixedsizechunkingconfiguration"></a>
Configurations for when you choose fixed-size chunking. If you set the `chunkingStrategy` as `NONE`, exclude this field.
*Required*: No
*Type*: [FixedSizeChunkingConfiguration](aws-properties-wisdom-knowledgebase-fixedsizechunkingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HierarchicalChunkingConfiguration`  <a name="cfn-wisdom-knowledgebase-chunkingconfiguration-hierarchicalchunkingconfiguration"></a>
Settings for hierarchical document chunking for a data source. Hierarchical chunking splits documents into layers of chunks where the first layer contains large chunks, and the second layer contains smaller chunks derived from the first layer.
*Required*: No
*Type*: [HierarchicalChunkingConfiguration](aws-properties-wisdom-knowledgebase-hierarchicalchunkingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SemanticChunkingConfiguration`  <a name="cfn-wisdom-knowledgebase-chunkingconfiguration-semanticchunkingconfiguration"></a>
Settings for semantic document chunking for a data source. Semantic chunking splits a document into smaller documents based on groups of similar content derived from the text with natural language processing.
*Required*: No
*Type*: [SemanticChunkingConfiguration](aws-properties-wisdom-knowledgebase-semanticchunkingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
