---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-vectorsearchrerankingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion VectorSearchRerankingConfiguration
<a name="aws-properties-bedrock-flowversion-vectorsearchrerankingconfiguration"></a>

Configuration for reranking vector search results to improve relevance. Reranking applies additional relevance models to reorder the initial vector search results based on more sophisticated criteria.

## Syntax
<a name="aws-properties-bedrock-flowversion-vectorsearchrerankingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-vectorsearchrerankingconfiguration-syntax.json"></a>

```
{
  "[BedrockRerankingConfiguration](#cfn-bedrock-flowversion-vectorsearchrerankingconfiguration-bedrockrerankingconfiguration)" : {{VectorSearchBedrockRerankingConfiguration}},
  "[Type](#cfn-bedrock-flowversion-vectorsearchrerankingconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-vectorsearchrerankingconfiguration-syntax.yaml"></a>

```
  [BedrockRerankingConfiguration](#cfn-bedrock-flowversion-vectorsearchrerankingconfiguration-bedrockrerankingconfiguration): {{
    VectorSearchBedrockRerankingConfiguration}}
  [Type](#cfn-bedrock-flowversion-vectorsearchrerankingconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-vectorsearchrerankingconfiguration-properties"></a>

`BedrockRerankingConfiguration`  <a name="cfn-bedrock-flowversion-vectorsearchrerankingconfiguration-bedrockrerankingconfiguration"></a>
Configuration for using Amazon Bedrock foundation models to rerank search results. This is required when the reranking type is set to BEDROCK.
*Required*: No
*Type*: [VectorSearchBedrockRerankingConfiguration](aws-properties-bedrock-flowversion-vectorsearchbedrockrerankingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrock-flowversion-vectorsearchrerankingconfiguration-type"></a>
The type of reranking to apply to vector search results. Currently, the only supported value is BEDROCK, which uses Amazon Bedrock foundation models for reranking.
*Required*: Yes
*Type*: String
*Allowed values*: `BEDROCK_RERANKING_MODEL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
