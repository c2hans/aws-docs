---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-mcpserversplunkauthorizationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service MCPServerSplunkAuthorizationConfig
<a name="aws-properties-devopsagent-service-mcpserversplunkauthorizationconfig"></a>

The authorization configuration for a Splunk MCP server.

## Syntax
<a name="aws-properties-devopsagent-service-mcpserversplunkauthorizationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-mcpserversplunkauthorizationconfig-syntax.json"></a>

```
{
  "[BearerToken](#cfn-devopsagent-service-mcpserversplunkauthorizationconfig-bearertoken)" : {{BearerTokenDetails}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-mcpserversplunkauthorizationconfig-syntax.yaml"></a>

```
  [BearerToken](#cfn-devopsagent-service-mcpserversplunkauthorizationconfig-bearertoken): {{
    BearerTokenDetails}}
```

## Properties
<a name="aws-properties-devopsagent-service-mcpserversplunkauthorizationconfig-properties"></a>

`BearerToken`  <a name="cfn-devopsagent-service-mcpserversplunkauthorizationconfig-bearertoken"></a>
The bearer token details for authenticating with the Splunk MCP server.
*Required*: Yes
*Type*: [BearerTokenDetails](aws-properties-devopsagent-service-bearertokendetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
