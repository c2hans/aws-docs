---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/salesforce-hyperforce-connectivity-dx-megaport/multicloud-vdi.html
---

# Use case: multicloud virtual desktop infrastructure

This use case covers a scenario where you have a virtual desktop infrastructure (VDI) running in another cloud provider that has a private connection to Megaport and is used as an on-ramp to Direct Connect.

Using Megaport MCR with Direct Connect gives your VDI users private connectivity to Salesforce Hyperforce. VDI users use their desktops for their daily work, and the VDI provides an on-ramp to Direct Connect by using a Megaport location.

![Using Megaport MCR with AWS Direct Connect to connect VDI users with Salesforce Hyperforce.](https://docs.aws.amazon.com/prescriptive-guidance/latest/salesforce-hyperforce-connectivity-dx-megaport/images/guide-img/947c8032-55f2-41bc-a4a7-8636d0b73891/images/13d828c0-b06d-4ff8-9f13-6cce750fc601.png)

## Requirements
<a name="multicloud-vdi-req"></a>
+ Users access Salesforce over private network connections.
+ Users use a VDI.
+ The VDI runs in an alternate cloud provider and has a private connection established to Megaport.
+ You own an AWS account to manage the Direct Connect hosted connection with Megaport.

## Configuring Megaport MCR with VXC
<a name="multicloud-vdi-vxc"></a>

For step-by-step instructions, see the following Megaport documentation:
+ [Creating an MCR](https://docs.megaport.com/mcr/creating-mcr/)
+ [Creating MCR Connections to AWS](https://docs.megaport.com/cloud/mcr/aws/)

**Notes**:
+ The BGP prefixes advertised from your router to AWS are configured in the AWS Management Console when you create the public VIF.
+ The prefixes advertised by Direct Connect must not be advertised beyond the network boundaries of your connection. For example, these prefixes must not be included in any public internet routing table. For more information, see [Public virtual interface routing policies](https://docs.aws.amazon.com/directconnect/latest/UserGuide/routing-and-bgp.html#routing-policies) in the Direct Connect documentation.

## Configuring Direct Connect
<a name="multicloud-vdi-dx"></a>

**Accept a hosted connection**

In your AWS account, accept the VXC created previously as a hosted connection. For instructions, see the [Direct Connect documentation](https://docs.aws.amazon.com/directconnect/latest/UserGuide/hosted_connection.html#accept-hosted-connection).

**Create a public VIF**

In your account, provision a public VIF under the connection you accepted from Megaport. Before you create this VIF, you need to obtain the following:
+ The BGP ASN of the MCR.
+ Public IPv4 addresses for peering (typically `/31` CIDR). You can own these or request them from Support. For more information, see *Peer IP addresses* in the section [Prerequisites for virtual interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html#vif-prerequisites) in the Direct Connect documentation.

To create a public VIF, follow the steps in the [Direct Connect documentation](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-vif.html#create-public-vif).

After you create the public VIF, you need to make sure that the BGP authentication key matches both ends of the BGP peer for the peering state to become available.

**Note**
Using a public VIF to connect to AWS from your on-premises or multicloud environment changes the way traffic is routed from AWS public prefixes to your users. We recommend that you use a prefix filter (route map) to make sure that the accepted Amazon prefixes are limited to the Hyperforce infrastructure and any other necessary AWS resources. For more information, see [Public virtual interface prefix advertisement rules](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html#advertise-prefixes) in the Direct Connect documentation.

## Configuring Megaport MCR with SEC
<a name="multicloud-vdi-sec"></a>

For step-by-step instructions, see [Creating MCR Connections to Salesforce Express Connect](https://docs.megaport.com/cloud/mcr/salesforce/) in the Megaport documentation.

## Configure Salesforce Hyperforce
<a name="multicloud-vdi-hyperforce"></a>

To enable inbound connections from your corporate network into Salesforce, you need to configure inbound access to Hyperforce as a security measure. To [allow the required domains](https://help.salesforce.com/s/articleView?id=sf.setup_domains.htm), follow the instructions in [Allow Domains for a Salesforce Console in Salesforce Classic](https://help.salesforce.com/s/articleView?id=sf.console2_allowed_domains.htm) in the Salesforce documentation. Do not use IP addresses.
