---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-handoffagentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent HandoffAgentConfiguration
<a name="aws-properties-wisdom-aiagent-handoffagentconfiguration"></a>

<a name="aws-properties-wisdom-aiagent-handoffagentconfiguration-description"></a>The `HandoffAgentConfiguration` property type specifies Property description not available. for an [AWS::Wisdom::AIAgent](aws-resource-wisdom-aiagent.md).

## Syntax
<a name="aws-properties-wisdom-aiagent-handoffagentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-handoffagentconfiguration-syntax.json"></a>

```
{
  "[AgentTarget](#cfn-wisdom-aiagent-handoffagentconfiguration-agenttarget)" : {{AgentTarget}},
  "[AudioStreamingEnabled](#cfn-wisdom-aiagent-handoffagentconfiguration-audiostreamingenabled)" : {{Boolean}},
  "[ImmediateHandoff](#cfn-wisdom-aiagent-handoffagentconfiguration-immediatehandoff)" : {{Boolean}},
  "[Instruction](#cfn-wisdom-aiagent-handoffagentconfiguration-instruction)" : {{MultiAgentInstruction}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-handoffagentconfiguration-syntax.yaml"></a>

```
  [AgentTarget](#cfn-wisdom-aiagent-handoffagentconfiguration-agenttarget): {{
    AgentTarget}}
  [AudioStreamingEnabled](#cfn-wisdom-aiagent-handoffagentconfiguration-audiostreamingenabled): {{Boolean}}
  [ImmediateHandoff](#cfn-wisdom-aiagent-handoffagentconfiguration-immediatehandoff): {{Boolean}}
  [Instruction](#cfn-wisdom-aiagent-handoffagentconfiguration-instruction): {{
    MultiAgentInstruction}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-handoffagentconfiguration-properties"></a>

`AgentTarget`  <a name="cfn-wisdom-aiagent-handoffagentconfiguration-agenttarget"></a>
Property description not available.
*Required*: Yes
*Type*: [AgentTarget](aws-properties-wisdom-aiagent-agenttarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AudioStreamingEnabled`  <a name="cfn-wisdom-aiagent-handoffagentconfiguration-audiostreamingenabled"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImmediateHandoff`  <a name="cfn-wisdom-aiagent-handoffagentconfiguration-immediatehandoff"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Instruction`  <a name="cfn-wisdom-aiagent-handoffagentconfiguration-instruction"></a>
Property description not available.
*Required*: No
*Type*: [MultiAgentInstruction](aws-properties-wisdom-aiagent-multiagentinstruction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
