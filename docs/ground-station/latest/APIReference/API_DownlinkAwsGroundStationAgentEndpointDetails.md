---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DownlinkAwsGroundStationAgentEndpointDetails.html
---

# DownlinkAwsGroundStationAgentEndpointDetails
<a name="API_DownlinkAwsGroundStationAgentEndpointDetails"></a>

Details for a downlink agent endpoint

## Contents
<a name="API_DownlinkAwsGroundStationAgentEndpointDetails_Contents"></a>

 ** dataflowDetails **   <a name="groundstation-Type-DownlinkAwsGroundStationAgentEndpointDetails-dataflowDetails"></a>
Dataflow details for the downlink endpoint
Type: [DownlinkDataflowDetails](API_DownlinkDataflowDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** name **   <a name="groundstation-Type-DownlinkAwsGroundStationAgentEndpointDetails-name"></a>
Downlink dataflow endpoint name
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[ a-zA-Z0-9_:-]{1,256}`
Required: Yes

 ** agentStatus **   <a name="groundstation-Type-DownlinkAwsGroundStationAgentEndpointDetails-agentStatus"></a>
Status of the agent associated with the downlink dataflow endpoint
Type: String
Valid Values: `SUCCESS | FAILED | ACTIVE | INACTIVE`
Required: No

 ** auditResults **   <a name="groundstation-Type-DownlinkAwsGroundStationAgentEndpointDetails-auditResults"></a>
Health audit results for the downlink dataflow endpoint
Type: String
Valid Values: `HEALTHY | UNHEALTHY`
Required: No

## See Also
<a name="API_DownlinkAwsGroundStationAgentEndpointDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/DownlinkAwsGroundStationAgentEndpointDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/DownlinkAwsGroundStationAgentEndpointDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/DownlinkAwsGroundStationAgentEndpointDetails)
