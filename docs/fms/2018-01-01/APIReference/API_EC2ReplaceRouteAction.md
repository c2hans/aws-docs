---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_EC2ReplaceRouteAction.html
---

# EC2ReplaceRouteAction
<a name="API_EC2ReplaceRouteAction"></a>

Information about the ReplaceRoute action in Amazon EC2.

## Contents
<a name="API_EC2ReplaceRouteAction_Contents"></a>

 ** RouteTableId **   <a name="fms-Type-EC2ReplaceRouteAction-RouteTableId"></a>
Information about the ID of the route table.
Type: [ActionTarget](API_ActionTarget.md) object
Required: Yes

 ** Description **   <a name="fms-Type-EC2ReplaceRouteAction-Description"></a>
A description of the ReplaceRoute action in Amazon EC2.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** DestinationCidrBlock **   <a name="fms-Type-EC2ReplaceRouteAction-DestinationCidrBlock"></a>
Information about the IPv4 CIDR address block used for the destination match. The value that you provide must match the CIDR of an existing route in the table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-f0-9:./]+`
Required: No

 ** DestinationIpv6CidrBlock **   <a name="fms-Type-EC2ReplaceRouteAction-DestinationIpv6CidrBlock"></a>
Information about the IPv6 CIDR address block used for the destination match. The value that you provide must match the CIDR of an existing route in the table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-f0-9:./]+`
Required: No

 ** DestinationPrefixListId **   <a name="fms-Type-EC2ReplaceRouteAction-DestinationPrefixListId"></a>
Information about the ID of the prefix list for the route.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** GatewayId **   <a name="fms-Type-EC2ReplaceRouteAction-GatewayId"></a>
Information about the ID of an internet gateway or virtual private gateway.
Type: [ActionTarget](API_ActionTarget.md) object
Required: No

## See Also
<a name="API_EC2ReplaceRouteAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/EC2ReplaceRouteAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/EC2ReplaceRouteAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/EC2ReplaceRouteAction)
