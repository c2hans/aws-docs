---
source_url: https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-how-it-works.html
---

# How Traffic Mirroring works
<a name="traffic-mirroring-how-it-works"></a>

Traffic Mirroring copies inbound and outbound traffic from the network interfaces that are attached to your instances. You can send the mirrored traffic to the network interface of another instance, a Network Load Balancer that has a UDP listener, or a Gateway Load Balancer that has a UDP listener. The traffic mirror source and the traffic mirror target (monitoring appliance) can be in the same VPC. Or they can be in a different VPCs that are connected through intra-Region VPC peering, a transit gateway, or by a Gateway Load Balancer endpoint to connect to a Gateway Load Balancer in a different VPC.

Consider the following scenario, where you mirror traffic from two sources (Source A and Source B) to a single traffic mirror target (Target D). After you create the traffic mirror session, any traffic that matches the filter rules is encapsulated in a VXLAN header. It is then sent to the target.

![Traffic from source A and source B is mirrored to mirror target D using filter A.](http://docs.aws.amazon.com/vpc/latest/mirroring/images/traffic-mirroring.png)

The following procedures are required:
+ Identify the traffic mirror source (Source A)
+ Identify the traffic mirror source (Source B)
+ Configure the traffic mirror target (Target D)
+ Configure the traffic mirror filter (Filter A)
+ Configure the traffic mirror session for Source A, Filter A, and Target D
+ Configure the traffic mirror session for Source B, Filter A, and Target D

**Topics**
+ [Targets](traffic-mirroring-targets.md)
+ [Filters](traffic-mirroring-filters.md)
+ [Sessions](traffic-mirroring-sessions.md)
+ [Connectivity options](traffic-mirroring-connection.md)
+ [Packet format](traffic-mirroring-packet-formats.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
