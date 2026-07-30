---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-audiooverrideconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject AudioOverrideConfiguration
<a name="aws-properties-bedrock-dataautomationproject-audiooverrideconfiguration"></a>

Sets whether your project will process audio or not.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-audiooverrideconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-audiooverrideconfiguration-syntax.json"></a>

```
{
  "[LanguageConfiguration](#cfn-bedrock-dataautomationproject-audiooverrideconfiguration-languageconfiguration)" : {{AudioLanguageConfiguration}},
  "[ModalityProcessing](#cfn-bedrock-dataautomationproject-audiooverrideconfiguration-modalityprocessing)" : {{ModalityProcessingConfiguration}},
  "[SensitiveDataConfiguration](#cfn-bedrock-dataautomationproject-audiooverrideconfiguration-sensitivedataconfiguration)" : {{SensitiveDataConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-audiooverrideconfiguration-syntax.yaml"></a>

```
  [LanguageConfiguration](#cfn-bedrock-dataautomationproject-audiooverrideconfiguration-languageconfiguration): {{
    AudioLanguageConfiguration}}
  [ModalityProcessing](#cfn-bedrock-dataautomationproject-audiooverrideconfiguration-modalityprocessing): {{
    ModalityProcessingConfiguration}}
  [SensitiveDataConfiguration](#cfn-bedrock-dataautomationproject-audiooverrideconfiguration-sensitivedataconfiguration): {{
    SensitiveDataConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-audiooverrideconfiguration-properties"></a>

`LanguageConfiguration`  <a name="cfn-bedrock-dataautomationproject-audiooverrideconfiguration-languageconfiguration"></a>
The output and input language configuration for your audio.
*Required*: No
*Type*: [AudioLanguageConfiguration](aws-properties-bedrock-dataautomationproject-audiolanguageconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModalityProcessing`  <a name="cfn-bedrock-dataautomationproject-audiooverrideconfiguration-modalityprocessing"></a>
Sets modality processing for audio files. All modalities are enabled by default.
*Required*: No
*Type*: [ModalityProcessingConfiguration](aws-properties-bedrock-dataautomationproject-modalityprocessingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SensitiveDataConfiguration`  <a name="cfn-bedrock-dataautomationproject-audiooverrideconfiguration-sensitivedataconfiguration"></a>
Configuration for sensitive data detection and redaction for audio files.
*Required*: No
*Type*: [SensitiveDataConfiguration](aws-properties-bedrock-dataautomationproject-sensitivedataconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
