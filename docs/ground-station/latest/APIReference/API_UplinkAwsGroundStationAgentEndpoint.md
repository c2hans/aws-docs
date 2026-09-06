---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UplinkAwsGroundStationAgentEndpoint.html
---

# UplinkAwsGroundStationAgentEndpoint
<a name="API_UplinkAwsGroundStationAgentEndpoint"></a>

Definition for an uplink agent endpoint

## Contents
<a name="API_UplinkAwsGroundStationAgentEndpoint_Contents"></a>

 ** dataflowDetails **   <a name="groundstation-Type-UplinkAwsGroundStationAgentEndpoint-dataflowDetails"></a>
Dataflow details for the uplink endpoint
Type: [UplinkDataflowDetails](API_UplinkDataflowDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** name **   <a name="groundstation-Type-UplinkAwsGroundStationAgentEndpoint-name"></a>
Uplink dataflow endpoint name
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[ a-zA-Z0-9_:-]{1,256}`
Required: Yes

## See Also
<a name="API_UplinkAwsGroundStationAgentEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/UplinkAwsGroundStationAgentEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/UplinkAwsGroundStationAgentEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/UplinkAwsGroundStationAgentEndpoint)
