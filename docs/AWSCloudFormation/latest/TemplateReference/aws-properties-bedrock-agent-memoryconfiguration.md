---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agent-memoryconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Agent MemoryConfiguration
<a name="aws-properties-bedrock-agent-memoryconfiguration"></a>

Details of the memory configuration.

## Syntax
<a name="aws-properties-bedrock-agent-memoryconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-agent-memoryconfiguration-syntax.json"></a>

```
{
  "[EnabledMemoryTypes](#cfn-bedrock-agent-memoryconfiguration-enabledmemorytypes)" : {{[ String, ... ]}},
  "[SessionSummaryConfiguration](#cfn-bedrock-agent-memoryconfiguration-sessionsummaryconfiguration)" : {{SessionSummaryConfiguration}},
  "[StorageDays](#cfn-bedrock-agent-memoryconfiguration-storagedays)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrock-agent-memoryconfiguration-syntax.yaml"></a>

```
  [EnabledMemoryTypes](#cfn-bedrock-agent-memoryconfiguration-enabledmemorytypes): {{
    - String}}
  [SessionSummaryConfiguration](#cfn-bedrock-agent-memoryconfiguration-sessionsummaryconfiguration): {{
    SessionSummaryConfiguration}}
  [StorageDays](#cfn-bedrock-agent-memoryconfiguration-storagedays): {{Number}}
```

## Properties
<a name="aws-properties-bedrock-agent-memoryconfiguration-properties"></a>

`EnabledMemoryTypes`  <a name="cfn-bedrock-agent-memoryconfiguration-enabledmemorytypes"></a>
The type of memory that is stored.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SessionSummaryConfiguration`  <a name="cfn-bedrock-agent-memoryconfiguration-sessionsummaryconfiguration"></a>
Contains the configuration for SESSION\_SUMMARY memory type enabled for the agent.
*Required*: No
*Type*: [SessionSummaryConfiguration](aws-properties-bedrock-agent-sessionsummaryconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageDays`  <a name="cfn-bedrock-agent-memoryconfiguration-storagedays"></a>
The number of days the agent is configured to retain the conversational context.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `365`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
