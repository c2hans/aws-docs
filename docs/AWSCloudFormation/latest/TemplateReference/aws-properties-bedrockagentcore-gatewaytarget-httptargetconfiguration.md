---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-httptargetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget HttpTargetConfiguration
<a name="aws-properties-bedrockagentcore-gatewaytarget-httptargetconfiguration"></a>

The HTTP target configuration for a gateway target. Contains the configuration for HTTP-based target endpoints.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-httptargetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-httptargetconfiguration-syntax.json"></a>

```
{
  "[AgentcoreRuntime](#cfn-bedrockagentcore-gatewaytarget-httptargetconfiguration-agentcoreruntime)" : {{RuntimeTargetConfiguration}},
  "[Passthrough](#cfn-bedrockagentcore-gatewaytarget-httptargetconfiguration-passthrough)" : {{PassthroughTargetConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-httptargetconfiguration-syntax.yaml"></a>

```
  [AgentcoreRuntime](#cfn-bedrockagentcore-gatewaytarget-httptargetconfiguration-agentcoreruntime): {{
    RuntimeTargetConfiguration}}
  [Passthrough](#cfn-bedrockagentcore-gatewaytarget-httptargetconfiguration-passthrough): {{
    PassthroughTargetConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-httptargetconfiguration-properties"></a>

`AgentcoreRuntime`  <a name="cfn-bedrockagentcore-gatewaytarget-httptargetconfiguration-agentcoreruntime"></a>
The AgentCore Runtime target configuration for HTTP-based communication with an agent runtime.
*Required*: No
*Type*: [RuntimeTargetConfiguration](aws-properties-bedrockagentcore-gatewaytarget-runtimetargetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Passthrough`  <a name="cfn-bedrockagentcore-gatewaytarget-httptargetconfiguration-passthrough"></a>
The passthrough configuration for the HTTP target. A passthrough target forwards requests directly to an external HTTP endpoint.
*Required*: No
*Type*: [PassthroughTargetConfiguration](aws-properties-bedrockagentcore-gatewaytarget-passthroughtargetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
