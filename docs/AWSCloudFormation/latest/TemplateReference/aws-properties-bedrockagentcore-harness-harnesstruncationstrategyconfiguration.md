---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnesstruncationstrategyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessTruncationStrategyConfiguration
<a name="aws-properties-bedrockagentcore-harness-harnesstruncationstrategyconfiguration"></a>

Strategy-specific truncation configuration.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnesstruncationstrategyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnesstruncationstrategyconfiguration-syntax.json"></a>

```
{
  "[SlidingWindow](#cfn-bedrockagentcore-harness-harnesstruncationstrategyconfiguration-slidingwindow)" : {{HarnessSlidingWindowConfiguration}},
  "[Summarization](#cfn-bedrockagentcore-harness-harnesstruncationstrategyconfiguration-summarization)" : {{HarnessSummarizationConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnesstruncationstrategyconfiguration-syntax.yaml"></a>

```
  [SlidingWindow](#cfn-bedrockagentcore-harness-harnesstruncationstrategyconfiguration-slidingwindow): {{
    HarnessSlidingWindowConfiguration}}
  [Summarization](#cfn-bedrockagentcore-harness-harnesstruncationstrategyconfiguration-summarization): {{
    HarnessSummarizationConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnesstruncationstrategyconfiguration-properties"></a>

`SlidingWindow`  <a name="cfn-bedrockagentcore-harness-harnesstruncationstrategyconfiguration-slidingwindow"></a>
Configuration for sliding window truncation.
*Required*: No
*Type*: [HarnessSlidingWindowConfiguration](aws-properties-bedrockagentcore-harness-harnessslidingwindowconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Summarization`  <a name="cfn-bedrockagentcore-harness-harnesstruncationstrategyconfiguration-summarization"></a>
Configuration for summarization-based truncation.
*Required*: No
*Type*: [HarnessSummarizationConfiguration](aws-properties-bedrockagentcore-harness-harnesssummarizationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
