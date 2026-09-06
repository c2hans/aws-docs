---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agentalias-agentaliasroutingconfigurationlistitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::AgentAlias AgentAliasRoutingConfigurationListItem
<a name="aws-properties-bedrock-agentalias-agentaliasroutingconfigurationlistitem"></a>

Contains details about the routing configuration of the alias.

## Syntax
<a name="aws-properties-bedrock-agentalias-agentaliasroutingconfigurationlistitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-agentalias-agentaliasroutingconfigurationlistitem-syntax.json"></a>

```
{
  "[AgentVersion](#cfn-bedrock-agentalias-agentaliasroutingconfigurationlistitem-agentversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-agentalias-agentaliasroutingconfigurationlistitem-syntax.yaml"></a>

```
  [AgentVersion](#cfn-bedrock-agentalias-agentaliasroutingconfigurationlistitem-agentversion): {{String}}
```

## Properties
<a name="aws-properties-bedrock-agentalias-agentaliasroutingconfigurationlistitem-properties"></a>

`AgentVersion`  <a name="cfn-bedrock-agentalias-agentaliasroutingconfigurationlistitem-agentversion"></a>
The version of the agent with which the alias is associated.
*Required*: Yes
*Type*: String
*Pattern*: `^(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})$`
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
