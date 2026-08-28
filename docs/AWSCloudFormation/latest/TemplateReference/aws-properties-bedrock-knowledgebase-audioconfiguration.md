---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-audioconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase AudioConfiguration
<a name="aws-properties-bedrock-knowledgebase-audioconfiguration"></a>

Configuration settings for processing audio content in multimodal knowledge bases.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-audioconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-audioconfiguration-syntax.json"></a>

```
{
  "[SegmentationConfiguration](#cfn-bedrock-knowledgebase-audioconfiguration-segmentationconfiguration)" : {{AudioSegmentationConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-audioconfiguration-syntax.yaml"></a>

```
  [SegmentationConfiguration](#cfn-bedrock-knowledgebase-audioconfiguration-segmentationconfiguration): {{
    AudioSegmentationConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-audioconfiguration-properties"></a>

`SegmentationConfiguration`  <a name="cfn-bedrock-knowledgebase-audioconfiguration-segmentationconfiguration"></a>
Configuration for segmenting audio content during processing.
*Required*: Yes
*Type*: [AudioSegmentationConfiguration](aws-properties-bedrock-knowledgebase-audiosegmentationconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
