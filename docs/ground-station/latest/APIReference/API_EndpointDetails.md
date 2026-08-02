---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_EndpointDetails.html
---

# EndpointDetails
<a name="API_EndpointDetails"></a>

Information about the endpoint details.

## Contents
<a name="API_EndpointDetails_Contents"></a>

 ** awsGroundStationAgentEndpoint **   <a name="groundstation-Type-EndpointDetails-awsGroundStationAgentEndpoint"></a>
An agent endpoint.
Type: [AwsGroundStationAgentEndpoint](API_AwsGroundStationAgentEndpoint.md) object
Required: No

 ** downlinkAwsGroundStationAgentEndpoint **   <a name="groundstation-Type-EndpointDetails-downlinkAwsGroundStationAgentEndpoint"></a>
Definition for a downlink agent endpoint
Type: [DownlinkAwsGroundStationAgentEndpointDetails](API_DownlinkAwsGroundStationAgentEndpointDetails.md) object
Required: No

 ** endpoint **   <a name="groundstation-Type-EndpointDetails-endpoint"></a>
A dataflow endpoint.
Type: [DataflowEndpoint](API_DataflowEndpoint.md) object
Required: No

 ** healthReasons **   <a name="groundstation-Type-EndpointDetails-healthReasons"></a>
Health reasons for a dataflow endpoint. This field is ignored when calling `CreateDataflowEndpointGroup`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Valid Values: `NO_REGISTERED_AGENT | INVALID_IP_OWNERSHIP | NOT_AUTHORIZED_TO_CREATE_SLR | UNVERIFIED_IP_OWNERSHIP | INITIALIZING_DATAPLANE | DATAPLANE_FAILURE | HEALTHY`
Required: No

 ** healthStatus **   <a name="groundstation-Type-EndpointDetails-healthStatus"></a>
A dataflow endpoint health status. This field is ignored when calling `CreateDataflowEndpointGroup`.
Type: String
Valid Values: `HEALTHY | UNHEALTHY`
Required: No

 ** securityDetails **   <a name="groundstation-Type-EndpointDetails-securityDetails"></a>
Endpoint security details including a list of subnets, a list of security groups and a role to connect streams to instances.
Type: [SecurityDetails](API_SecurityDetails.md) object
Required: No

 ** uplinkAwsGroundStationAgentEndpoint **   <a name="groundstation-Type-EndpointDetails-uplinkAwsGroundStationAgentEndpoint"></a>
Definition for an uplink agent endpoint
Type: [UplinkAwsGroundStationAgentEndpointDetails](API_UplinkAwsGroundStationAgentEndpointDetails.md) object
Required: No

## See Also
<a name="API_EndpointDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/EndpointDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/EndpointDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/EndpointDetails)
