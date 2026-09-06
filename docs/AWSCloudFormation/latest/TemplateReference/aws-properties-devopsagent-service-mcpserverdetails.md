---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-mcpserverdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service MCPServerDetails
<a name="aws-properties-devopsagent-service-mcpserverdetails"></a>

Configuration details for registering a custom MCP server.

## Syntax
<a name="aws-properties-devopsagent-service-mcpserverdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-mcpserverdetails-syntax.json"></a>

```
{
  "[AuthorizationConfig](#cfn-devopsagent-service-mcpserverdetails-authorizationconfig)" : {{MCPServerAuthorizationConfig}},
  "[Description](#cfn-devopsagent-service-mcpserverdetails-description)" : {{String}},
  "[Endpoint](#cfn-devopsagent-service-mcpserverdetails-endpoint)" : {{String}},
  "[Name](#cfn-devopsagent-service-mcpserverdetails-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-mcpserverdetails-syntax.yaml"></a>

```
  [AuthorizationConfig](#cfn-devopsagent-service-mcpserverdetails-authorizationconfig): {{
    MCPServerAuthorizationConfig}}
  [Description](#cfn-devopsagent-service-mcpserverdetails-description): {{String}}
  [Endpoint](#cfn-devopsagent-service-mcpserverdetails-endpoint): {{String}}
  [Name](#cfn-devopsagent-service-mcpserverdetails-name): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-service-mcpserverdetails-properties"></a>

`AuthorizationConfig`  <a name="cfn-devopsagent-service-mcpserverdetails-authorizationconfig"></a>
The authorization configuration for the MCP server.
*Required*: Yes
*Type*: [MCPServerAuthorizationConfig](aws-properties-devopsagent-service-mcpserverauthorizationconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-devopsagent-service-mcpserverdetails-description"></a>
A description of the MCP server. Maximum 500 characters.
*Required*: No
*Type*: String
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Endpoint`  <a name="cfn-devopsagent-service-mcpserverdetails-endpoint"></a>
The HTTPS endpoint URL of the MCP server.
*Required*: Yes
*Type*: String
*Pattern*: `^https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-devopsagent-service-mcpserverdetails-name"></a>
The name of the MCP server.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
