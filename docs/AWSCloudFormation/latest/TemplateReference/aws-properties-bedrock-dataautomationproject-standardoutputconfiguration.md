---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-standardoutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject StandardOutputConfiguration
<a name="aws-properties-bedrock-dataautomationproject-standardoutputconfiguration"></a>

The project's standard output configuration.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-standardoutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-standardoutputconfiguration-syntax.json"></a>

```
{
  "[Audio](#cfn-bedrock-dataautomationproject-standardoutputconfiguration-audio)" : {{AudioStandardOutputConfiguration}},
  "[Document](#cfn-bedrock-dataautomationproject-standardoutputconfiguration-document)" : {{DocumentStandardOutputConfiguration}},
  "[Image](#cfn-bedrock-dataautomationproject-standardoutputconfiguration-image)" : {{ImageStandardOutputConfiguration}},
  "[Video](#cfn-bedrock-dataautomationproject-standardoutputconfiguration-video)" : {{VideoStandardOutputConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-standardoutputconfiguration-syntax.yaml"></a>

```
  [Audio](#cfn-bedrock-dataautomationproject-standardoutputconfiguration-audio): {{
    AudioStandardOutputConfiguration}}
  [Document](#cfn-bedrock-dataautomationproject-standardoutputconfiguration-document): {{
    DocumentStandardOutputConfiguration}}
  [Image](#cfn-bedrock-dataautomationproject-standardoutputconfiguration-image): {{
    ImageStandardOutputConfiguration}}
  [Video](#cfn-bedrock-dataautomationproject-standardoutputconfiguration-video): {{
    VideoStandardOutputConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-standardoutputconfiguration-properties"></a>

`Audio`  <a name="cfn-bedrock-dataautomationproject-standardoutputconfiguration-audio"></a>
Settings for processing audio.
*Required*: No
*Type*: [AudioStandardOutputConfiguration](aws-properties-bedrock-dataautomationproject-audiostandardoutputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Document`  <a name="cfn-bedrock-dataautomationproject-standardoutputconfiguration-document"></a>
Settings for processing documents.
*Required*: No
*Type*: [DocumentStandardOutputConfiguration](aws-properties-bedrock-dataautomationproject-documentstandardoutputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Image`  <a name="cfn-bedrock-dataautomationproject-standardoutputconfiguration-image"></a>
Settings for processing images.
*Required*: No
*Type*: [ImageStandardOutputConfiguration](aws-properties-bedrock-dataautomationproject-imagestandardoutputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Video`  <a name="cfn-bedrock-dataautomationproject-standardoutputconfiguration-video"></a>
Settings for processing video.
*Required*: No
*Type*: [VideoStandardOutputConfiguration](aws-properties-bedrock-dataautomationproject-videostandardoutputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
