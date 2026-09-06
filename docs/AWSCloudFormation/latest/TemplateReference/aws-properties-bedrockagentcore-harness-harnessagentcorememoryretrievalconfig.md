---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessagentcorememoryretrievalconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessAgentCoreMemoryRetrievalConfig
<a name="aws-properties-bedrockagentcore-harness-harnessagentcorememoryretrievalconfig"></a>

Configuration for memory retrieval within a namespace.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessagentcorememoryretrievalconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessagentcorememoryretrievalconfig-syntax.json"></a>

```
{
  "[RelevanceScore](#cfn-bedrockagentcore-harness-harnessagentcorememoryretrievalconfig-relevancescore)" : {{String}},
  "[StrategyId](#cfn-bedrockagentcore-harness-harnessagentcorememoryretrievalconfig-strategyid)" : {{String}},
  "[TopK](#cfn-bedrockagentcore-harness-harnessagentcorememoryretrievalconfig-topk)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessagentcorememoryretrievalconfig-syntax.yaml"></a>

```
  [RelevanceScore](#cfn-bedrockagentcore-harness-harnessagentcorememoryretrievalconfig-relevancescore): {{String}}
  [StrategyId](#cfn-bedrockagentcore-harness-harnessagentcorememoryretrievalconfig-strategyid): {{String}}
  [TopK](#cfn-bedrockagentcore-harness-harnessagentcorememoryretrievalconfig-topk): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessagentcorememoryretrievalconfig-properties"></a>

`RelevanceScore`  <a name="cfn-bedrockagentcore-harness-harnessagentcorememoryretrievalconfig-relevancescore"></a>
The minimum relevance score for retrieved memories.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StrategyId`  <a name="cfn-bedrockagentcore-harness-harnessagentcorememoryretrievalconfig-strategyid"></a>
The ID of the retrieval strategy to use.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopK`  <a name="cfn-bedrockagentcore-harness-harnessagentcorememoryretrievalconfig-topk"></a>
The maximum number of memory entries to retrieve.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
