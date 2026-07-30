---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-documentoutputtextformat.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject DocumentOutputTextFormat
<a name="aws-properties-bedrock-dataautomationproject-documentoutputtextformat"></a>

An output text format.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-documentoutputtextformat-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-documentoutputtextformat-syntax.json"></a>

```
{
  "[Types](#cfn-bedrock-dataautomationproject-documentoutputtextformat-types)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-documentoutputtextformat-syntax.yaml"></a>

```
  [Types](#cfn-bedrock-dataautomationproject-documentoutputtextformat-types): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-documentoutputtextformat-properties"></a>

`Types`  <a name="cfn-bedrock-dataautomationproject-documentoutputtextformat-types"></a>
The types of output text to generate.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
