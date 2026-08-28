---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-vectoringestionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource VectorIngestionConfiguration
<a name="aws-properties-bedrock-datasource-vectoringestionconfiguration"></a>

Contains details about how to ingest the documents in a data source.

## Syntax
<a name="aws-properties-bedrock-datasource-vectoringestionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-vectoringestionconfiguration-syntax.json"></a>

```
{
  "[ChunkingConfiguration](#cfn-bedrock-datasource-vectoringestionconfiguration-chunkingconfiguration)" : {{ChunkingConfiguration}},
  "[ContextEnrichmentConfiguration](#cfn-bedrock-datasource-vectoringestionconfiguration-contextenrichmentconfiguration)" : {{ContextEnrichmentConfiguration}},
  "[CustomTransformationConfiguration](#cfn-bedrock-datasource-vectoringestionconfiguration-customtransformationconfiguration)" : {{CustomTransformationConfiguration}},
  "[ParsingConfiguration](#cfn-bedrock-datasource-vectoringestionconfiguration-parsingconfiguration)" : {{ParsingConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-vectoringestionconfiguration-syntax.yaml"></a>

```
  [ChunkingConfiguration](#cfn-bedrock-datasource-vectoringestionconfiguration-chunkingconfiguration): {{
    ChunkingConfiguration}}
  [ContextEnrichmentConfiguration](#cfn-bedrock-datasource-vectoringestionconfiguration-contextenrichmentconfiguration): {{
    ContextEnrichmentConfiguration}}
  [CustomTransformationConfiguration](#cfn-bedrock-datasource-vectoringestionconfiguration-customtransformationconfiguration): {{
    CustomTransformationConfiguration}}
  [ParsingConfiguration](#cfn-bedrock-datasource-vectoringestionconfiguration-parsingconfiguration): {{
    ParsingConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-datasource-vectoringestionconfiguration-properties"></a>

`ChunkingConfiguration`  <a name="cfn-bedrock-datasource-vectoringestionconfiguration-chunkingconfiguration"></a>
Details about how to chunk the documents in the data source. A *chunk* refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried.
*Required*: No
*Type*: [ChunkingConfiguration](aws-properties-bedrock-datasource-chunkingconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContextEnrichmentConfiguration`  <a name="cfn-bedrock-datasource-vectoringestionconfiguration-contextenrichmentconfiguration"></a>
The context enrichment configuration used for ingestion of the data into the vector store.
*Required*: No
*Type*: [ContextEnrichmentConfiguration](aws-properties-bedrock-datasource-contextenrichmentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomTransformationConfiguration`  <a name="cfn-bedrock-datasource-vectoringestionconfiguration-customtransformationconfiguration"></a>
A custom document transformer for parsed data source documents.
*Required*: No
*Type*: [CustomTransformationConfiguration](aws-properties-bedrock-datasource-customtransformationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParsingConfiguration`  <a name="cfn-bedrock-datasource-vectoringestionconfiguration-parsingconfiguration"></a>
Configurations for a parser to use for parsing documents in your data source. If you exclude this field, the default parser will be used.
*Required*: No
*Type*: [ParsingConfiguration](aws-properties-bedrock-datasource-parsingconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
