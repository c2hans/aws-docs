---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_RoutingInformationNextHop.html
---

# RoutingInformationNextHop
<a name="API_RoutingInformationNextHop"></a>

Information about the next hop for a route in the core network.

## Contents
<a name="API_RoutingInformationNextHop_Contents"></a>

 ** CoreNetworkAttachmentId **   <a name="networkmanager-Type-RoutingInformationNextHop-CoreNetworkAttachmentId"></a>
The ID of the core network attachment for the next hop.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** EdgeLocation **   <a name="networkmanager-Type-RoutingInformationNextHop-EdgeLocation"></a>
The edge location for the next hop.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\s\S]*`
Required: No

 ** IpAddress **   <a name="networkmanager-Type-RoutingInformationNextHop-IpAddress"></a>
The IP address of the next hop.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** ResourceId **   <a name="networkmanager-Type-RoutingInformationNextHop-ResourceId"></a>
The ID of the resource for the next hop.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** ResourceType **   <a name="networkmanager-Type-RoutingInformationNextHop-ResourceType"></a>
The type of resource for the next hop.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** SegmentName **   <a name="networkmanager-Type-RoutingInformationNextHop-SegmentName"></a>
The name of the segment for the next hop.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_RoutingInformationNextHop_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/RoutingInformationNextHop)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/RoutingInformationNextHop)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/RoutingInformationNextHop)
