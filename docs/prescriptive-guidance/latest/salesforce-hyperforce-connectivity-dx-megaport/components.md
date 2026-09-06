---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/salesforce-hyperforce-connectivity-dx-megaport/components.html
---

# Solution components
<a name="components"></a>

Direct Connect requires you to either create your own [dedicated connection](https://docs.aws.amazon.com/directconnect/latest/UserGuide/dedicated_connection.html) to AWS, or work with an Direct Connect Partner to create a [hosted connection](https://docs.aws.amazon.com/directconnect/latest/UserGuide/hosted_connection.html). This article provides guidance for using Megaport as an Direct Connect Partner to facilitate hybrid and multiple use cases for connecting to Salesforce Hyperforce.

## Direct Connect
<a name="direct-connect"></a>

Direct Connect establishes a private, dedicated network connection between on-premises data centers and AWS. This direct link helps organizations bypass the public internet and provides reliable and private communication with AWS resources.

Although Hyperforce runs on AWS infrastructure, using Direct Connect to access it requires you to manage an AWS account for billing and configuration of the connection. Using Direct Connect to connect to the Salesforce-managed Hyperforce AWS account isn't supported.

### Hosted connection
<a name="hosted-connection.8d203b15-a69a-5d7d-9ffb-cbcbd4105545"></a>

A [hosted connection](https://docs.aws.amazon.com/directconnect/latest/UserGuide/hosted_connection.html) is a physical Ethernet connection that an Direct Connect Partner provisions on behalf of a user. The use cases and architectures covered in this guide use a hosted connection with the Direct Connect Partner, Megaport. Hosted connections offer bandwidth ranges between 50 Mbps to 25 Gbps in multiple increments, whereas dedicated connections are provided in 1 Gbps, 10 Gbps, and 100 Gbps capacities. For more information about Direct Connect bandwidth and costs, see [Direct Connect pricing](https://aws.amazon.com/directconnect/pricing/).

### Public virtual interface
<a name="public-virtual-interface.977ed762-8794-512e-86dd-f9eb1088df99"></a>

The Hyperforce architecture requires access to the public IP address space of AWS resources from on-premises and multicloud locations. A public virtual interface (VIF) is used to connect your remote location to public AWS services and public IPs deployed on AWS. Using a private VIF to access Hyperforce is not supported.

**Notes:**
+ Using a public VIF requires the use of unique public IPv4 addresses. You will need to provide your own IPv4 CIDR or request a `/31` CIDR from [AWS Support](https://aws.amazon.com/support/createCase). For more information, see the [prerequisites for virtual interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html#vif-prerequisites) in the Direct Connect documentation.
+ Using a public VIF to connect to AWS from your on-premises or multicloud environment changes the way traffic is routed from AWS public prefixes to your users. We recommend that you use a prefix filter (route map) to make sure that the accepted Amazon prefixes are limited to the Hyperforce infrastructure and any other necessary AWS resources. For more information, review [public virtual interface prefix advertisement rules](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html#advertise-prefixes) in the Direct Connect documentation.
+ The prefixes that are advertised by Direct Connect must not be advertised beyond the network boundaries of your connection. For example, these prefixes must not be included in any public internet routing table. For information, review [public virtual interface routing policies](https://docs.aws.amazon.com/directconnect/latest/UserGuide/routing-and-bgp.html#routing-policies) in the Direct Connect documentation.

## Salesforce
<a name="salesforce"></a>

Salesforce is a customer relationship management (CRM) platform that's designed to help you sell, service, market, analyze, and connect with your customers.

### Hyperforce
<a name="hyperforce.43531f6b-0b5f-5fff-abb4-3c8d626146d5"></a>

[Salesforce Hyperforce](https://help.salesforce.com/s/articleView?id=000388902&type=1) is a next-generation Salesforce infrastructure architecture that's built for the public cloud. It provides enhanced scalability, flexibility, and agility by using the AWS infrastructure. It is the fastest and simplest way to run Salesforce on public cloud infrastructure.

### Salesforce Express Connect (SEC)
<a name="salesforce-express-connect--sec-.d01e76be-f768-59f6-ae03-06bab2fba12e"></a>

[Salesforce Express Connect (SEC)](https://www.salesforce.com/campaign/salesforce-express-connect/) enables private, reliable connectivity from users to Salesforce-operated data centers. Ensuring private connectivity to Hyperforce currently requires a SEC connection in conjunction with Direct Connect.

**Notes:**
+ A limited number of Salesforce services still run in Salesforce-managed infrastructure. To maintain connectivity to all services in Salesforce-managed infrastructure and Hyperforce, users who require private network access to Salesforce must continue to run SEC along with Direct Connect.
+ Salesforce and AWS do not sell SEC. If you require private network connectivity to Salesforce-managed infrastructure, you will need a SEC connection. This article covers establishing a new [SEC connection to Salesforce by using Megaport](https://docs.megaport.com/cloud/megaport/salesforce/).
+ SEC is not used for any data migration between Salesforce-managed infrastructure and Hyperforce. If you are migrating to Hyperforce, Salesforce facilitates data migrations in your organization on a private backbone. SEC is necessary for ongoing, private connectivity to Salesforce by users.

## Megaport
<a name="megaport"></a>

[Megaport](https://www.megaport.com/) simplifies and accelerates hybrid cloud connectivity to AWS Regions in a scalable, private, and on-demand manner. Megaport acts as a facilitator in this connectivity ecosystem, and offers SDN solutions to simplify and optimize the process of connecting to cloud services, including the AWS Cloud. Megaport connections are called *virtual cross connects (VXCs)*, which are Layer 2 Ethernet circuits that provide private, flexible, and on-demand connectivity between any of the locations on the Megaport network. To access the Megaport network, you must first create a Port, Megaport Virtual Edge (MVE), or Megaport Cloud Router (MCR), which are covered in the next sections.

### Megaport Port
<a name="megaport-port.617ae270-1f82-5f17-8e0c-8ed917a49636"></a>

[Megaport Port](https://docs.megaport.com/connections/creating-port/) is a high-speed Ethernet interface that creates a network-to-network interface (NNI) between your network and the Megaport network. It is configured as an 802.1Q virtual local area network (VLAN) trunk to support up to 100 VXCs, each presented as a unique VLAN. The Port provisioning process enables the Megaport interface and generates a Letter of Authorization (LOA) with instructions for the data center operator to establish the physical cross connect from your equipment to the new Port.

**Note**
Your network device requires either 10 or 100 Gbps interfaces with 10GBASE-LR (duplex on single-mode optical fiber [SMOF]) or 100G-LR4 (duplex on SMOF) optical transceivers.

### Megaport Virtual Edge (MVE)
<a name="megaport-virtual-edge--mve-.e5b6a6a8-f721-524c-a4bb-13ac34ff74bf"></a>

[Megaport Virtual Edge (MVE)](https://docs.megaport.com/mve/) is a network functions virtualization (NFV) platform that provides virtual infrastructure for network services at the edge of Megaport's global SDN.  You can use MVE to deploy a virtual network stack (or point of presence) without any physical data center presence or hardware.  MVE is available in 27 metro regions across the globe and is aligned closely with Direct Connect peering locations (NNIs).  MVE supports third-party VNF appliances from vendors such as Aruba, Cisco, Fortinet, Palo Alto Networks, Versa Networks, and VMware.

**Note**
Megaport doesn't sell third-party licenses and requires that you use a Bring Your Own License (BYOL) model.

### Megaport Cloud Router (MCR)
<a name="megaport-cloud-router--mcr-.bfffbb20-e079-56af-95fc-28802782cd0d"></a>

[Megaport Cloud Router (MCR)](https://docs.megaport.com/mcr/) is a managed virtual router service that enables direct Layer 2 and Layer 3 networking between endpoints on the Megaport network, including other cloud providers. The MCR can be deployed as a standalone service to route traffic between different cloud environments without requiring you to have a physical presence in that data center. It can also be connected to your Port to route pertinent traffic back to a physical location. The MCR is managed through the Megaport Portal to configure both static and dynamic Border Gateway Protocol (BGP) routing functions, including Bidirectional Forwarding Detection (BFD), Multi-Exit Discriminator (MED), Autonomous System Number (ASN), and NAT. For more information, see [Configuring BGP Advanced Settings](https://docs.megaport.com/mcr/mcr-bgp-advanced/) in the Megaport documentation.
