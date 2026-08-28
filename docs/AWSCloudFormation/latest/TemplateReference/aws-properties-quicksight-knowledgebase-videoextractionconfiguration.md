---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-knowledgebase-videoextractionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::KnowledgeBase VideoExtractionConfiguration
<a name="aws-properties-quicksight-knowledgebase-videoextractionconfiguration"></a>

The configuration for video extraction from knowledge base documents.

## Syntax
<a name="aws-properties-quicksight-knowledgebase-videoextractionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-knowledgebase-videoextractionconfiguration-syntax.json"></a>

```
{
  "[VideoExtractionStatus](#cfn-quicksight-knowledgebase-videoextractionconfiguration-videoextractionstatus)" : {{String}},
  "[VideoExtractionType](#cfn-quicksight-knowledgebase-videoextractionconfiguration-videoextractiontype)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-knowledgebase-videoextractionconfiguration-syntax.yaml"></a>

```
  [VideoExtractionStatus](#cfn-quicksight-knowledgebase-videoextractionconfiguration-videoextractionstatus): {{String}}
  [VideoExtractionType](#cfn-quicksight-knowledgebase-videoextractionconfiguration-videoextractiontype): {{String}}
```

## Properties
<a name="aws-properties-quicksight-knowledgebase-videoextractionconfiguration-properties"></a>

`VideoExtractionStatus`  <a name="cfn-quicksight-knowledgebase-videoextractionconfiguration-videoextractionstatus"></a>
The status of video extraction. Valid values are ENABLED and DISABLED.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VideoExtractionType`  <a name="cfn-quicksight-knowledgebase-videoextractionconfiguration-videoextractiontype"></a>
The type of video extraction to perform.
*Required*: No
*Type*: String
*Allowed values*: `AUDIO_TRANSCRIPTION_ONLY | VISUAL_CONTENT_AND_AUDIO_TRANSCRIPTION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
