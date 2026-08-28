---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessmemoryconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessMemoryConfiguration
<a name="aws-properties-bedrockagentcore-harness-harnessmemoryconfiguration"></a>

The memory configuration for a harness.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessmemoryconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessmemoryconfiguration-syntax.json"></a>

```
{
  "[AgentCoreMemoryConfiguration](#cfn-bedrockagentcore-harness-harnessmemoryconfiguration-agentcorememoryconfiguration)" : {{HarnessAgentCoreMemoryConfiguration}},
  "[Disabled](#cfn-bedrockagentcore-harness-harnessmemoryconfiguration-disabled)" : {{Json}},
  "[ManagedMemoryConfiguration](#cfn-bedrockagentcore-harness-harnessmemoryconfiguration-managedmemoryconfiguration)" : {{HarnessManagedMemoryConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessmemoryconfiguration-syntax.yaml"></a>

```
  [AgentCoreMemoryConfiguration](#cfn-bedrockagentcore-harness-harnessmemoryconfiguration-agentcorememoryconfiguration): {{
    HarnessAgentCoreMemoryConfiguration}}
  [Disabled](#cfn-bedrockagentcore-harness-harnessmemoryconfiguration-disabled): {{Json}}
  [ManagedMemoryConfiguration](#cfn-bedrockagentcore-harness-harnessmemoryconfiguration-managedmemoryconfiguration): {{
    HarnessManagedMemoryConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessmemoryconfiguration-properties"></a>

`AgentCoreMemoryConfiguration`  <a name="cfn-bedrockagentcore-harness-harnessmemoryconfiguration-agentcorememoryconfiguration"></a>
The AgentCore Memory configuration.
*Required*: No
*Type*: [HarnessAgentCoreMemoryConfiguration](aws-properties-bedrockagentcore-harness-harnessagentcorememoryconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Disabled`  <a name="cfn-bedrockagentcore-harness-harnessmemoryconfiguration-disabled"></a>
Explicitly opt out of memory.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManagedMemoryConfiguration`  <a name="cfn-bedrockagentcore-harness-harnessmemoryconfiguration-managedmemoryconfiguration"></a>
Harness creates and manages a memory resource in the customer's account.
*Required*: No
*Type*: [HarnessManagedMemoryConfiguration](aws-properties-bedrockagentcore-harness-harnessmanagedmemoryconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
