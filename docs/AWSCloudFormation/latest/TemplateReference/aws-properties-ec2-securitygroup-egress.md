---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-securitygroup-egress.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SecurityGroup Egress
<a name="aws-properties-ec2-securitygroup-egress"></a>

Adds the specified outbound (egress) rule to a security group.

An outbound rule permits instances to send traffic to the specified IPv4 or IPv6 address range, the IP address ranges that are specified by a prefix list, or the instances that are associated with a destination security group. For more information, see [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html).

You must specify exactly one of the following destinations: an IPv4 address range, an IPv6 address range, a prefix list, or a security group.

You must specify a protocol for each rule (for example, TCP). If the protocol is TCP or UDP, you must also specify a port or port range. If the protocol is ICMP or ICMPv6, you must also specify the ICMP/ICMPv6 type and code.

Rule changes are propagated to instances associated with the security group as quickly as possible. However, a small delay might occur.

## Syntax
<a name="aws-properties-ec2-securitygroup-egress-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-securitygroup-egress-syntax.json"></a>

```
{
  "[CidrIp](#cfn-ec2-securitygroup-egress-cidrip)" : {{String}},
  "[CidrIpv6](#cfn-ec2-securitygroup-egress-cidripv6)" : {{String}},
  "[Description](#cfn-ec2-securitygroup-egress-description)" : {{String}},
  "[DestinationPrefixListId](#cfn-ec2-securitygroup-egress-destinationprefixlistid)" : {{String}},
  "[DestinationSecurityGroupId](#cfn-ec2-securitygroup-egress-destinationsecuritygroupid)" : {{String}},
  "[FromPort](#cfn-ec2-securitygroup-egress-fromport)" : {{Integer}},
  "[IpProtocol](#cfn-ec2-securitygroup-egress-ipprotocol)" : {{String}},
  "[ToPort](#cfn-ec2-securitygroup-egress-toport)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ec2-securitygroup-egress-syntax.yaml"></a>

```
  [CidrIp](#cfn-ec2-securitygroup-egress-cidrip): {{String}}
  [CidrIpv6](#cfn-ec2-securitygroup-egress-cidripv6): {{String}}
  [Description](#cfn-ec2-securitygroup-egress-description): {{String}}
  [DestinationPrefixListId](#cfn-ec2-securitygroup-egress-destinationprefixlistid): {{String}}
  [DestinationSecurityGroupId](#cfn-ec2-securitygroup-egress-destinationsecuritygroupid): {{String}}
  [FromPort](#cfn-ec2-securitygroup-egress-fromport): {{Integer}}
  [IpProtocol](#cfn-ec2-securitygroup-egress-ipprotocol): {{String}}
  [ToPort](#cfn-ec2-securitygroup-egress-toport): {{Integer}}
```

## Properties
<a name="aws-properties-ec2-securitygroup-egress-properties"></a>

`CidrIp`  <a name="cfn-ec2-securitygroup-egress-cidrip"></a>
The IPv4 address range, in CIDR format.
You must specify exactly one of the following: `CidrIp`, `CidrIpv6`, `DestinationPrefixListId`, or `DestinationSecurityGroupId`.
For examples of rules that you can add to security groups for specific access scenarios, see [Security group rules for different use cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html) in the *Amazon EC2 User Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CidrIpv6`  <a name="cfn-ec2-securitygroup-egress-cidripv6"></a>
The IPv6 address range, in CIDR format.
You must specify exactly one of the following: `CidrIp`, `CidrIpv6`, `DestinationPrefixListId`, or `DestinationSecurityGroupId`.
For examples of rules that you can add to security groups for specific access scenarios, see [Security group rules for different use cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html) in the *Amazon EC2 User Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-ec2-securitygroup-egress-description"></a>
A description for the security group rule.
Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and .\_-:/()\#,@[]\+=;{}\!$\*
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationPrefixListId`  <a name="cfn-ec2-securitygroup-egress-destinationprefixlistid"></a>
The prefix list IDs for the destination AWS service. This is the AWS service that you want to access through a VPC endpoint from instances associated with the security group.
You must specify exactly one of the following: `CidrIp`, `CidrIpv6`, `DestinationPrefixListId`, or `DestinationSecurityGroupId`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationSecurityGroupId`  <a name="cfn-ec2-securitygroup-egress-destinationsecuritygroupid"></a>
The ID of the destination VPC security group.
You must specify exactly one of the following: `CidrIp`, `CidrIpv6`, `DestinationPrefixListId`, or `DestinationSecurityGroupId`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FromPort`  <a name="cfn-ec2-securitygroup-egress-fromport"></a>
If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpProtocol`  <a name="cfn-ec2-securitygroup-egress-ipprotocol"></a>
The IP protocol name (`tcp`, `udp`, `icmp`, `icmpv6`) or number (see [Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)).
Use `-1` to specify all protocols. When authorizing security group rules, specifying `-1` or a protocol number other than `tcp`, `udp`, `icmp`, or `icmpv6` allows traffic on all ports, regardless of any port range you specify. For `tcp`, `udp`, and `icmp`, you must specify a port range. For `icmpv6`, the port range is optional; if you omit the port range, traffic for all types and codes is allowed.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ToPort`  <a name="cfn-ec2-securitygroup-egress-toport"></a>
If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes). If the start port is -1 (all ICMP types), then the end port must be -1 (all ICMP codes).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
