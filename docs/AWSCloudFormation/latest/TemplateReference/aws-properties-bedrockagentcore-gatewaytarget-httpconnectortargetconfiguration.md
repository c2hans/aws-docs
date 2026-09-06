---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-httpconnectortargetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget HttpConnectorTargetConfiguration
<a name="aws-properties-bedrockagentcore-gatewaytarget-httpconnectortargetconfiguration"></a>

The configuration for an HTTP connector target. Use this configuration when you want to route HTTP requests through a managed connector.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-httpconnectortargetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-httpconnectortargetconfiguration-syntax.json"></a>

```
{
  "[Parameters](#cfn-bedrockagentcore-gatewaytarget-httpconnectortargetconfiguration-parameters)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Source](#cfn-bedrockagentcore-gatewaytarget-httpconnectortargetconfiguration-source)" : {{HttpConnectorSource}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-httpconnectortargetconfiguration-syntax.yaml"></a>

```
  [Parameters](#cfn-bedrockagentcore-gatewaytarget-httpconnectortargetconfiguration-parameters): {{
    {{Key}}: {{Value}}}}
  [Source](#cfn-bedrockagentcore-gatewaytarget-httpconnectortargetconfiguration-source): {{
    HttpConnectorSource}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-httpconnectortargetconfiguration-properties"></a>

`Parameters`  <a name="cfn-bedrockagentcore-gatewaytarget-httpconnectortargetconfiguration-parameters"></a>
The resource parameters for this connector (for example, `memoryId`). The service validates these parameters against the request path at runtime.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_-]*$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-bedrockagentcore-gatewaytarget-httpconnectortargetconfiguration-source"></a>
The source configuration identifying which HTTP connector to use.
*Required*: Yes
*Type*: [HttpConnectorSource](aws-properties-bedrockagentcore-gatewaytarget-httpconnectorsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
