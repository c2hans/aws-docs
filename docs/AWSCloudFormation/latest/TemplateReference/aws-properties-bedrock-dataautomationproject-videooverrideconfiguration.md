---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-videooverrideconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject VideoOverrideConfiguration
<a name="aws-properties-bedrock-dataautomationproject-videooverrideconfiguration"></a>

Sets whether your project will process videos or not.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-videooverrideconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-videooverrideconfiguration-syntax.json"></a>

```
{
  "[ModalityProcessing](#cfn-bedrock-dataautomationproject-videooverrideconfiguration-modalityprocessing)" : {{ModalityProcessingConfiguration}},
  "[SensitiveDataConfiguration](#cfn-bedrock-dataautomationproject-videooverrideconfiguration-sensitivedataconfiguration)" : {{SensitiveDataConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-videooverrideconfiguration-syntax.yaml"></a>

```
  [ModalityProcessing](#cfn-bedrock-dataautomationproject-videooverrideconfiguration-modalityprocessing): {{
    ModalityProcessingConfiguration}}
  [SensitiveDataConfiguration](#cfn-bedrock-dataautomationproject-videooverrideconfiguration-sensitivedataconfiguration): {{
    SensitiveDataConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-videooverrideconfiguration-properties"></a>

`ModalityProcessing`  <a name="cfn-bedrock-dataautomationproject-videooverrideconfiguration-modalityprocessing"></a>
Sets modality processing for video files. All modalities are enabled by default.
*Required*: No
*Type*: [ModalityProcessingConfiguration](aws-properties-bedrock-dataautomationproject-modalityprocessingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SensitiveDataConfiguration`  <a name="cfn-bedrock-dataautomationproject-videooverrideconfiguration-sensitivedataconfiguration"></a>
Configuration for sensitive data detection and redaction for video files.
*Required*: No
*Type*: [SensitiveDataConfiguration](aws-properties-bedrock-dataautomationproject-sensitivedataconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
