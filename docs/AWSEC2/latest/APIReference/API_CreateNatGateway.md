---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNatGateway.html
---

# CreateNatGateway
<a name="API_CreateNatGateway"></a>

Creates a NAT gateway in the specified subnet. This action creates a network interface in the specified subnet with a private IP address from the IP address range of the subnet. You can create either a public NAT gateway or a private NAT gateway.

With a public NAT gateway, internet-bound traffic from a private subnet can be routed to the NAT gateway, so that instances in a private subnet can connect to the internet.

With a private NAT gateway, private communication is routed across VPCs and on-premises networks through a transit gateway or virtual private gateway. Common use cases include running large workloads behind a small pool of allowlisted IPv4 addresses, preserving private IPv4 addresses, and communicating between overlapping networks.

For more information, see [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the *Amazon VPC User Guide*.

**Important**
When you create a public NAT gateway and assign it an EIP or secondary EIPs, the network border group of the EIPs must match the network border group of the Availability Zone (AZ) that the public NAT gateway is in. If it's not the same, the NAT gateway will fail to launch. You can see the network border group for the subnet's AZ by viewing the details of the subnet. Similarly, you can view the network border group of an EIP by viewing the details of the EIP address. For more information about network border groups and EIPs, see [Allocate an Elastic IP address](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithEIPs.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_CreateNatGateway_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AllocationId**
[Public NAT gateways only] The allocation ID of an Elastic IP address to associate with the NAT gateway. You cannot specify an Elastic IP address with a private NAT gateway. If the Elastic IP address is associated with another resource, you must first disassociate it.
Type: String
Required: No

 **AvailabilityMode**
Specifies whether to create a zonal (single-AZ) or regional (multi-AZ) NAT gateway. Defaults to `zonal`.
A zonal NAT gateway is a NAT Gateway that provides redundancy and scalability within a single availability zone. A regional NAT gateway is a single NAT Gateway that works across multiple availability zones (AZs) in your VPC, providing redundancy, scalability and availability across all the AZs in a Region.
For more information, see [Regional NAT gateways for automatic multi-AZ expansion](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html) in the *Amazon VPC User Guide*.
Type: String
Valid Values: `zonal | regional`
Required: No

 **AvailabilityZoneAddress.N**
For regional NAT gateways only: Specifies which Availability Zones you want the NAT gateway to support and the Elastic IP addresses (EIPs) to use in each AZ. The regional NAT gateway uses these EIPs to handle outbound NAT traffic from their respective AZs. If not specified, the NAT gateway will automatically expand to new AZs and associate EIPs upon detection of an elastic network interface. If you specify this parameter, auto-expansion is disabled and you must manually manage AZ coverage.
A regional NAT gateway is a single NAT Gateway that works across multiple availability zones (AZs) in your VPC, providing redundancy, scalability and availability across all the AZs in a Region.
For more information, see [Regional NAT gateways for automatic multi-AZ expansion](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html) in the *Amazon VPC User Guide*.
Type: Array of [AvailabilityZoneAddress](API_AvailabilityZoneAddress.md) objects
Required: No

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Constraint: Maximum 64 ASCII characters.
Type: String
Required: No

 **ConnectivityType**
Indicates whether the NAT gateway supports public or private connectivity. The default is public connectivity.
Type: String
Valid Values: `private | public`
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **PrivateIpAddress**
The private IPv4 address to assign to the NAT gateway. If you don't provide an address, a private IPv4 address will be automatically assigned.
Type: String
Required: No

 **SecondaryAllocationId.N**
Secondary EIP allocation IDs. For more information, see [Create a NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-working-with.html) in the *Amazon VPC User Guide*.
Type: Array of strings
Required: No

 **SecondaryPrivateIpAddress.N**
Secondary private IPv4 addresses. For more information about secondary addresses, see [Create a NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-working-with.html) in the *Amazon VPC User Guide*.
Type: Array of strings
Required: No

 **SecondaryPrivateIpAddressCount**
[Private NAT gateway only] The number of secondary private IPv4 addresses you want to assign to the NAT gateway. For more information about secondary addresses, see [Create a NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-working-with.html) in the *Amazon VPC User Guide*.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 31.
Required: No

 **SubnetId**
The ID of the subnet in which to create the NAT gateway.
Type: String
Required: No

 **TagSpecification.N**
The tags to assign to the NAT gateway.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **VpcId**
The ID of the VPC where you want to create a regional NAT gateway.
Type: String
Required: No

## Response Elements
<a name="API_CreateNatGateway_ResponseElements"></a>

The following elements are returned by the service.

 **clientToken**
Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.
Type: String

 **natGateway**
Information about the NAT gateway.
Type: [NatGateway](API_NatGateway.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateNatGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateNatGateway_Examples"></a>

### Example 1
<a name="API_CreateNatGateway_Example_1"></a>

This example creates a public NAT gateway in the specified subnet and associates the Elastic IP address with the specified allocation ID to the NAT gateway.

#### Sample Request
<a name="API_CreateNatGateway_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateNatGateway
&SubnetId=subnet-1234567890abcdef0
&AllocationId=eipalloc-0abcdef1234567890
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateNatGateway_Example_1_Response"></a>

```
<CreateNatGatewayResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>1b74dc5c-bcda-403f-867d-example</requestId>
    <natGateway>
        <subnetId>subnet-1234567890abcdef0</subnetId>
        <natGatewayAddressSet>
            <item>
                <allocationId>eipalloc-0abcdef1234567890</allocationId>
                <networkInterfaceId>eni-0123abc456def7890</networkInterfaceId>
                <privateIp>10.0.0.191</privateIp>
                <publicIp>203.0.113.5</publicIp>
            </item>
        </natGatewayAddressSet>
        <createTime>2019-11-25T14:00:55.416Z</createTime>
        <vpcId>vpc-0598c7d356eba48d7</vpcId>
        <natGatewayId>nat-04e77a5e9c34432f9</natGatewayId>
        <connectivityType>public</connectivityType>
        <state>pending</state>
    </natGateway>
</CreateNatGatewayResponse>
```

### Example 2
<a name="API_CreateNatGateway_Example_2"></a>

This example creates a private NAT gateway in the specified subnet.

#### Sample Request
<a name="API_CreateNatGateway_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateNatGateway
&SubnetId=subnet-1234567890abcdef0
&ConnectivityType=private
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateNatGateway_Example_2_Response"></a>

```
<CreateNatGatewayResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>1b74dc5c-bcda-403f-867d-example</requestId>
    <natGateway>
        <subnetId>subnet-1234567890abcdef0</subnetId>
        <natGatewayAddressSet>
            <item>
                <networkInterfaceId>eni-1a2b3c4d5e6f78901</networkInterfaceId>
                <privateIp>10.0.1.26</privateIp>
            </item>
        </natGatewayAddressSet>
        <createTime>2021-06-05T14:00:55.416Z</createTime>
        <vpcId>vpc-0598c7d356eba48d7</vpcId>
        <natGatewayId>nat-04e77a5e9c34432f9</natGatewayId>
        <connectivityType>private</connectivityType>
        <state>pending</state>
    </natGateway>
</CreateNatGatewayResponse>
```

## See Also
<a name="API_CreateNatGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateNatGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateNatGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateNatGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateNatGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateNatGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateNatGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateNatGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateNatGateway)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateNatGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateNatGateway)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
