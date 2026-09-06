---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-runtimetargetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget RuntimeTargetConfiguration
<a name="aws-properties-bedrockagentcore-gatewaytarget-runtimetargetconfiguration"></a>

Configuration for an AgentCore Runtime target. Specifies the agent runtime to route requests to via HTTP.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-runtimetargetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-runtimetargetconfiguration-syntax.json"></a>

```
{
  "[Arn](#cfn-bedrockagentcore-gatewaytarget-runtimetargetconfiguration-arn)" : {{String}},
  "[Qualifier](#cfn-bedrockagentcore-gatewaytarget-runtimetargetconfiguration-qualifier)" : {{String}},
  "[Schema](#cfn-bedrockagentcore-gatewaytarget-runtimetargetconfiguration-schema)" : {{HttpApiSchemaConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-runtimetargetconfiguration-syntax.yaml"></a>

```
  [Arn](#cfn-bedrockagentcore-gatewaytarget-runtimetargetconfiguration-arn): {{String}}
  [Qualifier](#cfn-bedrockagentcore-gatewaytarget-runtimetargetconfiguration-qualifier): {{String}}
  [Schema](#cfn-bedrockagentcore-gatewaytarget-runtimetargetconfiguration-schema): {{
    HttpApiSchemaConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-runtimetargetconfiguration-properties"></a>

`Arn`  <a name="cfn-bedrockagentcore-gatewaytarget-runtimetargetconfiguration-arn"></a>
The Amazon Resource Name (ARN) of the AgentCore Runtime to route requests to.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:runtime/[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Qualifier`  <a name="cfn-bedrockagentcore-gatewaytarget-runtimetargetconfiguration-qualifier"></a>
The qualifier for the agent runtime, used to target a specific endpoint version. If not specified, the default endpoint is used.
*Required*: No
*Type*: String
*Pattern*: `([1-9][0-9]{0,4})|([a-zA-Z][a-zA-Z0-9_]{0,47})`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Schema`  <a name="cfn-bedrockagentcore-gatewaytarget-runtimetargetconfiguration-schema"></a>
The API schema configuration that defines the structure of the runtime target's API.
*Required*: No
*Type*: [HttpApiSchemaConfiguration](aws-properties-bedrockagentcore-gatewaytarget-httpapischemaconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
