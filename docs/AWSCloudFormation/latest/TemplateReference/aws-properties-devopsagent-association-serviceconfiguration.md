---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-serviceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association ServiceConfiguration
<a name="aws-properties-devopsagent-association-serviceconfiguration"></a>

The configuration that directs how Agent Space interacts with the given service. You can specify only one configuration type per association.

## Syntax
<a name="aws-properties-devopsagent-association-serviceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-serviceconfiguration-syntax.json"></a>

```
{
  "[Aws](#cfn-devopsagent-association-serviceconfiguration-aws)" : {{AWSConfiguration}},
  "[Azure](#cfn-devopsagent-association-serviceconfiguration-azure)" : {{AzureConfiguration}},
  "[Dynatrace](#cfn-devopsagent-association-serviceconfiguration-dynatrace)" : {{DynatraceConfiguration}},
  "[EventChannel](#cfn-devopsagent-association-serviceconfiguration-eventchannel)" : {{EventChannelConfiguration}},
  "[GitHub](#cfn-devopsagent-association-serviceconfiguration-github)" : {{GitHubConfiguration}},
  "[GitLab](#cfn-devopsagent-association-serviceconfiguration-gitlab)" : {{GitLabConfiguration}},
  "[MCPServer](#cfn-devopsagent-association-serviceconfiguration-mcpserver)" : {{MCPServerConfiguration}},
  "[MCPServerDatadog](#cfn-devopsagent-association-serviceconfiguration-mcpserverdatadog)" : {{MCPServerDatadogConfiguration}},
  "[MCPServerGrafana](#cfn-devopsagent-association-serviceconfiguration-mcpservergrafana)" : {{MCPServerGrafanaConfiguration}},
  "[MCPServerNewRelic](#cfn-devopsagent-association-serviceconfiguration-mcpservernewrelic)" : {{MCPServerNewRelicConfiguration}},
  "[MCPServerSigV4](#cfn-devopsagent-association-serviceconfiguration-mcpserversigv4)" : {{MCPServerSigV4Configuration}},
  "[MCPServerSplunk](#cfn-devopsagent-association-serviceconfiguration-mcpserversplunk)" : {{MCPServerSplunkConfiguration}},
  "[PagerDuty](#cfn-devopsagent-association-serviceconfiguration-pagerduty)" : {{PagerDutyConfiguration}},
  "[ServiceNow](#cfn-devopsagent-association-serviceconfiguration-servicenow)" : {{ServiceNowConfiguration}},
  "[Slack](#cfn-devopsagent-association-serviceconfiguration-slack)" : {{SlackConfiguration}},
  "[SourceAws](#cfn-devopsagent-association-serviceconfiguration-sourceaws)" : {{SourceAwsConfiguration}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-serviceconfiguration-syntax.yaml"></a>

```
  [Aws](#cfn-devopsagent-association-serviceconfiguration-aws): {{
    AWSConfiguration}}
  [Azure](#cfn-devopsagent-association-serviceconfiguration-azure): {{
    AzureConfiguration}}
  [Dynatrace](#cfn-devopsagent-association-serviceconfiguration-dynatrace): {{
    DynatraceConfiguration}}
  [EventChannel](#cfn-devopsagent-association-serviceconfiguration-eventchannel): {{
    EventChannelConfiguration}}
  [GitHub](#cfn-devopsagent-association-serviceconfiguration-github): {{
    GitHubConfiguration}}
  [GitLab](#cfn-devopsagent-association-serviceconfiguration-gitlab): {{
    GitLabConfiguration}}
  [MCPServer](#cfn-devopsagent-association-serviceconfiguration-mcpserver): {{
    MCPServerConfiguration}}
  [MCPServerDatadog](#cfn-devopsagent-association-serviceconfiguration-mcpserverdatadog): {{
    MCPServerDatadogConfiguration}}
  [MCPServerGrafana](#cfn-devopsagent-association-serviceconfiguration-mcpservergrafana): {{
    MCPServerGrafanaConfiguration}}
  [MCPServerNewRelic](#cfn-devopsagent-association-serviceconfiguration-mcpservernewrelic): {{
    MCPServerNewRelicConfiguration}}
  [MCPServerSigV4](#cfn-devopsagent-association-serviceconfiguration-mcpserversigv4): {{
    MCPServerSigV4Configuration}}
  [MCPServerSplunk](#cfn-devopsagent-association-serviceconfiguration-mcpserversplunk): {{
    MCPServerSplunkConfiguration}}
  [PagerDuty](#cfn-devopsagent-association-serviceconfiguration-pagerduty): {{
    PagerDutyConfiguration}}
  [ServiceNow](#cfn-devopsagent-association-serviceconfiguration-servicenow): {{
    ServiceNowConfiguration}}
  [Slack](#cfn-devopsagent-association-serviceconfiguration-slack): {{
    SlackConfiguration}}
  [SourceAws](#cfn-devopsagent-association-serviceconfiguration-sourceaws): {{
    SourceAwsConfiguration}}
