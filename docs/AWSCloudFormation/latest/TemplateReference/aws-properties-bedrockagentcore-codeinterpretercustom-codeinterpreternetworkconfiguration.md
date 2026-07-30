---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::CodeInterpreterCustom CodeInterpreterNetworkConfiguration
<a name="aws-properties-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration"></a>

The network configuration for a code interpreter. This structure defines how the code interpreter connects to the network.

## Syntax
<a name="aws-properties-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration-syntax.json"></a>

```
{
  "[NetworkMode](#cfn-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration-networkmode)" : {{String}},
  "[VpcConfig](#cfn-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration-vpcconfig)" : {{VpcConfig}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration-syntax.yaml"></a>

```
  [NetworkMode](#cfn-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration-networkmode): {{String}}
  [VpcConfig](#cfn-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration-vpcconfig): {{
    VpcConfig}}
```

## Properties
<a name="aws-properties-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration-properties"></a>

`NetworkMode`  <a name="cfn-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration-networkmode"></a>
The network mode for the code interpreter. This field specifies how the code interpreter connects to the network.
*Required*: Yes
*Type*: String
*Allowed values*: `PUBLIC | SANDBOX | VPC`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcConfig`  <a name="cfn-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration-vpcconfig"></a>
The network mode configuration for the AgentCore Runtime.
*Required*: No
*Type*: [VpcConfig](aws-properties-bedrockagentcore-codeinterpretercustom-vpcconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
