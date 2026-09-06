---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_HostedZoneLimit.html
---

# HostedZoneLimit
<a name="API_HostedZoneLimit"></a>

A complex type that contains the type of limit that you specified in the request and the current value for that limit.

## Contents
<a name="API_HostedZoneLimit_Contents"></a>

 ** Type **   <a name="Route53-Type-HostedZoneLimit-Type"></a>
The limit that you requested. Valid values include the following:
+  **MAX\_RRSETS\_BY\_ZONE**: The maximum number of records that you can create in the specified hosted zone.
+  **MAX\_VPCS\_ASSOCIATED\_BY\_ZONE**: The maximum number of Amazon VPCs that you can associate with the specified private hosted zone.
Type: String
Valid Values: `MAX_RRSETS_BY_ZONE | MAX_VPCS_ASSOCIATED_BY_ZONE`
Required: Yes

 ** Value **   <a name="Route53-Type-HostedZoneLimit-Value"></a>
The current value for the limit that is specified by `Type`.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

## See Also
<a name="API_HostedZoneLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/HostedZoneLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/HostedZoneLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/HostedZoneLimit)
