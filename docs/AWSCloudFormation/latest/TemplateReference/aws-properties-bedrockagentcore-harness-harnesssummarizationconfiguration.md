---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnesssummarizationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessSummarizationConfiguration
<a name="aws-properties-bedrockagentcore-harness-harnesssummarizationconfiguration"></a>

Configuration for summarization-based truncation strategy.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnesssummarizationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnesssummarizationconfiguration-syntax.json"></a>

```
{
  "[PreserveRecentMessages](#cfn-bedrockagentcore-harness-harnesssummarizationconfiguration-preserverecentmessages)" : {{Integer}},
  "[SummarizationSystemPrompt](#cfn-bedrockagentcore-harness-harnesssummarizationconfiguration-summarizationsystemprompt)" : {{String}},
  "[SummaryRatio](#cfn-bedrockagentcore-harness-harnesssummarizationconfiguration-summaryratio)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnesssummarizationconfiguration-syntax.yaml"></a>

```
  [PreserveRecentMessages](#cfn-bedrockagentcore-harness-harnesssummarizationconfiguration-preserverecentmessages): {{Integer}}
  [SummarizationSystemPrompt](#cfn-bedrockagentcore-harness-harnesssummarizationconfiguration-summarizationsystemprompt): {{String}}
  [SummaryRatio](#cfn-bedrockagentcore-harness-harnesssummarizationconfiguration-summaryratio): {{Number}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnesssummarizationconfiguration-properties"></a>

`PreserveRecentMessages`  <a name="cfn-bedrockagentcore-harness-harnesssummarizationconfiguration-preserverecentmessages"></a>
The number of recent messages to preserve without summarization.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SummarizationSystemPrompt`  <a name="cfn-bedrockagentcore-harness-harnesssummarizationconfiguration-summarizationsystemprompt"></a>
The system prompt used for generating summaries.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SummaryRatio`  <a name="cfn-bedrockagentcore-harness-harnesssummarizationconfiguration-summaryratio"></a>
The ratio of content to summarize.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
