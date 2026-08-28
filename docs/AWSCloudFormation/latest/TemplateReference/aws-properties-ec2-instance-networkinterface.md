---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instance-networkinterface.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::Instance NetworkInterface
<a name="aws-properties-ec2-instance-networkinterface"></a>

Specifies a network interface that is to be attached to an instance.

You can create a network interface when launching an instance. For an example, see the [AWS::EC2::Instance examples](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#aws-properties-ec2-instance--examples--Automatically_assign_a_public_IP_address).

Alternatively, you can attach an existing network interface when launching an instance. For an example, see the [AWS::EC2:NetworkInterface examples](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterface.html#aws-resource-ec2-networkinterface--examples).

## Syntax
<a name="aws-properties-ec2-instance-networkinterface-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-instance-networkinterface-syntax.json"></a>

```
{
  "[AssociateCarrierIpAddress](#cfn-ec2-instance-networkinterface-associatecarrieripaddress)" : {{Boolean}},
  "[AssociatePublicIpAddress](#cfn-ec2-instance-networkinterface-associatepublicipaddress)" : {{Boolean}},
  "[DeleteOnTermination](#cfn-ec2-instance-networkinterface-deleteontermination)" : {{Boolean}},
  "[Description](#cfn-ec2-instance-networkinterface-description)" : {{String}},
  "[DeviceIndex](#cfn-ec2-instance-networkinterface-deviceindex)" : {{String}},
  "[EnaSrdSpecification](#cfn-ec2-instance-networkinterface-enasrdspecification)" : {{EnaSrdSpecification}},
  "[GroupSet](#cfn-ec2-instance-networkinterface-groupset)" : {{[ String, ... ]}},
  "[Ipv6AddressCount](#cfn-ec2-instance-networkinterface-ipv6addresscount)" : {{Integer}},
  "[Ipv6Addresses](#cfn-ec2-instance-networkinterface-ipv6addresses)" : {{[ InstanceIpv6Address, ... ]}},
  "[NetworkInterfaceId](#cfn-ec2-instance-networkinterface-networkinterfaceid)" : {{String}},
  "[PrivateIpAddress](#cfn-ec2-instance-networkinterface-privateipaddress)" : {{String}},
  "[PrivateIpAddresses](#cfn-ec2-instance-networkinterface-privateipaddresses)" : {{[ PrivateIpAddressSpecification, ... ]}},
  "[SecondaryPrivateIpAddressCount](#cfn-ec2-instance-networkinterface-secondaryprivateipaddresscount)" : {{Integer}},
  "[SubnetId](#cfn-ec2-instance-networkinterface-subnetid)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-instance-networkinterface-syntax.yaml"></a>

```
  [AssociateCarrierIpAddress](#cfn-ec2-instance-networkinterface-associatecarrieripaddress): {{Boolean}}
  [AssociatePublicIpAddress](#cfn-ec2-instance-networkinterface-associatepublicipaddress): {{Boolean}}
  [DeleteOnTermination](#cfn-ec2-instance-networkinterface-deleteontermination): {{Boolean}}
  [Description](#cfn-ec2-instance-networkinterface-description): {{String}}
  [DeviceIndex](#cfn-ec2-instance-networkinterface-deviceindex): {{String}}
  [EnaSrdSpecification](#cfn-ec2-instance-networkinterface-enasrdspecification): {{
    EnaSrdSpecification}}
  [GroupSet](#cfn-ec2-instance-networkinterface-groupset): {{
    - String}}
  [Ipv6AddressCount](#cfn-ec2-instance-networkinterface-ipv6addresscount): {{Integer}}
  [Ipv6Addresses](#cfn-ec2-instance-networkinterface-ipv6addresses): {{
    - InstanceIpv6Address}}
  [NetworkInterfaceId](#cfn-ec2-instance-networkinterface-networkinterfaceid): {{String}}
  [PrivateIpAddress](#cfn-ec2-instance-networkinterface-privateipaddress): {{String}}
  [PrivateIpAddresses](#cfn-ec2-instance-networkinterface-privateipaddresses): {{
    - PrivateIpAddressSpecification}}
  [SecondaryPrivateIpAddressCount](#cfn-ec2-instance-networkinterface-secondaryprivateipaddresscount): {{Integer}}
  [SubnetId](#cfn-ec2-instance-networkinterface-subnetid): {{String}}
```

## Properties
<a name="aws-properties-ec2-instance-networkinterface-properties"></a>

`AssociateCarrierIpAddress`  <a name="cfn-ec2-instance-networkinterface-associatecarrieripaddress"></a>
Indicates whether to assign a carrier IP address to the network interface.
You can only assign a carrier IP address to a network interface that is in a subnet in a Wavelength Zone. For more information about carrier IP addresses, see [Carrier IP address](https://docs.aws.amazon.com/wavelength/latest/developerguide/how-wavelengths-work.html#provider-owned-ip) in the *AWS Wavelength Developer Guide*.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AssociatePublicIpAddress`  <a name="cfn-ec2-instance-networkinterface-associatepublicipaddress"></a>
Indicates whether to assign a public IPv4 address to an instance. Applies only if creating a network interface when launching an instance. The network interface must be the primary network interface. If launching into a default subnet, the default value is `true`.
AWS charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the *Public IPv4 Address* tab on the [VPC pricing page](https://aws.amazon.com/vpc/pricing/).
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DeleteOnTermination`  <a name="cfn-ec2-instance-networkinterface-deleteontermination"></a>
Indicates whether the network interface is deleted when the instance is terminated. Applies only if creating a network interface when launching an instance.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-ec2-instance-networkinterface-description"></a>
The description of the network interface. Applies only if creating a network interface when launching an instance.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DeviceIndex`  <a name="cfn-ec2-instance-networkinterface-deviceindex"></a>
The position of the network interface in the attachment order. A primary network interface has a device index of 0.
If you create a network interface when launching an instance, you must specify the device index.
*Required*: Conditional
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnaSrdSpecification`  <a name="cfn-ec2-instance-networkinterface-enasrdspecification"></a>
Configures ENA Express for UDP network traffic.
*Required*: No
*Type*: [EnaSrdSpecification](aws-properties-ec2-instance-enasrdspecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GroupSet`  <a name="cfn-ec2-instance-networkinterface-groupset"></a>
The IDs of the security groups for the network interface. Applies only if creating a network interface when launching an instance.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ipv6AddressCount`  <a name="cfn-ec2-instance-networkinterface-ipv6addresscount"></a>
A number of IPv6 addresses to assign to the network interface. Amazon EC2 chooses the IPv6 addresses from the range of the subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you've specified a minimum number of instances to launch.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ipv6Addresses`  <a name="cfn-ec2-instance-networkinterface-ipv6addresses"></a>
The IPv6 addresses to assign to the network interface. You cannot specify this option and the option to assign a number of IPv6 addresses in the same request. You cannot specify this option if you've specified a minimum number of instances to launch.
*Required*: No
*Type*: Array of [InstanceIpv6Address](aws-properties-ec2-instance-instanceipv6address.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkInterfaceId`  <a name="cfn-ec2-instance-networkinterface-networkinterfaceid"></a>
The ID of the network interface, when attaching an existing network interface.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrivateIpAddress`  <a name="cfn-ec2-instance-networkinterface-privateipaddress"></a>
The private IPv4 address of the network interface. Applies only if creating a network interface when launching an instance.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrivateIpAddresses`  <a name="cfn-ec2-instance-networkinterface-privateipaddresses"></a>
One or more private IPv4 addresses to assign to the network interface. Only one private IPv4 address can be designated as primary.
*Required*: No
*Type*: Array of [PrivateIpAddressSpecification](aws-properties-ec2-instance-privateipaddressspecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecondaryPrivateIpAddressCount`  <a name="cfn-ec2-instance-networkinterface-secondaryprivateipaddresscount"></a>
The number of secondary private IPv4 addresses. You can't specify this option and specify more than one private IP address using the private IP addresses option.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetId`  <a name="cfn-ec2-instance-networkinterface-subnetid"></a>
The ID of the subnet associated with the network interface.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
