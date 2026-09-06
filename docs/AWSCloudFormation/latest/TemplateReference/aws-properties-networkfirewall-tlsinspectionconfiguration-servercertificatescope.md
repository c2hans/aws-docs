---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificatescope.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::TLSInspectionConfiguration ServerCertificateScope
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificatescope"></a>

Settings that define the Secure Sockets Layer/Transport Layer Security (SSL/TLS) traffic that Network Firewall should decrypt for inspection by the stateful rule engine.

## Syntax
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificatescope-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificatescope-syntax.json"></a>

```
{
  "[DestinationPorts](#cfn-networkfirewall-tlsinspectionconfiguration-servercertificatescope-destinationports)" : {{[ PortRange, ... ]}},
  "[Destinations](#cfn-networkfirewall-tlsinspectionconfiguration-servercertificatescope-destinations)" : {{[ Address, ... ]}},
  "[Protocols](#cfn-networkfirewall-tlsinspectionconfiguration-servercertificatescope-protocols)" : {{[ Integer, ... ]}},
  "[SourcePorts](#cfn-networkfirewall-tlsinspectionconfiguration-servercertificatescope-sourceports)" : {{[ PortRange, ... ]}},
  "[Sources](#cfn-networkfirewall-tlsinspectionconfiguration-servercertificatescope-sources)" : {{[ Address, ... ]}}
}
```

### YAML
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificatescope-syntax.yaml"></a>

```
  [DestinationPorts](#cfn-networkfirewall-tlsinspectionconfiguration-servercertificatescope-destinationports): {{
    - PortRange}}
  [Destinations](#cfn-networkfirewall-tlsinspectionconfiguration-servercertificatescope-destinations): {{
    - Address}}
  [Protocols](#cfn-networkfirewall-tlsinspectionconfiguration-servercertificatescope-protocols): {{
    - Integer}}
  [SourcePorts](#cfn-networkfirewall-tlsinspectionconfiguration-servercertificatescope-sourceports): {{
    - PortRange}}
  [Sources](#cfn-networkfirewall-tlsinspectionconfiguration-servercertificatescope-sources): {{
    - Address}}
```

## Properties
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificatescope-properties"></a>

`DestinationPorts`  <a name="cfn-networkfirewall-tlsinspectionconfiguration-servercertificatescope-destinationports"></a>
The destination ports to decrypt for inspection, in Transmission Control Protocol (TCP) format. If not specified, this matches with any destination port.
You can specify individual ports, for example `1994`, and you can specify port ranges, such as `1990:1994`.
*Required*: No
*Type*: Array of [PortRange](aws-properties-networkfirewall-tlsinspectionconfiguration-portrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Destinations`  <a name="cfn-networkfirewall-tlsinspectionconfiguration-servercertificatescope-destinations"></a>
The destination IP addresses and address ranges to decrypt for inspection, in CIDR notation. If not specified, this matches with any destination address.
*Required*: No
*Type*: Array of [Address](aws-properties-networkfirewall-tlsinspectionconfiguration-address.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocols`  <a name="cfn-networkfirewall-tlsinspectionconfiguration-servercertificatescope-protocols"></a>
The protocols to inspect for, specified using the assigned internet protocol number (IANA) for each protocol. If not specified, this matches with any protocol.
Network Firewall currently supports only TCP.
*Required*: No
*Type*: Array of Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourcePorts`  <a name="cfn-networkfirewall-tlsinspectionconfiguration-servercertificatescope-sourceports"></a>
The source ports to decrypt for inspection, in Transmission Control Protocol (TCP) format. If not specified, this matches with any source port.
You can specify individual ports, for example `1994`, and you can specify port ranges, such as `1990:1994`.
*Required*: No
*Type*: Array of [PortRange](aws-properties-networkfirewall-tlsinspectionconfiguration-portrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sources`  <a name="cfn-networkfirewall-tlsinspectionconfiguration-servercertificatescope-sources"></a>
The source IP addresses and address ranges to decrypt for inspection, in CIDR notation. If not specified, this matches with any source address.
*Required*: No
*Type*: Array of [Address](aws-properties-networkfirewall-tlsinspectionconfiguration-address.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
