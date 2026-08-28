---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-mcpserveroauthclientcredentialsconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service MCPServerOAuthClientCredentialsConfig
<a name="aws-properties-devopsagent-service-mcpserveroauthclientcredentialsconfig"></a>

The OAuth client credentials configuration for a custom MCP server.

## Syntax
<a name="aws-properties-devopsagent-service-mcpserveroauthclientcredentialsconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-mcpserveroauthclientcredentialsconfig-syntax.json"></a>

```
{
  "[ClientId](#cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-clientid)" : {{String}},
  "[ClientName](#cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-clientname)" : {{String}},
  "[ClientSecret](#cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-clientsecret)" : {{String}},
  "[ExchangeParameters](#cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-exchangeparameters)" : {{Json}},
  "[ExchangeUrl](#cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-exchangeurl)" : {{String}},
  "[Scopes](#cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-scopes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-mcpserveroauthclientcredentialsconfig-syntax.yaml"></a>

```
  [ClientId](#cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-clientid): {{String}}
  [ClientName](#cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-clientname): {{String}}
  [ClientSecret](#cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-clientsecret): {{String}}
  [ExchangeParameters](#cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-exchangeparameters): {{Json}}
  [ExchangeUrl](#cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-exchangeurl): {{String}}
  [Scopes](#cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-scopes): {{
    - String}}
```

## Properties
<a name="aws-properties-devopsagent-service-mcpserveroauthclientcredentialsconfig-properties"></a>

`ClientId`  <a name="cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-clientid"></a>
The OAuth client ID.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientName`  <a name="cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-clientname"></a>
A friendly name for the OAuth client.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecret`  <a name="cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-clientsecret"></a>
The OAuth client secret.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExchangeParameters`  <a name="cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-exchangeparameters"></a>
Additional parameters for the OAuth token exchange request.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExchangeUrl`  <a name="cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-exchangeurl"></a>
The OAuth token exchange endpoint URL.
*Required*: Yes
*Type*: String
*Pattern*: `^https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scopes`  <a name="cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-scopes"></a>
The OAuth scopes to request during authentication.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
