---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-sessionstorageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness SessionStorageConfiguration
<a name="aws-properties-bedrockagentcore-harness-sessionstorageconfiguration"></a>

Configuration for a session storage filesystem mounted into the AgentCore Runtime. Session storage provides persistent storage that is preserved across AgentCore Runtime session invocations.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-sessionstorageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-sessionstorageconfiguration-syntax.json"></a>

```
{
  "[MountPath](#cfn-bedrockagentcore-harness-sessionstorageconfiguration-mountpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-sessionstorageconfiguration-syntax.yaml"></a>

```
  [MountPath](#cfn-bedrockagentcore-harness-sessionstorageconfiguration-mountpath): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-sessionstorageconfiguration-properties"></a>

`MountPath`  <a name="cfn-bedrockagentcore-harness-sessionstorageconfiguration-mountpath"></a>
The mount path for the session storage filesystem inside the AgentCore Runtime. The path must be under `/mnt` with exactly one subdirectory level (for example, `/mnt/data`).
*Required*: Yes
*Type*: String
*Pattern*: `^/mnt/[a-zA-Z0-9._-]+/?$`
*Minimum*: `6`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
