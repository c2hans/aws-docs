---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceNetworkInterfaceSpecification.html
---

# InstanceNetworkInterfaceSpecification
<a name="API_InstanceNetworkInterfaceSpecification"></a>

Describes a network interface.

## Contents
<a name="API_InstanceNetworkInterfaceSpecification_Contents"></a>

 ** AssociateCarrierIpAddress ** (request), ** AssociateCarrierIpAddress ** (response)
Indicates whether to assign a carrier IP address to the network interface.
You can only assign a carrier IP address to a network interface that is in a subnet in a Wavelength Zone. For more information about carrier IP addresses, see [Carrier IP address](https://docs.aws.amazon.com/wavelength/latest/developerguide/how-wavelengths-work.html#provider-owned-ip) in the * AWS Wavelength Developer Guide*.
Type: Boolean
Required: No

 ** AssociatePublicIpAddress ** (request), ** associatePublicIpAddress ** (response)
Indicates whether to assign a public IPv4 address to an instance you launch in a VPC. The public IP address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is `true`.
 AWS charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the *Public IPv4 Address* tab on the [Amazon VPC pricing page](http://aws.amazon.com/vpc/pricing/).
Type: Boolean
Required: No

 ** ConnectionTrackingSpecification ** (request), ** ConnectionTrackingSpecification ** (response)
A security group connection tracking specification that enables you to set the timeout for connection tracking on an Elastic network interface. For more information, see [Connection tracking timeouts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts) in the *Amazon EC2 User Guide*.
Type: [ConnectionTrackingSpecificationRequest](API_ConnectionTrackingSpecificationRequest.md) object
Required: No

 ** DeleteOnTermination ** (request), ** deleteOnTermination ** (response)
If set to `true`, the interface is deleted when the instance is terminated. You can specify `true` only if creating a new network interface when launching an instance.
Type: Boolean
Required: No

 ** Description ** (request), ** description ** (response)
The description of the network interface. Applies only if creating a network interface when launching an instance.
Type: String
Required: No

 ** DeviceIndex ** (request), ** deviceIndex ** (response)
The position of the network interface in the attachment order. A primary network interface has a device index of 0.
If you specify a network interface when launching an instance, you must specify the device index.
Type: Integer
Required: No

 ** EnaQueueCount ** (request), ** EnaQueueCount ** (response)
The number of ENA queues to be created with the instance.
Type: Integer
Required: No

 ** EnaSrdSpecification ** (request), ** EnaSrdSpecification ** (response)
Specifies the ENA Express settings for the network interface that's attached to the instance.
Type: [EnaSrdSpecificationRequest](API_EnaSrdSpecificationRequest.md) object
Required: No

 ** InterfaceType ** (request), ** InterfaceType ** (response)
The type of network interface.
If you specify `efa-only`, do not assign any IP addresses to the network interface. EFA-only network interfaces do not support IP addresses.
Valid values: `interface` \| `efa` \| `efa-only`
Type: String
Required: No

 ** Ipv4Prefix.N **
The IPv4 delegated prefixes to be assigned to the network interface. You cannot use this option if you use the `Ipv4PrefixCount` option.
Type: Array of [Ipv4PrefixSpecificationRequest](API_Ipv4PrefixSpecificationRequest.md) objects
Required: No

 ** Ipv4PrefixCount ** (request), ** Ipv4PrefixCount ** (response)
The number of IPv4 delegated prefixes to be automatically assigned to the network interface. You cannot use this option if you use the `Ipv4Prefix` option.
Type: Integer
Required: No

 ** Ipv6AddressCount ** (request), ** ipv6AddressCount ** (response)
A number of IPv6 addresses to assign to the network interface. Amazon EC2 chooses the IPv6 addresses from the range of the subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you've specified a minimum number of instances to launch.
Type: Integer
Required: No

 ** Ipv6Addresses.N **
The IPv6 addresses to assign to the network interface. You cannot specify this option and the option to assign a number of IPv6 addresses in the same request. You cannot specify this option if you've specified a minimum number of instances to launch.
Type: Array of [InstanceIpv6Address](API_InstanceIpv6Address.md) objects
Required: No

 ** Ipv6Prefix.N **
The IPv6 delegated prefixes to be assigned to the network interface. You cannot use this option if you use the `Ipv6PrefixCount` option.
Type: Array of [Ipv6PrefixSpecificationRequest](API_Ipv6PrefixSpecificationRequest.md) objects
Required: No

 ** Ipv6PrefixCount ** (request), ** Ipv6PrefixCount ** (response)
The number of IPv6 delegated prefixes to be automatically assigned to the network interface. You cannot use this option if you use the `Ipv6Prefix` option.
Type: Integer
Required: No

 ** NetworkCardIndex ** (request), ** NetworkCardIndex ** (response)
The index of the network card. Some instance types support multiple network cards. The primary network interface must be assigned to network card index 0. The default is network card index 0.
If you are using [RequestSpotInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html) to create Spot Instances, omit this parameter because you can’t specify the network card index when using this API. To specify the network card index, use [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html).
Type: Integer
Required: No

 ** NetworkInterfaceId ** (request), ** networkInterfaceId ** (response)
The ID of the network interface.
If you are creating a Spot Fleet, omit this parameter because you can’t specify a network interface ID in a launch specification.
Type: String
Required: No

 ** PrimaryIpv6 ** (request), ** PrimaryIpv6 ** (response)
The primary IPv6 address of the network interface. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. For more information about primary IPv6 addresses, see [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html).
Type: Boolean
Required: No

 ** PrivateIpAddress ** (request), ** privateIpAddress ** (response)
The private IPv4 address of the network interface. Applies only if creating a network interface when launching an instance. You cannot specify this option if you're launching more than one instance in a [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) request.
Type: String
Required: No

 ** PrivateIpAddresses.N **
The private IPv4 addresses to assign to the network interface. Only one private IPv4 address can be designated as primary. You cannot specify this option if you're launching more than one instance in a [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) request.
Type: Array of [PrivateIpAddressSpecification](API_PrivateIpAddressSpecification.md) objects
Required: No

 ** SecondaryPrivateIpAddressCount ** (request), ** secondaryPrivateIpAddressCount ** (response)
The number of secondary private IPv4 addresses. You can’t specify this parameter and also specify a secondary private IP address using the `PrivateIpAddress` parameter.
Type: Integer
Required: No

 ** SecurityGroupId.N **
The IDs of the security groups for the network interface. Applies only if creating a network interface when launching an instance.
Type: Array of strings
Required: No

 ** SubnetId ** (request), ** subnetId ** (response)
The ID of the subnet associated with the network interface. Applies only if creating a network interface when launching an instance.
Type: String
Required: No

## See Also
<a name="API_InstanceNetworkInterfaceSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceNetworkInterfaceSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceNetworkInterfaceSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceNetworkInterfaceSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
