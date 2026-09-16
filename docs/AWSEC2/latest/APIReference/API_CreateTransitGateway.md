---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGateway.html
---

# CreateTransitGateway
<a name="API_CreateTransitGateway"></a>

Creates a transit gateway.

You can use a transit gateway to interconnect your virtual private clouds (VPC) and on-premises networks. After the transit gateway enters the `available` state, you can attach your VPCs and VPN connections to the transit gateway.

To attach your VPCs, use [CreateTransitGatewayVpcAttachment](API_CreateTransitGatewayVpcAttachment.md).

To attach a VPN connection, use [CreateCustomerGateway](API_CreateCustomerGateway.md) to create a customer gateway and specify the ID of the customer gateway and the ID of the transit gateway in a call to [CreateVpnConnection](API_CreateVpnConnection.md).

When you create a transit gateway, we create a default transit gateway route table and use it as the default association route table and the default propagation route table. You can use [CreateTransitGatewayRouteTable](API_CreateTransitGatewayRouteTable.md) to create additional transit gateway route tables. If you disable automatic route propagation, we do not create a default transit gateway route table. You can use [EnableTransitGatewayRouteTablePropagation](API_EnableTransitGatewayRouteTablePropagation.md) to propagate routes from a resource attachment to a transit gateway route table. If you disable automatic associations, you can use [AssociateTransitGatewayRouteTable](API_AssociateTransitGatewayRouteTable.md) to associate a resource attachment with a transit gateway route table.

## Request Parameters
<a name="API_CreateTransitGateway_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Description**
A description of the transit gateway.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Options**
The transit gateway options.
Type: [TransitGatewayRequestOptions](API_TransitGatewayRequestOptions.md) object
Required: No

 **TagSpecification.N**
The tags to apply to the transit gateway.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateTransitGateway_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **transitGateway**
Information about the transit gateway.
Type: [TransitGateway](API_TransitGateway.md) object

## Errors
<a name="API_CreateTransitGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateTransitGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateTransitGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateTransitGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateTransitGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateTransitGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateTransitGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateTransitGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateTransitGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateTransitGateway)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateTransitGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateTransitGateway)
