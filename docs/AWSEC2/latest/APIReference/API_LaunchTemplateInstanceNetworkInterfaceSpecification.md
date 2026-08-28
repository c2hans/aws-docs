---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateInstanceNetworkInterfaceSpecification.html
---

# LaunchTemplateInstanceNetworkInterfaceSpecification
<a name="API_LaunchTemplateInstanceNetworkInterfaceSpecification"></a>

Describes a network interface.

## Contents
<a name="API_LaunchTemplateInstanceNetworkInterfaceSpecification_Contents"></a>

 ** associateCarrierIpAddress **
Indicates whether to associate a Carrier IP address with eth0 for a new network interface.
Use this option when you launch an instance in a Wavelength Zone and want to associate a Carrier IP address with the network interface. For more information about Carrier IP addresses, see [Carrier IP address](https://docs.aws.amazon.com/wavelength/latest/developerguide/how-wavelengths-work.html#provider-owned-ip) in the * AWS Wavelength Developer Guide*.
Type: Boolean
Required: No

 ** associatePublicIpAddress **
Indicates whether to associate a public IPv4 address with eth0 for a new network interface.
 AWS charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the *Public IPv4 Address* tab on the [Amazon VPC pricing page](http://aws.amazon.com/vpc/pricing/).
Type: Boolean
Required: No

 ** connectionTrackingSpecification **
A security group connection tracking specification that enables you to set the timeout for connection tracking on an Elastic network interface. For more information, see [Idle connection tracking timeout](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts) in the *Amazon EC2 User Guide*.
Type: [ConnectionTrackingSpecification](API_ConnectionTrackingSpecification.md) object
Required: No

 ** deleteOnTermination **
Indicates whether the network interface is deleted when the instance is terminated.
Type: Boolean
Required: No

 ** description **
A description for the network interface.
Type: String
Required: No

 ** deviceIndex **
The device index for the network interface attachment.
Type: Integer
Required: No

 ** enaQueueCount **
The number of ENA queues created with the instance.
Type: Integer
Required: No

 ** enaSrdSpecification **
Contains the ENA Express settings for instances launched from your launch template.
Type: [LaunchTemplateEnaSrdSpecification](API_LaunchTemplateEnaSrdSpecification.md) object
Required: No

 ** GroupSet.N **
The IDs of one or more security groups.
Type: Array of strings
Required: No

 ** interfaceType **
The type of network interface.
Type: String
Required: No

 ** ipv4PrefixCount **
The number of IPv4 prefixes that AWS automatically assigned to the network interface.
Type: Integer
Required: No

 ** Ipv4PrefixSet.N **
One or more IPv4 prefixes assigned to the network interface.
Type: Array of [Ipv4PrefixSpecificationResponse](API_Ipv4PrefixSpecificationResponse.md) objects
Required: No

 ** ipv6AddressCount **
The number of IPv6 addresses for the network interface.
Type: Integer
Required: No

 ** Ipv6AddressesSet.N **
The IPv6 addresses for the network interface.
Type: Array of [InstanceIpv6Address](API_InstanceIpv6Address.md) objects
Required: No

 ** ipv6PrefixCount **
The number of IPv6 prefixes that AWS automatically assigned to the network interface.
Type: Integer
Required: No

 ** Ipv6PrefixSet.N **
One or more IPv6 prefixes assigned to the network interface.
Type: Array of [Ipv6PrefixSpecificationResponse](API_Ipv6PrefixSpecificationResponse.md) objects
Required: No

 ** networkCardIndex **
The index of the network card.
Type: Integer
Required: No

 ** networkInterfaceId **
The ID of the network interface.
Type: String
Required: No

 ** primaryIpv6 **
The primary IPv6 address of the network interface. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. For more information about primary IPv6 addresses, see [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html).
Type: Boolean
Required: No

 ** privateIpAddress **
The primary private IPv4 address of the network interface.
Type: String
Required: No

 ** PrivateIpAddressesSet.N **
One or more private IPv4 addresses.
Type: Array of [PrivateIpAddressSpecification](API_PrivateIpAddressSpecification.md) objects
Required: No

 ** secondaryPrivateIpAddressCount **
The number of secondary private IPv4 addresses for the network interface.
Type: Integer
Required: No

 ** subnetId **
The ID of the subnet for the network interface.
Type: String
Required: No

## See Also
<a name="API_LaunchTemplateInstanceNetworkInterfaceSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LaunchTemplateInstanceNetworkInterfaceSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LaunchTemplateInstanceNetworkInterfaceSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LaunchTemplateInstanceNetworkInterfaceSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
