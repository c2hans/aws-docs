---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-modalityprocessingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject ModalityProcessingConfiguration
<a name="aws-properties-bedrock-dataautomationproject-modalityprocessingconfiguration"></a>

This element is used to determine if the modality it is associated with is enabled or disabled. All modalities are enabled by default.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-modalityprocessingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-modalityprocessingconfiguration-syntax.json"></a>

```
{
  "[State](#cfn-bedrock-dataautomationproject-modalityprocessingconfiguration-state)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-modalityprocessingconfiguration-syntax.yaml"></a>

```
  [State](#cfn-bedrock-dataautomationproject-modalityprocessingconfiguration-state): {{String}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-modalityprocessingconfiguration-properties"></a>

`State`  <a name="cfn-bedrock-dataautomationproject-modalityprocessingconfiguration-state"></a>
Stores the state of the modality for your project, set to either enabled or disabled
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
