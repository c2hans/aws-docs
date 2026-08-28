---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-rulegroup-matchattributes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::RuleGroup MatchAttributes
<a name="aws-properties-networkfirewall-rulegroup-matchattributes"></a>

Criteria for Network Firewall to use to inspect an individual packet in stateless rule inspection. Each match attributes set can include one or more items such as IP address, CIDR range, port number, protocol, and TCP flags.

## Syntax
<a name="aws-properties-networkfirewall-rulegroup-matchattributes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-rulegroup-matchattributes-syntax.json"></a>

```
{
  "[DestinationPorts](#cfn-networkfirewall-rulegroup-matchattributes-destinationports)" : {{[ PortRange, ... ]}},
  "[Destinations](#cfn-networkfirewall-rulegroup-matchattributes-destinations)" : {{[ Address, ... ]}},
  "[Protocols](#cfn-networkfirewall-rulegroup-matchattributes-protocols)" : {{[ Integer, ... ]}},
  "[SourcePorts](#cfn-networkfirewall-rulegroup-matchattributes-sourceports)" : {{[ PortRange, ... ]}},
  "[Sources](#cfn-networkfirewall-rulegroup-matchattributes-sources)" : {{[ Address, ... ]}},
  "[TCPFlags](#cfn-networkfirewall-rulegroup-matchattributes-tcpflags)" : {{[ TCPFlagField, ... ]}}
}
```

### YAML
<a name="aws-properties-networkfirewall-rulegroup-matchattributes-syntax.yaml"></a>

```
  [DestinationPorts](#cfn-networkfirewall-rulegroup-matchattributes-destinationports): {{
    - PortRange}}
  [Destinations](#cfn-networkfirewall-rulegroup-matchattributes-destinations): {{
    - Address}}
  [Protocols](#cfn-networkfirewall-rulegroup-matchattributes-protocols): {{
    - Integer}}
  [SourcePorts](#cfn-networkfirewall-rulegroup-matchattributes-sourceports): {{
    - PortRange}}
  [Sources](#cfn-networkfirewall-rulegroup-matchattributes-sources): {{
    - Address}}
  [TCPFlags](#cfn-networkfirewall-rulegroup-matchattributes-tcpflags): {{
    - TCPFlagField}}
```

## Properties
<a name="aws-properties-networkfirewall-rulegroup-matchattributes-properties"></a>

`DestinationPorts`  <a name="cfn-networkfirewall-rulegroup-matchattributes-destinationports"></a>
The destination port to inspect for. You can specify an individual port, for example `1994` and you can specify a port range, for example `1990:1994`. To match with any port, specify `ANY`.
This setting is only used for protocols 6 (TCP) and 17 (UDP).
*Required*: No
*Type*: Array of [PortRange](aws-properties-networkfirewall-rulegroup-portrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Destinations`  <a name="cfn-networkfirewall-rulegroup-matchattributes-destinations"></a>
The destination IP addresses and address ranges to inspect for, in CIDR notation. If not specified, this matches with any destination address.
*Required*: No
*Type*: Array of [Address](aws-properties-networkfirewall-rulegroup-address.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocols`  <a name="cfn-networkfirewall-rulegroup-matchattributes-protocols"></a>
The protocols to inspect for, specified using the assigned internet protocol number (IANA) for each protocol. If not specified, this matches with any protocol.
*Required*: No
*Type*: Array of Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourcePorts`  <a name="cfn-networkfirewall-rulegroup-matchattributes-sourceports"></a>
The source port to inspect for. You can specify an individual port, for example `1994` and you can specify a port range, for example `1990:1994`. To match with any port, specify `ANY`.
 If not specified, this matches with any source port.
This setting is only used for protocols 6 (TCP) and 17 (UDP).
*Required*: No
*Type*: Array of [PortRange](aws-properties-networkfirewall-rulegroup-portrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sources`  <a name="cfn-networkfirewall-rulegroup-matchattributes-sources"></a>
The source IP addresses and address ranges to inspect for, in CIDR notation. If not specified, this matches with any source address.
*Required*: No
*Type*: Array of [Address](aws-properties-networkfirewall-rulegroup-address.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TCPFlags`  <a name="cfn-networkfirewall-rulegroup-matchattributes-tcpflags"></a>
The TCP flags and masks to inspect for. If not specified, this matches with any settings. This setting is only used for protocol 6 (TCP).
*Required*: No
*Type*: Array of [TCPFlagField](aws-properties-networkfirewall-rulegroup-tcpflagfield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
