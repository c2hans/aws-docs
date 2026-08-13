---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Subnet.html
---

# Subnet
<a name="API_Subnet"></a>

Describes a subnet.

## Contents
<a name="API_Subnet_Contents"></a>

 ** assignIpv6AddressOnCreation **
Indicates whether a network interface created in this subnet (including a network interface created by [RunInstances](API_RunInstances.md)) receives an IPv6 address.
Type: Boolean
Required: No

 ** availabilityZone **
The Availability Zone of the subnet.
Type: String
Required: No

 ** availabilityZoneId **
The AZ ID of the subnet.
Type: String
Required: No

 ** availableIpAddressCount **
The number of unused private IPv4 addresses in the subnet. The IPv4 addresses for any stopped instances are considered unavailable.
Type: Integer
Required: No

 ** blockPublicAccessStates **
The state of VPC Block Public Access (BPA).
Type: [BlockPublicAccessStates](API_BlockPublicAccessStates.md) object
Required: No

 ** cidrBlock **
The IPv4 CIDR block assigned to the subnet.
Type: String
Required: No

 ** customerOwnedIpv4Pool **
The customer-owned IPv4 address pool associated with the subnet.
Type: String
Required: No

 ** defaultForAz **
Indicates whether this is the default subnet for the Availability Zone.
Type: Boolean
Required: No

 ** enableDns64 **
Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations.
Type: Boolean
Required: No

 ** enableLniAtDeviceIndex **
 Indicates the device position for local network interfaces in this subnet. For example, `1` indicates local network interfaces in this subnet are the secondary network interface (eth1).
Type: Integer
Required: No

 ** Ipv6CidrBlockAssociationSet.N **
Information about the IPv6 CIDR blocks associated with the subnet.
Type: Array of [SubnetIpv6CidrBlockAssociation](API_SubnetIpv6CidrBlockAssociation.md) objects
Required: No

 ** ipv6Native **
Indicates whether this is an IPv6 only subnet.
Type: Boolean
Required: No

 ** mapCustomerOwnedIpOnLaunch **
Indicates whether a network interface created in this subnet (including a network interface created by [RunInstances](API_RunInstances.md)) receives a customer-owned IPv4 address.
Type: Boolean
Required: No

 ** mapPublicIpOnLaunch **
Indicates whether instances launched in this subnet receive a public IPv4 address.
 AWS charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the *Public IPv4 Address* tab on the [Amazon VPC pricing page](http://aws.amazon.com/vpc/pricing/).
Type: Boolean
Required: No

 ** outpostArn **
The Amazon Resource Name (ARN) of the Outpost.
Type: String
Required: No

 ** ownerId **
The ID of the AWS account that owns the subnet.
Type: String
Required: No

 ** privateDnsNameOptionsOnLaunch **
The type of hostnames to assign to instances in the subnet at launch. An instance hostname is based on the IPv4 address or ID of the instance.
Type: [PrivateDnsNameOptionsOnLaunch](API_PrivateDnsNameOptionsOnLaunch.md) object
Required: No

 ** state **
The current state of the subnet.
+  `failed`: The underlying infrastructure to support the subnet failed to provision as expected.
+  `failed-insufficient-capacity`: The underlying infrastructure to support the subnet failed to provision due to a shortage of EC2 instance capacity.
Type: String
Valid Values: `pending | available | unavailable | failed | failed-insufficient-capacity`
Required: No

 ** subnetArn **
The Amazon Resource Name (ARN) of the subnet.
Type: String
Required: No

 ** subnetId **
The ID of the subnet.
Type: String
Required: No

 ** TagSet.N **
Any tags assigned to the subnet.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** type **
Indicates if this is a subnet used with Amazon Elastic VMware Service (EVS). Possible values are `Elastic VMware Service` or no value. For more information about Amazon EVS, see [*Amazon Elastic VMware Service API Reference*](https://docs.aws.amazon.com/evs/latest/APIReference/Welcome.html).
Type: String
Required: No

 ** vpcId **
The ID of the VPC the subnet is in.
Type: String
Required: No

## See Also
<a name="API_Subnet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/Subnet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/Subnet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/Subnet)
