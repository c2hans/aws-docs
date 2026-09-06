---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-contextenrichmentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource ContextEnrichmentConfiguration
<a name="aws-properties-bedrock-datasource-contextenrichmentconfiguration"></a>

Context enrichment configuration is used to provide additional context to the RAG application.

## Syntax
<a name="aws-properties-bedrock-datasource-contextenrichmentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-contextenrichmentconfiguration-syntax.json"></a>

```
{
  "[BedrockFoundationModelConfiguration](#cfn-bedrock-datasource-contextenrichmentconfiguration-bedrockfoundationmodelconfiguration)" : {{BedrockFoundationModelContextEnrichmentConfiguration}},
  "[Type](#cfn-bedrock-datasource-contextenrichmentconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-contextenrichmentconfiguration-syntax.yaml"></a>

```
  [BedrockFoundationModelConfiguration](#cfn-bedrock-datasource-contextenrichmentconfiguration-bedrockfoundationmodelconfiguration): {{
    BedrockFoundationModelContextEnrichmentConfiguration}}
  [Type](#cfn-bedrock-datasource-contextenrichmentconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-bedrock-datasource-contextenrichmentconfiguration-properties"></a>

`BedrockFoundationModelConfiguration`  <a name="cfn-bedrock-datasource-contextenrichmentconfiguration-bedrockfoundationmodelconfiguration"></a>
The configuration of the Amazon Bedrock foundation model used for context enrichment.
*Required*: No
*Type*: [BedrockFoundationModelContextEnrichmentConfiguration](aws-properties-bedrock-datasource-bedrockfoundationmodelcontextenrichmentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrock-datasource-contextenrichmentconfiguration-type"></a>
The method used for context enrichment. It must be Amazon Bedrock foundation models.
*Required*: Yes
*Type*: String
*Allowed values*: `BEDROCK_FOUNDATION_MODEL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
