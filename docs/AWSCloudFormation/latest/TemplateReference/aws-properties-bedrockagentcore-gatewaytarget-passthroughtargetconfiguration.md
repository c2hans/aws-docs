---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-passthroughtargetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget PassthroughTargetConfiguration
<a name="aws-properties-bedrockagentcore-gatewaytarget-passthroughtargetconfiguration"></a>

The configuration for an HTTP passthrough target. A passthrough target forwards requests directly to an external HTTP endpoint.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-passthroughtargetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-passthroughtargetconfiguration-syntax.json"></a>

```
{
  "[Endpoint](#cfn-bedrockagentcore-gatewaytarget-passthroughtargetconfiguration-endpoint)" : {{String}},
  "[ProtocolType](#cfn-bedrockagentcore-gatewaytarget-passthroughtargetconfiguration-protocoltype)" : {{String}},
  "[Schema](#cfn-bedrockagentcore-gatewaytarget-passthroughtargetconfiguration-schema)" : {{HttpApiSchemaConfiguration}},
  "[StickinessConfiguration](#cfn-bedrockagentcore-gatewaytarget-passthroughtargetconfiguration-stickinessconfiguration)" : {{StickinessConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-passthroughtargetconfiguration-syntax.yaml"></a>

```
  [Endpoint](#cfn-bedrockagentcore-gatewaytarget-passthroughtargetconfiguration-endpoint): {{String}}
  [ProtocolType](#cfn-bedrockagentcore-gatewaytarget-passthroughtargetconfiguration-protocoltype): {{String}}
  [Schema](#cfn-bedrockagentcore-gatewaytarget-passthroughtargetconfiguration-schema): {{
    HttpApiSchemaConfiguration}}
  [StickinessConfiguration](#cfn-bedrockagentcore-gatewaytarget-passthroughtargetconfiguration-stickinessconfiguration): {{
    StickinessConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-passthroughtargetconfiguration-properties"></a>

`Endpoint`  <a name="cfn-bedrockagentcore-gatewaytarget-passthroughtargetconfiguration-endpoint"></a>
The HTTPS endpoint that the gateway forwards requests to for this passthrough target.
*Required*: Yes
*Type*: String
*Pattern*: `^https://[a-zA-Z0-9\-\.]+(:[0-9]{1,5})?(/.*)?$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProtocolType`  <a name="cfn-bedrockagentcore-gatewaytarget-passthroughtargetconfiguration-protocoltype"></a>
The application protocol that the passthrough target implements. This value is required for passthrough targets:
+ `MCP` - The Model Context Protocol.
+ `A2A` - The Agent-to-Agent protocol.
+ `INFERENCE` - The protocol for routing requests to a large language model (LLM) provider.
+ `CUSTOM` - A custom application protocol.
*Required*: Yes
*Type*: String
*Allowed values*: `MCP | A2A | INFERENCE | CUSTOM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Schema`  <a name="cfn-bedrockagentcore-gatewaytarget-passthroughtargetconfiguration-schema"></a>
The API schema configuration that defines the structure of the passthrough target's API.
*Required*: No
*Type*: [HttpApiSchemaConfiguration](aws-properties-bedrockagentcore-gatewaytarget-httpapischemaconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StickinessConfiguration`  <a name="cfn-bedrockagentcore-gatewaytarget-passthroughtargetconfiguration-stickinessconfiguration"></a>
The session stickiness configuration for the passthrough target. This configuration routes requests within the same session to the same target.
*Required*: No
*Type*: [StickinessConfiguration](aws-properties-bedrockagentcore-gatewaytarget-stickinessconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