```

## Properties
<a name="aws-properties-devopsagent-association-serviceconfiguration-properties"></a>

`Aws`  <a name="cfn-devopsagent-association-serviceconfiguration-aws"></a>
Configuration for AWS monitor account integration. Specifies the account ID, assumable role ARN, and resources to be monitored in the primary monitoring account.
*Required*: No
*Type*: [AWSConfiguration](aws-properties-devopsagent-association-awsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Azure`  <a name="cfn-devopsagent-association-serviceconfiguration-azure"></a>
Property description not available.
*Required*: No
*Type*: [AzureConfiguration](aws-properties-devopsagent-association-azureconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Dynatrace`  <a name="cfn-devopsagent-association-serviceconfiguration-dynatrace"></a>
Configuration for Dynatrace monitoring integration. Specifies the environment ID, resources to monitor, and webhook settings to enable the Agent Space to access Dynatrace metrics, traces, and logs.
*Required*: No
*Type*: [DynatraceConfiguration](aws-properties-devopsagent-association-dynatraceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventChannel`  <a name="cfn-devopsagent-association-serviceconfiguration-eventchannel"></a>
Configuration for Event Channel integration. Specifies webhook settings to enable the Agent Space to receive and process real-time events from external systems.
*Required*: No
*Type*: [EventChannelConfiguration](aws-properties-devopsagent-association-eventchannelconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GitHub`  <a name="cfn-devopsagent-association-serviceconfiguration-github"></a>
Configuration for GitHub repository integration. Specifies the repository name, repository ID, owner, and owner type to enable the Agent Space to access code, pull requests, and issues.
*Required*: No
*Type*: [GitHubConfiguration](aws-properties-devopsagent-association-githubconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GitLab`  <a name="cfn-devopsagent-association-serviceconfiguration-gitlab"></a>
Configuration for GitLab project integration. Specifies the project ID, project path, instance identifier, and webhook settings to enable the Agent Space to access code, merge requests, and issues.
*Required*: No
*Type*: [GitLabConfiguration](aws-properties-devopsagent-association-gitlabconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MCPServer`  <a name="cfn-devopsagent-association-serviceconfiguration-mcpserver"></a>
Configuration for custom MCP (Model Context Protocol) server integration. Specifies the server name, endpoint URL, available tools, description, and webhook settings to enable the Agent Space to interact with custom MCP servers.
*Required*: No
*Type*: [MCPServerConfiguration](aws-properties-devopsagent-association-mcpserverconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MCPServerDatadog`  <a name="cfn-devopsagent-association-serviceconfiguration-mcpserverdatadog"></a>
Configuration for Datadog MCP server integration. Specifies the server name, endpoint URL, optional description, and webhook settings to enable the Agent Space to query metrics, traces, and logs from Datadog.
*Required*: No
*Type*: [MCPServerDatadogConfiguration](aws-properties-devopsagent-association-mcpserverdatadogconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MCPServerGrafana`  <a name="cfn-devopsagent-association-serviceconfiguration-mcpservergrafana"></a>
Property description not available.
*Required*: No
*Type*: [MCPServerGrafanaConfiguration](aws-properties-devopsagent-association-mcpservergrafanaconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MCPServerNewRelic`  <a name="cfn-devopsagent-association-serviceconfiguration-mcpservernewrelic"></a>
Configuration for New Relic MCP server integration. Specifies the New Relic account ID and MCP endpoint URL to enable the Agent Space to query metrics, traces, and logs from New Relic.
*Required*: No
*Type*: [MCPServerNewRelicConfiguration](aws-properties-devopsagent-association-mcpservernewrelicconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MCPServerSigV4`  <a name="cfn-devopsagent-association-serviceconfiguration-mcpserversigv4"></a>
Property description not available.
*Required*: No
*Type*: [MCPServerSigV4Configuration](aws-properties-devopsagent-association-mcpserversigv4configuration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MCPServerSplunk`  <a name="cfn-devopsagent-association-serviceconfiguration-mcpserversplunk"></a>
Configuration for Splunk MCP server integration. Specifies the server name, endpoint URL, optional description, and webhook settings to enable the Agent Space to query logs, metrics, and events from Splunk.
*Required*: No
*Type*: [MCPServerSplunkConfiguration](aws-properties-devopsagent-association-mcpserversplunkconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PagerDuty`  <a name="cfn-devopsagent-association-serviceconfiguration-pagerduty"></a>
Property description not available.
*Required*: No
*Type*: [PagerDutyConfiguration](aws-properties-devopsagent-association-pagerdutyconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceNow`  <a name="cfn-devopsagent-association-serviceconfiguration-servicenow"></a>
Configuration for ServiceNow instance integration. Specifies the instance URL, instance ID, and webhook settings to enable the Agent Space to create, update, and manage ServiceNow incidents and change requests.
*Required*: No
*Type*: [ServiceNowConfiguration](aws-properties-devopsagent-association-servicenowconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Slack`  <a name="cfn-devopsagent-association-serviceconfiguration-slack"></a>
Configuration for Slack workspace integration. Specifies the workspace ID, workspace name, and transmission targets to enable the Agent Space to send notifications to designated Slack channels.
*Required*: No
*Type*: [SlackConfiguration](aws-properties-devopsagent-association-slackconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceAws`  <a name="cfn-devopsagent-association-serviceconfiguration-sourceaws"></a>
Configuration for AWS source account integration. Specifies the account ID, assumable role ARN, and resources to be monitored in the source account.
*Required*: No
*Type*: [SourceAwsConfiguration](aws-properties-devopsagent-association-sourceawsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
