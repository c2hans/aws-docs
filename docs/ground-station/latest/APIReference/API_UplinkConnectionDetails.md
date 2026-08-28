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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
