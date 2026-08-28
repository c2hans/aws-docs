---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-mcpservergrafanaauthorizationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service MCPServerGrafanaAuthorizationConfig
<a name="aws-properties-devopsagent-service-mcpservergrafanaauthorizationconfig"></a>

The authorization configuration for a Grafana MCP server.

## Syntax
<a name="aws-properties-devopsagent-service-mcpservergrafanaauthorizationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-mcpservergrafanaauthorizationconfig-syntax.json"></a>

```
{
  "[BearerToken](#cfn-devopsagent-service-mcpservergrafanaauthorizationconfig-bearertoken)" : {{BearerTokenDetails}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-mcpservergrafanaauthorizationconfig-syntax.yaml"></a>

```
  [BearerToken](#cfn-devopsagent-service-mcpservergrafanaauthorizationconfig-bearertoken): {{
    BearerTokenDetails}}
```

## Properties
<a name="aws-properties-devopsagent-service-mcpservergrafanaauthorizationconfig-properties"></a>

`BearerToken`  <a name="cfn-devopsagent-service-mcpservergrafanaauthorizationconfig-bearertoken"></a>
Bearer token authorization details.
*Required*: Yes
*Type*: [BearerTokenDetails](aws-properties-devopsagent-service-bearertokendetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
