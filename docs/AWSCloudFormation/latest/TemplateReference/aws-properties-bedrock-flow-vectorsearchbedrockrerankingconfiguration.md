---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-vectorsearchbedrockrerankingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow VectorSearchBedrockRerankingConfiguration
<a name="aws-properties-bedrock-flow-vectorsearchbedrockrerankingconfiguration"></a>

Configuration for using Amazon Bedrock foundation models to rerank Knowledge Base vector search results. This enables more sophisticated relevance ranking using large language models.

## Syntax
<a name="aws-properties-bedrock-flow-vectorsearchbedrockrerankingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-vectorsearchbedrockrerankingconfiguration-syntax.json"></a>

```
{
  "[MetadataConfiguration](#cfn-bedrock-flow-vectorsearchbedrockrerankingconfiguration-metadataconfiguration)" : {{MetadataConfigurationForReranking}},
  "[ModelConfiguration](#cfn-bedrock-flow-vectorsearchbedrockrerankingconfiguration-modelconfiguration)" : {{VectorSearchBedrockRerankingModelConfiguration}},
  "[NumberOfRerankedResults](#cfn-bedrock-flow-vectorsearchbedrockrerankingconfiguration-numberofrerankedresults)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-vectorsearchbedrockrerankingconfiguration-syntax.yaml"></a>

```
  [MetadataConfiguration](#cfn-bedrock-flow-vectorsearchbedrockrerankingconfiguration-metadataconfiguration): {{
    MetadataConfigurationForReranking}}
  [ModelConfiguration](#cfn-bedrock-flow-vectorsearchbedrockrerankingconfiguration-modelconfiguration): {{
    VectorSearchBedrockRerankingModelConfiguration}}
  [NumberOfRerankedResults](#cfn-bedrock-flow-vectorsearchbedrockrerankingconfiguration-numberofrerankedresults): {{
    Number}}
```

## Properties
<a name="aws-properties-bedrock-flow-vectorsearchbedrockrerankingconfiguration-properties"></a>

`MetadataConfiguration`  <a name="cfn-bedrock-flow-vectorsearchbedrockrerankingconfiguration-metadataconfiguration"></a>
Configuration for how document metadata should be used during the reranking process. This determines which metadata fields are included when reordering search results.
*Required*: No
*Type*: [MetadataConfigurationForReranking](aws-properties-bedrock-flow-metadataconfigurationforreranking.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelConfiguration`  <a name="cfn-bedrock-flow-vectorsearchbedrockrerankingconfiguration-modelconfiguration"></a>
Configuration for the Amazon Bedrock foundation model used for reranking. This includes the model ARN and any additional request fields required by the model.
*Required*: Yes
*Type*: [VectorSearchBedrockRerankingModelConfiguration](aws-properties-bedrock-flow-vectorsearchbedrockrerankingmodelconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberOfRerankedResults`  <a name="cfn-bedrock-flow-vectorsearchbedrockrerankingconfiguration-numberofrerankedresults"></a>
The maximum number of results to rerank. This limits how many of the initial vector search results will be processed by the reranking model. A smaller number improves performance but may exclude potentially relevant results.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
