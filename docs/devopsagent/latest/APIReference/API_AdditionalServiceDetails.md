---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_AdditionalServiceDetails.html
---

# AdditionalServiceDetails
<a name="API_AdditionalServiceDetails"></a>

Union of service-specific details for different service types.

## Contents
<a name="API_AdditionalServiceDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** azuredevops **   <a name="devopsagent-Type-AdditionalServiceDetails-azuredevops"></a>
Azure DevOps specific service details.
Type: [RegisteredAzureDevOpsServiceDetails](API_RegisteredAzureDevOpsServiceDetails.md) object
Required: No

 ** azureidentity **   <a name="devopsagent-Type-AdditionalServiceDetails-azureidentity"></a>
Azure identity details for services using Azure authentication.
Type: [RegisteredAzureIdentityDetails](API_RegisteredAzureIdentityDetails.md) object
Required: No

 ** github **   <a name="devopsagent-Type-AdditionalServiceDetails-github"></a>
GitHub-specific service details.
Type: [RegisteredGithubServiceDetails](API_RegisteredGithubServiceDetails.md) object
Required: No

 ** gitlab **   <a name="devopsagent-Type-AdditionalServiceDetails-gitlab"></a>
GitLab-specific service details.
Type: [RegisteredGitLabServiceDetails](API_RegisteredGitLabServiceDetails.md) object
Required: No

 ** mcpserver **   <a name="devopsagent-Type-AdditionalServiceDetails-mcpserver"></a>
MCP server-specific service details.
Type: [RegisteredMCPServerDetails](API_RegisteredMCPServerDetails.md) object
Required: No

 ** mcpserverdatadog **   <a name="devopsagent-Type-AdditionalServiceDetails-mcpserverdatadog"></a>
Datadog MCP server-specific service details.
Type: [RegisteredMCPServerDetails](API_RegisteredMCPServerDetails.md) object
Required: No

 ** mcpservergrafana **   <a name="devopsagent-Type-AdditionalServiceDetails-mcpservergrafana"></a>
Grafana MCP server-specific service details.
Type: [RegisteredGrafanaServerDetails](API_RegisteredGrafanaServerDetails.md) object
Required: No

 ** mcpservernewrelic **   <a name="devopsagent-Type-AdditionalServiceDetails-mcpservernewrelic"></a>
New Relic MCP server-specific service details.
Type: [RegisteredNewRelicDetails](API_RegisteredNewRelicDetails.md) object
Required: No

 ** mcpserversigv4 **   <a name="devopsagent-Type-AdditionalServiceDetails-mcpserversigv4"></a>
SigV4-authenticated MCP server-specific service details.
Type: [RegisteredMCPServerSigV4Details](API_RegisteredMCPServerSigV4Details.md) object
Required: No

 ** mcpserversplunk **   <a name="devopsagent-Type-AdditionalServiceDetails-mcpserversplunk"></a>
Splunk MCP server-specific service details.
Type: [RegisteredMCPServerDetails](API_RegisteredMCPServerDetails.md) object
Required: No

 ** pagerduty **   <a name="devopsagent-Type-AdditionalServiceDetails-pagerduty"></a>
Pagerduty service details.
Type: [RegisteredPagerDutyDetails](API_RegisteredPagerDutyDetails.md) object
Required: No

 ** remoteagent **   <a name="devopsagent-Type-AdditionalServiceDetails-remoteagent"></a>
Remote A2A agent-specific service details (token-based auth).
Type: [RegisteredRemoteAgentDetails](API_RegisteredRemoteAgentDetails.md) object
Required: No

 ** remoteagentsigv4 **   <a name="devopsagent-Type-AdditionalServiceDetails-remoteagentsigv4"></a>
Remote A2A agent-specific service details (SigV4 auth).
Type: [RegisteredRemoteAgentSigV4Details](API_RegisteredRemoteAgentSigV4Details.md) object
Required: No

 ** servicenow **   <a name="devopsagent-Type-AdditionalServiceDetails-servicenow"></a>
ServiceNow-specific service details.
Type: [RegisteredServiceNowDetails](API_RegisteredServiceNowDetails.md) object
Required: No

 ** slack **   <a name="devopsagent-Type-AdditionalServiceDetails-slack"></a>
Slack-specific service details.
Type: [RegisteredSlackServiceDetails](API_RegisteredSlackServiceDetails.md) object
Required: No

## See Also
<a name="API_AdditionalServiceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/AdditionalServiceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/AdditionalServiceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/AdditionalServiceDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
