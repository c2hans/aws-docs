---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_HostedZoneConfig.html
---

# HostedZoneConfig

A complex type that contains an optional comment about your hosted zone. If you don't want to specify a comment, omit both the `HostedZoneConfig` and `Comment` elements.

## Contents
<a name="API_HostedZoneConfig_Contents"></a>

 ** Comment **   <a name="Route53-Type-HostedZoneConfig-Comment"></a>
Any comments that you want to include about the hosted zone.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** HostedZoneTier **   <a name="Route53-Type-HostedZoneConfig-HostedZoneTier"></a>
The tier of the hosted zone. The tier controls which features you get and which optional features you can turn on. Valid values are the following:
STANDARD
 `STANDARD` is the default tier for new hosted zones.
ADVANCED
 `ADVANCED` is a tier that includes Change History and offers more optional features.
If you don't specify a tier when you create a hosted zone, Route 53 uses `STANDARD`. Route 53 always returns this value.
Type: String
Valid Values: `STANDARD | ADVANCED`
Required: No

 ** PrivateZone **   <a name="Route53-Type-HostedZoneConfig-PrivateZone"></a>
A value that indicates whether this is a private hosted zone.
Type: Boolean
Required: No

## See Also
<a name="API_HostedZoneConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/HostedZoneConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/HostedZoneConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/HostedZoneConfig)
