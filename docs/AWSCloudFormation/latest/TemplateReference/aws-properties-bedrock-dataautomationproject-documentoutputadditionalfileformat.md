---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-documentoutputadditionalfileformat.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject DocumentOutputAdditionalFileFormat
<a name="aws-properties-bedrock-dataautomationproject-documentoutputadditionalfileformat"></a>

Output settings for additional file formats.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-documentoutputadditionalfileformat-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-documentoutputadditionalfileformat-syntax.json"></a>

```
{
  "[State](#cfn-bedrock-dataautomationproject-documentoutputadditionalfileformat-state)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-documentoutputadditionalfileformat-syntax.yaml"></a>

```
  [State](#cfn-bedrock-dataautomationproject-documentoutputadditionalfileformat-state): {{String}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-documentoutputadditionalfileformat-properties"></a>

`State`  <a name="cfn-bedrock-dataautomationproject-documentoutputadditionalfileformat-state"></a>
Whether additional file formats are enabled for a project.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
