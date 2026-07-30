---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-agentflownodeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion AgentFlowNodeConfiguration
<a name="aws-properties-bedrock-flowversion-agentflownodeconfiguration"></a>

Defines an agent node in your flow. You specify the agent to invoke at this point in the flow. For more information, see [Node types in a flow](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html) in the Amazon Bedrock User Guide.

## Syntax
<a name="aws-properties-bedrock-flowversion-agentflownodeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-agentflownodeconfiguration-syntax.json"></a>

```
{
  "[AgentAliasArn](#cfn-bedrock-flowversion-agentflownodeconfiguration-agentaliasarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-agentflownodeconfiguration-syntax.yaml"></a>

```
  [AgentAliasArn](#cfn-bedrock-flowversion-agentflownodeconfiguration-agentaliasarn): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-agentflownodeconfiguration-properties"></a>

`AgentAliasArn`  <a name="cfn-bedrock-flowversion-agentflownodeconfiguration-agentaliasarn"></a>
The Amazon Resource Name (ARN) of the alias of the agent to invoke.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:agent-alias/[0-9a-zA-Z]{10}/[0-9a-zA-Z]{10}$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
