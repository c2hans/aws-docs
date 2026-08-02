---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CoreNetworkChangeValues.html
---

# CoreNetworkChangeValues
<a name="API_CoreNetworkChangeValues"></a>

Describes a core network change.

## Contents
<a name="API_CoreNetworkChangeValues_Contents"></a>

 ** Asn **   <a name="networkmanager-Type-CoreNetworkChangeValues-Asn"></a>
The ASN of a core network.
Type: Long
Required: No

 ** AttachmentId **   <a name="networkmanager-Type-CoreNetworkChangeValues-AttachmentId"></a>
The attachment identifier in the core network change values.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** Cidr **   <a name="networkmanager-Type-CoreNetworkChangeValues-Cidr"></a>
The IP addresses used for a core network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** DestinationIdentifier **   <a name="networkmanager-Type-CoreNetworkChangeValues-DestinationIdentifier"></a>
The ID of the destination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** DnsSupport **   <a name="networkmanager-Type-CoreNetworkChangeValues-DnsSupport"></a>
Indicates whether public DNS support is supported. The default is `true`.
Type: Boolean
Required: No

 ** EdgeLocations **   <a name="networkmanager-Type-CoreNetworkChangeValues-EdgeLocations"></a>
The Regions where edges are located in a core network.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\s\S]*`
Required: No

 ** InsideCidrBlocks **   <a name="networkmanager-Type-CoreNetworkChangeValues-InsideCidrBlocks"></a>
The inside IP addresses used for core network change values.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** NetworkFunctionGroupName **   <a name="networkmanager-Type-CoreNetworkChangeValues-NetworkFunctionGroupName"></a>
The network function group name if the change event is associated with a network function group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** PeerEdgeLocations **   <a name="networkmanager-Type-CoreNetworkChangeValues-PeerEdgeLocations"></a>
The edge locations of peers in the core network change values.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\s\S]*`
Required: No

 ** RoutingPolicy **   <a name="networkmanager-Type-CoreNetworkChangeValues-RoutingPolicy"></a>
The routing policy configuration in the core network change values.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000000.
Pattern: `[\s\S]*`
Required: No

 ** RoutingPolicyAssociationDetails **   <a name="networkmanager-Type-CoreNetworkChangeValues-RoutingPolicyAssociationDetails"></a>
The names of the routing policies and other association details in the core network change values.
Type: Array of [RoutingPolicyAssociationDetail](API_RoutingPolicyAssociationDetail.md) objects
Required: No

 ** RoutingPolicyDirection **   <a name="networkmanager-Type-CoreNetworkChangeValues-RoutingPolicyDirection"></a>
The routing policy direction (inbound/outbound) in a core network change event.
Type: String
Valid Values: `inbound | outbound`
Required: No

 ** SecurityGroupReferencingSupport **   <a name="networkmanager-Type-CoreNetworkChangeValues-SecurityGroupReferencingSupport"></a>
Indicates whether security group referencing is enabled for the core network.
Type: Boolean
Required: No

 ** SegmentName **   <a name="networkmanager-Type-CoreNetworkChangeValues-SegmentName"></a>
The names of the segments in a core network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** ServiceInsertionActions **   <a name="networkmanager-Type-CoreNetworkChangeValues-ServiceInsertionActions"></a>
Describes the service insertion action.
Type: Array of [ServiceInsertionAction](API_ServiceInsertionAction.md) objects
Required: No

 ** SharedSegments **   <a name="networkmanager-Type-CoreNetworkChangeValues-SharedSegments"></a>
The shared segments for a core network change value.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** VpnEcmpSupport **   <a name="networkmanager-Type-CoreNetworkChangeValues-VpnEcmpSupport"></a>
Indicates whether Equal Cost Multipath (ECMP) is enabled for the core network.
Type: Boolean
Required: No

## See Also
<a name="API_CoreNetworkChangeValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkChangeValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkChangeValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkChangeValues)
