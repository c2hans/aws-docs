---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-registeredmcpservergrafanadetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service RegisteredMCPServerGrafanaDetails
<a name="aws-properties-devopsagent-service-registeredmcpservergrafanadetails"></a>

Grafana MCP server details returned after registration.

## Syntax
<a name="aws-properties-devopsagent-service-registeredmcpservergrafanadetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-registeredmcpservergrafanadetails-syntax.json"></a>

```
{
  "[AuthorizationMethod](#cfn-devopsagent-service-registeredmcpservergrafanadetails-authorizationmethod)" : {{String}},
  "[Description](#cfn-devopsagent-service-registeredmcpservergrafanadetails-description)" : {{String}},
  "[Endpoint](#cfn-devopsagent-service-registeredmcpservergrafanadetails-endpoint)" : {{String}},
  "[Name](#cfn-devopsagent-service-registeredmcpservergrafanadetails-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-registeredmcpservergrafanadetails-syntax.yaml"></a>

```
  [AuthorizationMethod](#cfn-devopsagent-service-registeredmcpservergrafanadetails-authorizationmethod): {{String}}
  [Description](#cfn-devopsagent-service-registeredmcpservergrafanadetails-description): {{String}}
  [Endpoint](#cfn-devopsagent-service-registeredmcpservergrafanadetails-endpoint): {{String}}
  [Name](#cfn-devopsagent-service-registeredmcpservergrafanadetails-name): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-service-registeredmcpservergrafanadetails-properties"></a>

`AuthorizationMethod`  <a name="cfn-devopsagent-service-registeredmcpservergrafanadetails-authorizationmethod"></a>
The authorization method that the MCP server uses.
*Required*: Yes
*Type*: String
*Allowed values*: `bearer-token`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-devopsagent-service-registeredmcpservergrafanadetails-description"></a>
An optional description for the MCP server.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Endpoint`  <a name="cfn-devopsagent-service-registeredmcpservergrafanadetails-endpoint"></a>
The MCP server endpoint URL.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-devopsagent-service-registeredmcpservergrafanadetails-name"></a>
The MCP server name.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
