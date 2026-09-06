---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-customoutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject CustomOutputConfiguration
<a name="aws-properties-bedrock-dataautomationproject-customoutputconfiguration"></a>

Blueprints to apply to objects processed by the project.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-customoutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-customoutputconfiguration-syntax.json"></a>

```
{
  "[Blueprints](#cfn-bedrock-dataautomationproject-customoutputconfiguration-blueprints)" : {{[ BlueprintItem, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-customoutputconfiguration-syntax.yaml"></a>

```
  [Blueprints](#cfn-bedrock-dataautomationproject-customoutputconfiguration-blueprints): {{
    - BlueprintItem}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-customoutputconfiguration-properties"></a>

`Blueprints`  <a name="cfn-bedrock-dataautomationproject-customoutputconfiguration-blueprints"></a>
A list of blueprints.
*Required*: No
*Type*: Array of [BlueprintItem](aws-properties-bedrock-dataautomationproject-blueprintitem.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
