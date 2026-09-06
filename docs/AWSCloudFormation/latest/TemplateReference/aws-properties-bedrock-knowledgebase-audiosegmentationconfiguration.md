---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-audiosegmentationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase AudioSegmentationConfiguration
<a name="aws-properties-bedrock-knowledgebase-audiosegmentationconfiguration"></a>

Configuration for segmenting audio content during multimodal knowledge base ingestion. Determines how audio files are divided into chunks for processing.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-audiosegmentationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-audiosegmentationconfiguration-syntax.json"></a>

```
{
  "[FixedLengthDuration](#cfn-bedrock-knowledgebase-audiosegmentationconfiguration-fixedlengthduration)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-audiosegmentationconfiguration-syntax.yaml"></a>

```
  [FixedLengthDuration](#cfn-bedrock-knowledgebase-audiosegmentationconfiguration-fixedlengthduration): {{Integer}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-audiosegmentationconfiguration-properties"></a>

`FixedLengthDuration`  <a name="cfn-bedrock-knowledgebase-audiosegmentationconfiguration-fixedlengthduration"></a>
The duration in seconds for each audio segment. Audio files will be divided into chunks of this length for processing.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `30`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
