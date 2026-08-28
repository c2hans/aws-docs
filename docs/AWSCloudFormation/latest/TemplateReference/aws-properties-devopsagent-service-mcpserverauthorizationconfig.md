---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-mcpserverauthorizationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service MCPServerAuthorizationConfig
<a name="aws-properties-devopsagent-service-mcpserverauthorizationconfig"></a>

The authorization configuration for a custom MCP server. Specify OAuth client credentials, an API key, or a bearer token.

## Syntax
<a name="aws-properties-devopsagent-service-mcpserverauthorizationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-mcpserverauthorizationconfig-syntax.json"></a>

```
{
  "[ApiKey](#cfn-devopsagent-service-mcpserverauthorizationconfig-apikey)" : {{ApiKeyDetails}},
  "[BearerToken](#cfn-devopsagent-service-mcpserverauthorizationconfig-bearertoken)" : {{BearerTokenDetails}},
  "[OAuthClientCredentials](#cfn-devopsagent-service-mcpserverauthorizationconfig-oauthclientcredentials)" : {{MCPServerOAuthClientCredentialsConfig}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-mcpserverauthorizationconfig-syntax.yaml"></a>

```
  [ApiKey](#cfn-devopsagent-service-mcpserverauthorizationconfig-apikey): {{
    ApiKeyDetails}}
  [BearerToken](#cfn-devopsagent-service-mcpserverauthorizationconfig-bearertoken): {{
    BearerTokenDetails}}
  [OAuthClientCredentials](#cfn-devopsagent-service-mcpserverauthorizationconfig-oauthclientcredentials): {{
    MCPServerOAuthClientCredentialsConfig}}
```

## Properties
<a name="aws-properties-devopsagent-service-mcpserverauthorizationconfig-properties"></a>

`ApiKey`  <a name="cfn-devopsagent-service-mcpserverauthorizationconfig-apikey"></a>
The API key details for authenticating with the MCP server.
*Required*: No
*Type*: [ApiKeyDetails](aws-properties-devopsagent-service-apikeydetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BearerToken`  <a name="cfn-devopsagent-service-mcpserverauthorizationconfig-bearertoken"></a>
The bearer token details for authenticating with the MCP server.
*Required*: No
*Type*: [BearerTokenDetails](aws-properties-devopsagent-service-bearertokendetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuthClientCredentials`  <a name="cfn-devopsagent-service-mcpserverauthorizationconfig-oauthclientcredentials"></a>
The OAuth client credentials for authenticating with the MCP server.
*Required*: No
*Type*: [MCPServerOAuthClientCredentialsConfig](aws-properties-devopsagent-service-mcpserveroauthclientcredentialsconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
