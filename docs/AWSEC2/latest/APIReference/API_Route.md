---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Route.html
---

# Route
<a name="API_Route"></a>

Describes a route in a route table.

## Contents
<a name="API_Route_Contents"></a>

 ** carrierGatewayId **
The ID of the carrier gateway.
Type: String
Required: No

 ** coreNetworkArn **
The Amazon Resource Name (ARN) of the core network.
Type: String
Required: No

 ** destinationCidrBlock **
The IPv4 CIDR block used for the destination match.
Type: String
Required: No

 ** destinationIpv6CidrBlock **
The IPv6 CIDR block used for the destination match.
Type: String
Required: No

 ** destinationPrefixListId **
The prefix of the AWS service.
Type: String
Required: No

 ** egressOnlyInternetGatewayId **
The ID of the egress-only internet gateway.
Type: String
Required: No

 ** gatewayId **
The ID of a gateway attached to your VPC.
Type: String
Required: No

 ** instanceId **
The ID of a NAT instance in your VPC.
Type: String
Required: No

 ** instanceOwnerId **
The ID of AWS account that owns the instance.
Type: String
Required: No

 ** ipAddress **
The next hop IP address for routes propagated by VPC Route Server into VPC route tables.
Type: String
Required: No

 ** localGatewayId **
The ID of the local gateway.
Type: String
Required: No

 ** natGatewayId **
The ID of a NAT gateway.
Type: String
Required: No

 ** networkInterfaceId **
The ID of the network interface.
Type: String
Required: No

 ** odbNetworkArn **
The Amazon Resource Name (ARN) of the ODB network.
Type: String
Required: No

 ** origin **
Describes how the route was created.
+  `CreateRouteTable` - The route was automatically created when the route table was created.
+  `CreateRoute` - The route was manually added to the route table.
+  `EnableVgwRoutePropagation` - The route was propagated by route propagation.
+  `Advertisement` - The route was created dynamically by Amazon VPC Route Server.
Type: String
Valid Values: `CreateRouteTable | CreateRoute | EnableVgwRoutePropagation`
Required: No

 ** state **
The state of the route. The `blackhole` state indicates that the route's target isn't available (for example, the specified gateway isn't attached to the VPC, or the specified NAT instance has been terminated).
Type: String
Valid Values: `active | blackhole`
Required: No

 ** transitGatewayId **
The ID of a transit gateway.
Type: String
Required: No

 ** vpcPeeringConnectionId **
The ID of a VPC peering connection.
Type: String
Required: No

## See Also
<a name="API_Route_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/Route)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/Route)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/Route)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
