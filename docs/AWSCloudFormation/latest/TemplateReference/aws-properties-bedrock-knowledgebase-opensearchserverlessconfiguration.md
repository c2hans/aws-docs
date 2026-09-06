---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-opensearchserverlessconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase OpenSearchServerlessConfiguration
<a name="aws-properties-bedrock-knowledgebase-opensearchserverlessconfiguration"></a>

Contains details about the storage configuration of the knowledge base in Amazon OpenSearch Service. For more information, see [Create a vector index in Amazon OpenSearch Service](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-oss.html).

## Syntax
<a name="aws-properties-bedrock-knowledgebase-opensearchserverlessconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-opensearchserverlessconfiguration-syntax.json"></a>

```
{
  "[CollectionArn](#cfn-bedrock-knowledgebase-opensearchserverlessconfiguration-collectionarn)" : {{String}},
  "[FieldMapping](#cfn-bedrock-knowledgebase-opensearchserverlessconfiguration-fieldmapping)" : {{OpenSearchServerlessFieldMapping}},
  "[VectorIndexName](#cfn-bedrock-knowledgebase-opensearchserverlessconfiguration-vectorindexname)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-opensearchserverlessconfiguration-syntax.yaml"></a>

```
  [CollectionArn](#cfn-bedrock-knowledgebase-opensearchserverlessconfiguration-collectionarn): {{String}}
  [FieldMapping](#cfn-bedrock-knowledgebase-opensearchserverlessconfiguration-fieldmapping): {{
    OpenSearchServerlessFieldMapping}}
  [VectorIndexName](#cfn-bedrock-knowledgebase-opensearchserverlessconfiguration-vectorindexname): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-opensearchserverlessconfiguration-properties"></a>

`CollectionArn`  <a name="cfn-bedrock-knowledgebase-opensearchserverlessconfiguration-collectionarn"></a>
The Amazon Resource Name (ARN) of the OpenSearch Service vector store.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov|-iso):aoss:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:collection/[a-z0-9-]{3,32}$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FieldMapping`  <a name="cfn-bedrock-knowledgebase-opensearchserverlessconfiguration-fieldmapping"></a>
Contains the names of the fields to which to map information about the vector store.
*Required*: Yes
*Type*: [OpenSearchServerlessFieldMapping](aws-properties-bedrock-knowledgebase-opensearchserverlessfieldmapping.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VectorIndexName`  <a name="cfn-bedrock-knowledgebase-opensearchserverlessconfiguration-vectorindexname"></a>
The name of the vector store.
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
