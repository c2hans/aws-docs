---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-delegateagentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent DelegateAgentConfiguration
<a name="aws-properties-wisdom-aiagent-delegateagentconfiguration"></a>

<a name="aws-properties-wisdom-aiagent-delegateagentconfiguration-description"></a>The `DelegateAgentConfiguration` property type specifies Property description not available. for an [AWS::Wisdom::AIAgent](aws-resource-wisdom-aiagent.md).

## Syntax
<a name="aws-properties-wisdom-aiagent-delegateagentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-delegateagentconfiguration-syntax.json"></a>

```
{
  "[AgentTarget](#cfn-wisdom-aiagent-delegateagentconfiguration-agenttarget)" : {{AgentTarget}},
  "[Instruction](#cfn-wisdom-aiagent-delegateagentconfiguration-instruction)" : {{MultiAgentInstruction}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-delegateagentconfiguration-syntax.yaml"></a>

```
  [AgentTarget](#cfn-wisdom-aiagent-delegateagentconfiguration-agenttarget): {{
    AgentTarget}}
  [Instruction](#cfn-wisdom-aiagent-delegateagentconfiguration-instruction): {{
    MultiAgentInstruction}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-delegateagentconfiguration-properties"></a>

`AgentTarget`  <a name="cfn-wisdom-aiagent-delegateagentconfiguration-agenttarget"></a>
Property description not available.
*Required*: Yes
*Type*: [AgentTarget](aws-properties-wisdom-aiagent-agenttarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Instruction`  <a name="cfn-wisdom-aiagent-delegateagentconfiguration-instruction"></a>
Property description not available.
*Required*: No
*Type*: [MultiAgentInstruction](aws-properties-wisdom-aiagent-multiagentinstruction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
