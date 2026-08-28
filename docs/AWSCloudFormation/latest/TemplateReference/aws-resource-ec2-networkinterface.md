---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-networkinterface.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::NetworkInterface
<a name="aws-resource-ec2-networkinterface"></a>

Describes a network interface in an Amazon EC2 instance for AWS CloudFormation.

## Syntax
<a name="aws-resource-ec2-networkinterface-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-networkinterface-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::NetworkInterface",
  "Properties" : {
      "[ConnectionTrackingSpecification](#cfn-ec2-networkinterface-connectiontrackingspecification)" : {{ConnectionTrackingSpecification}},
      "[Description](#cfn-ec2-networkinterface-description)" : {{String}},
      "[EnablePrimaryIpv6](#cfn-ec2-networkinterface-enableprimaryipv6)" : {{Boolean}},
      "[GroupSet](#cfn-ec2-networkinterface-groupset)" : {{[ String, ... ]}},
      "[InterfaceType](#cfn-ec2-networkinterface-interfacetype)" : {{String}},
      "[Ipv4PrefixCount](#cfn-ec2-networkinterface-ipv4prefixcount)" : {{Integer}},
      "[Ipv4Prefixes](#cfn-ec2-networkinterface-ipv4prefixes)" : {{[ Ipv4PrefixSpecification, ... ]}},
      "[Ipv6AddressCount](#cfn-ec2-networkinterface-ipv6addresscount)" : {{Integer}},
      "[Ipv6Addresses](#cfn-ec2-networkinterface-ipv6addresses)" : {{[ InstanceIpv6Address, ... ]}},
      "[Ipv6PrefixCount](#cfn-ec2-networkinterface-ipv6prefixcount)" : {{Integer}},
      "[Ipv6Prefixes](#cfn-ec2-networkinterface-ipv6prefixes)" : {{[ Ipv6PrefixSpecification, ... ]}},
      "[PrivateIpAddress](#cfn-ec2-networkinterface-privateipaddress)" : {{String}},
      "[PrivateIpAddresses](#cfn-ec2-networkinterface-privateipaddresses)" : {{[ PrivateIpAddressSpecification, ... ]}},
      "[PublicIpDnsHostnameTypeSpecification](#cfn-ec2-networkinterface-publicipdnshostnametypespecification)" : {{String}},
      "[SecondaryPrivateIpAddressCount](#cfn-ec2-networkinterface-secondaryprivateipaddresscount)" : {{Integer}},
      "[SourceDestCheck](#cfn-ec2-networkinterface-sourcedestcheck)" : {{Boolean}},
      "[SubnetId](#cfn-ec2-networkinterface-subnetid)" : {{String}},
      "[Tags](#cfn-ec2-networkinterface-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ec2-networkinterface-syntax.yaml"></a>

```
Type: AWS::EC2::NetworkInterface
Properties:
  [ConnectionTrackingSpecification](#cfn-ec2-networkinterface-connectiontrackingspecification): {{
    ConnectionTrackingSpecification}}
  [Description](#cfn-ec2-networkinterface-description): {{String}}
  [EnablePrimaryIpv6](#cfn-ec2-networkinterface-enableprimaryipv6): {{Boolean}}
  [GroupSet](#cfn-ec2-networkinterface-groupset): {{
    - String}}
  [InterfaceType](#cfn-ec2-networkinterface-interfacetype): {{String}}
  [Ipv4PrefixCount](#cfn-ec2-networkinterface-ipv4prefixcount): {{Integer}}
  [Ipv4Prefixes](#cfn-ec2-networkinterface-ipv4prefixes): {{
    - Ipv4PrefixSpecification}}
  [Ipv6AddressCount](#cfn-ec2-networkinterface-ipv6addresscount): {{Integer}}
  [Ipv6Addresses](#cfn-ec2-networkinterface-ipv6addresses): {{
    - InstanceIpv6Address}}
  [Ipv6PrefixCount](#cfn-ec2-networkinterface-ipv6prefixcount): {{Integer}}
  [Ipv6Prefixes](#cfn-ec2-networkinterface-ipv6prefixes): {{
    - Ipv6PrefixSpecification}}
  [PrivateIpAddress](#cfn-ec2-networkinterface-privateipaddress): {{String}}
  [PrivateIpAddresses](#cfn-ec2-networkinterface-privateipaddresses): {{
    - PrivateIpAddressSpecification}}
  [PublicIpDnsHostnameTypeSpecification](#cfn-ec2-networkinterface-publicipdnshostnametypespecification): {{String}}
  [SecondaryPrivateIpAddressCount](#cfn-ec2-networkinterface-secondaryprivateipaddresscount): {{Integer}}
  [SourceDestCheck](#cfn-ec2-networkinterface-sourcedestcheck): {{Boolean}}
  [SubnetId](#cfn-ec2-networkinterface-subnetid): {{String}}
  [Tags](#cfn-ec2-networkinterface-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ec2-networkinterface-properties"></a>

`ConnectionTrackingSpecification`  <a name="cfn-ec2-networkinterface-connectiontrackingspecification"></a>
A connection tracking specification for the network interface.
*Required*: No
*Type*: [ConnectionTrackingSpecification](aws-properties-ec2-networkinterface-connectiontrackingspecification.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Description`  <a name="cfn-ec2-networkinterface-description"></a>
A description for the network interface.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnablePrimaryIpv6`  <a name="cfn-ec2-networkinterface-enableprimaryipv6"></a>
If you’re modifying a network interface in a dual-stack or IPv6-only subnet, you have the option to assign a primary IPv6 IP address. A primary IPv6 address is an IPv6 GUA address associated with an ENI that you have enabled to use a primary IPv6 address. Use this option if the instance that this ENI will be attached to relies on its IPv6 address not changing. AWS will automatically assign an IPv6 address associated with the ENI attached to your instance to be the primary IPv6 address. Once you enable an IPv6 GUA address to be a primary IPv6, you cannot disable it. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. If you have multiple IPv6 addresses associated with an ENI attached to your instance and you enable a primary IPv6 address, the first IPv6 GUA address associated with the ENI becomes the primary IPv6 address.
*Required*: No
*Type*: Boolean
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`GroupSet`  <a name="cfn-ec2-networkinterface-groupset"></a>
The IDs of the security groups associated with this network interface.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InterfaceType`  <a name="cfn-ec2-networkinterface-interfacetype"></a>
The type of network interface. The default is `interface`. The supported values are `efa` and `trunk`.
*Required*: No
*Type*: String
*Allowed values*: `efa | efa-only | branch | trunk`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ipv4PrefixCount`  <a name="cfn-ec2-networkinterface-ipv4prefixcount"></a>
The number of IPv4 prefixes to be automatically assigned to the network interface.
When creating a network interface, you can't specify a count of IPv4 prefixes if you've specified one of the following: specific IPv4 prefixes, specific private IPv4 addresses, or a count of private IPv4 addresses.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv4Prefixes`  <a name="cfn-ec2-networkinterface-ipv4prefixes"></a>
The IPv4 delegated prefixes that are assigned to the network interface.
When creating a network interface, you can't specify IPv4 prefixes if you've specified one of the following: a count of IPv4 prefixes, specific private IPv4 addresses, or a count of private IPv4 addresses.
*Required*: No
*Type*: Array of [Ipv4PrefixSpecification](aws-properties-ec2-networkinterface-ipv4prefixspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv6AddressCount`  <a name="cfn-ec2-networkinterface-ipv6addresscount"></a>
The number of IPv6 addresses to assign to the network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. To specify specific IPv6 addresses, use the `Ipv6Addresses` property and don't specify this property.
When creating a network interface, you can't specify a count of IPv6 addresses if you've specified one of the following: specific IPv6 addresses, specific IPv6 prefixes, or a count of IPv6 prefixes.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv6Addresses`  <a name="cfn-ec2-networkinterface-ipv6addresses"></a>
The IPv6 addresses from the IPv6 CIDR block range of your subnet to assign to the network interface. If you're specifying a number of IPv6 addresses, use the `Ipv6AddressCount` property and don't specify this property.
When creating a network interface, you can't specify IPv6 addresses if you've specified one of the following: a count of IPv6 addresses, specific IPv6 prefixes, or a count of IPv6 prefixes.
*Required*: No
*Type*: Array of [InstanceIpv6Address](aws-properties-ec2-networkinterface-instanceipv6address.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv6PrefixCount`  <a name="cfn-ec2-networkinterface-ipv6prefixcount"></a>
The number of IPv6 prefixes to be automatically assigned to the network interface.
When creating a network interface, you can't specify a count of IPv6 prefixes if you've specified one of the following: specific IPv6 prefixes, specific IPv6 addresses, or a count of IPv6 addresses.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv6Prefixes`  <a name="cfn-ec2-networkinterface-ipv6prefixes"></a>
The IPv6 delegated prefixes that are assigned to the network interface.
When creating a network interface, you can't specify IPv6 prefixes if you've specified one of the following: a count of IPv6 prefixes, specific IPv6 addresses, or a count of IPv6 addresses.
*Required*: No
*Type*: Array of [Ipv6PrefixSpecification](aws-properties-ec2-networkinterface-ipv6prefixspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateIpAddress`  <a name="cfn-ec2-networkinterface-privateipaddress"></a>
The private IPv4 address to assign to the network interface as the primary private IP address. If you want to specify multiple private IP addresses, use the `PrivateIpAddresses` property.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrivateIpAddresses`  <a name="cfn-ec2-networkinterface-privateipaddresses"></a>
The private IPv4 addresses to assign to the network interface. You can specify a primary private IP address by setting the value of the `Primary` property to `true` in the `PrivateIpAddressSpecification` property. If you want EC2 to automatically assign private IP addresses, use the `SecondaryPrivateIpAddressCount` property and do not specify this property.
When creating a network interface, you can't specify private IPv4 addresses if you've specified one of the following: a count of private IPv4 addresses, specific IPv4 prefixes, or a count of IPv4 prefixes.
*Required*: No
*Type*: Array of [PrivateIpAddressSpecification](aws-properties-ec2-networkinterface-privateipaddressspecification.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`PublicIpDnsHostnameTypeSpecification`  <a name="cfn-ec2-networkinterface-publicipdnshostnametypespecification"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `public-dual-stack-dns-name | public-ipv4-dns-name | public-ipv6-dns-name`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecondaryPrivateIpAddressCount`  <a name="cfn-ec2-networkinterface-secondaryprivateipaddresscount"></a>
The number of secondary private IPv4 addresses to assign to a network interface. When you specify a number of secondary IPv4 addresses, Amazon EC2 selects these IP addresses within the subnet's IPv4 CIDR range. You can't specify this option and specify more than one private IP address using `privateIpAddresses`.
When creating a Network Interface, you can't specify a count of private IPv4 addresses if you've specified one of the following: specific private IPv4 addresses, specific IPv4 prefixes, or a count of IPv4 prefixes.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceDestCheck`  <a name="cfn-ec2-networkinterface-sourcedestcheck"></a>
Enable or disable source/destination checks, which ensure that the instance is either the source or the destination of any traffic that it receives. If the value is `true`, source/destination checks are enabled; otherwise, they are disabled. The default value is `true`. You must disable source/destination checks if the instance runs services such as network address translation, routing, or firewalls.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetId`  <a name="cfn-ec2-networkinterface-subnetid"></a>
The ID of the subnet to associate with the network interface.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-networkinterface-tags"></a>
The tags to apply to the network interface.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-networkinterface-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-networkinterface-return-values"></a>

### Ref
<a name="aws-resource-ec2-networkinterface-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the network interface.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-networkinterface-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-networkinterface-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The ID of the network interface.

`PrimaryIpv6Address`  <a name="PrimaryIpv6Address-fn::getatt"></a>
The primary IPv6 address of the network interface.

`PrimaryPrivateIpAddress`  <a name="PrimaryPrivateIpAddress-fn::getatt"></a>
The primary private IP address of the network interface. For example, `10.0.0.192`.

`SecondaryPrivateIpAddresses`  <a name="SecondaryPrivateIpAddresses-fn::getatt"></a>
The secondary private IP addresses of the network interface. For example, `["10.0.0.161", "10.0.0.162", "10.0.0.163"]`.

`VpcId`  <a name="VpcId-fn::getatt"></a>
The ID of the VPC.

## Examples
<a name="aws-resource-ec2-networkinterface--examples"></a>

**Topics**
+ [Basic network interface](#aws-resource-ec2-networkinterface--examples--Basic_network_interface)
+ [Attach a network interface to an EC2 instance at launch](#aws-resource-ec2-networkinterface--examples--Attach_a_network_interface_to_an_EC2_instance_at_launch)

### Basic network interface
<a name="aws-resource-ec2-networkinterface--examples--Basic_network_interface"></a>

This example creates a standalone elastic network interface (ENI). To learn how to attach this network interface to an instance at launch, see the next example on this page.

#### JSON
<a name="aws-resource-ec2-networkinterface--examples--Basic_network_interface--json"></a>

```
"myENI" : {
   "Type" : "AWS::EC2::NetworkInterface",
   "Properties" : {
      "Tags": [{"Key":"stack","Value":"production"}],
      "Description": "A nice description.",
      "SourceDestCheck": "false",
      "GroupSet": ["sg-75zzz219"],
      "SubnetId": "subnet-3z648z53",
      "PrivateIpAddress": "10.0.0.16"
   }
}
```

#### YAML
<a name="aws-resource-ec2-networkinterface--examples--Basic_network_interface--yaml"></a>

```
   myENI:
      Type: AWS::EC2::NetworkInterface
      Properties:
         Tags:
         - Key: stack
           Value: production
         Description: A nice description.
         SourceDestCheck: 'false'
         GroupSet:
         - sg-75zzz219
         SubnetId: subnet-3z648z53
         PrivateIpAddress: 10.0.0.16
```

### Attach a network interface to an EC2 instance at launch
<a name="aws-resource-ec2-networkinterface--examples--Attach_a_network_interface_to_an_EC2_instance_at_launch"></a>

This example attaches a network interface to an EC2 instance. You can use the NetworkInterface property to add more than one network interface. However, you can specify multiple network interfaces if they all have only private IP addresses (no associated public IP address). If you have a network interface with a public IP address, specify when you launch the instance and then use `AWS::EC2::NetworkInterfaceAttachment` to attach the additional network interfaces.

#### JSON
<a name="aws-resource-ec2-networkinterface--examples--Attach_a_network_interface_to_an_EC2_instance_at_launch--json"></a>

```
"Ec2Instance" : {
   "Type" : "AWS::EC2::Instance",
   "Properties" : {
      "ImageId" : { "Fn::FindInMap" : [ "RegionMap", { "Ref" : "AWS::Region" }, "AMI" ]},
      "KeyName" : { "Ref" : "KeyName" },
      "SecurityGroupIds" : [{ "Ref" : "WebSecurityGroup" }],
      "SubnetId" : { "Ref" : "SubnetId" },
      "NetworkInterfaces" : [ {
         "NetworkInterfaceId" : {"Ref" : "myENI"}, "DeviceIndex" : "1" } ],
      "Tags" : [ {"Key" : "Role", "Value" : "Test Instance"}],
      "UserData" : { "Fn::Base64" : { "Ref" : "WebServerPort" }}
   }
}
```

#### YAML
<a name="aws-resource-ec2-networkinterface--examples--Attach_a_network_interface_to_an_EC2_instance_at_launch--yaml"></a>

```
Ec2Instance:
   Type: AWS::EC2::Instance
   Properties:
      ImageId:
         Fn::FindInMap:
         - RegionMap
         - Ref: AWS::Region
         - AMI
      KeyName:
         Ref: KeyName
      SecurityGroupIds:
      - Ref: WebSecurityGroup
      SubnetId:
         Ref: SubnetId
      NetworkInterfaces:
      - NetworkInterfaceId:
         Ref: myENI
        DeviceIndex: '1'
      Tags:
      - Key: Role
        Value: Test Instance
      UserData:
         Fn::Base64:
            Ref: WebServerPort
```

## See also
<a name="aws-resource-ec2-networkinterface--seealso"></a>
+ [NetworkInterface](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_NetworkInterface.html) in the *Amazon EC2 API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
