---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-browsercustom-browsernetworkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::BrowserCustom BrowserNetworkConfiguration
<a name="aws-properties-bedrockagentcore-browsercustom-browsernetworkconfiguration"></a>

The network configuration for a browser. This structure defines how the browser connects to the network.

## Syntax
<a name="aws-properties-bedrockagentcore-browsercustom-browsernetworkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-browsercustom-browsernetworkconfiguration-syntax.json"></a>

```
{
  "[NetworkMode](#cfn-bedrockagentcore-browsercustom-browsernetworkconfiguration-networkmode)" : {{String}},
  "[VpcConfig](#cfn-bedrockagentcore-browsercustom-browsernetworkconfiguration-vpcconfig)" : {{VpcConfig}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-browsercustom-browsernetworkconfiguration-syntax.yaml"></a>

```
  [NetworkMode](#cfn-bedrockagentcore-browsercustom-browsernetworkconfiguration-networkmode): {{String}}
  [VpcConfig](#cfn-bedrockagentcore-browsercustom-browsernetworkconfiguration-vpcconfig): {{
    VpcConfig}}
```

## Properties
<a name="aws-properties-bedrockagentcore-browsercustom-browsernetworkconfiguration-properties"></a>

`NetworkMode`  <a name="cfn-bedrockagentcore-browsercustom-browsernetworkconfiguration-networkmode"></a>
The network mode for the browser. This field specifies how the browser connects to the network.
*Required*: Yes
*Type*: String
*Allowed values*: `PUBLIC | VPC`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcConfig`  <a name="cfn-bedrockagentcore-browsercustom-browsernetworkconfiguration-vpcconfig"></a>
The network mode configuration for the AgentCore Runtime.
*Required*: No
*Type*: [VpcConfig](aws-properties-bedrockagentcore-browsercustom-vpcconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
