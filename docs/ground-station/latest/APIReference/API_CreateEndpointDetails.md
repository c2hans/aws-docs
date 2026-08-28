---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateEndpointDetails.html
---

# CreateEndpointDetails
<a name="API_CreateEndpointDetails"></a>

Endpoint definition used for creating a dataflow endpoint

## Contents
<a name="API_CreateEndpointDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** downlinkAwsGroundStationAgentEndpoint **   <a name="groundstation-Type-CreateEndpointDetails-downlinkAwsGroundStationAgentEndpoint"></a>
Definition for a downlink agent endpoint
Type: [DownlinkAwsGroundStationAgentEndpoint](API_DownlinkAwsGroundStationAgentEndpoint.md) object
Required: No

 ** uplinkAwsGroundStationAgentEndpoint **   <a name="groundstation-Type-CreateEndpointDetails-uplinkAwsGroundStationAgentEndpoint"></a>
Definition for an uplink agent endpoint
Type: [UplinkAwsGroundStationAgentEndpoint](API_UplinkAwsGroundStationAgentEndpoint.md) object
Required: No

## See Also
<a name="API_CreateEndpointDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/CreateEndpointDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/CreateEndpointDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/CreateEndpointDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
