---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-opensearchserverlessfieldmapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase OpenSearchServerlessFieldMapping
<a name="aws-properties-bedrock-knowledgebase-opensearchserverlessfieldmapping"></a>

Contains the names of the fields to which to map information about the vector store.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-opensearchserverlessfieldmapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-opensearchserverlessfieldmapping-syntax.json"></a>

```
{
  "[MetadataField](#cfn-bedrock-knowledgebase-opensearchserverlessfieldmapping-metadatafield)" : {{String}},
  "[TextField](#cfn-bedrock-knowledgebase-opensearchserverlessfieldmapping-textfield)" : {{String}},
  "[VectorField](#cfn-bedrock-knowledgebase-opensearchserverlessfieldmapping-vectorfield)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-opensearchserverlessfieldmapping-syntax.yaml"></a>

```
  [MetadataField](#cfn-bedrock-knowledgebase-opensearchserverlessfieldmapping-metadatafield): {{String}}
  [TextField](#cfn-bedrock-knowledgebase-opensearchserverlessfieldmapping-textfield): {{String}}
  [VectorField](#cfn-bedrock-knowledgebase-opensearchserverlessfieldmapping-vectorfield): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-opensearchserverlessfieldmapping-properties"></a>

`MetadataField`  <a name="cfn-bedrock-knowledgebase-opensearchserverlessfieldmapping-metadatafield"></a>
The name of the field in which Amazon Bedrock stores metadata about the vector store.
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TextField`  <a name="cfn-bedrock-knowledgebase-opensearchserverlessfieldmapping-textfield"></a>
The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VectorField`  <a name="cfn-bedrock-knowledgebase-opensearchserverlessfieldmapping-vectorfield"></a>
The name of the field in which Amazon Bedrock stores the vector embeddings for your data sources.
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
