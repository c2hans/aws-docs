---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-httpconnectorsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget HttpConnectorSource
<a name="aws-properties-bedrockagentcore-gatewaytarget-httpconnectorsource"></a>

The source identifying the HTTP connector integration.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-httpconnectorsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-httpconnectorsource-syntax.json"></a>

```
{
  "[ConnectorId](#cfn-bedrockagentcore-gatewaytarget-httpconnectorsource-connectorid)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-httpconnectorsource-syntax.yaml"></a>

```
  [ConnectorId](#cfn-bedrockagentcore-gatewaytarget-httpconnectorsource-connectorid): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-httpconnectorsource-properties"></a>

`ConnectorId`  <a name="cfn-bedrockagentcore-gatewaytarget-httpconnectorsource-connectorid"></a>
The identifier for the HTTP connector integration.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
