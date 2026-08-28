---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-documentoutputformat.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject DocumentOutputFormat
<a name="aws-properties-bedrock-dataautomationproject-documentoutputformat"></a>

A document output format.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-documentoutputformat-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-documentoutputformat-syntax.json"></a>

```
{
  "[AdditionalFileFormat](#cfn-bedrock-dataautomationproject-documentoutputformat-additionalfileformat)" : {{DocumentOutputAdditionalFileFormat}},
  "[TextFormat](#cfn-bedrock-dataautomationproject-documentoutputformat-textformat)" : {{DocumentOutputTextFormat}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-documentoutputformat-syntax.yaml"></a>

```
  [AdditionalFileFormat](#cfn-bedrock-dataautomationproject-documentoutputformat-additionalfileformat): {{
    DocumentOutputAdditionalFileFormat}}
  [TextFormat](#cfn-bedrock-dataautomationproject-documentoutputformat-textformat): {{
    DocumentOutputTextFormat}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-documentoutputformat-properties"></a>

`AdditionalFileFormat`  <a name="cfn-bedrock-dataautomationproject-documentoutputformat-additionalfileformat"></a>
Output settings for additional file formats.
*Required*: Yes
*Type*: [DocumentOutputAdditionalFileFormat](aws-properties-bedrock-dataautomationproject-documentoutputadditionalfileformat.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextFormat`  <a name="cfn-bedrock-dataautomationproject-documentoutputformat-textformat"></a>
An output text format.
*Required*: Yes
*Type*: [DocumentOutputTextFormat](aws-properties-bedrock-dataautomationproject-documentoutputtextformat.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
