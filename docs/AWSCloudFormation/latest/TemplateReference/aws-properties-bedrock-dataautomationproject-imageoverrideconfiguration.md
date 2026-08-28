---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-imageoverrideconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject ImageOverrideConfiguration
<a name="aws-properties-bedrock-dataautomationproject-imageoverrideconfiguration"></a>

Sets whether your project will process images or not.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-imageoverrideconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-imageoverrideconfiguration-syntax.json"></a>

```
{
  "[ModalityProcessing](#cfn-bedrock-dataautomationproject-imageoverrideconfiguration-modalityprocessing)" : {{ModalityProcessingConfiguration}},
  "[SensitiveDataConfiguration](#cfn-bedrock-dataautomationproject-imageoverrideconfiguration-sensitivedataconfiguration)" : {{SensitiveDataConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-imageoverrideconfiguration-syntax.yaml"></a>

```
  [ModalityProcessing](#cfn-bedrock-dataautomationproject-imageoverrideconfiguration-modalityprocessing): {{
    ModalityProcessingConfiguration}}
  [SensitiveDataConfiguration](#cfn-bedrock-dataautomationproject-imageoverrideconfiguration-sensitivedataconfiguration): {{
    SensitiveDataConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-imageoverrideconfiguration-properties"></a>

`ModalityProcessing`  <a name="cfn-bedrock-dataautomationproject-imageoverrideconfiguration-modalityprocessing"></a>
Sets modality processing for image files. All modalities are enabled by default.
*Required*: No
*Type*: [ModalityProcessingConfiguration](aws-properties-bedrock-dataautomationproject-modalityprocessingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SensitiveDataConfiguration`  <a name="cfn-bedrock-dataautomationproject-imageoverrideconfiguration-sensitivedataconfiguration"></a>
Configuration for sensitive data detection and redaction for image files.
*Required*: No
*Type*: [SensitiveDataConfiguration](aws-properties-bedrock-dataautomationproject-sensitivedataconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
