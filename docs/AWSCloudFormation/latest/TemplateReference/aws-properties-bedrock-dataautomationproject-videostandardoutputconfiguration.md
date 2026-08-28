---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-videostandardoutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject VideoStandardOutputConfiguration
<a name="aws-properties-bedrock-dataautomationproject-videostandardoutputconfiguration"></a>

Output settings for processing video.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-videostandardoutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-videostandardoutputconfiguration-syntax.json"></a>

```
{
  "[Extraction](#cfn-bedrock-dataautomationproject-videostandardoutputconfiguration-extraction)" : {{VideoStandardExtraction}},
  "[GenerativeField](#cfn-bedrock-dataautomationproject-videostandardoutputconfiguration-generativefield)" : {{VideoStandardGenerativeField}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-videostandardoutputconfiguration-syntax.yaml"></a>

```
  [Extraction](#cfn-bedrock-dataautomationproject-videostandardoutputconfiguration-extraction): {{
    VideoStandardExtraction}}
  [GenerativeField](#cfn-bedrock-dataautomationproject-videostandardoutputconfiguration-generativefield): {{
    VideoStandardGenerativeField}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-videostandardoutputconfiguration-properties"></a>

`Extraction`  <a name="cfn-bedrock-dataautomationproject-videostandardoutputconfiguration-extraction"></a>
Settings for populating data fields that describe the video.
*Required*: No
*Type*: [VideoStandardExtraction](aws-properties-bedrock-dataautomationproject-videostandardextraction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GenerativeField`  <a name="cfn-bedrock-dataautomationproject-videostandardoutputconfiguration-generativefield"></a>
Whether to generate descriptions of the video.
*Required*: No
*Type*: [VideoStandardGenerativeField](aws-properties-bedrock-dataautomationproject-videostandardgenerativefield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
