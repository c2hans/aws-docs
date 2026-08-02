---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupegress.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SecurityGroupEgress
<a name="aws-resource-ec2-securitygroupegress"></a>

Adds the specified outbound (egress) rule to a security group.

An outbound rule permits instances to send traffic to the specified IPv4 or IPv6 address range, the IP addresses that are specified by a prefix list, or the instances that are associated with a destination security group. For more information, see [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html).

You must specify exactly one of the following destinations: an IPv4 address range, an IPv6 address range, a prefix list, or a security group.

You must specify a protocol for each rule (for example, TCP). If the protocol is TCP or UDP, you must also specify a port or port range. If the protocol is ICMP or ICMPv6, you must also specify the ICMP/ICMPv6 type and code. To specify all types or all codes, use -1.

Rule changes are propagated to instances associated with the security group as quickly as possible. However, a small delay might occur.

## Syntax
<a name="aws-resource-ec2-securitygroupegress-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-securitygroupegress-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::SecurityGroupEgress",
  "Properties" : {
      "[CidrIp](#cfn-ec2-securitygroupegress-cidrip)" : {{String}},
      "[CidrIpv6](#cfn-ec2-securitygroupegress-cidripv6)" : {{String}},
      "[Description](#cfn-ec2-securitygroupegress-description)" : {{String}},
      "[DestinationPrefixListId](#cfn-ec2-securitygroupegress-destinationprefixlistid)" : {{String}},
      "[DestinationSecurityGroupId](#cfn-ec2-securitygroupegress-destinationsecuritygroupid)" : {{String}},
      "[FromPort](#cfn-ec2-securitygroupegress-fromport)" : {{Integer}},
      "[GroupId](#cfn-ec2-securitygroupegress-groupid)" : {{String}},
      "[IpProtocol](#cfn-ec2-securitygroupegress-ipprotocol)" : {{String}},
      "[ToPort](#cfn-ec2-securitygroupegress-toport)" : {{Integer}}
    }
}
```

### YAML
<a name="aws-resource-ec2-securitygroupegress-syntax.yaml"></a>

```
Type: AWS::EC2::SecurityGroupEgress
Properties:
  [CidrIp](#cfn-ec2-securitygroupegress-cidrip): {{String}}
  [CidrIpv6](#cfn-ec2-securitygroupegress-cidripv6): {{String}}
  [Description](#cfn-ec2-securitygroupegress-description): {{String}}
  [DestinationPrefixListId](#cfn-ec2-securitygroupegress-destinationprefixlistid): {{String}}
  [DestinationSecurityGroupId](#cfn-ec2-securitygroupegress-destinationsecuritygroupid): {{String}}
  [FromPort](#cfn-ec2-securitygroupegress-fromport): {{Integer}}
  [GroupId](#cfn-ec2-securitygroupegress-groupid): {{String}}
  [IpProtocol](#cfn-ec2-securitygroupegress-ipprotocol): {{String}}
  [ToPort](#cfn-ec2-securitygroupegress-toport): {{Integer}}
```

## Properties
<a name="aws-resource-ec2-securitygroupegress-properties"></a>

`CidrIp`  <a name="cfn-ec2-securitygroupegress-cidrip"></a>
The IPv4 address range, in CIDR format.
You must specify exactly one of the following: `CidrIp`, `CidrIpv6`, `DestinationPrefixListId`, or `DestinationSecurityGroupId`.
For examples of rules that you can add to security groups for specific access scenarios, see [Security group rules for different use cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html) in the *Amazon EC2 User Guide*.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CidrIpv6`  <a name="cfn-ec2-securitygroupegress-cidripv6"></a>
The IPv6 address range, in CIDR format.
You must specify exactly one of the following: `CidrIp`, `CidrIpv6`, `DestinationPrefixListId`, or `DestinationSecurityGroupId`.
For examples of rules that you can add to security groups for specific access scenarios, see [Security group rules for different use cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html) in the *Amazon EC2 User Guide*.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-ec2-securitygroupegress-description"></a>
The description of an egress (outbound) security group rule.
Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and .\_-:/()\#,@[]\+=;{}\!$\*
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationPrefixListId`  <a name="cfn-ec2-securitygroupegress-destinationprefixlistid"></a>
The prefix list IDs for an AWS service. This is the AWS service to access through a VPC endpoint from instances associated with the security group.
You must specify exactly one of the following: `CidrIp`, `CidrIpv6`, `DestinationPrefixListId`, or `DestinationSecurityGroupId`.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DestinationSecurityGroupId`  <a name="cfn-ec2-securitygroupegress-destinationsecuritygroupid"></a>
The ID of the security group.
You must specify exactly one of the following: `CidrIp`, `CidrIpv6`, `DestinationPrefixListId`, or `DestinationSecurityGroupId`.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FromPort`  <a name="cfn-ec2-securitygroupegress-fromport"></a>
If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GroupId`  <a name="cfn-ec2-securitygroupegress-groupid"></a>
The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IpProtocol`  <a name="cfn-ec2-securitygroupegress-ipprotocol"></a>
The IP protocol name (`tcp`, `udp`, `icmp`, `icmpv6`) or number (see [Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)).
Use `-1` to specify all protocols. When authorizing security group rules, specifying `-1` or a protocol number other than `tcp`, `udp`, `icmp`, or `icmpv6` allows traffic on all ports, regardless of any port range you specify. For `tcp`, `udp`, and `icmp`, you must specify a port range. For `icmpv6`, the port range is optional; if you omit the port range, traffic for all types and codes is allowed.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ToPort`  <a name="cfn-ec2-securitygroupegress-toport"></a>
If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes). If the start port is -1 (all ICMP types), then the end port must be -1 (all ICMP codes).
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-securitygroupegress-return-values"></a>

### Ref
<a name="aws-resource-ec2-securitygroupegress-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the security egress rule.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-ec2-securitygroupegress--examples"></a>

### VPC security groups with egress and ingress rules
<a name="aws-resource-ec2-securitygroupegress--examples--VPC_security_groups_with_egress_and_ingress_rules"></a>

In some cases, you might have an originating (source) security group to which you want to add an outbound rule that allows traffic to a destination (target) security group. The target security group also needs an inbound rule that allows traffic from the source security group. Note that you cannot use the `Ref` function to specify the outbound and inbound rules for each security group. Doing so creates a circular dependency; you cannot have two resources that depend on each other. Instead, use the egress and ingress resources to declare these outbound and inbound rules, as shown in the following template example.

#### JSON
<a name="aws-resource-ec2-securitygroupegress--examples--VPC_security_groups_with_egress_and_ingress_rules--json"></a>

```
"SourceSG": {
   "Type": "AWS::EC2::SecurityGroup",
   "Properties": {
      "VpcId" : "vpc-1a2b3c4d",
      "GroupDescription": "Sample source security group"
   }
},
"TargetSG": {
   "Type": "AWS::EC2::SecurityGroup",
   "Properties": {
      "VpcId" : "vpc-1a2b3c4d",
      "GroupDescription": "Sample target security group"
   }
},
"OutboundRule": {
   "Type": "AWS::EC2::SecurityGroupEgress",
   "Properties":{
      "IpProtocol": "tcp",
      "FromPort": 0,
      "ToPort": 65535,
      "DestinationSecurityGroupId": {
         "Fn::GetAtt": [
            "TargetSG",
            "GroupId"
         ]
      },
      "GroupId": {
         "Fn::GetAtt": [
            "SourceSG",
            "GroupId"
         ]
      }
   }
},
"InboundRule": {
   "Type": "AWS::EC2::SecurityGroupIngress",
   "Properties":{
      "IpProtocol": "tcp",
      "FromPort": 0,
      "ToPort": 65535,
      "SourceSecurityGroupId": {
         "Fn::GetAtt": [
            "SourceSG",
            "GroupId"
         ]
      },
      "GroupId": {
         "Fn::GetAtt": [
            "TargetSG",
            "GroupId"
         ]
      }
   }
}
```

#### YAML
<a name="aws-resource-ec2-securitygroupegress--examples--VPC_security_groups_with_egress_and_ingress_rules--yaml"></a>

```
SourceSG:
  Type: AWS::EC2::SecurityGroup
  Properties:
    VpcId: vpc-1a2b3c4d
    GroupDescription: Sample source security group
TargetSG:
  Type: AWS::EC2::SecurityGroup
  Properties:
    VpcId: vpc-1a2b3c4d
    GroupDescription: Sample target security group
OutboundRule:
  Type: AWS::EC2::SecurityGroupEgress
  Properties:
    IpProtocol: tcp
    FromPort: 0
    ToPort: 65535
    DestinationSecurityGroupId:
      Fn::GetAtt:
        - TargetSG
        - GroupId
    GroupId:
      Fn::GetAtt:
        - SourceSG
        - GroupId
InboundRule:
  Type: AWS::EC2::SecurityGroupIngress
  Properties:
    IpProtocol: tcp
    FromPort: 0
    ToPort: 65535
    SourceSecurityGroupId:
      Fn::GetAtt:
        - SourceSG
        - GroupId
    GroupId:
      Fn::GetAtt:
        - TargetSG
        - GroupId
```
