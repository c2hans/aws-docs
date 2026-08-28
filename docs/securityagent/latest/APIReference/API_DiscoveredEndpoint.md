---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_DiscoveredEndpoint.html
---

# DiscoveredEndpoint
<a name="API_DiscoveredEndpoint"></a>

Represents an endpoint discovered during a pentest job.

## Contents
<a name="API_DiscoveredEndpoint_Contents"></a>

 ** agentSpaceId **   <a name="securityagent-Type-DiscoveredEndpoint-agentSpaceId"></a>
The unique identifier of the agent space associated with the discovered endpoint.
Type: String
Required: Yes

 ** pentestJobId **   <a name="securityagent-Type-DiscoveredEndpoint-pentestJobId"></a>
The unique identifier of the pentest job that discovered the endpoint.
Type: String
Required: Yes

 ** taskId **   <a name="securityagent-Type-DiscoveredEndpoint-taskId"></a>
The unique identifier of the task that discovered the endpoint.
Type: String
Required: Yes

 ** uri **   <a name="securityagent-Type-DiscoveredEndpoint-uri"></a>
The URI of the discovered endpoint.
Type: String
Required: Yes

 ** description **   <a name="securityagent-Type-DiscoveredEndpoint-description"></a>
A description of the discovered endpoint.
Type: String
Required: No

 ** evidence **   <a name="securityagent-Type-DiscoveredEndpoint-evidence"></a>
The evidence that led to the discovery of the endpoint.
Type: String
Required: No

 ** operation **   <a name="securityagent-Type-DiscoveredEndpoint-operation"></a>
The HTTP operation associated with the discovered endpoint.
Type: String
Required: No

## See Also
<a name="API_DiscoveredEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/DiscoveredEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/DiscoveredEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/DiscoveredEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
