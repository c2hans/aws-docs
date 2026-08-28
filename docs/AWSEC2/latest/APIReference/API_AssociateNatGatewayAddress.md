---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateNatGatewayAddress.html
---

# AssociateNatGatewayAddress
<a name="API_AssociateNatGatewayAddress"></a>

Associates Elastic IP addresses (EIPs) and private IPv4 addresses with a public NAT gateway. For more information, see [Work with NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-working-with.html) in the *Amazon VPC User Guide*.

By default, you can associate up to 2 Elastic IP addresses per public NAT gateway. You can increase the limit by requesting a quota adjustment. For more information, see [Elastic IP address quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html#vpc-limits-eips) in the *Amazon VPC User Guide*.

**Important**
When you associate an EIP or secondary EIPs with a public NAT gateway, the network border group of the EIPs must match the network border group of the Availability Zone (AZ) that the public NAT gateway is in. If it's not the same, the EIP will fail to associate. You can see the network border group for the subnet's AZ by viewing the details of the subnet. Similarly, you can view the network border group of an EIP by viewing the details of the EIP address. For more information about network border groups and EIPs, see [Allocate an Elastic IP address](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithEIPs.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_AssociateNatGatewayAddress_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AllocationId.N**
The allocation IDs of EIPs that you want to associate with your NAT gateway.
Type: Array of strings
Required: Yes

 **AvailabilityZone**
For regional NAT gateways only: The Availability Zone where you want to associate an Elastic IP address (EIP). The regional NAT gateway uses a separate EIP in each AZ to handle outbound NAT traffic from that AZ.
A regional NAT gateway is a single NAT Gateway that works across multiple availability zones (AZs) in your VPC, providing redundancy, scalability and availability across all the AZs in a Region.
Type: String
Required: No

 **AvailabilityZoneId**
For regional NAT gateways only: The ID of the Availability Zone where you want to associate an Elastic IP address (EIP). The regional NAT gateway uses a separate EIP in each AZ to handle outbound NAT traffic from that AZ. Use this instead of AvailabilityZone for consistent identification of AZs across AWS Regions.
A regional NAT gateway is a single NAT Gateway that works across multiple availability zones (AZs) in your VPC, providing redundancy, scalability and availability across all the AZs in a Region.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **NatGatewayId**
The ID of the NAT gateway.
Type: String
Required: Yes

 **PrivateIpAddress.N**
The private IPv4 addresses that you want to assign to the NAT gateway.
Type: Array of strings
Required: No

## Response Elements
<a name="API_AssociateNatGatewayAddress_ResponseElements"></a>

The following elements are returned by the service.

 **natGatewayAddressSet**
The IP addresses.
Type: Array of [NatGatewayAddress](API_NatGatewayAddress.md) objects

 **natGatewayId**
The ID of the NAT gateway.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_AssociateNatGatewayAddress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_AssociateNatGatewayAddress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AssociateNatGatewayAddress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AssociateNatGatewayAddress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AssociateNatGatewayAddress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AssociateNatGatewayAddress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AssociateNatGatewayAddress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AssociateNatGatewayAddress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AssociateNatGatewayAddress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AssociateNatGatewayAddress)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AssociateNatGatewayAddress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AssociateNatGatewayAddress)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
