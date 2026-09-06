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
