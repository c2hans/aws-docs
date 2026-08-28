---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-launchtemplate-networkinterface.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate NetworkInterface
<a name="aws-properties-ec2-launchtemplate-networkinterface"></a>

Specifies the parameters for a network interface.

`NetworkInterface` is a property of [AWS::EC2::LaunchTemplate LaunchTemplateData](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html).

## Syntax
<a name="aws-properties-ec2-launchtemplate-networkinterface-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-launchtemplate-networkinterface-syntax.json"></a>

```
{
  "[AssociateCarrierIpAddress](#cfn-ec2-launchtemplate-networkinterface-associatecarrieripaddress)" : {{Boolean}},
  "[AssociatePublicIpAddress](#cfn-ec2-launchtemplate-networkinterface-associatepublicipaddress)" : {{Boolean}},
  "[ConnectionTrackingSpecification](#cfn-ec2-launchtemplate-networkinterface-connectiontrackingspecification)" : {{ConnectionTrackingSpecification}},
  "[DeleteOnTermination](#cfn-ec2-launchtemplate-networkinterface-deleteontermination)" : {{Boolean}},
  "[Description](#cfn-ec2-launchtemplate-networkinterface-description)" : {{String}},
  "[DeviceIndex](#cfn-ec2-launchtemplate-networkinterface-deviceindex)" : {{Integer}},
  "[EnaQueueCount](#cfn-ec2-launchtemplate-networkinterface-enaqueuecount)" : {{Integer}},
  "[EnaSrdSpecification](#cfn-ec2-launchtemplate-networkinterface-enasrdspecification)" : {{EnaSrdSpecification}},
  "[Groups](#cfn-ec2-launchtemplate-networkinterface-groups)" : {{[ String, ... ]}},
  "[InterfaceType](#cfn-ec2-launchtemplate-networkinterface-interfacetype)" : {{String}},
  "[Ipv4PrefixCount](#cfn-ec2-launchtemplate-networkinterface-ipv4prefixcount)" : {{Integer}},
  "[Ipv4Prefixes](#cfn-ec2-launchtemplate-networkinterface-ipv4prefixes)" : {{[ Ipv4PrefixSpecification, ... ]}},
  "[Ipv6AddressCount](#cfn-ec2-launchtemplate-networkinterface-ipv6addresscount)" : {{Integer}},
  "[Ipv6Addresses](#cfn-ec2-launchtemplate-networkinterface-ipv6addresses)" : {{[ Ipv6Add, ... ]}},
  "[Ipv6PrefixCount](#cfn-ec2-launchtemplate-networkinterface-ipv6prefixcount)" : {{Integer}},
  "[Ipv6Prefixes](#cfn-ec2-launchtemplate-networkinterface-ipv6prefixes)" : {{[ Ipv6PrefixSpecification, ... ]}},
  "[NetworkCardIndex](#cfn-ec2-launchtemplate-networkinterface-networkcardindex)" : {{Integer}},
  "[NetworkInterfaceId](#cfn-ec2-launchtemplate-networkinterface-networkinterfaceid)" : {{String}},
  "[PrimaryIpv6](#cfn-ec2-launchtemplate-networkinterface-primaryipv6)" : {{Boolean}},
  "[PrivateIpAddress](#cfn-ec2-launchtemplate-networkinterface-privateipaddress)" : {{String}},
  "[PrivateIpAddresses](#cfn-ec2-launchtemplate-networkinterface-privateipaddresses)" : {{[ PrivateIpAdd, ... ]}},
  "[SecondaryPrivateIpAddressCount](#cfn-ec2-launchtemplate-networkinterface-secondaryprivateipaddresscount)" : {{Integer}},
  "[SubnetId](#cfn-ec2-launchtemplate-networkinterface-subnetid)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-launchtemplate-networkinterface-syntax.yaml"></a>

```
  [AssociateCarrierIpAddress](#cfn-ec2-launchtemplate-networkinterface-associatecarrieripaddress): {{Boolean}}
  [AssociatePublicIpAddress](#cfn-ec2-launchtemplate-networkinterface-associatepublicipaddress): {{Boolean}}
  [ConnectionTrackingSpecification](#cfn-ec2-launchtemplate-networkinterface-connectiontrackingspecification): {{
    ConnectionTrackingSpecification}}
  [DeleteOnTermination](#cfn-ec2-launchtemplate-networkinterface-deleteontermination): {{Boolean}}
  [Description](#cfn-ec2-launchtemplate-networkinterface-description): {{String}}
  [DeviceIndex](#cfn-ec2-launchtemplate-networkinterface-deviceindex): {{Integer}}
  [EnaQueueCount](#cfn-ec2-launchtemplate-networkinterface-enaqueuecount): {{Integer}}
  [EnaSrdSpecification](#cfn-ec2-launchtemplate-networkinterface-enasrdspecification): {{
    EnaSrdSpecification}}
  [Groups](#cfn-ec2-launchtemplate-networkinterface-groups): {{
    - String}}
  [InterfaceType](#cfn-ec2-launchtemplate-networkinterface-interfacetype): {{String}}
  [Ipv4PrefixCount](#cfn-ec2-launchtemplate-networkinterface-ipv4prefixcount): {{Integer}}
  [Ipv4Prefixes](#cfn-ec2-launchtemplate-networkinterface-ipv4prefixes): {{
    - Ipv4PrefixSpecification}}
  [Ipv6AddressCount](#cfn-ec2-launchtemplate-networkinterface-ipv6addresscount): {{Integer}}
  [Ipv6Addresses](#cfn-ec2-launchtemplate-networkinterface-ipv6addresses): {{
    - Ipv6Add}}
  [Ipv6PrefixCount](#cfn-ec2-launchtemplate-networkinterface-ipv6prefixcount): {{Integer}}
  [Ipv6Prefixes](#cfn-ec2-launchtemplate-networkinterface-ipv6prefixes): {{
    - Ipv6PrefixSpecification}}
  [NetworkCardIndex](#cfn-ec2-launchtemplate-networkinterface-networkcardindex): {{Integer}}
  [NetworkInterfaceId](#cfn-ec2-launchtemplate-networkinterface-networkinterfaceid): {{String}}
  [PrimaryIpv6](#cfn-ec2-launchtemplate-networkinterface-primaryipv6): {{Boolean}}
  [PrivateIpAddress](#cfn-ec2-launchtemplate-networkinterface-privateipaddress): {{String}}
  [PrivateIpAddresses](#cfn-ec2-launchtemplate-networkinterface-privateipaddresses): {{
    - PrivateIpAdd}}
  [SecondaryPrivateIpAddressCount](#cfn-ec2-launchtemplate-networkinterface-secondaryprivateipaddresscount): {{Integer}}
  [SubnetId](#cfn-ec2-launchtemplate-networkinterface-subnetid): {{String}}
```

## Properties
<a name="aws-properties-ec2-launchtemplate-networkinterface-properties"></a>

`AssociateCarrierIpAddress`  <a name="cfn-ec2-launchtemplate-networkinterface-associatecarrieripaddress"></a>
Associates a Carrier IP address with eth0 for a new network interface.
Use this option when you launch an instance in a Wavelength Zone and want to associate a Carrier IP address with the network interface. For more information about Carrier IP addresses, see [Carrier IP addresses](https://docs.aws.amazon.com/wavelength/latest/developerguide/how-wavelengths-work.html#provider-owned-ip) in the *AWS Wavelength Developer Guide*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssociatePublicIpAddress`  <a name="cfn-ec2-launchtemplate-networkinterface-associatepublicipaddress"></a>
Associates a public IPv4 address with eth0 for a new network interface.
AWS charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the *Public IPv4 Address* tab on the [Amazon VPC pricing page](https://aws.amazon.com/vpc/pricing/).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectionTrackingSpecification`  <a name="cfn-ec2-launchtemplate-networkinterface-connectiontrackingspecification"></a>
A connection tracking specification for the network interface.
*Required*: No
*Type*: [ConnectionTrackingSpecification](aws-properties-ec2-launchtemplate-connectiontrackingspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeleteOnTermination`  <a name="cfn-ec2-launchtemplate-networkinterface-deleteontermination"></a>
Indicates whether the network interface is deleted when the instance is terminated.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-ec2-launchtemplate-networkinterface-description"></a>
A description for the network interface.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceIndex`  <a name="cfn-ec2-launchtemplate-networkinterface-deviceindex"></a>
The device index for the network interface attachment. The primary network interface has a device index of 0. If the network interface is of type `interface`, you must specify a device index.
If you create a launch template that includes secondary network interfaces but no primary network interface, and you specify it using the `LaunchTemplate` property of `AWS::EC2::Instance`, then you must include a primary network interface using the `NetworkInterfaces` property of `AWS::EC2::Instance`.
*Required*: Conditional
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnaQueueCount`  <a name="cfn-ec2-launchtemplate-networkinterface-enaqueuecount"></a>
The number of ENA queues to be created with the instance.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnaSrdSpecification`  <a name="cfn-ec2-launchtemplate-networkinterface-enasrdspecification"></a>
The ENA Express configuration for the network interface.
*Required*: No
*Type*: [EnaSrdSpecification](aws-properties-ec2-launchtemplate-enasrdspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Groups`  <a name="cfn-ec2-launchtemplate-networkinterface-groups"></a>
The IDs of one or more security groups.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InterfaceType`  <a name="cfn-ec2-launchtemplate-networkinterface-interfacetype"></a>
The type of network interface. To create an Elastic Fabric Adapter (EFA), specify `efa` or `efa`. For more information, see [Elastic Fabric Adapter for AI/ML and HPC workloads on Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html) in the *Amazon EC2 User Guide*.
If you are not creating an EFA, specify `interface` or omit this parameter.
If you specify `efa-only`, do not assign any IP addresses to the network interface. EFA-only network interfaces do not support IP addresses.
Valid values: `interface` \| `efa` \| `efa-only`
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv4PrefixCount`  <a name="cfn-ec2-launchtemplate-networkinterface-ipv4prefixcount"></a>
The number of IPv4 prefixes to be automatically assigned to the network interface. You cannot use this option if you use the `Ipv4Prefix` option.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv4Prefixes`  <a name="cfn-ec2-launchtemplate-networkinterface-ipv4prefixes"></a>
One or more IPv4 prefixes to be assigned to the network interface. You cannot use this option if you use the `Ipv4PrefixCount` option.
*Required*: No
*Type*: Array of [Ipv4PrefixSpecification](aws-properties-ec2-launchtemplate-ipv4prefixspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv6AddressCount`  <a name="cfn-ec2-launchtemplate-networkinterface-ipv6addresscount"></a>
The number of IPv6 addresses to assign to a network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. You can't use this option if specifying specific IPv6 addresses.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv6Addresses`  <a name="cfn-ec2-launchtemplate-networkinterface-ipv6addresses"></a>
One or more specific IPv6 addresses from the IPv6 CIDR block range of your subnet. You can't use this option if you're specifying a number of IPv6 addresses.
*Required*: No
*Type*: Array of [Ipv6Add](aws-properties-ec2-launchtemplate-ipv6add.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv6PrefixCount`  <a name="cfn-ec2-launchtemplate-networkinterface-ipv6prefixcount"></a>
The number of IPv6 prefixes to be automatically assigned to the network interface. You cannot use this option if you use the `Ipv6Prefix` option.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv6Prefixes`  <a name="cfn-ec2-launchtemplate-networkinterface-ipv6prefixes"></a>
One or more IPv6 prefixes to be assigned to the network interface. You cannot use this option if you use the `Ipv6PrefixCount` option.
*Required*: No
*Type*: Array of [Ipv6PrefixSpecification](aws-properties-ec2-launchtemplate-ipv6prefixspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkCardIndex`  <a name="cfn-ec2-launchtemplate-networkinterface-networkcardindex"></a>
The index of the network card. Some instance types support multiple network cards. The primary network interface must be assigned to network card index 0. The default is network card index 0.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkInterfaceId`  <a name="cfn-ec2-launchtemplate-networkinterface-networkinterfaceid"></a>
The ID of the network interface.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryIpv6`  <a name="cfn-ec2-launchtemplate-networkinterface-primaryipv6"></a>
The primary IPv6 address of the network interface. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. For more information about primary IPv6 addresses, see [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateIpAddress`  <a name="cfn-ec2-launchtemplate-networkinterface-privateipaddress"></a>
The primary private IPv4 address of the network interface.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateIpAddresses`  <a name="cfn-ec2-launchtemplate-networkinterface-privateipaddresses"></a>
One or more private IPv4 addresses.
*Required*: No
*Type*: Array of [PrivateIpAdd](aws-properties-ec2-launchtemplate-privateipadd.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecondaryPrivateIpAddressCount`  <a name="cfn-ec2-launchtemplate-networkinterface-secondaryprivateipaddresscount"></a>
The number of secondary private IPv4 addresses to assign to a network interface.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetId`  <a name="cfn-ec2-launchtemplate-networkinterface-subnetid"></a>
The ID of the subnet for the network interface.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ec2-launchtemplate-networkinterface--seealso"></a>
+ [ LaunchTemplateInstanceNetworkInterfaceSpecificationRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateInstanceNetworkInterfaceSpecificationRequest.html) in the *Amazon EC2 API Reference*
+ [ Create a launch template for an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html) in the *Amazon EC2 Auto Scaling User Guide*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
