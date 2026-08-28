---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CoreNetworkChangeEventValues.html
---

# CoreNetworkChangeEventValues
<a name="API_CoreNetworkChangeEventValues"></a>

Describes a core network change event.

## Contents
<a name="API_CoreNetworkChangeEventValues_Contents"></a>

 ** AttachmentId **   <a name="networkmanager-Type-CoreNetworkChangeEventValues-AttachmentId"></a>
The ID of the attachment if the change event is associated with an attachment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^attachment-([0-9a-f]{8,17})$`
Required: No

 ** Cidr **   <a name="networkmanager-Type-CoreNetworkChangeEventValues-Cidr"></a>
For a `STATIC_ROUTE` event, this is the IP address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** EdgeLocation **   <a name="networkmanager-Type-CoreNetworkChangeEventValues-EdgeLocation"></a>
The edge location for the core network change event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\s\S]*`
Required: No

 ** NetworkFunctionGroupName **   <a name="networkmanager-Type-CoreNetworkChangeEventValues-NetworkFunctionGroupName"></a>
The changed network function group name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** PeerEdgeLocation **   <a name="networkmanager-Type-CoreNetworkChangeEventValues-PeerEdgeLocation"></a>
The edge location of the peer in a core network change event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\s\S]*`
Required: No

 ** RoutingPolicyAssociationDetails **   <a name="networkmanager-Type-CoreNetworkChangeEventValues-RoutingPolicyAssociationDetails"></a>
The names of the routing policies and other association details in the core network change values.
Type: Array of [RoutingPolicyAssociationDetail](API_RoutingPolicyAssociationDetail.md) objects
Required: No

 ** RoutingPolicyDirection **   <a name="networkmanager-Type-CoreNetworkChangeEventValues-RoutingPolicyDirection"></a>
The routing policy direction (inbound/outbound) in a core network change event.
Type: String
Valid Values: `inbound | outbound`
Required: No

 ** SegmentName **   <a name="networkmanager-Type-CoreNetworkChangeEventValues-SegmentName"></a>
The segment name if the change event is associated with a segment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_CoreNetworkChangeEventValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkChangeEventValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkChangeEventValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkChangeEventValues)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
