---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_RouteTableIdentifier.html
---

# RouteTableIdentifier
<a name="API_RouteTableIdentifier"></a>

Describes a route table.

## Contents
<a name="API_RouteTableIdentifier_Contents"></a>

 ** CoreNetworkNetworkFunctionGroup **   <a name="networkmanager-Type-RouteTableIdentifier-CoreNetworkNetworkFunctionGroup"></a>
The route table identifier associated with the network function group.
Type: [CoreNetworkNetworkFunctionGroupIdentifier](API_CoreNetworkNetworkFunctionGroupIdentifier.md) object
Required: No

 ** CoreNetworkSegmentEdge **   <a name="networkmanager-Type-RouteTableIdentifier-CoreNetworkSegmentEdge"></a>
The segment edge in a core network.
Type: [CoreNetworkSegmentEdgeIdentifier](API_CoreNetworkSegmentEdgeIdentifier.md) object
Required: No

 ** TransitGatewayRouteTableArn **   <a name="networkmanager-Type-RouteTableIdentifier-TransitGatewayRouteTableArn"></a>
The ARN of the transit gateway route table for the attachment request. For example, `"TransitGatewayRouteTableArn": "arn:aws:ec2:us-west-2:123456789012:transit-gateway-route-table/tgw-rtb-9876543210123456"`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_RouteTableIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/RouteTableIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/RouteTableIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/RouteTableIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
