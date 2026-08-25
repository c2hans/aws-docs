---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registry-discoveryconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::Registry DiscoveryConfiguration
<a name="aws-properties-agentregistry-registry-discoveryconfiguration"></a>

Discovery configuration for the registry. It controls how consumers are authorized to search the registry and invoke its Model Context Protocol (MCP) endpoint.

## Syntax
<a name="aws-properties-agentregistry-registry-discoveryconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registry-discoveryconfiguration-syntax.json"></a>

```
{
  "[AuthorizerConfiguration](#cfn-agentregistry-registry-discoveryconfiguration-authorizerconfiguration)" : {{AuthorizerConfiguration}}
}
```

### YAML
<a name="aws-properties-agentregistry-registry-discoveryconfiguration-syntax.yaml"></a>

```
  [AuthorizerConfiguration](#cfn-agentregistry-registry-discoveryconfiguration-authorizerconfiguration): {{
    AuthorizerConfiguration}}
```

## Properties
<a name="aws-properties-agentregistry-registry-discoveryconfiguration-properties"></a>

`AuthorizerConfiguration`  <a name="cfn-agentregistry-registry-discoveryconfiguration-authorizerconfiguration"></a>
The authorizer configuration for the registry. This is required when the authorizer type is `CUSTOM_JWT`.
*Required*: No
*Type*: [AuthorizerConfiguration](aws-properties-agentregistry-registry-authorizerconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
