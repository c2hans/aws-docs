---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-capacityproviderconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime CapacityProviderConfiguration
<a name="aws-properties-bedrockagentcore-runtime-capacityproviderconfiguration"></a>

<a name="aws-properties-bedrockagentcore-runtime-capacityproviderconfiguration-description"></a>The `CapacityProviderConfiguration` property type specifies Property description not available. for an [AWS::BedrockAgentCore::Runtime](aws-resource-bedrockagentcore-runtime.md).

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-capacityproviderconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-capacityproviderconfiguration-syntax.json"></a>

```
{
  "[CapacityProviderArn](#cfn-bedrockagentcore-runtime-capacityproviderconfiguration-capacityproviderarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-capacityproviderconfiguration-syntax.yaml"></a>

```
  [CapacityProviderArn](#cfn-bedrockagentcore-runtime-capacityproviderconfiguration-capacityproviderarn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-capacityproviderconfiguration-properties"></a>

`CapacityProviderArn`  <a name="cfn-bedrockagentcore-runtime-capacityproviderconfiguration-capacityproviderarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:capacity-provider/[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
