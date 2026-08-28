---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_NatGateway.html
---

# NatGateway
<a name="API_NatGateway"></a>

Describes a NAT gateway.

## Contents
<a name="API_NatGateway_Contents"></a>

 ** AttachedApplianceSet.N **
The proxy appliances attached to the NAT Gateway for filtering and inspecting traffic to prevent data exfiltration.
Type: Array of [NatGatewayAttachedAppliance](API_NatGatewayAttachedAppliance.md) objects
Required: No

 ** autoProvisionZones **
For regional NAT gateways only: Indicates whether AWS automatically manages AZ coverage. When enabled, the NAT gateway associates EIPs in all AZs where your VPC has subnets to handle outbound NAT traffic, expands to new AZs when you create subnets there, and retracts from AZs where you've removed all subnets. When disabled, you must manually manage which AZs the NAT gateway supports and their corresponding EIPs.
A regional NAT gateway is a single NAT Gateway that works across multiple availability zones (AZs) in your VPC, providing redundancy, scalability and availability across all the AZs in a Region.
For more information, see [Regional NAT gateways for automatic multi-AZ expansion](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html) in the *Amazon VPC User Guide*.
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** autoScalingIps **
For regional NAT gateways only: Indicates whether AWS automatically allocates additional Elastic IP addresses (EIPs) in an AZ when the NAT gateway needs more ports due to increased concurrent connections to a single destination from that AZ.
For more information, see [Regional NAT gateways for automatic multi-AZ expansion](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html) in the *Amazon VPC User Guide*.
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** availabilityMode **
Indicates whether this is a zonal (single-AZ) or regional (multi-AZ) NAT gateway.
A zonal NAT gateway is a NAT Gateway that provides redundancy and scalability within a single availability zone. A regional NAT gateway is a single NAT Gateway that works across multiple availability zones (AZs) in your VPC, providing redundancy, scalability and availability across all the AZs in a Region.
For more information, see [Regional NAT gateways for automatic multi-AZ expansion](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html) in the *Amazon VPC User Guide*.
Type: String
Valid Values: `zonal | regional`
Required: No

 ** connectivityType **
Indicates whether the NAT gateway supports public or private connectivity.
Type: String
Valid Values: `private | public`
Required: No

 ** createTime **
The date and time the NAT gateway was created.
Type: Timestamp
Required: No

 ** deleteTime **
The date and time the NAT gateway was deleted, if applicable.
Type: Timestamp
Required: No

 ** failureCode **
If the NAT gateway could not be created, specifies the error code for the failure. (`InsufficientFreeAddressesInSubnet` \| `Gateway.NotAttached` \| `InvalidAllocationID.NotFound` \| `Resource.AlreadyAssociated` \| `InternalError` \| `InvalidSubnetID.NotFound`)
Type: String
Required: No

 ** failureMessage **
If the NAT gateway could not be created, specifies the error message for the failure, that corresponds to the error code.
+ For InsufficientFreeAddressesInSubnet: "Subnet has insufficient free addresses to create this NAT gateway"
+ For Gateway.NotAttached: "Network vpc-xxxxxxxx has no Internet gateway attached"
+ For InvalidAllocationID.NotFound: "Elastic IP address eipalloc-xxxxxxxx could not be associated with this NAT gateway"
+ For Resource.AlreadyAssociated: "Elastic IP address eipalloc-xxxxxxxx is already associated"
+ For InternalError: "Network interface eni-xxxxxxxx, created and used internally by this NAT gateway is in an invalid state. Please try again."
+ For InvalidSubnetID.NotFound: "The specified subnet subnet-xxxxxxxx does not exist or could not be found."
Type: String
Required: No

 ** NatGatewayAddressSet.N **
Information about the IP addresses and network interface associated with the NAT gateway.
Type: Array of [NatGatewayAddress](API_NatGatewayAddress.md) objects
Required: No

 ** natGatewayId **
The ID of the NAT gateway.
Type: String
Required: No

 ** provisionedBandwidth **
Reserved. If you need to sustain traffic greater than the [documented limits](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html#vpc-limits-gateways), contact AWS Support.
Type: [ProvisionedBandwidth](API_ProvisionedBandwidth.md) object
Required: No

 ** routeTableId **
For regional NAT gateways only, this is the ID of the NAT gateway.
Type: String
Required: No

 ** state **
The state of the NAT gateway.
+  `pending`: The NAT gateway is being created and is not ready to process traffic.
+  `failed`: The NAT gateway could not be created. Check the `failureCode` and `failureMessage` fields for the reason.
+  `available`: The NAT gateway is able to process traffic. This status remains until you delete the NAT gateway, and does not indicate the health of the NAT gateway.
+  `deleting`: The NAT gateway is in the process of being terminated and may still be processing traffic.
+  `deleted`: The NAT gateway has been terminated and is no longer processing traffic.
Type: String
Valid Values: `pending | failed | available | deleting | deleted`
Required: No

 ** subnetId **
The ID of the subnet in which the NAT gateway is located.
Type: String
Required: No

 ** TagSet.N **
The tags for the NAT gateway.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** vpcId **
The ID of the VPC in which the NAT gateway is located.
Type: String
Required: No

## See Also
<a name="API_NatGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/NatGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/NatGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/NatGateway)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
