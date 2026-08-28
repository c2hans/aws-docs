---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AwsGroundStationAgentEndpoint.html
---

# AwsGroundStationAgentEndpoint
<a name="API_AwsGroundStationAgentEndpoint"></a>

Information about AwsGroundStationAgentEndpoint.

## Contents
<a name="API_AwsGroundStationAgentEndpoint_Contents"></a>

 ** egressAddress **   <a name="groundstation-Type-AwsGroundStationAgentEndpoint-egressAddress"></a>
The egress address of AgentEndpoint.
Type: [ConnectionDetails](API_ConnectionDetails.md) object
Required: Yes

 ** ingressAddress **   <a name="groundstation-Type-AwsGroundStationAgentEndpoint-ingressAddress"></a>
The ingress address of AgentEndpoint.
Type: [RangedConnectionDetails](API_RangedConnectionDetails.md) object
Required: Yes

 ** name **   <a name="groundstation-Type-AwsGroundStationAgentEndpoint-name"></a>
Name string associated with AgentEndpoint. Used as a human-readable identifier for AgentEndpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[ a-zA-Z0-9_:-]{1,256}`
Required: Yes

 ** agentStatus **   <a name="groundstation-Type-AwsGroundStationAgentEndpoint-agentStatus"></a>
The status of AgentEndpoint.
Type: String
Valid Values: `SUCCESS | FAILED | ACTIVE | INACTIVE`
Required: No

 ** auditResults **   <a name="groundstation-Type-AwsGroundStationAgentEndpoint-auditResults"></a>
The results of the audit.
Type: String
Valid Values: `HEALTHY | UNHEALTHY`
Required: No

## See Also
<a name="API_AwsGroundStationAgentEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/AwsGroundStationAgentEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/AwsGroundStationAgentEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/AwsGroundStationAgentEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
