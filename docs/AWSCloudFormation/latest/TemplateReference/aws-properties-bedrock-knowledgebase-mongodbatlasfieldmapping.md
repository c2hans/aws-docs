---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-mongodbatlasfieldmapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase MongoDbAtlasFieldMapping
<a name="aws-properties-bedrock-knowledgebase-mongodbatlasfieldmapping"></a>

Contains the names of the fields to which to map information about the vector store.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-mongodbatlasfieldmapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-mongodbatlasfieldmapping-syntax.json"></a>

```
{
  "[MetadataField](#cfn-bedrock-knowledgebase-mongodbatlasfieldmapping-metadatafield)" : {{String}},
  "[TextField](#cfn-bedrock-knowledgebase-mongodbatlasfieldmapping-textfield)" : {{String}},
  "[VectorField](#cfn-bedrock-knowledgebase-mongodbatlasfieldmapping-vectorfield)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-mongodbatlasfieldmapping-syntax.yaml"></a>

```
  [MetadataField](#cfn-bedrock-knowledgebase-mongodbatlasfieldmapping-metadatafield): {{String}}
  [TextField](#cfn-bedrock-knowledgebase-mongodbatlasfieldmapping-textfield): {{String}}
  [VectorField](#cfn-bedrock-knowledgebase-mongodbatlasfieldmapping-vectorfield): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-mongodbatlasfieldmapping-properties"></a>

`MetadataField`  <a name="cfn-bedrock-knowledgebase-mongodbatlasfieldmapping-metadatafield"></a>
The name of the field in which Amazon Bedrock stores metadata about the vector store.
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TextField`  <a name="cfn-bedrock-knowledgebase-mongodbatlasfieldmapping-textfield"></a>
The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VectorField`  <a name="cfn-bedrock-knowledgebase-mongodbatlasfieldmapping-vectorfield"></a>
The name of the field in which Amazon Bedrock stores the vector embeddings for your data sources.
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
