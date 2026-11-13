---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-firewallpolicy-address.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::FirewallPolicy Address
<a name="aws-properties-networkfirewall-firewallpolicy-address"></a>

A single IP address or CIDR block. Resolved IP validation uses this to define its source IP ranges and its bypass destination IP ranges.

## Syntax
<a name="aws-properties-networkfirewall-firewallpolicy-address-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-firewallpolicy-address-syntax.json"></a>

```
{
  "[AddressDefinition](#cfn-networkfirewall-firewallpolicy-address-addressdefinition)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkfirewall-firewallpolicy-address-syntax.yaml"></a>

```
  [AddressDefinition](#cfn-networkfirewall-firewallpolicy-address-addressdefinition): {{String}}
```

## Properties
<a name="aws-properties-networkfirewall-firewallpolicy-address-properties"></a>

`AddressDefinition`  <a name="cfn-networkfirewall-firewallpolicy-address-addressdefinition"></a>
Specify an IP address or a block of IP addresses in Classless Inter-Domain Routing (CIDR) notation. Network Firewall supports all address ranges for IPv4 and IPv6.
Examples:
+ To configure Network Firewall to inspect for the IP address 192.0.2.44, specify `192.0.2.44/32`.
+ To configure Network Firewall to inspect for IP addresses from 192.0.2.0 to 192.0.2.255, specify `192.0.2.0/24`.
+ To configure Network Firewall to inspect for the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify `1111:0000:0000:0000:0000:0000:0000:0111/128`.
+ To configure Network Firewall to inspect for IP addresses from 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify `1111:0000:0000:0000:0000:0000:0000:0000/64`.
For more information about CIDR notation, see the Wikipedia entry [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).
*Required*: Yes
*Type*: String
*Pattern*: `^([a-fA-F\d:\.]+/\d{1,3})$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
