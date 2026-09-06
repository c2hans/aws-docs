---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-targetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget TargetConfiguration
<a name="aws-properties-bedrockagentcore-gatewaytarget-targetconfiguration"></a>

The configuration for a gateway target. This structure defines how the gateway connects to and interacts with the target endpoint.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-targetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-targetconfiguration-syntax.json"></a>

```
{
  "[Http](#cfn-bedrockagentcore-gatewaytarget-targetconfiguration-http)" : {{HttpTargetConfiguration}},
  "[Inference](#cfn-bedrockagentcore-gatewaytarget-targetconfiguration-inference)" : {{InferenceTargetConfiguration}},
  "[Mcp](#cfn-bedrockagentcore-gatewaytarget-targetconfiguration-mcp)" : {{McpTargetConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-targetconfiguration-syntax.yaml"></a>

```
  [Http](#cfn-bedrockagentcore-gatewaytarget-targetconfiguration-http): {{
    HttpTargetConfiguration}}
  [Inference](#cfn-bedrockagentcore-gatewaytarget-targetconfiguration-inference): {{
    InferenceTargetConfiguration}}
  [Mcp](#cfn-bedrockagentcore-gatewaytarget-targetconfiguration-mcp): {{
    McpTargetConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-targetconfiguration-properties"></a>

`Http`  <a name="cfn-bedrockagentcore-gatewaytarget-targetconfiguration-http"></a>
The HTTP target configuration. Use this to route gateway requests to an HTTP-based endpoint such as an AgentCore Runtime.
*Required*: No
*Type*: [HttpTargetConfiguration](aws-properties-bedrockagentcore-gatewaytarget-httptargetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Inference`  <a name="cfn-bedrockagentcore-gatewaytarget-targetconfiguration-inference"></a>
The inference configuration for the target. This configuration routes requests to a large language model (LLM) provider.
*Required*: No
*Type*: [InferenceTargetConfiguration](aws-properties-bedrockagentcore-gatewaytarget-inferencetargetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Mcp`  <a name="cfn-bedrockagentcore-gatewaytarget-targetconfiguration-mcp"></a>
The Model Context Protocol (MCP) configuration for the target. This configuration defines how the gateway uses MCP to communicate with the target.
*Required*: No
*Type*: [McpTargetConfiguration](aws-properties-bedrockagentcore-gatewaytarget-mcptargetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
