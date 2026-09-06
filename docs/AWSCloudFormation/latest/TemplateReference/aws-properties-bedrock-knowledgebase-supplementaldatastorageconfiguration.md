---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-supplementaldatastorageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase SupplementalDataStorageConfiguration
<a name="aws-properties-bedrock-knowledgebase-supplementaldatastorageconfiguration"></a>

Specifies configurations for the storage location of multimedia content (images, audio, and video) extracted from multimodal documents in your data source. This content can be retrieved and returned to the end user with timestamp references for audio and video segments.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-supplementaldatastorageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-supplementaldatastorageconfiguration-syntax.json"></a>

```
{
  "[SupplementalDataStorageLocations](#cfn-bedrock-knowledgebase-supplementaldatastorageconfiguration-supplementaldatastoragelocations)" : {{[ SupplementalDataStorageLocation, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-supplementaldatastorageconfiguration-syntax.yaml"></a>

```
  [SupplementalDataStorageLocations](#cfn-bedrock-knowledgebase-supplementaldatastorageconfiguration-supplementaldatastoragelocations): {{
    - SupplementalDataStorageLocation}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-supplementaldatastorageconfiguration-properties"></a>

`SupplementalDataStorageLocations`  <a name="cfn-bedrock-knowledgebase-supplementaldatastorageconfiguration-supplementaldatastoragelocations"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [SupplementalDataStorageLocation](aws-properties-bedrock-knowledgebase-supplementaldatastoragelocation.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
