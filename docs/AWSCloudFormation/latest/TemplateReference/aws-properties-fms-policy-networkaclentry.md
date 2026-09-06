---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fms-policy-networkaclentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FMS::Policy NetworkAclEntry
<a name="aws-properties-fms-policy-networkaclentry"></a>

Describes a rule in a network ACL.

Each network ACL has a set of numbered ingress rules and a separate set of numbered egress rules. When determining whether a packet should be allowed in or out of a subnet associated with the network ACL, AWS processes the entries in the network ACL according to the rule numbers, in ascending order.

When you manage an individual network ACL, you explicitly specify the rule numbers. When you specify the network ACL rules in a Firewall Manager policy, you provide the rules to run first, in the order that you want them to run, and the rules to run last, in the order that you want them to run. Firewall Manager assigns the rule numbers for you when you save the network ACL policy specification.

## Syntax
<a name="aws-properties-fms-policy-networkaclentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fms-policy-networkaclentry-syntax.json"></a>

```
{
  "[CidrBlock](#cfn-fms-policy-networkaclentry-cidrblock)" : {{String}},
  "[Egress](#cfn-fms-policy-networkaclentry-egress)" : {{Boolean}},
  "[IcmpTypeCode](#cfn-fms-policy-networkaclentry-icmptypecode)" : {{IcmpTypeCode}},
  "[Ipv6CidrBlock](#cfn-fms-policy-networkaclentry-ipv6cidrblock)" : {{String}},
  "[PortRange](#cfn-fms-policy-networkaclentry-portrange)" : {{PortRange}},
  "[Protocol](#cfn-fms-policy-networkaclentry-protocol)" : {{String}},
  "[RuleAction](#cfn-fms-policy-networkaclentry-ruleaction)" : {{String}}
}
```

### YAML
<a name="aws-properties-fms-policy-networkaclentry-syntax.yaml"></a>

```
  [CidrBlock](#cfn-fms-policy-networkaclentry-cidrblock): {{String}}
  [Egress](#cfn-fms-policy-networkaclentry-egress): {{Boolean}}
  [IcmpTypeCode](#cfn-fms-policy-networkaclentry-icmptypecode): {{
    IcmpTypeCode}}
  [Ipv6CidrBlock](#cfn-fms-policy-networkaclentry-ipv6cidrblock): {{String}}
  [PortRange](#cfn-fms-policy-networkaclentry-portrange): {{
    PortRange}}
  [Protocol](#cfn-fms-policy-networkaclentry-protocol): {{String}}
  [RuleAction](#cfn-fms-policy-networkaclentry-ruleaction): {{String}}
```

## Properties
<a name="aws-properties-fms-policy-networkaclentry-properties"></a>

`CidrBlock`  <a name="cfn-fms-policy-networkaclentry-cidrblock"></a>
The IPv4 network range to allow or deny, in CIDR notation.
*Required*: No
*Type*: String
*Pattern*: `^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(\/([0-9]|[1-2][0-9]|3[0-2]))$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Egress`  <a name="cfn-fms-policy-networkaclentry-egress"></a>
Indicates whether the rule is an egress, or outbound, rule (applied to traffic leaving the subnet). If it's not an egress rule, then it's an ingress, or inbound, rule.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IcmpTypeCode`  <a name="cfn-fms-policy-networkaclentry-icmptypecode"></a>
ICMP protocol: The ICMP type and code.
*Required*: No
*Type*: [IcmpTypeCode](aws-properties-fms-policy-icmptypecode.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv6CidrBlock`  <a name="cfn-fms-policy-networkaclentry-ipv6cidrblock"></a>
The IPv6 network range to allow or deny, in CIDR notation.
*Required*: No
*Type*: String
*Pattern*: `^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))(/(1[0-2]|[0-9]))?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PortRange`  <a name="cfn-fms-policy-networkaclentry-portrange"></a>
TCP or UDP protocols: The range of ports the rule applies to.
*Required*: No
*Type*: [PortRange](aws-properties-fms-policy-portrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-fms-policy-networkaclentry-protocol"></a>
The protocol number. A value of "-1" means all protocols.
*Required*: Yes
*Type*: String
*Pattern*: `^(tcp|udp|icmp|-1|([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleAction`  <a name="cfn-fms-policy-networkaclentry-ruleaction"></a>
Indicates whether to allow or deny the traffic that matches the rule.
*Required*: Yes
*Type*: String
*Allowed values*: `allow | deny`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
