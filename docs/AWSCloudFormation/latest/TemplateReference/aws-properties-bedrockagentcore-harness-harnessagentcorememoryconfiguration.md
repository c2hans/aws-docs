---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessagentcorememoryconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessAgentCoreMemoryConfiguration
<a name="aws-properties-bedrockagentcore-harness-harnessagentcorememoryconfiguration"></a>

Configuration for AgentCore Memory integration.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessagentcorememoryconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessagentcorememoryconfiguration-syntax.json"></a>

```
{
  "[ActorId](#cfn-bedrockagentcore-harness-harnessagentcorememoryconfiguration-actorid)" : {{String}},
  "[Arn](#cfn-bedrockagentcore-harness-harnessagentcorememoryconfiguration-arn)" : {{String}},
  "[MessagesCount](#cfn-bedrockagentcore-harness-harnessagentcorememoryconfiguration-messagescount)" : {{Integer}},
  "[RetrievalConfig](#cfn-bedrockagentcore-harness-harnessagentcorememoryconfiguration-retrievalconfig)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessagentcorememoryconfiguration-syntax.yaml"></a>

```
  [ActorId](#cfn-bedrockagentcore-harness-harnessagentcorememoryconfiguration-actorid): {{String}}
  [Arn](#cfn-bedrockagentcore-harness-harnessagentcorememoryconfiguration-arn): {{String}}
  [MessagesCount](#cfn-bedrockagentcore-harness-harnessagentcorememoryconfiguration-messagescount): {{Integer}}
  [RetrievalConfig](#cfn-bedrockagentcore-harness-harnessagentcorememoryconfiguration-retrievalconfig): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessagentcorememoryconfiguration-properties"></a>

`ActorId`  <a name="cfn-bedrockagentcore-harness-harnessagentcorememoryconfiguration-actorid"></a>
The actor ID for memory operations.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Arn`  <a name="cfn-bedrockagentcore-harness-harnessagentcorememoryconfiguration-arn"></a>
The ARN of the AgentCore Memory resource.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MessagesCount`  <a name="cfn-bedrockagentcore-harness-harnessagentcorememoryconfiguration-messagescount"></a>
The number of messages to retrieve from memory.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetrievalConfig`  <a name="cfn-bedrockagentcore-harness-harnessagentcorememoryconfiguration-retrievalconfig"></a>
The retrieval configuration for long-term memory, mapping namespace path templates to retrieval settings.
*Required*: No
*Type*: Object of [HarnessAgentCoreMemoryRetrievalConfig](aws-properties-bedrockagentcore-harness-harnessagentcorememoryretrievalconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
