---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/salesforce-hyperforce-connectivity-dx-megaport/vpn-workforce.html
---

# Use case: VPN-connected workforce

This use case covers a scenario where you use a virtual VPN concentrator at a Megaport location as an on-ramp to Direct Connect. In this scenario, you have remote branch offices or workers with site-to-site VPNs that connect to the VPN concentrator.

Using Megaport MVE with a third-party virtual firewall and Direct Connect gives your remote workers private connectivity to Salesforce Hyperforce. The remote workers connect to the VPN concentrator from an internet-connected router at a branch office or from a VPN client that is running on their device. The remote workers then on-ramp to Direct Connect by using a Megaport location.

![Using Megaport MVE with a firewall and AWS Direct Connect to connect to Salesforce Hyperforce.](https://docs.aws.amazon.com/prescriptive-guidance/latest/salesforce-hyperforce-connectivity-dx-megaport/images/guide-img/947c8032-55f2-41bc-a4a7-8636d0b73891/images/8e486ec9-0894-4550-86c5-198481845099.png)

## Requirements
<a name="vpn-workforce-req"></a>
+ Your remote workers access Salesforce over private network connections.
+ Your remote workers or users at branch offices have site-to-site VPN connectivity to a Megaport-enabled location over the internet.
+ You own an AWS account to manage the Direct Connect hosted connection with Megaport.

## Configuring Megaport MVE with VXC
<a name="vpn-workforce-vxc"></a>

The Megaport MVE that's configured with a VXC provides the private Layer 2 network segment to AWS. The MVE is a virtual solution and doesn't require a Port. However, you must specify the third-party virtual network appliance to be deployed. The VXC deployment process and functionality are the same, whether you use a Port, MVE, or MCR. Direct Connect should be provisioned as a hosted connection and attached to a public VIF.

For an overview and step-by-step instructions, see the following Megaport documentation:
+ [Introducing MVE](https://docs.megaport.com/mve/)
+ [Configuring and Maintaining AWS Hosted Connections](https://docs.megaport.com/cloud/megaport/aws/hosted-connection/)

## Configuring VNF applicances
<a name="vpn-workforce-vnf"></a>

MVE supports third-party virtual network function (VNF) appliances from vendors such as Aruba, Cisco, Fortinet, Palo Alto Networks, Versa Networks, and VMware. You can choose a vendor to handle routing, security, and the SSL VPN functions of the MVE. For a full list of MVE integration partners, see the [Megaport documentation](https://docs.megaport.com/mve/#sd-wan-and-next-generation-firewall-partners).

For example, this use case describes a high-level architecture where Megaport MVE supports VPN/SD-WAN connections from regional branch offices and remote users who have an SSL VPN connection. This MVE peers with AWS and routes these connections privately to Hyperforce through Direct Connect.

The key elements of this architecture include:
+ Route filters to limit AWS prefixes for relevant Hyperforce instances
+ SSL VPN policies based on Hyperforce fully qualified domain name (FQDN) and IP address ranges
+ NAT policy for Hyperforce users behind a single public IP address that faces AWS

## Configuring route filters
<a name="vpn-workforce-filters"></a>

When the VNF has established BGP peering with the AWS public VIF, the route table should populate with prefixes for all AWS public services and Hyperforce. You can apply route filtering by using IP lists or BGP community tags. We recommend that you configure a route map of prefixes that include a range of Hyperforce instances in an AWS Region.

**Notes**:
+ The BGP prefixes advertised from your router to AWS are configured in the AWS Management Console when you create the public VIF.
+ The prefixes advertised by Direct Connect must not be advertised beyond the network boundaries of your connection. For example, these prefixes must not be included in any public internet routing table. For more information, see [Public virtual interface routing policies](https://docs.aws.amazon.com/directconnect/latest/UserGuide/routing-and-bgp.html#routing-policies) in the Direct Connect documentation.

## Configuring Direct Connect
<a name="vpn-workforce-dx"></a>

**Accept a hosted connection**

In your AWS account, accept the VXC created previously as a hosted connection. For instructions, see the [Direct Connect documentation](https://docs.aws.amazon.com/directconnect/latest/UserGuide/hosted_connection.html#accept-hosted-connection).

**Create a public VIF**

In your account, provision a public VIF under the connection you accepted from Megaport. Before you create this VIF, you need to obtain the following:
+ The BGP ASN of the VNF appliance.
+ Public IPv4 addresses for peering (typically `/31` CIDR). You can own these or request them from Support. For more information, see *Peer IP addresses* in the section [Prerequisites for virtual interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html#vif-prerequisites) in the Direct Connect documentation.

To create a public VIF, follow the steps in the [Direct Connect documentation](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-vif.html#create-public-vif).

After you create the public VIF, you need to make sure that the BGP authentication key matches both ends of the BGP peer for the peering state to become available.

**Note**
** **Using a public VIF to connect to AWS from your on-premises environment changes the way traffic is routed to your on-premises location from AWS. We recommend that you use a prefix filter (route map) to make sure that the accepted Amazon prefixes are limited to the Hyperforce infrastructure and any other necessary AWS resources. For more information, see [Public virtual interface prefix advertisement rules](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html#advertise-prefixes) in the Direct Connect documentation.

## Configuring Megaport MVE with SEC
<a name="vpn-workforce-sec"></a>

In some cases, Hyperforce login requests are redirected to Salesforce-managed data centers. To keep this traffic on a private network, you can add a Megaport VXC to Salesforce by using SEC. You can configure your VNF security policies with rules by using the Salesforce login FQDN. This is similar to the Direct Connect architecture described earlier in this guide.

For step-by-step instructions, see [Connecting to Salesforce Express Connect](https://docs.megaport.com/cloud/megaport/salesforce/) in the Megaport documentation.

## Configuring Salesforce Hyperforce
<a name="vpn-workforce-hyperforce"></a>

To enable inbound connections from your corporate network into Salesforce, you need to configure inbound access to Hyperforce as a security measure. To [allow the required domains](https://help.salesforce.com/s/articleView?id=sf.setup_domains.htm), follow the instructions in [Allow Domains for a Salesforce Console in Salesforce Classic](https://help.salesforce.com/s/articleView?id=sf.console2_allowed_domains.htm) in the Salesforce documentation. Do not use IP addresses.
