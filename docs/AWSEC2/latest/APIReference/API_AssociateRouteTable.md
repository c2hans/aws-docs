---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateRouteTable.html
---

# AssociateRouteTable
<a name="API_AssociateRouteTable"></a>

Associates a subnet in your VPC or an internet gateway or virtual private gateway attached to your VPC with a route table in your VPC. This association causes traffic from the subnet or gateway to be routed according to the routes in the route table. The action returns an association ID, which you need in order to disassociate the route table later. A route table can be associated with multiple subnets.

For more information, see [Route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_AssociateRouteTable_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **GatewayId**
The ID of the internet gateway or virtual private gateway.
Type: String
Required: No

 **PublicIpv4Pool**
The ID of a public IPv4 pool. A public IPv4 pool is a pool of IPv4 addresses that you've brought to AWS with BYOIP.
Type: String
Required: No

 **RouteTableId**
The ID of the route table.
Type: String
Required: Yes

 **SubnetId**
The ID of the subnet.
Type: String
Required: No

## Response Elements
<a name="API_AssociateRouteTable_ResponseElements"></a>

The following elements are returned by the service.

 **associationId**
The route table association ID. This ID is required for disassociating the route table.
Type: String

 **associationState**
The state of the association.
Type: [RouteTableAssociationState](API_RouteTableAssociationState.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_AssociateRouteTable_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_AssociateRouteTable_Examples"></a>

### Example 1
<a name="API_AssociateRouteTable_Example_1"></a>

This example associates a route table with the ID `rtb-11223344556677889` with a subnet with the ID `subnet-12345678901234567`.

#### Sample Request
<a name="API_AssociateRouteTable_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=AssociateRouteTable
&RouteTableId=rtb-11223344556677889
&SubnetId=subnet-12345678901234567
```

#### Sample Response
<a name="API_AssociateRouteTable_Example_1_Response"></a>

```
<AssociateRouteTableResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <associationId>rtbassoc-04ca27a6914a0b4f</associationId>
</AssociateRouteTableResponse>
```

### Example 2
<a name="API_AssociateRouteTable_Example_2"></a>

This example associates a route table with the ID `rtb-11223344556677889` with an internet gateway with the ID `igw-1a2b3c4d1a2b3c4d1`.

#### Sample Request
<a name="API_AssociateRouteTable_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=AssociateRouteTable
&RouteTableId=rtb-11223344556677889
&GatewayId=igw-1a2b3c4d1a2b3c4d1
```

## See Also
<a name="API_AssociateRouteTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AssociateRouteTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AssociateRouteTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AssociateRouteTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AssociateRouteTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AssociateRouteTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AssociateRouteTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AssociateRouteTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AssociateRouteTable)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AssociateRouteTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AssociateRouteTable)
