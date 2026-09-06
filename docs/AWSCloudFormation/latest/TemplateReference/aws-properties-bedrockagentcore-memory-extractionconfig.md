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
