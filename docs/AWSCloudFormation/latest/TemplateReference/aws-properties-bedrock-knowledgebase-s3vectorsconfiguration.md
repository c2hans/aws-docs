---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-s3vectorsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase S3VectorsConfiguration
<a name="aws-properties-bedrock-knowledgebase-s3vectorsconfiguration"></a>

Contains the storage configuration of the knowledge base for S3 vectors.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-s3vectorsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-s3vectorsconfiguration-syntax.json"></a>

```
{
  "[IndexArn](#cfn-bedrock-knowledgebase-s3vectorsconfiguration-indexarn)" : {{String}},
  "[IndexName](#cfn-bedrock-knowledgebase-s3vectorsconfiguration-indexname)" : {{String}},
  "[VectorBucketArn](#cfn-bedrock-knowledgebase-s3vectorsconfiguration-vectorbucketarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-s3vectorsconfiguration-syntax.yaml"></a>

```
  [IndexArn](#cfn-bedrock-knowledgebase-s3vectorsconfiguration-indexarn): {{String}}
  [IndexName](#cfn-bedrock-knowledgebase-s3vectorsconfiguration-indexname): {{String}}
  [VectorBucketArn](#cfn-bedrock-knowledgebase-s3vectorsconfiguration-vectorbucketarn): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-s3vectorsconfiguration-properties"></a>

`IndexArn`  <a name="cfn-bedrock-knowledgebase-s3vectorsconfiguration-indexarn"></a>
The Amazon Resource Name (ARN) of the vector index used for the knowledge base. This ARN identifies the specific vector index resource within Amazon Bedrock.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IndexName`  <a name="cfn-bedrock-knowledgebase-s3vectorsconfiguration-indexname"></a>
The name of the vector index used for the knowledge base. This name identifies the vector index within the Amazon Bedrock service.
*Required*: No
*Type*: String
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VectorBucketArn`  <a name="cfn-bedrock-knowledgebase-s3vectorsconfiguration-vectorbucketarn"></a>
The Amazon Resource Name (ARN) of the S3 bucket where vector embeddings are stored. This bucket contains the vector data used by the knowledge base.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
