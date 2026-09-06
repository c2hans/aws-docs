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
  "[Connector](#cfn-bedrockagentcore-gatewaytarget-httptargetconfiguration-connector)" : {{HttpConnectorTargetConfiguration}},
  "[Passthrough](#cfn-bedrockagentcore-gatewaytarget-httptargetconfiguration-passthrough)" : {{PassthroughTargetConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-httptargetconfiguration-syntax.yaml"></a>

```
  [AgentcoreRuntime](#cfn-bedrockagentcore-gatewaytarget-httptargetconfiguration-agentcoreruntime): {{
    RuntimeTargetConfiguration}}
  [Connector](#cfn-bedrockagentcore-gatewaytarget-httptargetconfiguration-connector): {{
    HttpConnectorTargetConfiguration}}
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

`Connector`  <a name="cfn-bedrockagentcore-gatewaytarget-httptargetconfiguration-connector"></a>
Property description not available.
*Required*: No
*Type*: [HttpConnectorTargetConfiguration](aws-properties-bedrockagentcore-gatewaytarget-httpconnectortargetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Passthrough`  <a name="cfn-bedrockagentcore-gatewaytarget-httptargetconfiguration-passthrough"></a>
The passthrough configuration for the HTTP target. A passthrough target forwards requests directly to an external HTTP endpoint.
*Required*: No
*Type*: [PassthroughTargetConfiguration](aws-properties-bedrockagentcore-gatewaytarget-passthroughtargetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
