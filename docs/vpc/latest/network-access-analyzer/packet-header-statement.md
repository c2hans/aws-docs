---
source_url: https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/packet-header-statement.html
---

# Packet header statements in Network Access Analyzer
<a name="packet-header-statement"></a>

A packet header statement defines the traffic types for a match or exclude condition. If you omit the packet header statement, all traffic types match. All fields are optional, but if you use a packet header statement, you must use at least one of its fields.

You can specify the following fields:
+ `Protocols` – The protocol strings to match. The possible values are `tcp` and `udp`. You can specify one of the values or both of the values. If you omit this field, packets with either the `tcp` or `udp` protocol are admitted.
+ `SourceAddress` – The IP addresses or CIDR ranges. You can't specify this option with `SourcePrefixLists`. If specified, only packets with matching source addresses are admitted. If you don't specify `SourcePrefixLists` or `SourceAddresses`, packets with any source address are admitted.
+ `SourcePrefixLists` – The IDs or ARNs of the prefix lists. You can't specify this option with `SourceAddresses`. If specified, only packets with matching source addresses are admitted. If you don't specify `SourcePrefixLists` or `SourceAddresses`, packets with any source address are admitted.
+ `DestinationAddress` – The IP addresses or CIDR ranges. This option is mutually exclusive with `DestinationPrefixLists`. If specified, only packets with matching destination addresses are admitted. If you don't specify `DestinationPrefixLists` or `DestinationAddress`, packets with any destination address are admitted.
+ `DestinationPrefixLists` – The IDs or ARNs of the prefix lists. This option is mutually exclusive with `DestinationAddress`. If specified, only packets with matching destination addresses are admitted. If you don't specify `DestinationPrefixLists` or `DestinationAddress`, packets with any destination address are admitted.
+ `SourcePorts` – The ports or port ranges. If specified, only packets with source ports that match one of the ports or port ranges are admitted. If omitted, packets with any source port are admitted.
+  `DestinationPorts` – The ports or port ranges. If specified, only packets with destination ports that match one of the ports or ranges are admitted. If omitted, packets with any destination port are admitted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Virtual Private Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
