---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_PrivateConnectionSummary.html
---

# PrivateConnectionSummary
<a name="API_PrivateConnectionSummary"></a>

Summarizes a private connection.

## Contents
<a name="API_PrivateConnectionSummary_Contents"></a>

 ** name **   <a name="securityagent-Type-PrivateConnectionSummary-name"></a>
The name of the private connection.
Type: String
Required: Yes

 ** status **   <a name="securityagent-Type-PrivateConnectionSummary-status"></a>
The current status of the private connection.
Type: String
Valid Values: `ACTIVE | CREATE_IN_PROGRESS | CREATE_FAILED | DELETE_IN_PROGRESS | DELETE_FAILED`
Required: Yes

 ** type **   <a name="securityagent-Type-PrivateConnectionSummary-type"></a>
The type of the private connection, indicating whether it is service-managed or self-managed.
Type: String
Valid Values: `SERVICE_MANAGED | SELF_MANAGED`
Required: Yes

 ** certificateExpiryTime **   <a name="securityagent-Type-PrivateConnectionSummary-certificateExpiryTime"></a>
The date and time the connection's certificate expires, in UTC format.
Type: Timestamp
Required: No

 ** dnsResolution **   <a name="securityagent-Type-PrivateConnectionSummary-dnsResolution"></a>
The DNS resolution mode for the resource gateway.
Type: String
Valid Values: `PUBLIC | IN_VPC`
Required: No

 ** failureMessage **   <a name="securityagent-Type-PrivateConnectionSummary-failureMessage"></a>
A message describing why the private connection entered a failed state, if applicable.
Type: String
Required: No

 ** hostAddress **   <a name="securityagent-Type-PrivateConnectionSummary-hostAddress"></a>
The IP address or DNS name of the target resource.
Type: String
Required: No

 ** resourceConfigurationId **   <a name="securityagent-Type-PrivateConnectionSummary-resourceConfigurationId"></a>
The identifier or ARN of the VPC Lattice resource configuration.
Type: String
Required: No

 ** resourceGatewayId **   <a name="securityagent-Type-PrivateConnectionSummary-resourceGatewayId"></a>
The identifier or ARN of the VPC Lattice resource gateway.
Type: String
Required: No

 ** tags **   <a name="securityagent-Type-PrivateConnectionSummary-tags"></a>
The tags attached to the private connection.
Type: String to string map
Required: No

 ** vpcId **   <a name="securityagent-Type-PrivateConnectionSummary-vpcId"></a>
The identifier of the VPC the resource gateway is created in.
Type: String
Required: No

## See Also
<a name="API_PrivateConnectionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/PrivateConnectionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/PrivateConnectionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/PrivateConnectionSummary)
