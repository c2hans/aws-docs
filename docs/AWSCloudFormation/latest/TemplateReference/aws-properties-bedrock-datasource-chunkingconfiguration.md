---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-chunkingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource ChunkingConfiguration
<a name="aws-properties-bedrock-datasource-chunkingconfiguration"></a>

Details about how to chunk the documents in the data source. A *chunk* refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried.

## Syntax
<a name="aws-properties-bedrock-datasource-chunkingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-chunkingconfiguration-syntax.json"></a>

```
{
  "[ChunkingStrategy](#cfn-bedrock-datasource-chunkingconfiguration-chunkingstrategy)" : {{String}},
  "[FixedSizeChunkingConfiguration](#cfn-bedrock-datasource-chunkingconfiguration-fixedsizechunkingconfiguration)" : {{FixedSizeChunkingConfiguration}},
  "[HierarchicalChunkingConfiguration](#cfn-bedrock-datasource-chunkingconfiguration-hierarchicalchunkingconfiguration)" : {{HierarchicalChunkingConfiguration}},
  "[SemanticChunkingConfiguration](#cfn-bedrock-datasource-chunkingconfiguration-semanticchunkingconfiguration)" : {{SemanticChunkingConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-chunkingconfiguration-syntax.yaml"></a>

```
  [ChunkingStrategy](#cfn-bedrock-datasource-chunkingconfiguration-chunkingstrategy): {{String}}
  [FixedSizeChunkingConfiguration](#cfn-bedrock-datasource-chunkingconfiguration-fixedsizechunkingconfiguration): {{
    FixedSizeChunkingConfiguration}}
  [HierarchicalChunkingConfiguration](#cfn-bedrock-datasource-chunkingconfiguration-hierarchicalchunkingconfiguration): {{
    HierarchicalChunkingConfiguration}}
  [SemanticChunkingConfiguration](#cfn-bedrock-datasource-chunkingconfiguration-semanticchunkingconfiguration): {{
    SemanticChunkingConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-datasource-chunkingconfiguration-properties"></a>

`ChunkingStrategy`  <a name="cfn-bedrock-datasource-chunkingconfiguration-chunkingstrategy"></a>
Knowledge base can split your source data into chunks. A *chunk* refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried. You have the following options for chunking your data. If you opt for `NONE`, then you may want to pre-process your files by splitting them up such that each file corresponds to a chunk.
+ `FIXED_SIZE` – Amazon Bedrock splits your source data into chunks of the approximate size that you set in the `fixedSizeChunkingConfiguration`.
+ `HIERARCHICAL` – Split documents into layers of chunks where the first layer contains large chunks, and the second layer contains smaller chunks derived from the first layer.
+ `SEMANTIC` – Split documents into chunks based on groups of similar content derived with natural language processing.
+ `NONE` – Amazon Bedrock treats each file as one chunk. If you choose this option, you may want to pre-process your documents by splitting them into separate files.
*Required*: Yes
*Type*: String
*Allowed values*: `FIXED_SIZE | NONE | HIERARCHICAL | SEMANTIC`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FixedSizeChunkingConfiguration`  <a name="cfn-bedrock-datasource-chunkingconfiguration-fixedsizechunkingconfiguration"></a>
Configurations for when you choose fixed-size chunking. If you set the `chunkingStrategy` as `NONE`, exclude this field.
*Required*: No
*Type*: [FixedSizeChunkingConfiguration](aws-properties-bedrock-datasource-fixedsizechunkingconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HierarchicalChunkingConfiguration`  <a name="cfn-bedrock-datasource-chunkingconfiguration-hierarchicalchunkingconfiguration"></a>
Settings for hierarchical document chunking for a data source. Hierarchical chunking splits documents into layers of chunks where the first layer contains large chunks, and the second layer contains smaller chunks derived from the first layer.
*Required*: No
*Type*: [HierarchicalChunkingConfiguration](aws-properties-bedrock-datasource-hierarchicalchunkingconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SemanticChunkingConfiguration`  <a name="cfn-bedrock-datasource-chunkingconfiguration-semanticchunkingconfiguration"></a>
Settings for semantic document chunking for a data source. Semantic chunking splits a document into into smaller documents based on groups of similar content derived from the text with natural language processing.
*Required*: No
*Type*: [SemanticChunkingConfiguration](aws-properties-bedrock-datasource-semanticchunkingconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
