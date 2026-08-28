---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_NetworkInterface.html
---

# NetworkInterface
<a name="API_NetworkInterface"></a>

Describes a network interface.

## Contents
<a name="API_NetworkInterface_Contents"></a>

 ** AssociatedSubnetSet.N **
The subnets associated with this network interface.
Type: Array of strings
Required: No

 ** association **
The association information for an Elastic IP address (IPv4) associated with the network interface.
Type: [NetworkInterfaceAssociation](API_NetworkInterfaceAssociation.md) object
Required: No

 ** attachment **
The network interface attachment.
Type: [NetworkInterfaceAttachment](API_NetworkInterfaceAttachment.md) object
Required: No

 ** availabilityZone **
The Availability Zone.
Type: String
Required: No

 ** availabilityZoneId **
The ID of the Availability Zone.
Type: String
Required: No

 ** connectionTrackingConfiguration **
A security group connection tracking configuration that enables you to set the timeout for connection tracking on an Elastic network interface. For more information, see [Connection tracking timeouts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts) in the *Amazon EC2 User Guide*.
Type: [ConnectionTrackingConfiguration](API_ConnectionTrackingConfiguration.md) object
Required: No

 ** denyAllIgwTraffic **
Indicates whether a network interface with an IPv6 address is unreachable from the public internet. If the value is `true`, inbound traffic from the internet is dropped and you cannot assign an elastic IP address to the network interface. The network interface is reachable from peered VPCs and resources connected through a transit gateway, including on-premises networks.
Type: Boolean
Required: No

 ** description **
A description.
Type: String
Required: No

 ** GroupSet.N **
Any security groups for the network interface.
Type: Array of [GroupIdentifier](API_GroupIdentifier.md) objects
Required: No

 ** interfaceType **
The type of network interface.
Type: String
Valid Values: `api_gateway_managed | aws_codestar_connections_managed | branch | ec2_instance_connect_endpoint | efa | efa-only | efs | evs | gateway_load_balancer | gateway_load_balancer_endpoint | global_accelerator_managed | interface | iot_rules_managed | lambda | load_balancer | nat_gateway | network_load_balancer | quicksight | transit_gateway | trunk | vpc_endpoint`
Required: No

 ** Ipv4PrefixSet.N **
The IPv4 prefixes that are assigned to the network interface.
Type: Array of [Ipv4PrefixSpecification](API_Ipv4PrefixSpecification.md) objects
Required: No

 ** ipv6Address **
The IPv6 globally unique address associated with the network interface.
Type: String
Required: No

 ** Ipv6AddressesSet.N **
The IPv6 addresses associated with the network interface.
Type: Array of [NetworkInterfaceIpv6Address](API_NetworkInterfaceIpv6Address.md) objects
Required: No

 ** ipv6Native **
Indicates whether this is an IPv6 only network interface.
Type: Boolean
Required: No

 ** Ipv6PrefixSet.N **
The IPv6 prefixes that are assigned to the network interface.
Type: Array of [Ipv6PrefixSpecification](API_Ipv6PrefixSpecification.md) objects
Required: No

 ** macAddress **
The MAC address.
Type: String
Required: No

 ** networkInterfaceId **
The ID of the network interface.
Type: String
Required: No

 ** operator **
The service provider that manages the network interface.
Type: [OperatorResponse](API_OperatorResponse.md) object
Required: No

 ** outpostArn **
The Amazon Resource Name (ARN) of the Outpost.
Type: String
Required: No

 ** ownerId **
The AWS account ID of the owner of the network interface.
Type: String
Required: No

 ** privateDnsName **
The private hostname. For more information, see [EC2 instance hostnames, DNS names, and domains](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) in the *Amazon EC2 User Guide*.
Type: String
Required: No

 ** privateIpAddress **
The IPv4 address of the network interface within the subnet.
Type: String
Required: No

 ** PrivateIpAddressesSet.N **
The private IPv4 addresses associated with the network interface.
Type: Array of [NetworkInterfacePrivateIpAddress](API_NetworkInterfacePrivateIpAddress.md) objects
Required: No

 ** publicDnsName **
A public hostname. For more information, see [EC2 instance hostnames, DNS names, and domains](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) in the *Amazon EC2 User Guide*.
Type: String
Required: No

 ** publicIpDnsNameOptions **
Public hostname type options. For more information, see [EC2 instance hostnames, DNS names, and domains](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) in the *Amazon EC2 User Guide*.
Type: [PublicIpDnsNameOptions](API_PublicIpDnsNameOptions.md) object
Required: No

 ** requesterId **
The alias or AWS account ID of the principal or service that created the network interface.
Type: String
Required: No

 ** requesterManaged **
Indicates whether the network interface is being managed by AWS.
Type: Boolean
Required: No

 ** sourceDestCheck **
Indicates whether source/destination checking is enabled.
Type: Boolean
Required: No

 ** status **
The status of the network interface.
Type: String
Valid Values: `available | associated | attaching | in-use | detaching`
Required: No

 ** subnetId **
The ID of the subnet.
Type: String
Required: No

 ** TagSet.N **
Any tags assigned to the network interface.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** vpcId **
The ID of the VPC.
Type: String
Required: No

## See Also
<a name="API_NetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/NetworkInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/NetworkInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/NetworkInterface)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
