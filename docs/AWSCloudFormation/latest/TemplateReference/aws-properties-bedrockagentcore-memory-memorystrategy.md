---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-memorystrategy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory MemoryStrategy
<a name="aws-properties-bedrockagentcore-memory-memorystrategy"></a>

The memory strategy.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-memorystrategy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-memorystrategy-syntax.json"></a>

```
{
  "[CustomMemoryStrategy](#cfn-bedrockagentcore-memory-memorystrategy-custommemorystrategy)" : {{CustomMemoryStrategy}},
  "[EpisodicMemoryStrategy](#cfn-bedrockagentcore-memory-memorystrategy-episodicmemorystrategy)" : {{EpisodicMemoryStrategy}},
  "[SemanticMemoryStrategy](#cfn-bedrockagentcore-memory-memorystrategy-semanticmemorystrategy)" : {{SemanticMemoryStrategy}},
  "[SummaryMemoryStrategy](#cfn-bedrockagentcore-memory-memorystrategy-summarymemorystrategy)" : {{SummaryMemoryStrategy}},
  "[UserPreferenceMemoryStrategy](#cfn-bedrockagentcore-memory-memorystrategy-userpreferencememorystrategy)" : {{UserPreferenceMemoryStrategy}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-memorystrategy-syntax.yaml"></a>

```
  [CustomMemoryStrategy](#cfn-bedrockagentcore-memory-memorystrategy-custommemorystrategy): {{
    CustomMemoryStrategy}}
  [EpisodicMemoryStrategy](#cfn-bedrockagentcore-memory-memorystrategy-episodicmemorystrategy): {{
    EpisodicMemoryStrategy}}
  [SemanticMemoryStrategy](#cfn-bedrockagentcore-memory-memorystrategy-semanticmemorystrategy): {{
    SemanticMemoryStrategy}}
  [SummaryMemoryStrategy](#cfn-bedrockagentcore-memory-memorystrategy-summarymemorystrategy): {{
    SummaryMemoryStrategy}}
  [UserPreferenceMemoryStrategy](#cfn-bedrockagentcore-memory-memorystrategy-userpreferencememorystrategy): {{
    UserPreferenceMemoryStrategy}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-memorystrategy-properties"></a>

`CustomMemoryStrategy`  <a name="cfn-bedrockagentcore-memory-memorystrategy-custommemorystrategy"></a>
The memory strategy.
*Required*: No
*Type*: [CustomMemoryStrategy](aws-properties-bedrockagentcore-memory-custommemorystrategy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EpisodicMemoryStrategy`  <a name="cfn-bedrockagentcore-memory-memorystrategy-episodicmemorystrategy"></a>
The episodic memory strategy configuration.
*Required*: No
*Type*: [EpisodicMemoryStrategy](aws-properties-bedrockagentcore-memory-episodicmemorystrategy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SemanticMemoryStrategy`  <a name="cfn-bedrockagentcore-memory-memorystrategy-semanticmemorystrategy"></a>
The memory strategy.
*Required*: No
*Type*: [SemanticMemoryStrategy](aws-properties-bedrockagentcore-memory-semanticmemorystrategy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SummaryMemoryStrategy`  <a name="cfn-bedrockagentcore-memory-memorystrategy-summarymemorystrategy"></a>
The memory strategy summary.
*Required*: No
*Type*: [SummaryMemoryStrategy](aws-properties-bedrockagentcore-memory-summarymemorystrategy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPreferenceMemoryStrategy`  <a name="cfn-bedrockagentcore-memory-memorystrategy-userpreferencememorystrategy"></a>
The memory strategy.
*Required*: No
*Type*: [UserPreferenceMemoryStrategy](aws-properties-bedrockagentcore-memory-userpreferencememorystrategy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
