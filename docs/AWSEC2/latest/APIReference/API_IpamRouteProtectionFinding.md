---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamRouteProtectionFinding.html
---

# IpamRouteProtectionFinding
<a name="API_IpamRouteProtectionFinding"></a>

Contains information about a route protection finding, including the RPKI validation status of a BYOIP route announcement.

## Contents
<a name="API_IpamRouteProtectionFinding_Contents"></a>

 ** advertisementType **
The advertisement type. Possible values:
+  `regional` - The IP address is advertised from a single location (regional services such as Amazon EC2).
+  `global` - The IP address is advertised from multiple global locations simultaneously (global services such as Amazon CloudFront).
Type: String
Valid Values: `regional | global`
Required: No

 ** asn **
The Autonomous System Number (ASN) that originates the route.
Type: String
Required: No

 ** cidr **
The IP address prefix in CIDR notation.
Type: String
Required: No

 ** ipamPoolId **
The ID of the IPAM pool associated with the finding.
Type: String
Required: No

 ** networkBorderGroup **
The network border group.
Type: String
Required: No

 ** poolId **
The ID of the BYOIP pool.
Type: String
Required: No

 ** resourceOwnerId **
The ID of the resource owner.
Type: String
Required: No

 ** resourceRegion **
The AWS Region of the resource.
Type: String
Required: No

 ** roaSampleTime **
The time when the ROA data was last sampled.
Type: Timestamp
Required: No

 ** RoaSet.N **
The Route Origin Authorizations (ROAs) that cover the prefix.
Type: Array of [IpamRouteOriginAuthorization](API_IpamRouteOriginAuthorization.md) objects
Required: No

 ** RouteOverlapSet.N **
The overlapping routes detected for this prefix.
Type: Array of [IpamRouteOverlap](API_IpamRouteOverlap.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** rpkiStatus **
The RPKI validation status of the route. Possible values:
+  `valid` - The route has a matching ROA that covers the prefix and origin ASN.
+  `invalid` - The route has a ROA for the prefix, but the origin ASN or prefix length does not match.
+  `unknown` - No ROA exists for the prefix, so RPKI validation cannot be performed.
Type: String
Valid Values: `valid | invalid | unknown`
Required: No

 ** rpkiStrength **
The RPKI enforcement strength for the route. Possible values:
+  `strict` - Invalid routes are rejected.
+  `permissive` - Invalid routes are accepted but flagged.
Type: String
Valid Values: `strict | permissive`
Required: No

 ** sampleTime **
The time when the route was last sampled.
Type: Timestamp
Required: No

 ** state **
The state of the BYOIP CIDR. Possible values:
+  `advertised` - The CIDR is being advertised.
+  `deprovisioned` - The CIDR has been deprovisioned.
+  `failed-deprovision` - Deprovisioning failed.
+  `failed-provision` - Provisioning failed.
+  `pending-deprovision` - Deprovisioning is in progress.
+  `pending-provision` - Provisioning is in progress.
+  `provisioned` - The CIDR is provisioned.
+  `provisioned-not-publicly-advertisable` - The CIDR is provisioned but not publicly advertisable.
Type: String
Valid Values: `advertised | deprovisioned | failed-deprovision | failed-provision | pending-advertising | pending-deprovision | pending-provision | pending-withdrawal | provisioned | provisioned-not-publicly-advertisable`
Required: No

## See Also
<a name="API_IpamRouteProtectionFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamRouteProtectionFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamRouteProtectionFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamRouteProtectionFinding)
