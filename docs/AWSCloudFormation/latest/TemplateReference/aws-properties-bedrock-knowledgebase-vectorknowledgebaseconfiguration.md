---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-vectorknowledgebaseconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase VectorKnowledgeBaseConfiguration
<a name="aws-properties-bedrock-knowledgebase-vectorknowledgebaseconfiguration"></a>

Contains details about the model used to create vector embeddings for the knowledge base.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-vectorknowledgebaseconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-vectorknowledgebaseconfiguration-syntax.json"></a>

```
{
  "[EmbeddingModelArn](#cfn-bedrock-knowledgebase-vectorknowledgebaseconfiguration-embeddingmodelarn)" : {{String}},
  "[EmbeddingModelConfiguration](#cfn-bedrock-knowledgebase-vectorknowledgebaseconfiguration-embeddingmodelconfiguration)" : {{EmbeddingModelConfiguration}},
  "[SupplementalDataStorageConfiguration](#cfn-bedrock-knowledgebase-vectorknowledgebaseconfiguration-supplementaldatastorageconfiguration)" : {{SupplementalDataStorageConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-vectorknowledgebaseconfiguration-syntax.yaml"></a>

```
  [EmbeddingModelArn](#cfn-bedrock-knowledgebase-vectorknowledgebaseconfiguration-embeddingmodelarn): {{String}}
  [EmbeddingModelConfiguration](#cfn-bedrock-knowledgebase-vectorknowledgebaseconfiguration-embeddingmodelconfiguration): {{
    EmbeddingModelConfiguration}}
  [SupplementalDataStorageConfiguration](#cfn-bedrock-knowledgebase-vectorknowledgebaseconfiguration-supplementaldatastorageconfiguration): {{
    SupplementalDataStorageConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-vectorknowledgebaseconfiguration-properties"></a>

`EmbeddingModelArn`  <a name="cfn-bedrock-knowledgebase-vectorknowledgebaseconfiguration-embeddingmodelarn"></a>
The Amazon Resource Name (ARN) of the model used to create vector embeddings for the knowledge base.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:aws(-[^:]+)?:[a-z0-9-]+:[a-z0-9-]{1,20}:[0-9]{0,12}:[a-zA-Z0-9-:/._+]+)$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EmbeddingModelConfiguration`  <a name="cfn-bedrock-knowledgebase-vectorknowledgebaseconfiguration-embeddingmodelconfiguration"></a>
The embeddings model configuration details for the vector model used in Knowledge Base.
*Required*: No
*Type*: [EmbeddingModelConfiguration](aws-properties-bedrock-knowledgebase-embeddingmodelconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SupplementalDataStorageConfiguration`  <a name="cfn-bedrock-knowledgebase-vectorknowledgebaseconfiguration-supplementaldatastorageconfiguration"></a>
If you include multimodal data from your data source, use this object to specify configurations for the storage location of the images extracted from your documents. These images can be retrieved and returned to the end user. They can also be used in generation when using [RetrieveAndGenerate](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html).
*Required*: No
*Type*: [SupplementalDataStorageConfiguration](aws-properties-bedrock-knowledgebase-supplementaldatastorageconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
