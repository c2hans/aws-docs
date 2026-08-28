---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-videoconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase VideoConfiguration
<a name="aws-properties-bedrock-knowledgebase-videoconfiguration"></a>

Configuration settings for processing video content in multimodal knowledge bases.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-videoconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-videoconfiguration-syntax.json"></a>

```
{
  "[SegmentationConfiguration](#cfn-bedrock-knowledgebase-videoconfiguration-segmentationconfiguration)" : {{VideoSegmentationConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-videoconfiguration-syntax.yaml"></a>

```
  [SegmentationConfiguration](#cfn-bedrock-knowledgebase-videoconfiguration-segmentationconfiguration): {{
    VideoSegmentationConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-videoconfiguration-properties"></a>

`SegmentationConfiguration`  <a name="cfn-bedrock-knowledgebase-videoconfiguration-segmentationconfiguration"></a>
Configuration for segmenting video content during processing.
*Required*: Yes
*Type*: [VideoSegmentationConfiguration](aws-properties-bedrock-knowledgebase-videosegmentationconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
