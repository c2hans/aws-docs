---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_EC2CreateRouteAction.html
---

# EC2CreateRouteAction
<a name="API_EC2CreateRouteAction"></a>

Information about the CreateRoute action in Amazon EC2.

## Contents
<a name="API_EC2CreateRouteAction_Contents"></a>

 ** RouteTableId **   <a name="fms-Type-EC2CreateRouteAction-RouteTableId"></a>
Information about the ID of the route table for the route.
Type: [ActionTarget](API_ActionTarget.md) object
Required: Yes

 ** Description **   <a name="fms-Type-EC2CreateRouteAction-Description"></a>
A description of CreateRoute action in Amazon EC2.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** DestinationCidrBlock **   <a name="fms-Type-EC2CreateRouteAction-DestinationCidrBlock"></a>
Information about the IPv4 CIDR address block used for the destination match.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-f0-9:./]+`
Required: No

 ** DestinationIpv6CidrBlock **   <a name="fms-Type-EC2CreateRouteAction-DestinationIpv6CidrBlock"></a>
Information about the IPv6 CIDR block destination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-f0-9:./]+`
Required: No

 ** DestinationPrefixListId **   <a name="fms-Type-EC2CreateRouteAction-DestinationPrefixListId"></a>
Information about the ID of a prefix list used for the destination match.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** GatewayId **   <a name="fms-Type-EC2CreateRouteAction-GatewayId"></a>
Information about the ID of an internet gateway or virtual private gateway attached to your VPC.
Type: [ActionTarget](API_ActionTarget.md) object
Required: No

 ** VpcEndpointId **   <a name="fms-Type-EC2CreateRouteAction-VpcEndpointId"></a>
Information about the ID of a VPC endpoint. Supported for Gateway Load Balancer endpoints only.
Type: [ActionTarget](API_ActionTarget.md) object
Required: No

## See Also
<a name="API_EC2CreateRouteAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/EC2CreateRouteAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/EC2CreateRouteAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/EC2CreateRouteAction)
