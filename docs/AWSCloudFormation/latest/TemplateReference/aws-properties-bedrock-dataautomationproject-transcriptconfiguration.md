---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-transcriptconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject TranscriptConfiguration
<a name="aws-properties-bedrock-dataautomationproject-transcriptconfiguration"></a>

Configuration for transcript options. This option allows you to enable speaker labeling and channel labeling.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-transcriptconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-transcriptconfiguration-syntax.json"></a>

```
{
  "[ChannelLabeling](#cfn-bedrock-dataautomationproject-transcriptconfiguration-channellabeling)" : {{ChannelLabelingConfiguration}},
  "[SpeakerLabeling](#cfn-bedrock-dataautomationproject-transcriptconfiguration-speakerlabeling)" : {{SpeakerLabelingConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-transcriptconfiguration-syntax.yaml"></a>

```
  [ChannelLabeling](#cfn-bedrock-dataautomationproject-transcriptconfiguration-channellabeling): {{
    ChannelLabelingConfiguration}}
  [SpeakerLabeling](#cfn-bedrock-dataautomationproject-transcriptconfiguration-speakerlabeling): {{
    SpeakerLabelingConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-transcriptconfiguration-properties"></a>

`ChannelLabeling`  <a name="cfn-bedrock-dataautomationproject-transcriptconfiguration-channellabeling"></a>
Enables channel labeling. Each audio channel will be labeled with a number, and the transcript will indicate which channel is being used.
*Required*: No
*Type*: [ChannelLabelingConfiguration](aws-properties-bedrock-dataautomationproject-channellabelingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpeakerLabeling`  <a name="cfn-bedrock-dataautomationproject-transcriptconfiguration-speakerlabeling"></a>
Enables speaker labeling. Each speaker within a transcript will recieve a number, and the transcript will note which speaker is talking.
*Required*: No
*Type*: [SpeakerLabelingConfiguration](aws-properties-bedrock-dataautomationproject-speakerlabelingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
