---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-supplementaldatastoragelocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase SupplementalDataStorageLocation
<a name="aws-properties-bedrock-knowledgebase-supplementaldatastoragelocation"></a>

Contains information about a storage location for multimedia content (images, audio, and video) extracted from multimodal documents in your data source.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-supplementaldatastoragelocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-supplementaldatastoragelocation-syntax.json"></a>

```
{
  "[S3Location](#cfn-bedrock-knowledgebase-supplementaldatastoragelocation-s3location)" : {{S3Location}},
  "[SupplementalDataStorageLocationType](#cfn-bedrock-knowledgebase-supplementaldatastoragelocation-supplementaldatastoragelocationtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-supplementaldatastoragelocation-syntax.yaml"></a>

```
  [S3Location](#cfn-bedrock-knowledgebase-supplementaldatastoragelocation-s3location): {{
    S3Location}}
  [SupplementalDataStorageLocationType](#cfn-bedrock-knowledgebase-supplementaldatastoragelocation-supplementaldatastoragelocationtype): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-supplementaldatastoragelocation-properties"></a>

`S3Location`  <a name="cfn-bedrock-knowledgebase-supplementaldatastoragelocation-s3location"></a>
Contains information about the Amazon S3 location for the extracted multimedia content.
*Required*: No
*Type*: [S3Location](aws-properties-bedrock-knowledgebase-s3location.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SupplementalDataStorageLocationType`  <a name="cfn-bedrock-knowledgebase-supplementaldatastoragelocation-supplementaldatastoragelocationtype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `S3`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
