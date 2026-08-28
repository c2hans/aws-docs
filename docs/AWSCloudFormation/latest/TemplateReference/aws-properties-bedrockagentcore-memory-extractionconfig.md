---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-extractionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory ExtractionConfig
<a name="aws-properties-bedrockagentcore-memory-extractionconfig"></a>

Configuration for metadata extraction from conversational content.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-extractionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-extractionconfig-syntax.json"></a>

```
{
  "[LlmExtractionConfig](#cfn-bedrockagentcore-memory-extractionconfig-llmextractionconfig)" : {{LlmExtractionConfig}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-extractionconfig-syntax.yaml"></a>

```
  [LlmExtractionConfig](#cfn-bedrockagentcore-memory-extractionconfig-llmextractionconfig): {{
    LlmExtractionConfig}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-extractionconfig-properties"></a>

`LlmExtractionConfig`  <a name="cfn-bedrockagentcore-memory-extractionconfig-llmextractionconfig"></a>
Model-based extraction using a definition and instructions.
*Required*: No
*Type*: [LlmExtractionConfig](aws-properties-bedrockagentcore-memory-llmextractionconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
