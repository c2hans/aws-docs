---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UplinkAwsGroundStationAgentEndpointDetails.html
---

# UplinkAwsGroundStationAgentEndpointDetails
<a name="API_UplinkAwsGroundStationAgentEndpointDetails"></a>

Details for an uplink agent endpoint

## Contents
<a name="API_UplinkAwsGroundStationAgentEndpointDetails_Contents"></a>

 ** dataflowDetails **   <a name="groundstation-Type-UplinkAwsGroundStationAgentEndpointDetails-dataflowDetails"></a>
Dataflow details for the uplink endpoint
Type: [UplinkDataflowDetails](API_UplinkDataflowDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** name **   <a name="groundstation-Type-UplinkAwsGroundStationAgentEndpointDetails-name"></a>
Uplink dataflow endpoint name
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[ a-zA-Z0-9_:-]{1,256}`
Required: Yes

 ** agentStatus **   <a name="groundstation-Type-UplinkAwsGroundStationAgentEndpointDetails-agentStatus"></a>
Status of the agent associated with the uplink dataflow endpoint
Type: String
Valid Values: `SUCCESS | FAILED | ACTIVE | INACTIVE`
Required: No

 ** auditResults **   <a name="groundstation-Type-UplinkAwsGroundStationAgentEndpointDetails-auditResults"></a>
Health audit results for the uplink dataflow endpoint
Type: String
Valid Values: `HEALTHY | UNHEALTHY`
Required: No

## See Also
<a name="API_UplinkAwsGroundStationAgentEndpointDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/UplinkAwsGroundStationAgentEndpointDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/UplinkAwsGroundStationAgentEndpointDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/UplinkAwsGroundStationAgentEndpointDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
