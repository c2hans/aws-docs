---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-documentoverrideconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject DocumentOverrideConfiguration
<a name="aws-properties-bedrock-dataautomationproject-documentoverrideconfiguration"></a>

Additional settings for a project.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-documentoverrideconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-documentoverrideconfiguration-syntax.json"></a>

```
{
  "[ModalityProcessing](#cfn-bedrock-dataautomationproject-documentoverrideconfiguration-modalityprocessing)" : {{ModalityProcessingConfiguration}},
  "[SensitiveDataConfiguration](#cfn-bedrock-dataautomationproject-documentoverrideconfiguration-sensitivedataconfiguration)" : {{SensitiveDataConfiguration}},
  "[Splitter](#cfn-bedrock-dataautomationproject-documentoverrideconfiguration-splitter)" : {{SplitterConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-documentoverrideconfiguration-syntax.yaml"></a>

```
  [ModalityProcessing](#cfn-bedrock-dataautomationproject-documentoverrideconfiguration-modalityprocessing): {{
    ModalityProcessingConfiguration}}
  [SensitiveDataConfiguration](#cfn-bedrock-dataautomationproject-documentoverrideconfiguration-sensitivedataconfiguration): {{
    SensitiveDataConfiguration}}
  [Splitter](#cfn-bedrock-dataautomationproject-documentoverrideconfiguration-splitter): {{
    SplitterConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-documentoverrideconfiguration-properties"></a>

`ModalityProcessing`  <a name="cfn-bedrock-dataautomationproject-documentoverrideconfiguration-modalityprocessing"></a>
Sets modality processing for document files. All modalities are enabled by default.
*Required*: No
*Type*: [ModalityProcessingConfiguration](aws-properties-bedrock-dataautomationproject-modalityprocessingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SensitiveDataConfiguration`  <a name="cfn-bedrock-dataautomationproject-documentoverrideconfiguration-sensitivedataconfiguration"></a>
Configuration for sensitive data detection and redaction for document files.
*Required*: No
*Type*: [SensitiveDataConfiguration](aws-properties-bedrock-dataautomationproject-sensitivedataconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Splitter`  <a name="cfn-bedrock-dataautomationproject-documentoverrideconfiguration-splitter"></a>
Whether document splitter is enabled for a project.
*Required*: No
*Type*: [SplitterConfiguration](aws-properties-bedrock-dataautomationproject-splitterconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
