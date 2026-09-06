---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-managedknowledgebaseconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase ManagedKnowledgeBaseConfiguration
<a name="aws-properties-bedrock-knowledgebase-managedknowledgebaseconfiguration"></a>

Configurations for a managed knowledge base.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-managedknowledgebaseconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-managedknowledgebaseconfiguration-syntax.json"></a>

```
{
  "[EmbeddingModelArn](#cfn-bedrock-knowledgebase-managedknowledgebaseconfiguration-embeddingmodelarn)" : {{String}},
  "[EmbeddingModelConfiguration](#cfn-bedrock-knowledgebase-managedknowledgebaseconfiguration-embeddingmodelconfiguration)" : {{EmbeddingModelConfiguration}},
  "[EmbeddingModelType](#cfn-bedrock-knowledgebase-managedknowledgebaseconfiguration-embeddingmodeltype)" : {{String}},
  "[ServerSideEncryptionConfiguration](#cfn-bedrock-knowledgebase-managedknowledgebaseconfiguration-serversideencryptionconfiguration)" : {{ManagedKnowledgeBaseServerSideEncryptionConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-managedknowledgebaseconfiguration-syntax.yaml"></a>

```
  [EmbeddingModelArn](#cfn-bedrock-knowledgebase-managedknowledgebaseconfiguration-embeddingmodelarn): {{String}}
  [EmbeddingModelConfiguration](#cfn-bedrock-knowledgebase-managedknowledgebaseconfiguration-embeddingmodelconfiguration): {{
    EmbeddingModelConfiguration}}
  [EmbeddingModelType](#cfn-bedrock-knowledgebase-managedknowledgebaseconfiguration-embeddingmodeltype): {{String}}
  [ServerSideEncryptionConfiguration](#cfn-bedrock-knowledgebase-managedknowledgebaseconfiguration-serversideencryptionconfiguration): {{
    ManagedKnowledgeBaseServerSideEncryptionConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-managedknowledgebaseconfiguration-properties"></a>

`EmbeddingModelArn`  <a name="cfn-bedrock-knowledgebase-managedknowledgebaseconfiguration-embeddingmodelarn"></a>
The ARN for the embeddings model.
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws(-[^:]+)?:[a-z0-9-]+:[a-z0-9-]{1,20}:[0-9]{0,12}:[a-zA-Z0-9-:/._+]+)$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EmbeddingModelConfiguration`  <a name="cfn-bedrock-knowledgebase-managedknowledgebaseconfiguration-embeddingmodelconfiguration"></a>
The configuration details for the embeddings model. Not required when choosing the MANAGED embeddingModelType.
*Required*: No
*Type*: [EmbeddingModelConfiguration](aws-properties-bedrock-knowledgebase-embeddingmodelconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EmbeddingModelType`  <a name="cfn-bedrock-knowledgebase-managedknowledgebaseconfiguration-embeddingmodeltype"></a>
Choose CUSTOM to provide your own Bedrock embedding model ARN. Choose MANAGED to use a service-managed embedding model.
*Required*: No
*Type*: String
*Allowed values*: `CUSTOM | MANAGED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServerSideEncryptionConfiguration`  <a name="cfn-bedrock-knowledgebase-managedknowledgebaseconfiguration-serversideencryptionconfiguration"></a>
Contains the configuration for server-side encryption for your managed knowledge base.
*Required*: No
*Type*: [ManagedKnowledgeBaseServerSideEncryptionConfiguration](aws-properties-bedrock-knowledgebase-managedknowledgebaseserversideencryptionconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
