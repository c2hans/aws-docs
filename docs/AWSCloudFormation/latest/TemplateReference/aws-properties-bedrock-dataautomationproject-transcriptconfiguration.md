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
