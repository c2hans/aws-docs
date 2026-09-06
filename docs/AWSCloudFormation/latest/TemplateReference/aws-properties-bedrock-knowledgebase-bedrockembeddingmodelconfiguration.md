---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-bedrockembeddingmodelconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase BedrockEmbeddingModelConfiguration
<a name="aws-properties-bedrock-knowledgebase-bedrockembeddingmodelconfiguration"></a>

The vector configuration details for the Bedrock embeddings model.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-bedrockembeddingmodelconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-bedrockembeddingmodelconfiguration-syntax.json"></a>

```
{
  "[Audio](#cfn-bedrock-knowledgebase-bedrockembeddingmodelconfiguration-audio)" : {{[ AudioConfiguration, ... ]}},
  "[Dimensions](#cfn-bedrock-knowledgebase-bedrockembeddingmodelconfiguration-dimensions)" : {{Integer}},
  "[EmbeddingDataType](#cfn-bedrock-knowledgebase-bedrockembeddingmodelconfiguration-embeddingdatatype)" : {{String}},
  "[Video](#cfn-bedrock-knowledgebase-bedrockembeddingmodelconfiguration-video)" : {{[ VideoConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-bedrockembeddingmodelconfiguration-syntax.yaml"></a>

```
  [Audio](#cfn-bedrock-knowledgebase-bedrockembeddingmodelconfiguration-audio): {{
    - AudioConfiguration}}
  [Dimensions](#cfn-bedrock-knowledgebase-bedrockembeddingmodelconfiguration-dimensions): {{Integer}}
  [EmbeddingDataType](#cfn-bedrock-knowledgebase-bedrockembeddingmodelconfiguration-embeddingdatatype): {{String}}
  [Video](#cfn-bedrock-knowledgebase-bedrockembeddingmodelconfiguration-video): {{
    - VideoConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-bedrockembeddingmodelconfiguration-properties"></a>

`Audio`  <a name="cfn-bedrock-knowledgebase-bedrockembeddingmodelconfiguration-audio"></a>
Configuration settings for processing audio content in multimodal knowledge bases.
*Required*: No
*Type*: Array of [AudioConfiguration](aws-properties-bedrock-knowledgebase-audioconfiguration.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Dimensions`  <a name="cfn-bedrock-knowledgebase-bedrockembeddingmodelconfiguration-dimensions"></a>
The dimensions details for the vector configuration used on the Bedrock embeddings model.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EmbeddingDataType`  <a name="cfn-bedrock-knowledgebase-bedrockembeddingmodelconfiguration-embeddingdatatype"></a>
The data type for the vectors when using a model to convert text into vector embeddings. The model must support the specified data type for vector embeddings. Floating-point (float32) is the default data type, and is supported by most models for vector embeddings. See [Supported embeddings models](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-supported.html) for information on the available models and their vector data types.
*Required*: No
*Type*: String
*Allowed values*: `FLOAT32 | BINARY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Video`  <a name="cfn-bedrock-knowledgebase-bedrockembeddingmodelconfiguration-video"></a>
Configuration settings for processing video content in multimodal knowledge bases.
*Required*: No
*Type*: Array of [VideoConfiguration](aws-properties-bedrock-knowledgebase-videoconfiguration.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
