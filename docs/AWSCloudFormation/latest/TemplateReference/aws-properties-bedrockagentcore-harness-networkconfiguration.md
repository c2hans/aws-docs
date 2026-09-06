---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-networkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness NetworkConfiguration
<a name="aws-properties-bedrockagentcore-harness-networkconfiguration"></a>

SecurityConfig for the Agent.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-networkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-networkconfiguration-syntax.json"></a>

```
{
  "[NetworkMode](#cfn-bedrockagentcore-harness-networkconfiguration-networkmode)" : {{String}},
  "[NetworkModeConfig](#cfn-bedrockagentcore-harness-networkconfiguration-networkmodeconfig)" : {{VpcConfig}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-networkconfiguration-syntax.yaml"></a>

```
  [NetworkMode](#cfn-bedrockagentcore-harness-networkconfiguration-networkmode): {{String}}
  [NetworkModeConfig](#cfn-bedrockagentcore-harness-networkconfiguration-networkmodeconfig): {{
    VpcConfig}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-networkconfiguration-properties"></a>

`NetworkMode`  <a name="cfn-bedrockagentcore-harness-networkconfiguration-networkmode"></a>
The network mode for the AgentCore Runtime.
*Required*: Yes
*Type*: String
*Allowed values*: `PUBLIC | VPC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkModeConfig`  <a name="cfn-bedrockagentcore-harness-networkconfiguration-networkmodeconfig"></a>
The network mode configuration for the AgentCore Runtime.
*Required*: No
*Type*: [VpcConfig](aws-properties-bedrockagentcore-harness-vpcconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
