---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-embeddingmodelconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase EmbeddingModelConfiguration
<a name="aws-properties-bedrock-knowledgebase-embeddingmodelconfiguration"></a>

The configuration details for the embeddings model.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-embeddingmodelconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-embeddingmodelconfiguration-syntax.json"></a>

```
{
  "[BedrockEmbeddingModelConfiguration](#cfn-bedrock-knowledgebase-embeddingmodelconfiguration-bedrockembeddingmodelconfiguration)" : {{BedrockEmbeddingModelConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-embeddingmodelconfiguration-syntax.yaml"></a>

```
  [BedrockEmbeddingModelConfiguration](#cfn-bedrock-knowledgebase-embeddingmodelconfiguration-bedrockembeddingmodelconfiguration): {{
    BedrockEmbeddingModelConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-embeddingmodelconfiguration-properties"></a>

`BedrockEmbeddingModelConfiguration`  <a name="cfn-bedrock-knowledgebase-embeddingmodelconfiguration-bedrockembeddingmodelconfiguration"></a>
The vector configuration details on the Bedrock embeddings model.
*Required*: No
*Type*: [BedrockEmbeddingModelConfiguration](aws-properties-bedrock-knowledgebase-bedrockembeddingmodelconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
