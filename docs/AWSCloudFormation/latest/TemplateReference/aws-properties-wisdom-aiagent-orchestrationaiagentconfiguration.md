---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-orchestrationaiagentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent OrchestrationAIAgentConfiguration
<a name="aws-properties-wisdom-aiagent-orchestrationaiagentconfiguration"></a>

The configuration for AI Agents of type `ORCHESTRATION`.

## Syntax
<a name="aws-properties-wisdom-aiagent-orchestrationaiagentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-orchestrationaiagentconfiguration-syntax.json"></a>

```
{
  "[ConnectInstanceArn](#cfn-wisdom-aiagent-orchestrationaiagentconfiguration-connectinstancearn)" : {{String}},
  "[Locale](#cfn-wisdom-aiagent-orchestrationaiagentconfiguration-locale)" : {{String}},
  "[OrchestrationAIGuardrailId](#cfn-wisdom-aiagent-orchestrationaiagentconfiguration-orchestrationaiguardrailid)" : {{String}},
  "[OrchestrationAIPromptId](#cfn-wisdom-aiagent-orchestrationaiagentconfiguration-orchestrationaipromptid)" : {{String}},
  "[ToolConfigurations](#cfn-wisdom-aiagent-orchestrationaiagentconfiguration-toolconfigurations)" : {{[ ToolConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-orchestrationaiagentconfiguration-syntax.yaml"></a>

```
  [ConnectInstanceArn](#cfn-wisdom-aiagent-orchestrationaiagentconfiguration-connectinstancearn): {{String}}
  [Locale](#cfn-wisdom-aiagent-orchestrationaiagentconfiguration-locale): {{String}}
  [OrchestrationAIGuardrailId](#cfn-wisdom-aiagent-orchestrationaiagentconfiguration-orchestrationaiguardrailid): {{String}}
  [OrchestrationAIPromptId](#cfn-wisdom-aiagent-orchestrationaiagentconfiguration-orchestrationaipromptid): {{String}}
  [ToolConfigurations](#cfn-wisdom-aiagent-orchestrationaiagentconfiguration-toolconfigurations): {{
    - ToolConfiguration}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-orchestrationaiagentconfiguration-properties"></a>

`ConnectInstanceArn`  <a name="cfn-wisdom-aiagent-orchestrationaiagentconfiguration-connectinstancearn"></a>
The Amazon Resource Name (ARN) of the Amazon Connect instance used by the Orchestration AI Agent.
*Required*: No
*Type*: String
*Pattern*: `^arn:[a-z-]+?:[a-z-]+?:[a-z0-9-]*?:([0-9]{12})?:[a-zA-Z0-9-:/]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Locale`  <a name="cfn-wisdom-aiagent-orchestrationaiagentconfiguration-locale"></a>
The locale setting for the Orchestration AI Agent.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OrchestrationAIGuardrailId`  <a name="cfn-wisdom-aiagent-orchestrationaiagentconfiguration-orchestrationaiguardrailid"></a>
The AI Guardrail identifier used by the Orchestration AI Agent.
*Required*: No
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OrchestrationAIPromptId`  <a name="cfn-wisdom-aiagent-orchestrationaiagentconfiguration-orchestrationaipromptid"></a>
The AI Prompt identifier used by the Orchestration AI Agent.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ToolConfigurations`  <a name="cfn-wisdom-aiagent-orchestrationaiagentconfiguration-toolconfigurations"></a>
The tool configurations used by the Orchestration AI Agent.
*Required*: No
*Type*: Array of [ToolConfiguration](aws-properties-wisdom-aiagent-toolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
