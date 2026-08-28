---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RouteServerBgpOptionsRequest.html
---

# RouteServerBgpOptionsRequest
<a name="API_RouteServerBgpOptionsRequest"></a>

The BGP configuration options requested for a route server peer.

## Contents
<a name="API_RouteServerBgpOptionsRequest_Contents"></a>

 ** PeerAsn **
The Border Gateway Protocol (BGP) Autonomous System Number (ASN) for the appliance. Valid values are from 1 to 4294967295. We recommend using a private ASN in the 64512–65534 (16-bit ASN) or 4200000000–4294967294 (32-bit ASN) range.
Type: Long
Required: Yes

 ** PeerLivenessDetection **
The requested liveness detection protocol for the BGP peer.
+  `bgp-keepalive`: The standard BGP keep alive mechanism ([RFC4271](https://www.rfc-editor.org/rfc/rfc4271#page-21)) that is stable but may take longer to fail-over in cases of network impact or router failure.
+  `bfd`: An additional Bidirectional Forwarding Detection (BFD) protocol ([RFC5880](https://www.rfc-editor.org/rfc/rfc5880)) that enables fast failover by using more sensitive liveness detection.
Defaults to `bgp-keepalive`.
Type: String
Valid Values: `bfd | bgp-keepalive`
Required: No

## See Also
<a name="API_RouteServerBgpOptionsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RouteServerBgpOptionsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RouteServerBgpOptionsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RouteServerBgpOptionsRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
