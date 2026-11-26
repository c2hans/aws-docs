---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_SubnetAndZone.html
---

# SubnetAndZone

A subnet and its associated Availability Zone.

## Contents
<a name="API_SubnetAndZone_Contents"></a>

 ** subnetId **   <a name="elasticloadbalancing-Type-SubnetAndZone-subnetId"></a>
The ID of the subnet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `subnet-.+`
Required: Yes

 ** zoneId **   <a name="elasticloadbalancing-Type-SubnetAndZone-zoneId"></a>
The ID of the Availability Zone.
Type: String
Required: Yes

 ** zoneName **   <a name="elasticloadbalancing-Type-SubnetAndZone-zoneName"></a>
The name of the Availability Zone (for example, `us-east-1a`).
Type: String
Required: No

## See Also
<a name="API_SubnetAndZone_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elb-proxy-2026-11-20/SubnetAndZone)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elb-proxy-2026-11-20/SubnetAndZone)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elb-proxy-2026-11-20/SubnetAndZone)
