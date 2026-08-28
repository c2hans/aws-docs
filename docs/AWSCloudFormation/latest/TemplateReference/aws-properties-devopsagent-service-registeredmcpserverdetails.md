---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-registeredmcpserverdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service RegisteredMCPServerDetails
<a name="aws-properties-devopsagent-service-registeredmcpserverdetails"></a>

MCP server details returned after registration. Used for both custom MCP server and Splunk MCP server service types.

## Syntax
<a name="aws-properties-devopsagent-service-registeredmcpserverdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-registeredmcpserverdetails-syntax.json"></a>

```
{
  "[ApiKeyHeader](#cfn-devopsagent-service-registeredmcpserverdetails-apikeyheader)" : {{String}},
  "[AuthorizationMethod](#cfn-devopsagent-service-registeredmcpserverdetails-authorizationmethod)" : {{String}},
  "[Description](#cfn-devopsagent-service-registeredmcpserverdetails-description)" : {{String}},
  "[Endpoint](#cfn-devopsagent-service-registeredmcpserverdetails-endpoint)" : {{String}},
  "[Name](#cfn-devopsagent-service-registeredmcpserverdetails-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-registeredmcpserverdetails-syntax.yaml"></a>

```
  [ApiKeyHeader](#cfn-devopsagent-service-registeredmcpserverdetails-apikeyheader): {{String}}
  [AuthorizationMethod](#cfn-devopsagent-service-registeredmcpserverdetails-authorizationmethod): {{String}}
  [Description](#cfn-devopsagent-service-registeredmcpserverdetails-description): {{String}}
  [Endpoint](#cfn-devopsagent-service-registeredmcpserverdetails-endpoint): {{String}}
  [Name](#cfn-devopsagent-service-registeredmcpserverdetails-name): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-service-registeredmcpserverdetails-properties"></a>

`ApiKeyHeader`  <a name="cfn-devopsagent-service-registeredmcpserverdetails-apikeyheader"></a>
The API key header name, if using API key authentication.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizationMethod`  <a name="cfn-devopsagent-service-registeredmcpserverdetails-authorizationmethod"></a>
The authorization method used by the MCP server.
*Allowed Values*: `oauth-client-credentials` \| `api-key` \| `bearer-token`
*Required*: Yes
*Type*: String
*Allowed values*: `oauth-client-credentials | api-key | bearer-token`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-devopsagent-service-registeredmcpserverdetails-description"></a>
The description of the MCP server.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Endpoint`  <a name="cfn-devopsagent-service-registeredmcpserverdetails-endpoint"></a>
The MCP server endpoint URL.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-devopsagent-service-registeredmcpserverdetails-name"></a>
The name of the MCP server.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
