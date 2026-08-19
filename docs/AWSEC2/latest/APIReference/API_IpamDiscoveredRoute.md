---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamDiscoveredRoute.html
---

# IpamDiscoveredRoute
<a name="API_IpamDiscoveredRoute"></a>

Contains information about a BGP route discovered by IPAM resource discovery.

## Contents
<a name="API_IpamDiscoveredRoute_Contents"></a>

 ** advertisementType **
The advertisement type of the route. Possible values:
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
The IP address prefix of the discovered route in CIDR notation.
Type: String
Required: No

 ** ipamPoolId **
The ID of the IPAM pool associated with the route.
Type: String
Required: No

 ** ipamResourceDiscoveryId **
The ID of the IPAM resource discovery that discovered the route.
Type: String
Required: No

 ** networkBorderGroup **
The network border group for the route.
Type: String
Required: No

 ** poolId **
The ID of the BYOIP pool associated with the route.
Type: String
Required: No

 ** resourceOwnerId **
The ID of the resource owner.
Type: String
Required: No

 ** resourceRegion **
The AWS Region where the route was discovered.
Type: String
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
<a name="API_IpamDiscoveredRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamDiscoveredRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamDiscoveredRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamDiscoveredRoute)
