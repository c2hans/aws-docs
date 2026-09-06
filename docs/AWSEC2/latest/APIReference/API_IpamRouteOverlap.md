---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamRouteOverlap.html
---

# IpamRouteOverlap
<a name="API_IpamRouteOverlap"></a>

Contains information about an overlapping route detected for a BYOIP prefix.

## Contents
<a name="API_IpamRouteOverlap_Contents"></a>

 ** asn **
The ASN originating the overlapping route.
Type: String
Required: No

 ** detectedAt **
The time when the overlap was detected.
Type: Timestamp
Required: No

 ** prefix **
The overlapping IP address prefix in CIDR notation.
Type: String
Required: No

## See Also
<a name="API_IpamRouteOverlap_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamRouteOverlap)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamRouteOverlap)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamRouteOverlap)
