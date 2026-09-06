---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-overrideconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject OverrideConfiguration
<a name="aws-properties-bedrock-dataautomationproject-overrideconfiguration"></a>

Additional settings for a project.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-overrideconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-overrideconfiguration-syntax.json"></a>

```
{
  "[Audio](#cfn-bedrock-dataautomationproject-overrideconfiguration-audio)" : {{AudioOverrideConfiguration}},
  "[Document](#cfn-bedrock-dataautomationproject-overrideconfiguration-document)" : {{DocumentOverrideConfiguration}},
  "[Image](#cfn-bedrock-dataautomationproject-overrideconfiguration-image)" : {{ImageOverrideConfiguration}},
  "[ModalityRouting](#cfn-bedrock-dataautomationproject-overrideconfiguration-modalityrouting)" : {{ModalityRoutingConfiguration}},
  "[Video](#cfn-bedrock-dataautomationproject-overrideconfiguration-video)" : {{VideoOverrideConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-overrideconfiguration-syntax.yaml"></a>

```
  [Audio](#cfn-bedrock-dataautomationproject-overrideconfiguration-audio): {{
    AudioOverrideConfiguration}}
  [Document](#cfn-bedrock-dataautomationproject-overrideconfiguration-document): {{
    DocumentOverrideConfiguration}}
  [Image](#cfn-bedrock-dataautomationproject-overrideconfiguration-image): {{
    ImageOverrideConfiguration}}
  [ModalityRouting](#cfn-bedrock-dataautomationproject-overrideconfiguration-modalityrouting): {{
    ModalityRoutingConfiguration}}
  [Video](#cfn-bedrock-dataautomationproject-overrideconfiguration-video): {{
    VideoOverrideConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-overrideconfiguration-properties"></a>

`Audio`  <a name="cfn-bedrock-dataautomationproject-overrideconfiguration-audio"></a>
This element declares whether your project will process audio files.
*Required*: No
*Type*: [AudioOverrideConfiguration](aws-properties-bedrock-dataautomationproject-audiooverrideconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Document`  <a name="cfn-bedrock-dataautomationproject-overrideconfiguration-document"></a>
Additional settings for a project.
*Required*: No
*Type*: [DocumentOverrideConfiguration](aws-properties-bedrock-dataautomationproject-documentoverrideconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Image`  <a name="cfn-bedrock-dataautomationproject-overrideconfiguration-image"></a>
This element declares whether your project will process image files.
*Required*: No
*Type*: [ImageOverrideConfiguration](aws-properties-bedrock-dataautomationproject-imageoverrideconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModalityRouting`  <a name="cfn-bedrock-dataautomationproject-overrideconfiguration-modalityrouting"></a>
Lets you set which modalities certain file types are processed as.
*Required*: No
*Type*: [ModalityRoutingConfiguration](aws-properties-bedrock-dataautomationproject-modalityroutingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Video`  <a name="cfn-bedrock-dataautomationproject-overrideconfiguration-video"></a>
This element declares whether your project will process video files.
*Required*: No
*Type*: [VideoOverrideConfiguration](aws-properties-bedrock-dataautomationproject-videooverrideconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
