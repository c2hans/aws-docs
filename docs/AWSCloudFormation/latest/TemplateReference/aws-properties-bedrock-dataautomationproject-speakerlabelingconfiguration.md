---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-speakerlabelingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject SpeakerLabelingConfiguration
<a name="aws-properties-bedrock-dataautomationproject-speakerlabelingconfiguration"></a>

Enables or disables speaker labeling. Speaker labeling, when enabled will assign a number to each speaker, and indicate which speaker is talking in each portion of the transcript. This appears in the response as "spk\_0" for the first speaker, "spk\_1" for the second, and so on for up to 30 speakers.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-speakerlabelingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-speakerlabelingconfiguration-syntax.json"></a>

```
{
  "[State](#cfn-bedrock-dataautomationproject-speakerlabelingconfiguration-state)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-speakerlabelingconfiguration-syntax.yaml"></a>

```
  [State](#cfn-bedrock-dataautomationproject-speakerlabelingconfiguration-state): {{String}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-speakerlabelingconfiguration-properties"></a>

`State`  <a name="cfn-bedrock-dataautomationproject-speakerlabelingconfiguration-state"></a>
State of speaker labeling, either enabled or disabled.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
