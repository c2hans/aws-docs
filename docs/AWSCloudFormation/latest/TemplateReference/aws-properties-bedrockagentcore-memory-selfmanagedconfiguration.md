---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-selfmanagedconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory SelfManagedConfiguration
<a name="aws-properties-bedrockagentcore-memory-selfmanagedconfiguration"></a>

The self managed configuration.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-selfmanagedconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-selfmanagedconfiguration-syntax.json"></a>

```
{
  "[HistoricalContextWindowSize](#cfn-bedrockagentcore-memory-selfmanagedconfiguration-historicalcontextwindowsize)" : {{Integer}},
  "[InvocationConfiguration](#cfn-bedrockagentcore-memory-selfmanagedconfiguration-invocationconfiguration)" : {{InvocationConfigurationInput}},
  "[TriggerConditions](#cfn-bedrockagentcore-memory-selfmanagedconfiguration-triggerconditions)" : {{[ TriggerConditionInput, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-selfmanagedconfiguration-syntax.yaml"></a>

```
  [HistoricalContextWindowSize](#cfn-bedrockagentcore-memory-selfmanagedconfiguration-historicalcontextwindowsize): {{Integer}}
  [InvocationConfiguration](#cfn-bedrockagentcore-memory-selfmanagedconfiguration-invocationconfiguration): {{
    InvocationConfigurationInput}}
  [TriggerConditions](#cfn-bedrockagentcore-memory-selfmanagedconfiguration-triggerconditions): {{
    - TriggerConditionInput}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-selfmanagedconfiguration-properties"></a>

`HistoricalContextWindowSize`  <a name="cfn-bedrockagentcore-memory-selfmanagedconfiguration-historicalcontextwindowsize"></a>
The memory configuration for self managed.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InvocationConfiguration`  <a name="cfn-bedrockagentcore-memory-selfmanagedconfiguration-invocationconfiguration"></a>
The self managed configuration.
*Required*: No
*Type*: [InvocationConfigurationInput](aws-properties-bedrockagentcore-memory-invocationconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TriggerConditions`  <a name="cfn-bedrockagentcore-memory-selfmanagedconfiguration-triggerconditions"></a>
A list of conditions that trigger memory processing.
*Required*: No
*Type*: Array of [TriggerConditionInput](aws-properties-bedrockagentcore-memory-triggerconditioninput.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
