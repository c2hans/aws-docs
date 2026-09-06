---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-connectortargetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget ConnectorTargetConfiguration
<a name="aws-properties-bedrockagentcore-gatewaytarget-connectortargetconfiguration"></a>

Configuration for a connector integration target. Connectors provide pre-built integrations with AWS services and third-party tools.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-connectortargetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-connectortargetconfiguration-syntax.json"></a>

```
{
  "[Configurations](#cfn-bedrockagentcore-gatewaytarget-connectortargetconfiguration-configurations)" : {{[ ConnectorConfiguration, ... ]}},
  "[Enabled](#cfn-bedrockagentcore-gatewaytarget-connectortargetconfiguration-enabled)" : {{[ String, ... ]}},
  "[Source](#cfn-bedrockagentcore-gatewaytarget-connectortargetconfiguration-source)" : {{ConnectorSource}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-connectortargetconfiguration-syntax.yaml"></a>

```
  [Configurations](#cfn-bedrockagentcore-gatewaytarget-connectortargetconfiguration-configurations): {{
    - ConnectorConfiguration}}
  [Enabled](#cfn-bedrockagentcore-gatewaytarget-connectortargetconfiguration-enabled): {{
    - String}}
  [Source](#cfn-bedrockagentcore-gatewaytarget-connectortargetconfiguration-source): {{
    ConnectorSource}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-connectortargetconfiguration-properties"></a>

`Configurations`  <a name="cfn-bedrockagentcore-gatewaytarget-connectortargetconfiguration-configurations"></a>
A list of per-tool configurations for the connector.
*Required*: No
*Type*: Array of [ConnectorConfiguration](aws-properties-bedrockagentcore-gatewaytarget-connectorconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-bedrockagentcore-gatewaytarget-connectortargetconfiguration-enabled"></a>
A list of tool names to enable from this connector. If absent, all tools provided by the connector are enabled.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-bedrockagentcore-gatewaytarget-connectortargetconfiguration-source"></a>
The source configuration identifying which connector to use.
*Required*: Yes
*Type*: [ConnectorSource](aws-properties-bedrockagentcore-gatewaytarget-connectorsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
