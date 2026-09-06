---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-documentstandardoutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject DocumentStandardOutputConfiguration
<a name="aws-properties-bedrock-dataautomationproject-documentstandardoutputconfiguration"></a>

Output settings for processing documents.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-documentstandardoutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-documentstandardoutputconfiguration-syntax.json"></a>

```
{
  "[Extraction](#cfn-bedrock-dataautomationproject-documentstandardoutputconfiguration-extraction)" : {{DocumentStandardExtraction}},
  "[GenerativeField](#cfn-bedrock-dataautomationproject-documentstandardoutputconfiguration-generativefield)" : {{DocumentStandardGenerativeField}},
  "[OutputFormat](#cfn-bedrock-dataautomationproject-documentstandardoutputconfiguration-outputformat)" : {{DocumentOutputFormat}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-documentstandardoutputconfiguration-syntax.yaml"></a>

```
  [Extraction](#cfn-bedrock-dataautomationproject-documentstandardoutputconfiguration-extraction): {{
    DocumentStandardExtraction}}
  [GenerativeField](#cfn-bedrock-dataautomationproject-documentstandardoutputconfiguration-generativefield): {{
    DocumentStandardGenerativeField}}
  [OutputFormat](#cfn-bedrock-dataautomationproject-documentstandardoutputconfiguration-outputformat): {{
    DocumentOutputFormat}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-documentstandardoutputconfiguration-properties"></a>

`Extraction`  <a name="cfn-bedrock-dataautomationproject-documentstandardoutputconfiguration-extraction"></a>
Settings for populating data fields that describe the document.
*Required*: No
*Type*: [DocumentStandardExtraction](aws-properties-bedrock-dataautomationproject-documentstandardextraction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GenerativeField`  <a name="cfn-bedrock-dataautomationproject-documentstandardoutputconfiguration-generativefield"></a>
Whether to generate descriptions.
*Required*: No
*Type*: [DocumentStandardGenerativeField](aws-properties-bedrock-dataautomationproject-documentstandardgenerativefield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputFormat`  <a name="cfn-bedrock-dataautomationproject-documentstandardoutputconfiguration-outputformat"></a>
The output format to generate.
*Required*: No
*Type*: [DocumentOutputFormat](aws-properties-bedrock-dataautomationproject-documentoutputformat.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
