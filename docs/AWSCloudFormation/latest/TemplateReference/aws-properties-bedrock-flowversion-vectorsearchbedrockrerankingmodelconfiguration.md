---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-vectorsearchbedrockrerankingmodelconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion VectorSearchBedrockRerankingModelConfiguration
<a name="aws-properties-bedrock-flowversion-vectorsearchbedrockrerankingmodelconfiguration"></a>

Configuration for the Amazon Bedrock foundation model used for reranking vector search results. This specifies which model to use and any additional parameters required by the model.

## Syntax
<a name="aws-properties-bedrock-flowversion-vectorsearchbedrockrerankingmodelconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-vectorsearchbedrockrerankingmodelconfiguration-syntax.json"></a>

```
{
  "[AdditionalModelRequestFields](#cfn-bedrock-flowversion-vectorsearchbedrockrerankingmodelconfiguration-additionalmodelrequestfields)" : {{Json}},
  "[ModelArn](#cfn-bedrock-flowversion-vectorsearchbedrockrerankingmodelconfiguration-modelarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-vectorsearchbedrockrerankingmodelconfiguration-syntax.yaml"></a>

```
  [AdditionalModelRequestFields](#cfn-bedrock-flowversion-vectorsearchbedrockrerankingmodelconfiguration-additionalmodelrequestfields): {{Json}}
  [ModelArn](#cfn-bedrock-flowversion-vectorsearchbedrockrerankingmodelconfiguration-modelarn): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-vectorsearchbedrockrerankingmodelconfiguration-properties"></a>

`AdditionalModelRequestFields`  <a name="cfn-bedrock-flowversion-vectorsearchbedrockrerankingmodelconfiguration-additionalmodelrequestfields"></a>
A list of additional fields to include in the model request during reranking. These fields provide extra context or configuration options specific to the selected foundation model.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelArn`  <a name="cfn-bedrock-flowversion-vectorsearchbedrockrerankingmodelconfiguration-modelarn"></a>
The Amazon Resource Name (ARN) of the foundation model to use for reranking. This model processes the query and search results to determine a more relevant ordering.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model/(.*))?$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
