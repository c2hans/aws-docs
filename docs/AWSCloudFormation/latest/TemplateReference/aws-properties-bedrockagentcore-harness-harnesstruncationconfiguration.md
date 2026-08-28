---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnesstruncationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessTruncationConfiguration
<a name="aws-properties-bedrockagentcore-harness-harnesstruncationconfiguration"></a>

Configuration for truncating conversation context when it exceeds model limits.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnesstruncationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnesstruncationconfiguration-syntax.json"></a>

```
{
  "[Config](#cfn-bedrockagentcore-harness-harnesstruncationconfiguration-config)" : {{HarnessTruncationStrategyConfiguration}},
  "[Strategy](#cfn-bedrockagentcore-harness-harnesstruncationconfiguration-strategy)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnesstruncationconfiguration-syntax.yaml"></a>

```
  [Config](#cfn-bedrockagentcore-harness-harnesstruncationconfiguration-config): {{
    HarnessTruncationStrategyConfiguration}}
  [Strategy](#cfn-bedrockagentcore-harness-harnesstruncationconfiguration-strategy): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnesstruncationconfiguration-properties"></a>

`Config`  <a name="cfn-bedrockagentcore-harness-harnesstruncationconfiguration-config"></a>
The strategy-specific configuration.
*Required*: No
*Type*: [HarnessTruncationStrategyConfiguration](aws-properties-bedrockagentcore-harness-harnesstruncationstrategyconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Strategy`  <a name="cfn-bedrockagentcore-harness-harnesstruncationconfiguration-strategy"></a>
The truncation strategy to use.
*Required*: Yes
*Type*: String
*Allowed values*: `sliding_window | summarization | none`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
