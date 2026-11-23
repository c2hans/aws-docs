---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/salesforce-hyperforce-connectivity-dx-megaport/branch-offices.html
---

# Use case: branch offices

This use case covers a scenario where you have a physical router in one Megaport location, and you use it as an on-ramp to Direct Connect. In this scenario, you also have one or more branch offices connected to this location through private circuits.

Using Megaport Port with Direct Connect gives your users who work in branch offices private connectivity to Salesforce Hyperforce. The branch offices consist of a single office or a cluster of offices inter-networked across a metropolitan area network (MAN). The offices on-ramp to Direct Connect by using a Megaport location. The following diagram shows the architecture for this use case.

![Architecture for using Megaport Port with AWS Direct Connect to connect branch offices with Salesforce Hyperforce.](https://docs.aws.amazon.com/prescriptive-guidance/latest/salesforce-hyperforce-connectivity-dx-megaport/images/guide-img/947c8032-55f2-41bc-a4a7-8636d0b73891/images/2adfa31d-2f34-474d-b766-a22907242feb.png)

## Requirements
<a name="branch-offices-req"></a>
+ Your users access Salesforce over private network connections.
+ Your users work primarily from branch offices that have private connectivity to a Megaport-enabled location.
+ You own an AWS account to manage the Direct Connect hosted connection with Megaport.
+ You have a physical router that's deployed at a Megaport location that facilitates a cross connect with Megaport's router.

## Configuring Megaport Port with VXC
<a name="branch-offices-vxc"></a>

The Megaport Port is configured with a VXC and provides the private Layer 2 network segment to AWS. The Direct Connect connection is provisioned as a hosted connection and attached to a public VIF. For step-by-step instructions, see the following Megaport documentation:
+ [Creating a Port](https://docs.megaport.com/connections/creating-port/)
+ [Configuring and Maintaining AWS Hosted Connections](https://docs.megaport.com/cloud/megaport/aws/hosted-connection/)

## Configuring your network devices
<a name="branch-offices-network"></a>

Network devices that are deployed at the Megaport location within your rack are configured to support the connectivity to the Hyperforce instances through Direct Connect. These devices might include a router, switch, firewall, or a combined network stack of multiple devices. The vendor and model types are optional, depending on your requirements. We recommend that you work with your network administrator to configure these devices.

The device that is used to establish the physical cross connect to the Megaport rack must support 802.1Q VLAN tagging to establish Layer 2 adjacency. Layer 3 adjacency is then established between your router and the AWS public VIF by using BGP.

**Notes**:
+ The BGP prefixes advertised from your router to AWS are configured in the AWS Management Console when you create the public VIF.
+ The prefixes advertised by Direct Connect must not be advertised beyond the network boundaries of your connection. For example, these prefixes must not be included in any public internet routing table. For more information, see [Public virtual interface routing policies](https://docs.aws.amazon.com/directconnect/latest/UserGuide/routing-and-bgp.html#routing-policies) in the Direct Connect documentation.

## Configuring Direct Connect
<a name="branch-offices-dx"></a>

**Accept a hosted connection**

In your AWS account, accept the VXC created previously as a hosted connection. For instructions, see the [Direct Connect documentation](https://docs.aws.amazon.com/directconnect/latest/UserGuide/hosted_connection.html#accept-hosted-connection).

**Create a public VIF**

In your account, provision a public VIF under the connection you accepted from Megaport. Before you create this VIF, you need to obtain the following:
+ The BGP ASN of the router that's deployed to the Megaport location.
+ Public IPv4 addresses for peering (typically `/31` CIDR). You can own these or request them from AWS Support. For more information, see *Peer IP addresses* in the section [Prerequisites for virtual interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html#vif-prerequisites) in the Direct Connect documentation.

To create a public VIF, follow the steps in the [Direct Connect documentation](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-vif.html#create-public-vif).

After you create the public VIF, you need to make sure that the BGP authentication key matches both ends of the BGP peer for the peering state to become available.

**Note**
Using a public VIF to connect to AWS from your on-premises environment changes the way traffic is routed from AWS public prefixes to your users. We recommend that you use a prefix filter (route map) to make sure that the accepted Amazon prefixes are limited to the Hyperforce infrastructure and any other necessary AWS resources. For more information, see [Public virtual interface prefix advertisement rules](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html#advertise-prefixes) in the Direct Connect documentation.

## Configuring Megaport Port with SEC
<a name="branch-offices-sec"></a>

You can also provision the Megaport Port with a SEC VXC, which provides the Layer 2 networking elements for the private connection to Salesforce-managed data centers. SEC lets you access Salesforce applications and services directly with a private, dedicated connection. SEC is delivered as a Layer 3 routed service. You access Salesforce services by using public IPs and must run BGP to receive Salesforce routes. Megaport allocates a `/31` public IP range for each Salesforce peering.

**Note**
** **SEC offers a choice between two IP addressing options:
+ Source NAT your LAN traffic to use the `/31` public IP space provided by Megaport.
+ Advertise your own public IP address space to Salesforce. (Salesforce won't accept [RFC1918](https://datatracker.ietf.org/doc/html/rfc1918#section-3) blocks of IP address space.)

For step-by-step instructions, see [Connecting to Salesforce Express Connect](https://docs.megaport.com/cloud/megaport/salesforce/) in the Megaport documentation.

## Configuring Salesforce Hyperforce
<a name="branch-offices-hyperforce"></a>

To enable inbound connections from your corporate network into Salesforce, you need to configure inbound access to Hyperforce as a security measure. To [allow the required domains](https://help.salesforce.com/s/articleView?id=sf.setup_domains.htm), follow the instructions in [Allow Domains for a Salesforce Console in Salesforce Classic](https://help.salesforce.com/s/articleView?id=sf.console2_allowed_domains.htm) in the Salesforce documentation. Do not use IP addresses.
