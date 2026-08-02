---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpoint.html
---

# ModifyVpcEndpoint
<a name="API_ModifyVpcEndpoint"></a>

Modifies attributes of a specified VPC endpoint. The attributes that you can modify depend on the type of VPC endpoint (interface, gateway, or Gateway Load Balancer). For more information, see the [AWS PrivateLink Guide](https://docs.aws.amazon.com/vpc/latest/privatelink/).

## Request Parameters
<a name="API_ModifyVpcEndpoint_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AddRouteTableId.N**
(Gateway endpoint) The IDs of the route tables to associate with the endpoint.
Type: Array of strings
Required: No

 **AddSecurityGroupId.N**
(Interface endpoint) The IDs of the security groups to associate with the endpoint network interfaces.
Type: Array of strings
Required: No

 **AddSubnetId.N**
(Interface and Gateway Load Balancer endpoints) The IDs of the subnets in which to serve the endpoint. For a Gateway Load Balancer endpoint, you can specify only one subnet.
Type: Array of strings
Required: No

 **DnsOptions**
The DNS options for the endpoint.
Type: [DnsOptionsSpecification](API_DnsOptionsSpecification.md) object
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **IpAddressType**
The IP address type for the endpoint.
Type: String
Valid Values: `ipv4 | dualstack | ipv6`
Required: No

 **PolicyDocument**
(Interface and gateway endpoints) A policy to attach to the endpoint that controls access to the service. The policy must be in valid JSON format.
Type: String
Required: No

 **PrivateDnsEnabled**
(Interface endpoint) Indicates whether a private hosted zone is associated with the VPC.
Type: Boolean
Required: No

 **RemoveRouteTableId.N**
(Gateway endpoint) The IDs of the route tables to disassociate from the endpoint.
Type: Array of strings
Required: No

 **RemoveSecurityGroupId.N**
(Interface endpoint) The IDs of the security groups to disassociate from the endpoint network interfaces.
Type: Array of strings
Required: No

 **RemoveSubnetId.N**
(Interface endpoint) The IDs of the subnets from which to remove the endpoint.
Type: Array of strings
Required: No

 **ResetPolicy**
(Gateway endpoint) Specify `true` to reset the policy document to the default policy. The default policy allows full access to the service.
Type: Boolean
Required: No

 **SubnetConfiguration.N**
The subnet configurations for the endpoint.
Type: Array of [SubnetConfiguration](API_SubnetConfiguration.md) objects
Required: No

 **VpcEndpointId**
The ID of the endpoint.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyVpcEndpoint_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, it returns an error.
Type: Boolean

## Errors
<a name="API_ModifyVpcEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyVpcEndpoint_Examples"></a>

### Example 1
<a name="API_ModifyVpcEndpoint_Example_1"></a>

This example modifies gateway endpoint `vpce-1a2b3c4d` by associating route table `rtb-aaa222bb` with the endpoint, and resetting the policy document.

#### Sample Request
<a name="API_ModifyVpcEndpoint_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyVpcEndpoint
&VpcEndpointId=vpce-1a2b3c4d
&ResetPolicy=true
&AddRouteTableId.1=rtb-aaa222bb
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyVpcEndpoint_Example_1_Response"></a>

```
<ModifyVpcEndpointResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <return>true</return>
    <requestId>125acea6-ba5c-4c6e-8e17-example</requestId>
</ModifyVpcEndpointResponse>
```

### Example 2
<a name="API_ModifyVpcEndpoint_Example_2"></a>

This example modifies interface endpoint `vpce-0fe5b17a0707d6fa5` by adding subnet `subnet-d6fcaa8d` to the endpoint.

#### Sample Request
<a name="API_ModifyVpcEndpoint_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyVpcEndpoint
&VpcEndpointId=vpce-0fe5b17a0707d6fa5
&AddSubnetId.1=subnet-d6fcaa8db
&AUTHPARAMS
```

## See Also
<a name="API_ModifyVpcEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyVpcEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyVpcEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyVpcEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyVpcEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyVpcEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyVpcEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyVpcEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyVpcEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyVpcEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyVpcEndpoint)
