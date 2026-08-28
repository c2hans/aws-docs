---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ServiceConfiguration.html
---

# ServiceConfiguration
<a name="API_ServiceConfiguration"></a>

Union of all supported service configuration types. Each service has its own specific configuration structure.

## Contents
<a name="API_ServiceConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** aws **   <a name="devopsagent-Type-ServiceConfiguration-aws"></a>
AWS monitor account configuration.
Type: [AWSConfiguration](API_AWSConfiguration.md) object
Required: No

 ** azure **   <a name="devopsagent-Type-ServiceConfiguration-azure"></a>
Azure subscription integration configuration.
Type: [AzureConfiguration](API_AzureConfiguration.md) object
Required: No

 ** azuredevops **   <a name="devopsagent-Type-ServiceConfiguration-azuredevops"></a>
Azure DevOps project integration configuration.
Type: [AzureDevOpsConfiguration](API_AzureDevOpsConfiguration.md) object
Required: No

 ** dynatrace **   <a name="devopsagent-Type-ServiceConfiguration-dynatrace"></a>
Dynatrace monitoring integration configuration.
Type: [DynatraceConfiguration](API_DynatraceConfiguration.md) object
Required: No

 ** eventChannel **   <a name="devopsagent-Type-ServiceConfiguration-eventChannel"></a>
Event Channel instance integration configuration.
Type: [EventChannelConfiguration](API_EventChannelConfiguration.md) object
Required: No

 ** github **   <a name="devopsagent-Type-ServiceConfiguration-github"></a>
GitHub repository integration configuration.
Type: [GitHubConfiguration](API_GitHubConfiguration.md) object
Required: No

 ** gitlab **   <a name="devopsagent-Type-ServiceConfiguration-gitlab"></a>
GitLab project integration configuration.
Type: [GitLabConfiguration](API_GitLabConfiguration.md) object
Required: No

 ** mcpserver **   <a name="devopsagent-Type-ServiceConfiguration-mcpserver"></a>
MCP (Model Context Protocol) server integration configuration.
Type: [MCPServerConfiguration](API_MCPServerConfiguration.md) object
Required: No

 ** mcpserverdatadog **   <a name="devopsagent-Type-ServiceConfiguration-mcpserverdatadog"></a>
Datadog MCP server integration configuration.
Type: [MCPServerDatadogConfiguration](API_MCPServerDatadogConfiguration.md) object
Required: No

 ** mcpservergrafana **   <a name="devopsagent-Type-ServiceConfiguration-mcpservergrafana"></a>
Grafana MCP server integration configuration.
Type: [MCPServerGrafanaConfiguration](API_MCPServerGrafanaConfiguration.md) object
Required: No

 ** mcpservernewrelic **   <a name="devopsagent-Type-ServiceConfiguration-mcpservernewrelic"></a>
NewRelic instance integration configuration.
Type: [MCPServerNewRelicConfiguration](API_MCPServerNewRelicConfiguration.md) object
Required: No

 ** mcpserversigv4 **   <a name="devopsagent-Type-ServiceConfiguration-mcpserversigv4"></a>
SigV4-authenticated MCP server integration configuration.
Type: [MCPServerSigV4Configuration](API_MCPServerSigV4Configuration.md) object
Required: No

 ** mcpserversplunk **   <a name="devopsagent-Type-ServiceConfiguration-mcpserversplunk"></a>
Splunk MCP server integration configuration.
Type: [MCPServerSplunkConfiguration](API_MCPServerSplunkConfiguration.md) object
Required: No

 ** pagerduty **   <a name="devopsagent-Type-ServiceConfiguration-pagerduty"></a>
PagerDuty integration configuration
Type: [PagerDutyConfiguration](API_PagerDutyConfiguration.md) object
Required: No

 ** remoteagent **   <a name="devopsagent-Type-ServiceConfiguration-remoteagent"></a>
Remote A2A agent integration configuration (token-based auth).
Type: [RemoteAgentConfiguration](API_RemoteAgentConfiguration.md) object
Required: No

 ** remoteagentsigv4 **   <a name="devopsagent-Type-ServiceConfiguration-remoteagentsigv4"></a>
Remote A2A agent integration configuration (SigV4 auth).
Type: [RemoteAgentSigV4Configuration](API_RemoteAgentSigV4Configuration.md) object
Required: No

 ** servicenow **   <a name="devopsagent-Type-ServiceConfiguration-servicenow"></a>
ServiceNow instance integration configuration.
Type: [ServiceNowConfiguration](API_ServiceNowConfiguration.md) object
Required: No

 ** slack **   <a name="devopsagent-Type-ServiceConfiguration-slack"></a>
Slack workspace integration configuration.
Type: [SlackConfiguration](API_SlackConfiguration.md) object
Required: No

 ** sourceAws **   <a name="devopsagent-Type-ServiceConfiguration-sourceAws"></a>
AWS source account configuration for monitoring resources.
Type: [SourceAwsConfiguration](API_SourceAwsConfiguration.md) object
Required: No

## See Also
<a name="API_ServiceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/ServiceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/ServiceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/ServiceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
