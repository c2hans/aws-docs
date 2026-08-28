---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-mcpserversplunkdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service MCPServerSplunkDetails
<a name="aws-properties-devopsagent-service-mcpserversplunkdetails"></a>

Configuration details for registering a Splunk MCP server.

## Syntax
<a name="aws-properties-devopsagent-service-mcpserversplunkdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-mcpserversplunkdetails-syntax.json"></a>

```
{
  "[AuthorizationConfig](#cfn-devopsagent-service-mcpserversplunkdetails-authorizationconfig)" : {{MCPServerSplunkAuthorizationConfig}},
  "[Description](#cfn-devopsagent-service-mcpserversplunkdetails-description)" : {{String}},
  "[Endpoint](#cfn-devopsagent-service-mcpserversplunkdetails-endpoint)" : {{String}},
  "[Name](#cfn-devopsagent-service-mcpserversplunkdetails-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-mcpserversplunkdetails-syntax.yaml"></a>

```
  [AuthorizationConfig](#cfn-devopsagent-service-mcpserversplunkdetails-authorizationconfig): {{
    MCPServerSplunkAuthorizationConfig}}
  [Description](#cfn-devopsagent-service-mcpserversplunkdetails-description): {{String}}
  [Endpoint](#cfn-devopsagent-service-mcpserversplunkdetails-endpoint): {{String}}
  [Name](#cfn-devopsagent-service-mcpserversplunkdetails-name): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-service-mcpserversplunkdetails-properties"></a>

`AuthorizationConfig`  <a name="cfn-devopsagent-service-mcpserversplunkdetails-authorizationconfig"></a>
The authorization configuration for the Splunk MCP server.
*Required*: Yes
*Type*: [MCPServerSplunkAuthorizationConfig](aws-properties-devopsagent-service-mcpserversplunkauthorizationconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-devopsagent-service-mcpserversplunkdetails-description"></a>
A description of the MCP server. Maximum 500 characters.
*Required*: No
*Type*: String
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Endpoint`  <a name="cfn-devopsagent-service-mcpserversplunkdetails-endpoint"></a>
The HTTPS endpoint URL of the MCP server.
*Required*: Yes
*Type*: String
*Pattern*: `^https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-devopsagent-service-mcpserversplunkdetails-name"></a>
The name of the MCP server.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
