---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-llmextractionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory LlmExtractionConfig
<a name="aws-properties-bedrockagentcore-memory-llmextractionconfig"></a>

Model-based metadata extraction configuration.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-llmextractionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-llmextractionconfig-syntax.json"></a>

```
{
  "[Definition](#cfn-bedrockagentcore-memory-llmextractionconfig-definition)" : {{String}},
  "[LlmExtractionInstruction](#cfn-bedrockagentcore-memory-llmextractionconfig-llmextractioninstruction)" : {{String}},
  "[Validation](#cfn-bedrockagentcore-memory-llmextractionconfig-validation)" : {{Validation}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-llmextractionconfig-syntax.yaml"></a>

```
  [Definition](#cfn-bedrockagentcore-memory-llmextractionconfig-definition): {{String}}
  [LlmExtractionInstruction](#cfn-bedrockagentcore-memory-llmextractionconfig-llmextractioninstruction): {{String}}
  [Validation](#cfn-bedrockagentcore-memory-llmextractionconfig-validation): {{
    Validation}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-llmextractionconfig-properties"></a>

`Definition`  <a name="cfn-bedrockagentcore-memory-llmextractionconfig-definition"></a>
Description of what this metadata field represents.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LlmExtractionInstruction`  <a name="cfn-bedrockagentcore-memory-llmextractionconfig-llmextractioninstruction"></a>
Instructions for extraction. Supports built-in operators like LATEST\_VALUE or custom natural-language instructions.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Validation`  <a name="cfn-bedrockagentcore-memory-llmextractionconfig-validation"></a>
Validation rules to constrain extracted values.
*Required*: No
*Type*: [Validation](aws-properties-bedrockagentcore-memory-validation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
