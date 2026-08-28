---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_NetworkRouteDestination.html
---

# NetworkRouteDestination
<a name="API_NetworkRouteDestination"></a>

Describes the destination of a network route.

## Contents
<a name="API_NetworkRouteDestination_Contents"></a>

 ** CoreNetworkAttachmentId **   <a name="networkmanager-Type-NetworkRouteDestination-CoreNetworkAttachmentId"></a>
The ID of a core network attachment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^attachment-([0-9a-f]{8,17})$`
Required: No

 ** EdgeLocation **   <a name="networkmanager-Type-NetworkRouteDestination-EdgeLocation"></a>
The edge location for the network destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\s\S]*`
Required: No

 ** NetworkFunctionGroupName **   <a name="networkmanager-Type-NetworkRouteDestination-NetworkFunctionGroupName"></a>
The network function group name associated with the destination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** ResourceId **   <a name="networkmanager-Type-NetworkRouteDestination-ResourceId"></a>
The ID of the resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** ResourceType **   <a name="networkmanager-Type-NetworkRouteDestination-ResourceType"></a>
The resource type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** SegmentName **   <a name="networkmanager-Type-NetworkRouteDestination-SegmentName"></a>
The name of the segment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** TransitGatewayAttachmentId **   <a name="networkmanager-Type-NetworkRouteDestination-TransitGatewayAttachmentId"></a>
The ID of the transit gateway attachment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_NetworkRouteDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/NetworkRouteDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/NetworkRouteDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/NetworkRouteDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
