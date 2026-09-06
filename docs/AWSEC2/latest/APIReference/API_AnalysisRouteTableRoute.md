---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AnalysisRouteTableRoute.html
---

# AnalysisRouteTableRoute
<a name="API_AnalysisRouteTableRoute"></a>

Describes a route table route.

## Contents
<a name="API_AnalysisRouteTableRoute_Contents"></a>

 ** carrierGatewayId **
The ID of a carrier gateway.
Type: String
Required: No

 ** coreNetworkArn **
The Amazon Resource Name (ARN) of a core network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** destinationCidr **
The destination IPv4 address, in CIDR notation.
Type: String
Required: No

 ** destinationPrefixListId **
The prefix of the AWS service.
Type: String
Required: No

 ** egressOnlyInternetGatewayId **
The ID of an egress-only internet gateway.
Type: String
Required: No

 ** gatewayId **
The ID of the gateway, such as an internet gateway or virtual private gateway.
Type: String
Required: No

 ** instanceId **
The ID of the instance, such as a NAT instance.
Type: String
Required: No

 ** localGatewayId **
The ID of a local gateway.
Type: String
Required: No

 ** natGatewayId **
The ID of a NAT gateway.
Type: String
Required: No

 ** networkInterfaceId **
The ID of a network interface.
Type: String
Required: No

 ** origin **
Describes how the route was created. The following are the possible values:
+ CreateRouteTable - The route was automatically created when the route table was created.
+ CreateRoute - The route was manually added to the route table.
+ EnableVgwRoutePropagation - The route was propagated by route propagation.
Type: String
Required: No

 ** state **
The state. The following are the possible values:
+ active
+ blackhole
Type: String
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
<a name="API_AnalysisRouteTableRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AnalysisRouteTableRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AnalysisRouteTableRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AnalysisRouteTableRoute)
