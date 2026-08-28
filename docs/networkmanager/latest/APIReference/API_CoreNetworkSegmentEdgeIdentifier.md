---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CoreNetworkSegmentEdgeIdentifier.html
---

# CoreNetworkSegmentEdgeIdentifier
<a name="API_CoreNetworkSegmentEdgeIdentifier"></a>

Returns details about a core network edge.

## Contents
<a name="API_CoreNetworkSegmentEdgeIdentifier_Contents"></a>

 ** CoreNetworkId **   <a name="networkmanager-Type-CoreNetworkSegmentEdgeIdentifier-CoreNetworkId"></a>
The ID of a core network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: No

 ** EdgeLocation **   <a name="networkmanager-Type-CoreNetworkSegmentEdgeIdentifier-EdgeLocation"></a>
The Region where the segment edge is located.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\s\S]*`
Required: No

 ** SegmentName **   <a name="networkmanager-Type-CoreNetworkSegmentEdgeIdentifier-SegmentName"></a>
The name of the segment edge.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_CoreNetworkSegmentEdgeIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkSegmentEdgeIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkSegmentEdgeIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkSegmentEdgeIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
