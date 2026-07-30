---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agentalias-agentaliashistoryevent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::AgentAlias AgentAliasHistoryEvent
<a name="aws-properties-bedrock-agentalias-agentaliashistoryevent"></a>

Contains details about the history of the alias.

## Syntax
<a name="aws-properties-bedrock-agentalias-agentaliashistoryevent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-agentalias-agentaliashistoryevent-syntax.json"></a>

```
{
  "[EndDate](#cfn-bedrock-agentalias-agentaliashistoryevent-enddate)" : {{String}},
  "[RoutingConfiguration](#cfn-bedrock-agentalias-agentaliashistoryevent-routingconfiguration)" : {{[ AgentAliasRoutingConfigurationListItem, ... ]}},
  "[StartDate](#cfn-bedrock-agentalias-agentaliashistoryevent-startdate)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-agentalias-agentaliashistoryevent-syntax.yaml"></a>

```
  [EndDate](#cfn-bedrock-agentalias-agentaliashistoryevent-enddate): {{String}}
  [RoutingConfiguration](#cfn-bedrock-agentalias-agentaliashistoryevent-routingconfiguration): {{
    - AgentAliasRoutingConfigurationListItem}}
  [StartDate](#cfn-bedrock-agentalias-agentaliashistoryevent-startdate): {{String}}
```

## Properties
<a name="aws-properties-bedrock-agentalias-agentaliashistoryevent-properties"></a>

`EndDate`  <a name="cfn-bedrock-agentalias-agentaliashistoryevent-enddate"></a>
The date that the alias stopped being associated to the version in the `routingConfiguration` object
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoutingConfiguration`  <a name="cfn-bedrock-agentalias-agentaliashistoryevent-routingconfiguration"></a>
Contains details about the version of the agent with which the alias is associated.
*Required*: No
*Type*: Array of [AgentAliasRoutingConfigurationListItem](aws-properties-bedrock-agentalias-agentaliasroutingconfigurationlistitem.md)
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartDate`  <a name="cfn-bedrock-agentalias-agentaliashistoryevent-startdate"></a>
The date that the alias began being associated to the version in the `routingConfiguration` object.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
