---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_InstanceNetworkInterfaceSpecification.html
---

# InstanceNetworkInterfaceSpecification
<a name="API_InstanceNetworkInterfaceSpecification"></a>

Defines network interface configuration for WorkSpace Instance.

## Contents
<a name="API_InstanceNetworkInterfaceSpecification_Contents"></a>

 ** AssociateCarrierIpAddress **   <a name="workspacesinstances-Type-InstanceNetworkInterfaceSpecification-AssociateCarrierIpAddress"></a>
Enables carrier IP address association.
Type: Boolean
Required: No

 ** AssociatePublicIpAddress **   <a name="workspacesinstances-Type-InstanceNetworkInterfaceSpecification-AssociatePublicIpAddress"></a>
Enables public IP address assignment.
Type: Boolean
Required: No

 ** ConnectionTrackingSpecification **   <a name="workspacesinstances-Type-InstanceNetworkInterfaceSpecification-ConnectionTrackingSpecification"></a>
Configures network connection tracking parameters.
Type: [ConnectionTrackingSpecificationRequest](API_ConnectionTrackingSpecificationRequest.md) object
Required: No

 ** Description **   <a name="workspacesinstances-Type-InstanceNetworkInterfaceSpecification-Description"></a>
Descriptive text for the network interface.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `[\S\s]*`
Required: No

 ** DeviceIndex **   <a name="workspacesinstances-Type-InstanceNetworkInterfaceSpecification-DeviceIndex"></a>
Unique index for the network interface.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** EnaSrdSpecification **   <a name="workspacesinstances-Type-InstanceNetworkInterfaceSpecification-EnaSrdSpecification"></a>
Configures Elastic Network Adapter Scalable Reliable Datagram settings.
Type: [EnaSrdSpecificationRequest](API_EnaSrdSpecificationRequest.md) object
Required: No

 ** Groups **   <a name="workspacesinstances-Type-InstanceNetworkInterfaceSpecification-Groups"></a>
Security groups associated with the network interface.
Type: Array of strings
Pattern: `sg-[0-9a-zA-Z]{1,63}`
Required: No

 ** InterfaceType **   <a name="workspacesinstances-Type-InstanceNetworkInterfaceSpecification-InterfaceType"></a>
Specifies the type of network interface.
Type: String
Valid Values: `interface | efa | efa-only`
Required: No

 ** Ipv4PrefixCount **   <a name="workspacesinstances-Type-InstanceNetworkInterfaceSpecification-Ipv4PrefixCount"></a>
Number of IPv4 prefixes to assign.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Ipv4Prefixes **   <a name="workspacesinstances-Type-InstanceNetworkInterfaceSpecification-Ipv4Prefixes"></a>
IPv4 prefix configurations for the interface.
Type: Array of [Ipv4PrefixSpecificationRequest](API_Ipv4PrefixSpecificationRequest.md) objects
Required: No

 ** Ipv6AddressCount **   <a name="workspacesinstances-Type-InstanceNetworkInterfaceSpecification-Ipv6AddressCount"></a>
Number of IPv6 addresses to assign.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Ipv6Addresses **   <a name="workspacesinstances-Type-InstanceNetworkInterfaceSpecification-Ipv6Addresses"></a>
Specific IPv6 addresses for the interface.
Type: Array of [InstanceIpv6Address](API_InstanceIpv6Address.md) objects
Required: No

 ** Ipv6PrefixCount **   <a name="workspacesinstances-Type-InstanceNetworkInterfaceSpecification-Ipv6PrefixCount"></a>
Number of IPv6 prefixes to assign.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Ipv6Prefixes **   <a name="workspacesinstances-Type-InstanceNetworkInterfaceSpecification-Ipv6Prefixes"></a>
IPv6 prefix configurations for the interface.
Type: Array of [Ipv6PrefixSpecificationRequest](API_Ipv6PrefixSpecificationRequest.md) objects
Required: No

 ** NetworkCardIndex **   <a name="workspacesinstances-Type-InstanceNetworkInterfaceSpecification-NetworkCardIndex"></a>
Index of the network card for multiple network interfaces.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** NetworkInterfaceId **   <a name="workspacesinstances-Type-InstanceNetworkInterfaceSpecification-NetworkInterfaceId"></a>
Unique identifier for the network interface.
Type: String
Pattern: `eni-[0-9a-zA-Z]{1,63}`
Required: No

 ** PrimaryIpv6 **   <a name="workspacesinstances-Type-InstanceNetworkInterfaceSpecification-PrimaryIpv6"></a>
Indicates the primary IPv6 configuration.
Type: Boolean
Required: No

 ** PrivateIpAddress **   <a name="workspacesinstances-Type-InstanceNetworkInterfaceSpecification-PrivateIpAddress"></a>
Primary private IP address for the interface.
Type: String
Pattern: `(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}`
Required: No

 ** PrivateIpAddresses **   <a name="workspacesinstances-Type-InstanceNetworkInterfaceSpecification-PrivateIpAddresses"></a>
List of private IP addresses for the interface.
Type: Array of [PrivateIpAddressSpecification](API_PrivateIpAddressSpecification.md) objects
Required: No

 ** SecondaryPrivateIpAddressCount **   <a name="workspacesinstances-Type-InstanceNetworkInterfaceSpecification-SecondaryPrivateIpAddressCount"></a>
Number of additional private IP addresses to assign.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** SubnetId **   <a name="workspacesinstances-Type-InstanceNetworkInterfaceSpecification-SubnetId"></a>
Subnet identifier for the network interface.
Type: String
Pattern: `subnet-[0-9a-zA-Z]{1,63}`
Required: No

## See Also
<a name="API_InstanceNetworkInterfaceSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/InstanceNetworkInterfaceSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/InstanceNetworkInterfaceSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/InstanceNetworkInterfaceSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for WorkSpaces Instances. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-instances` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
