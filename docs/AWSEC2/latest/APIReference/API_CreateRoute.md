---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateRoute.html
---

# CreateRoute
<a name="API_CreateRoute"></a>

Creates a route in a route table within a VPC.

You must specify either a destination CIDR block or a prefix list ID. You must also specify exactly one of the resources from the parameter list.

When determining how to route traffic, we use the route with the most specific match. For example, traffic is destined for the IPv4 address `192.0.2.3`, and the route table includes the following two IPv4 routes:
+  `192.0.2.0/24` (goes to some target A)
+  `192.0.2.0/28` (goes to some target B)

Both routes apply to the traffic destined for `192.0.2.3`. However, the second route in the list covers a smaller number of IP addresses and is therefore more specific, so we use that route to determine where to target the traffic.

For more information about route tables, see [Route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_CreateRoute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CarrierGatewayId**
The ID of the carrier gateway.
You can only use this option when the VPC contains a subnet which is associated with a Wavelength Zone.
Type: String
Required: No

 **CoreNetworkArn**
The Amazon Resource Name (ARN) of the core network.
Type: String
Required: No

 **DestinationCidrBlock**
The IPv4 CIDR address block used for the destination match. Routing decisions are based on the most specific match. We modify the specified CIDR block to its canonical form; for example, if you specify `100.68.0.18/18`, we modify it to `100.68.0.0/18`.
Type: String
Required: No

 **DestinationIpv6CidrBlock**
The IPv6 CIDR block used for the destination match. Routing decisions are based on the most specific match.
Type: String
Required: No

 **DestinationPrefixListId**
The ID of a prefix list used for the destination match.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **EgressOnlyInternetGatewayId**
[IPv6 traffic only] The ID of an egress-only internet gateway.
Type: String
Required: No

 **GatewayId**
The ID of an internet gateway or virtual private gateway attached to your VPC.
Type: String
Required: No

 **InstanceId**
The ID of a NAT instance in your VPC. The operation fails if you specify an instance ID unless exactly one network interface is attached.
Type: String
Required: No

 **LocalGatewayId**
The ID of the local gateway.
Type: String
Required: No

 **NatGatewayId**
[IPv4 traffic only] The ID of a NAT gateway.
Type: String
Required: No

 **NetworkInterfaceId**
The ID of a network interface.
Type: String
Required: No

 **OdbNetworkArn**
The Amazon Resource Name (ARN) of the ODB network.
Type: String
Required: No

 **RouteTableId**
The ID of the route table for the route.
Type: String
Required: Yes

 **TransitGatewayId**
The ID of a transit gateway.
Type: String
Required: No

 **VpcEndpointId**
The ID of a VPC endpoint. Supported for Gateway Load Balancer endpoints only.
Type: String
Required: No

 **VpcPeeringConnectionId**
The ID of a VPC peering connection.
Type: String
Required: No

## Response Elements
<a name="API_CreateRoute_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, it returns an error.
Type: Boolean

## Errors
<a name="API_CreateRoute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateRoute_Examples"></a>

### Example 1
<a name="API_CreateRoute_Example_1"></a>

This example creates a route in the route table with the ID `rtb-1122334455667788a`. The route matches all IPv4 traffic (`0.0.0.0/0`) and routes it to the internet gateway with the ID `igw-eaad4883`.

#### Sample Request
<a name="API_CreateRoute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateRoute
&RouteTableId=rtb-1122334455667788a
&DestinationCidrBlock=0.0.0.0/0
&GatewayId=igw-eaad4883
&AUTHPARAMS
```

### Example 2
<a name="API_CreateRoute_Example_2"></a>

This example creates a route in the route table with the ID `rtb-1122334455667788a`. The route sends all IPv4 traffic (`0.0.0.0/0`) to the NAT instance with the ID `i-1234567890abcdef0`.

#### Sample Request
<a name="API_CreateRoute_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateRoute
&RouteTableId=rtb-1122334455667788a
&DestinationCidrBlock=0.0.0.0/0
&InstanceId=i-1234567890abcdef0
&AUTHPARAMS
```

### Example 3
<a name="API_CreateRoute_Example_3"></a>

This example creates a route in route table `rtb-1122334455667788a`. The route matches traffic for the IPv4 CIDR block `10.0.0.0/16` and routes it to VPC peering connection, `pcx-111aaa22`. This route enables IPv4 traffic to be directed to the other peered VPC in the VPC peering connection.

#### Sample Request
<a name="API_CreateRoute_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateRoute
&RouteTableId=rtb-1122334455667788a&DestinationCidrBlock=10.0.0.0/16
&vpcPeeringConnectionId=pcx-111aaa22
&AUTHPARAMS
```

### Example 4
<a name="API_CreateRoute_Example_4"></a>

This example creates a route in route table `rtb-1122334455667788a`. The route sends all IPv6 traffic `::/0` to an egress-only internet gateway.

#### Sample Request
<a name="API_CreateRoute_Example_4_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateRoute
&RouteTableId=rtb-1122334455667788a
&DestinationIpv6CidrBlock=::/0
&EgressOnlyInternetGatewayId=eigw-1234567890abc1234
&AUTHPARAMS
```

## See Also
<a name="API_CreateRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateRoute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateRoute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateRoute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateRoute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateRoute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateRoute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateRoute)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateRoute)
