---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-lifecycleconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness LifecycleConfiguration
<a name="aws-properties-bedrockagentcore-harness-lifecycleconfiguration"></a>

LifecycleConfiguration lets you manage the lifecycle of runtime sessions and resources in AgentCore Runtime. This configuration helps optimize resource utilization by automatically cleaning up idle sessions and preventing long-running instances from consuming resources indefinitely.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-lifecycleconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-lifecycleconfiguration-syntax.json"></a>

```
{
  "[IdleRuntimeSessionTimeout](#cfn-bedrockagentcore-harness-lifecycleconfiguration-idleruntimesessiontimeout)" : {{Integer}},
  "[MaxLifetime](#cfn-bedrockagentcore-harness-lifecycleconfiguration-maxlifetime)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-lifecycleconfiguration-syntax.yaml"></a>

```
  [IdleRuntimeSessionTimeout](#cfn-bedrockagentcore-harness-lifecycleconfiguration-idleruntimesessiontimeout): {{Integer}}
  [MaxLifetime](#cfn-bedrockagentcore-harness-lifecycleconfiguration-maxlifetime): {{Integer}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-lifecycleconfiguration-properties"></a>

`IdleRuntimeSessionTimeout`  <a name="cfn-bedrockagentcore-harness-lifecycleconfiguration-idleruntimesessiontimeout"></a>
Timeout in seconds for idle runtime sessions. When a session remains idle for this duration, it will be automatically terminated. Default: 900 seconds (15 minutes).
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `28800`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxLifetime`  <a name="cfn-bedrockagentcore-harness-lifecycleconfiguration-maxlifetime"></a>
Maximum lifetime for the instance in seconds. Once reached, instances will be automatically terminated and replaced. Default: 28800 seconds (8 hours).
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `28800`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
