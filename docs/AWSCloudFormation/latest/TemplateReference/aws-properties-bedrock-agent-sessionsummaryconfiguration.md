---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agent-sessionsummaryconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Agent SessionSummaryConfiguration
<a name="aws-properties-bedrock-agent-sessionsummaryconfiguration"></a>

Configuration for SESSION\_SUMMARY memory type enabled for the agent.

## Syntax
<a name="aws-properties-bedrock-agent-sessionsummaryconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-agent-sessionsummaryconfiguration-syntax.json"></a>

```
{
  "[MaxRecentSessions](#cfn-bedrock-agent-sessionsummaryconfiguration-maxrecentsessions)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrock-agent-sessionsummaryconfiguration-syntax.yaml"></a>

```
  [MaxRecentSessions](#cfn-bedrock-agent-sessionsummaryconfiguration-maxrecentsessions): {{Number}}
```

## Properties
<a name="aws-properties-bedrock-agent-sessionsummaryconfiguration-properties"></a>

`MaxRecentSessions`  <a name="cfn-bedrock-agent-sessionsummaryconfiguration-maxrecentsessions"></a>
Maximum number of recent session summaries to include in the agent's prompt context.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
