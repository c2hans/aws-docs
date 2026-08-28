---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-audioextractioncategorytypeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject AudioExtractionCategoryTypeConfiguration
<a name="aws-properties-bedrock-dataautomationproject-audioextractioncategorytypeconfiguration"></a>

Allows configuration of extractions for different types of data, such as transcript and content moderation.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-audioextractioncategorytypeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-audioextractioncategorytypeconfiguration-syntax.json"></a>

```
{
  "[Transcript](#cfn-bedrock-dataautomationproject-audioextractioncategorytypeconfiguration-transcript)" : {{TranscriptConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-audioextractioncategorytypeconfiguration-syntax.yaml"></a>

```
  [Transcript](#cfn-bedrock-dataautomationproject-audioextractioncategorytypeconfiguration-transcript): {{
    TranscriptConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-audioextractioncategorytypeconfiguration-properties"></a>

`Transcript`  <a name="cfn-bedrock-dataautomationproject-audioextractioncategorytypeconfiguration-transcript"></a>
This element allows you to configure different extractions for your transcript data, such as speaker and channel labeling.
*Required*: No
*Type*: [TranscriptConfiguration](aws-properties-bedrock-dataautomationproject-transcriptconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
