---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-mcpservernewrelicconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association MCPServerNewRelicConfiguration
<a name="aws-properties-devopsagent-association-mcpservernewrelicconfiguration"></a>

Configuration for New Relic MCP server integration. Defines the New Relic account ID and MCP server endpoint URL required for the Agent Space to authenticate and query observability data from New Relic.

## Syntax
<a name="aws-properties-devopsagent-association-mcpservernewrelicconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-mcpservernewrelicconfiguration-syntax.json"></a>

```
{
  "[AccountId](#cfn-devopsagent-association-mcpservernewrelicconfiguration-accountid)" : {{String}},
  "[Endpoint](#cfn-devopsagent-association-mcpservernewrelicconfiguration-endpoint)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-mcpservernewrelicconfiguration-syntax.yaml"></a>

```
  [AccountId](#cfn-devopsagent-association-mcpservernewrelicconfiguration-accountid): {{String}}
  [Endpoint](#cfn-devopsagent-association-mcpservernewrelicconfiguration-endpoint): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-association-mcpservernewrelicconfiguration-properties"></a>

`AccountId`  <a name="cfn-devopsagent-association-mcpservernewrelicconfiguration-accountid"></a>
The New Relic account ID. Must be a numeric string of at least 6 characters.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]+$`
*Minimum*: `6`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Endpoint`  <a name="cfn-devopsagent-association-mcpservernewrelicconfiguration-endpoint"></a>
The MCP server endpoint URL. Must be an HTTPS URL (for example, `https://mcp.newrelic.com/mcp/`).
*Required*: Yes
*Type*: String
*Pattern*: `^https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
