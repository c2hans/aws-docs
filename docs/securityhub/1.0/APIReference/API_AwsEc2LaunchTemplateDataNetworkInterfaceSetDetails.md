---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails.html
---

# AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails
<a name="API_AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails"></a>

 One or more network interfaces to attach to an Amazon EC2 instance. If you specify a network interface, you must specify security groups and subnets as part of the network interface.

## Contents
<a name="API_AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails_Contents"></a>

 ** AssociateCarrierIpAddress **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails-AssociateCarrierIpAddress"></a>
 Indicates whether to associate a Carrier IP address with eth0 for a new network interface. You use this option when you launch an instance in a Wavelength Zone and want to associate a Carrier IP address with the network interface. For more information, see [Carrier IP address](https://docs.aws.amazon.com/wavelength/latest/developerguide/how-wavelengths-work.html#provider-owned-ip) in the * AWS Wavelength Developer Guide*.
Type: Boolean
Required: No

 ** AssociatePublicIpAddress **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails-AssociatePublicIpAddress"></a>
 Associates a public IPv4 address with eth0 for a new network interface.
Type: Boolean
Required: No

 ** DeleteOnTermination **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails-DeleteOnTermination"></a>
 Indicates whether the network interface is deleted when the instance is terminated.
Type: Boolean
Required: No

 ** Description **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails-Description"></a>
 A description for the network interface.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DeviceIndex **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails-DeviceIndex"></a>
 The device index for the network interface attachment.
Type: Integer
Required: No

 ** Groups **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails-Groups"></a>
 The IDs of one or more security groups.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** InterfaceType **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails-InterfaceType"></a>
 The type of network interface.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Ipv4PrefixCount **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails-Ipv4PrefixCount"></a>
 The number of IPv4 prefixes to be automatically assigned to the network interface. You cannot use this option if you use the `Ipv4Prefixes` option.
Type: Integer
Required: No

 ** Ipv4Prefixes **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails-Ipv4Prefixes"></a>
 One or more IPv4 prefixes to be assigned to the network interface. You cannot use this option if you use the `Ipv4PrefixCount` option.
Type: Array of [AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetails](API_AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetails.md) objects
Required: No

 ** Ipv6AddressCount **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails-Ipv6AddressCount"></a>
 The number of IPv6 addresses to assign to a network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. You can't use this option if you use `Ipv6Addresses`.
Type: Integer
Required: No

 ** Ipv6Addresses **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails-Ipv6Addresses"></a>
 One or more specific IPv6 addresses from the IPv6 CIDR block range of your subnet. You can't use this option if you use `Ipv6AddressCount`.
Type: Array of [AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetails](API_AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetails.md) objects
Required: No

 ** Ipv6PrefixCount **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails-Ipv6PrefixCount"></a>
 The number of IPv6 prefixes to be automatically assigned to the network interface. You cannot use this option if you use the `Ipv6Prefix` option.
Type: Integer
Required: No

 ** Ipv6Prefixes **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails-Ipv6Prefixes"></a>
 One or more IPv6 prefixes to be assigned to the network interface. You cannot use this option if you use the `Ipv6PrefixCount` option.
Type: Array of [AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetails](API_AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetails.md) objects
Required: No

 ** NetworkCardIndex **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails-NetworkCardIndex"></a>
 The index of the network card. Some instance types support multiple network cards. The primary network interface must be assigned to network card index `0`. The default is network card index `0`.
Type: Integer
Required: No

 ** NetworkInterfaceId **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails-NetworkInterfaceId"></a>
 The ID of the network interface.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PrivateIpAddress **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails-PrivateIpAddress"></a>
 The primary private IPv4 address of the network interface.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PrivateIpAddresses **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails-PrivateIpAddresses"></a>
 One or more private IPv4 addresses.
Type: Array of [AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetails](API_AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetails.md) objects
Required: No

 ** SecondaryPrivateIpAddressCount **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails-SecondaryPrivateIpAddressCount"></a>
 The number of secondary private IPv4 addresses to assign to a network interface.
Type: Integer
Required: No

 ** SubnetId **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails-SubnetId"></a>
 The ID of the subnet for the network interface.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails)
