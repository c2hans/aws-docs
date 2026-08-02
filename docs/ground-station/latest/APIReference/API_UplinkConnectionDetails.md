---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UplinkConnectionDetails.html
---

# UplinkConnectionDetails
<a name="API_UplinkConnectionDetails"></a>

Connection details for customer to Agent and Agent to Ground Station

## Contents
<a name="API_UplinkConnectionDetails_Contents"></a>

 ** agentIpAndPortAddress **   <a name="groundstation-Type-UplinkConnectionDetails-agentIpAndPortAddress"></a>
Ingress address of AgentEndpoint with a port range and an optional mtu.
Type: [RangedConnectionDetails](API_RangedConnectionDetails.md) object
Required: Yes

 ** ingressAddressAndPort **   <a name="groundstation-Type-UplinkConnectionDetails-ingressAddressAndPort"></a>
Egress address of AgentEndpoint with an optional mtu.
Type: [ConnectionDetails](API_ConnectionDetails.md) object
Required: Yes

## See Also
<a name="API_UplinkConnectionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/UplinkConnectionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/UplinkConnectionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/UplinkConnectionDetails)
