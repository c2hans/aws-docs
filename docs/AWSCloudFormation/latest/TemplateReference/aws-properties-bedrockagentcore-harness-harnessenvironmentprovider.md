---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessenvironmentprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessEnvironmentProvider
<a name="aws-properties-bedrockagentcore-harness-harnessenvironmentprovider"></a>

The environment provider for a harness.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessenvironmentprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessenvironmentprovider-syntax.json"></a>

```
{
  "[AgentCoreRuntimeEnvironment](#cfn-bedrockagentcore-harness-harnessenvironmentprovider-agentcoreruntimeenvironment)" : {{HarnessAgentCoreRuntimeEnvironment}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessenvironmentprovider-syntax.yaml"></a>

```
  [AgentCoreRuntimeEnvironment](#cfn-bedrockagentcore-harness-harnessenvironmentprovider-agentcoreruntimeenvironment): {{
    HarnessAgentCoreRuntimeEnvironment}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessenvironmentprovider-properties"></a>

`AgentCoreRuntimeEnvironment`  <a name="cfn-bedrockagentcore-harness-harnessenvironmentprovider-agentcoreruntimeenvironment"></a>
The AgentCore Runtime environment configuration.
*Required*: No
*Type*: [HarnessAgentCoreRuntimeEnvironment](aws-properties-bedrockagentcore-harness-harnessagentcoreruntimeenvironment.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
