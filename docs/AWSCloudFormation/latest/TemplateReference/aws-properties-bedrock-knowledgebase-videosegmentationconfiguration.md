---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-videosegmentationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase VideoSegmentationConfiguration
<a name="aws-properties-bedrock-knowledgebase-videosegmentationconfiguration"></a>

Configuration for segmenting video content during multimodal knowledge base ingestion. Determines how video files are divided into chunks for processing.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-videosegmentationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-videosegmentationconfiguration-syntax.json"></a>

```
{
  "[FixedLengthDuration](#cfn-bedrock-knowledgebase-videosegmentationconfiguration-fixedlengthduration)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-videosegmentationconfiguration-syntax.yaml"></a>

```
  [FixedLengthDuration](#cfn-bedrock-knowledgebase-videosegmentationconfiguration-fixedlengthduration): {{Integer}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-videosegmentationconfiguration-properties"></a>

`FixedLengthDuration`  <a name="cfn-bedrock-knowledgebase-videosegmentationconfiguration-fixedlengthduration"></a>
The duration in seconds for each video segment. Video files will be divided into chunks of this length for processing.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `30`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
