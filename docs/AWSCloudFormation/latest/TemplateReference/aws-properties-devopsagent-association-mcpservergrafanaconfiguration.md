---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-mcpservergrafanaconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association MCPServerGrafanaConfiguration
<a name="aws-properties-devopsagent-association-mcpservergrafanaconfiguration"></a>

Configuration for Grafana MCP server integration. Specifies the endpoint URL, tool categories, and webhook settings. Use this configuration to query metrics, dashboards, and alerting data from Grafana.

## Syntax
<a name="aws-properties-devopsagent-association-mcpservergrafanaconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-mcpservergrafanaconfiguration-syntax.json"></a>

```
{
  "[EnableWebhookUpdates](#cfn-devopsagent-association-mcpservergrafanaconfiguration-enablewebhookupdates)" : {{Boolean}},
  "[Endpoint](#cfn-devopsagent-association-mcpservergrafanaconfiguration-endpoint)" : {{String}},
  "[Tools](#cfn-devopsagent-association-mcpservergrafanaconfiguration-tools)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-mcpservergrafanaconfiguration-syntax.yaml"></a>

```
  [EnableWebhookUpdates](#cfn-devopsagent-association-mcpservergrafanaconfiguration-enablewebhookupdates): {{Boolean}}
  [Endpoint](#cfn-devopsagent-association-mcpservergrafanaconfiguration-endpoint): {{String}}
  [Tools](#cfn-devopsagent-association-mcpservergrafanaconfiguration-tools): {{
    - String}}
```

## Properties
<a name="aws-properties-devopsagent-association-mcpservergrafanaconfiguration-properties"></a>

`EnableWebhookUpdates`  <a name="cfn-devopsagent-association-mcpservergrafanaconfiguration-enablewebhookupdates"></a>
Specifies whether the Agent Space creates and updates webhooks for receiving notifications and events from the service.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Endpoint`  <a name="cfn-devopsagent-association-mcpservergrafanaconfiguration-endpoint"></a>
The MCP server endpoint URL.
*Required*: Yes
*Type*: String
*Pattern*: `^https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tools`  <a name="cfn-devopsagent-association-mcpservergrafanaconfiguration-tools"></a>
The list of tool categories to enable for the Grafana MCP server.
*Required*: No
*Type*: Array of String
*Allowed values*: `alerting | annotations | asserts | cloudwatch | dashboard | datasource | elasticsearch | examples | incident | loki | navigation | oncall | prometheus | pyroscope | rendering | runpanelquery | search | searchlogs | sift`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
