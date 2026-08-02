---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ServiceDetails.html
---

# ServiceDetails
<a name="API_ServiceDetails"></a>

Union of service-specific configuration details for service registration.

## Contents
<a name="API_ServiceDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** azureidentity **   <a name="devopsagent-Type-ServiceDetails-azureidentity"></a>
Azure integration with AWS Outbound Identity Federation specific service details.
Type: [RegisteredAzureIdentityDetails](API_RegisteredAzureIdentityDetails.md) object
Required: No

 ** dynatrace **   <a name="devopsagent-Type-ServiceDetails-dynatrace"></a>
Dynatrace-specific service details.
Type: [DynatraceServiceDetails](API_DynatraceServiceDetails.md) object
Required: No

 ** eventChannel **   <a name="devopsagent-Type-ServiceDetails-eventChannel"></a>
Event Channel specific service details.
Type: [EventChannelDetails](API_EventChannelDetails.md) object
Required: No

 ** gitlab **   <a name="devopsagent-Type-ServiceDetails-gitlab"></a>
GitLab-specific service details.
Type: [GitLabDetails](API_GitLabDetails.md) object
Required: No

 ** mcpserver **   <a name="devopsagent-Type-ServiceDetails-mcpserver"></a>
MCP server-specific service details.
Type: [MCPServerDetails](API_MCPServerDetails.md) object
Required: No

 ** mcpserverdatadog **   <a name="devopsagent-Type-ServiceDetails-mcpserverdatadog"></a>
Datadog MCP server-specific service details.
Type: [DatadogServiceDetails](API_DatadogServiceDetails.md) object
Required: No

 ** mcpservergrafana **   <a name="devopsagent-Type-ServiceDetails-mcpservergrafana"></a>
Datadog MCP server-specific service details.
Type: [GrafanaServiceDetails](API_GrafanaServiceDetails.md) object
Required: No

 ** mcpservernewrelic **   <a name="devopsagent-Type-ServiceDetails-mcpservernewrelic"></a>
New Relic-specific service details.
Type: [NewRelicServiceDetails](API_NewRelicServiceDetails.md) object
Required: No

 ** mcpserversigv4 **   <a name="devopsagent-Type-ServiceDetails-mcpserversigv4"></a>
SigV4-authenticated MCP server-specific service details.
Type: [MCPServerSigV4ServiceDetails](API_MCPServerSigV4ServiceDetails.md) object
Required: No

 ** mcpserversplunk **   <a name="devopsagent-Type-ServiceDetails-mcpserversplunk"></a>
Splunk MCP server-specific service details.
Type: [MCPServerDetails](API_MCPServerDetails.md) object
Required: No

 ** pagerduty **   <a name="devopsagent-Type-ServiceDetails-pagerduty"></a>
PagerDuty specific service details.
Type: [PagerDutyDetails](API_PagerDutyDetails.md) object
Required: No

 ** remoteagent **   <a name="devopsagent-Type-ServiceDetails-remoteagent"></a>
Remote A2A agent service details (token-based auth).
Type: [RemoteAgentServiceDetails](API_RemoteAgentServiceDetails.md) object
Required: No

 ** remoteagentsigv4 **   <a name="devopsagent-Type-ServiceDetails-remoteagentsigv4"></a>
Remote A2A agent service details (SigV4 auth).
Type: [RemoteAgentSigV4ServiceDetails](API_RemoteAgentSigV4ServiceDetails.md) object
Required: No

 ** servicenow **   <a name="devopsagent-Type-ServiceDetails-servicenow"></a>
ServiceNow-specific service details.
Type: [ServiceNowServiceDetails](API_ServiceNowServiceDetails.md) object
Required: No

## See Also
<a name="API_ServiceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/ServiceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/ServiceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/ServiceDetails)
