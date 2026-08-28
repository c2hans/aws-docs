---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/network-attachment.html
---

# Network attachment
<a name="network-attachment"></a>

 Each AWS Outposts rack is configured with redundant top-of-rack switches called Outpost Networking Devices (ONDs). The compute and storage servers in each rack connect to both ONDs. You should connect each OND to a separate switch called a Customer Networking Device (CND) in your data center to provide diverse physical and logical paths for each Outpost rack. ONDs connect to your CNDs with one or more physical connections using fiber optic cables and optical transceivers. The [physical connections](https://docs.aws.amazon.com/outposts/latest/userguide/local-network-connectivity.html#physical-connectivity) are configured in logical [link aggregation group (LAG) links](https://docs.aws.amazon.com/outposts/latest/userguide/local-network-connectivity.html#link-aggregation).

![Diagram showing Multi-rack Outpost with redundant network attachments](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/multi-rack-outpost.png)

 The OND to CND links are always configured in a LAG – even if the physical connection is a single fiber optic cable. Configuring the links as LAG groups allow you to increase the link bandwidth by adding additional physical connections to the logical group. The LAG links are configured as IEEE 802.1q Ethernet trunks to enable segregated networking between the Outpost and the on-premises network.

 Every Outpost has at least two logically segregated networks that need to communicate with or across the customer network:
+  **Service link network** – allocates the service link IP addresses to the Outpost servers and facilitates communication with the on-premises network to allow the servers to connect back to the Outpost anchor points in the Region. When you have multiple rack implementations in a single logical Outposts, you need to assign a Service Link /26 CIDR for each Rack.
+  **Local Gateway network** – enables communication between the VPC subnets on the Outpost and the on-premises network via the Outpost Local Gateway (LGW).

 These segregated networks attach to the on-premises network by a set of [point-to-point IP connections](https://docs.aws.amazon.com/outposts/latest/userguide/local-network-connectivity.html#network-layer-connectivity) over the LAG links. Each OND to CND LAG link is configured with VLAN IDs, point-to-point (/30 or /31) IP subnets, and eBGP peering for each segregated network (service link and LGW). You should consider the LAG links, with their point-to-point VLANs and subnets, as layer-2 segmented, routed layer-3 connections. The routed IP connections provide redundant logical paths that facilitate communication between the segregated networks on the Outpost and the on-premises network.

![Diagram showing service link peering](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/service-link-peering.png)

![Diagram showing Local Gateway peering](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/page-20-local-gateway-peering.png)

 You should terminate the layer-2 LAG links (and their VLANs) on the directly attached CND switches and configure the IP interfaces and BGP peering on the CND switches. You should not bridge the LAG VLANs between your data center switches. For more information, see [Network layer connectivity](https://docs.aws.amazon.com/outposts/latest/userguide/local-network-connectivity.html#network-layer-connectivity) in the *AWS Outposts User Guide*.

 Inside a logical multi-rack Outpost, the ONDs are redundantly interconnected to provide highly available network connectivity between the racks and the workloads running on the servers. AWS is responsible for network availability within the Outpost.

## Recommended practices for highly available network attachment without ACE
<a name="recommended-practices-for-highly-available-network-attachment-no-ace"></a>
+  Connect each Outpost Networking Device (OND) in an Outpost rack to a separate Customer Networking Device (CND) in the data center.
+  Terminate the layer-2 links, VLANs, layer-3 IP subnets, and BGP peering on the directly attached Customer Networking Device (CND) switches. Do not bridge the OND to CND VLANs between the CNDs or across the on-premises network.
+  Add links to the Link Aggregation Groups (LAGs) to increase the available bandwidth between the Outpost and the data center. Do not rely on the aggregate bandwidth of the diverse paths through both ONDs.
+  Use the diverse paths through the redundant ONDs to provide resilient connectivity between the Outpost networks and the on-premises network.
+ To achieve optimal redundancy and allow for non-disruptive OND maintenance, we recommend that customers configure BGP advertisements and policies as follows:
  + Customer network equipment should receive BGP advertisements from Outpost without changing BGP attributes and to enable BGP multipath/load-balancing to achieve optimal inbound traffic flows (from customer towards Outpost). AS-Path prepending is used for Outpost BGP prefixes to shift traffic away from a particular OND/uplink in case maintenance is required. The customer network should prefer routes from Outpost with AS-Path length 1 over routes with AS-Path length 4, that is, react to AS-Path prepending.
  + The customer network should advertise equal BGP prefixes with the same attributes towards all ONDs in Outpost. By default, the Outpost network load balances outbound traffic (towards the customer) between all uplinks. Routing policies are used on the Outpost side to shift traffic away from a particular OND in case maintenance is required. Equal BGP prefixes from the customer side on all ONDs are required to perform this traffic shift, and perform maintenance in a non-disruptive way. When maintenance is required on the customer’s network, we recommend using AS-Path prepending to temporarily shift away traffic from particular uplink or device.

## Recommended practices for highly available network attachment with ACE
<a name="recommended-practices-for-highly-available-network-attachment-with-ace"></a>

For a multi-rack deployment with four or more compute racks, you must use the Aggregation, Core, Edge (ACE) rack, which will act as a network aggregation point to reduce the number of fiber links to your on-premises networking devices. The ACE rack provides the connectivity to the ONDs in each Outposts rack, so AWS will own the VLAN interface allocation and configuration between ONDs and ACE networking devices.

Isolated network layers for Service Link and Local Gateway networks are still required regardless of whether or not an ACE rack is used, which aim to have a VLAN point-to-point (/30 or /31) IP subnets, and eBGP peering configuration for each segregated network. The proposed architectures should follow any of two architectures:

**Topics**
+ [Two customer networking devices](#two-customer-devices)
+ [Four customer networking devices](#four-customer-devices)

### Two customer networking devices
<a name="two-customer-devices"></a>

![Two-customer networking devices](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/page-22-two-customer-networking-devices.png)

+ With this architecture, the customer should have two networking devices (CND) to interconnect the ACE networking devices, providing redundancy.
+ For each physical connections, you must enable a LAG (to increase the available bandwidth between the Outpost and the data center), even if it is a single physical port, and it will carry two network segments, having 2 point-to-point VLANs (/30 or /31), and eBGP configurations between ACEs and CNDs.
+ In a steady state the traffic is load balanced following Equal-cost multipath (ECMP) pattern to/from the customer network from the ACE layer, 25% traffic distribution across the ACE to customer. In order to allow this behavior, the eBGP peering’s between ACEs and CNDs must have BGP multipath/load-balancing enabled, and announced the customer prefixes with the same BGP metric on the 4 eBGP peering connections.
+ To achieve optimal redundancy and allow for non-disruptive OND maintenance, we recommend that customers to follow these recommendations:
  + Customer networking device should advertise equal BGP prefixes with the same attributes towards all ONDs in Outpost.
  + Customer networking device should receive BGP advertisements from Outpost without changing BGP attributes and to enable BGP multipath/load-balancing.

### Four customer networking devices
<a name="four-customer-devices"></a>

![Four-customer network devices](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/page-23-four-customer-networking-devices.png)

With this architecture, the customer will have four networking devices (CND) to interconnect the ACE networking devices, providing redundancy and the same networking logic, including VLANs, eBGP, and ECMP applicable to a 2 CND architecture.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
