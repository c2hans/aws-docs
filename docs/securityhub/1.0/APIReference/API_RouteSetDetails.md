---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_RouteSetDetails.html
---

# RouteSetDetails
<a name="API_RouteSetDetails"></a>

 Provides details about the routes in the route table.

## Contents
<a name="API_RouteSetDetails_Contents"></a>

 ** CarrierGatewayId **   <a name="securityhub-Type-RouteSetDetails-CarrierGatewayId"></a>
 The ID of the carrier gateway.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CoreNetworkArn **   <a name="securityhub-Type-RouteSetDetails-CoreNetworkArn"></a>
 The Amazon Resource Name (ARN) of the core network.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DestinationCidrBlock **   <a name="securityhub-Type-RouteSetDetails-DestinationCidrBlock"></a>
 The IPv4 CIDR block used for the destination match.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DestinationIpv6CidrBlock **   <a name="securityhub-Type-RouteSetDetails-DestinationIpv6CidrBlock"></a>
 The IPv6 CIDR block used for the destination match.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DestinationPrefixListId **   <a name="securityhub-Type-RouteSetDetails-DestinationPrefixListId"></a>
 The prefix of the destination AWS service.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EgressOnlyInternetGatewayId **   <a name="securityhub-Type-RouteSetDetails-EgressOnlyInternetGatewayId"></a>
 The ID of the egress-only internet gateway.
Type: String
Pattern: `.*\S.*`
Required: No

 ** GatewayId **   <a name="securityhub-Type-RouteSetDetails-GatewayId"></a>
 The ID of a gateway attached to your VPC.
Type: String
Pattern: `.*\S.*`
Required: No

 ** InstanceId **   <a name="securityhub-Type-RouteSetDetails-InstanceId"></a>
 The ID of a NAT instance in your VPC.
Type: String
Pattern: `.*\S.*`
Required: No

 ** InstanceOwnerId **   <a name="securityhub-Type-RouteSetDetails-InstanceOwnerId"></a>
 The ID of the AWS account that owns the instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LocalGatewayId **   <a name="securityhub-Type-RouteSetDetails-LocalGatewayId"></a>
 The ID of the local gateway.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NatGatewayId **   <a name="securityhub-Type-RouteSetDetails-NatGatewayId"></a>
 The ID of a NAT gateway.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NetworkInterfaceId **   <a name="securityhub-Type-RouteSetDetails-NetworkInterfaceId"></a>
 The ID of the network interface.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Origin **   <a name="securityhub-Type-RouteSetDetails-Origin"></a>
 Describes how the route was created.
Type: String
Pattern: `.*\S.*`
Required: No

 ** State **   <a name="securityhub-Type-RouteSetDetails-State"></a>
 The state of the route.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TransitGatewayId **   <a name="securityhub-Type-RouteSetDetails-TransitGatewayId"></a>
 The ID of a transit gateway.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VpcPeeringConnectionId **   <a name="securityhub-Type-RouteSetDetails-VpcPeeringConnectionId"></a>
 The ID of a VPC peering connection.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_RouteSetDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/RouteSetDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/RouteSetDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/RouteSetDetails)
