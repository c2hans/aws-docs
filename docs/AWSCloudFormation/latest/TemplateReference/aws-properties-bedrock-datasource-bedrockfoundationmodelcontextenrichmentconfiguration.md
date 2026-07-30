---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-bedrockfoundationmodelcontextenrichmentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource BedrockFoundationModelContextEnrichmentConfiguration
<a name="aws-properties-bedrock-datasource-bedrockfoundationmodelcontextenrichmentconfiguration"></a>

Context enrichment configuration is used to provide additional context to the RAG application using Amazon Bedrock foundation models.

## Syntax
<a name="aws-properties-bedrock-datasource-bedrockfoundationmodelcontextenrichmentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-bedrockfoundationmodelcontextenrichmentconfiguration-syntax.json"></a>

```
{
  "[EnrichmentStrategyConfiguration](#cfn-bedrock-datasource-bedrockfoundationmodelcontextenrichmentconfiguration-enrichmentstrategyconfiguration)" : {{EnrichmentStrategyConfiguration}},
  "[ModelArn](#cfn-bedrock-datasource-bedrockfoundationmodelcontextenrichmentconfiguration-modelarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-bedrockfoundationmodelcontextenrichmentconfiguration-syntax.yaml"></a>

```
  [EnrichmentStrategyConfiguration](#cfn-bedrock-datasource-bedrockfoundationmodelcontextenrichmentconfiguration-enrichmentstrategyconfiguration): {{
    EnrichmentStrategyConfiguration}}
  [ModelArn](#cfn-bedrock-datasource-bedrockfoundationmodelcontextenrichmentconfiguration-modelarn): {{String}}
```

## Properties
<a name="aws-properties-bedrock-datasource-bedrockfoundationmodelcontextenrichmentconfiguration-properties"></a>

`EnrichmentStrategyConfiguration`  <a name="cfn-bedrock-datasource-bedrockfoundationmodelcontextenrichmentconfiguration-enrichmentstrategyconfiguration"></a>
The enrichment stategy used to provide additional context. For example, Neptune GraphRAG uses Amazon Bedrock foundation models to perform chunk entity extraction.
*Required*: Yes
*Type*: [EnrichmentStrategyConfiguration](aws-properties-bedrock-datasource-enrichmentstrategyconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelArn`  <a name="cfn-bedrock-datasource-bedrockfoundationmodelcontextenrichmentconfiguration-modelarn"></a>
The Amazon Resource Name (ARN) of the model used to create vector embeddings for the knowledge base.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:aws(-cn|-us-gov|-eusc|-iso(-[b-f])?)?:(bedrock):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
