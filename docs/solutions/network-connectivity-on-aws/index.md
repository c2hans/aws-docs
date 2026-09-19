---
source_url: https://docs.aws.amazon.com/solutions/network-connectivity-on-aws/index.html
---

---
title: 'Guidance for Network Connectivity on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/network-connectivity-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Network Connectivity on AWS

## Overview

The Network Connectivity capability enables you to construct secure, scalable, and highly available networks for your applications and workloads with constant high performance and extensive global coverage. This expertise will also assist your team in learning about cost-effective methods for managing a growing infrastructure and hybrid connection between two infrastructures.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/network-connectivity-on-aws.pdf)

![Architecture diagram](/images/solutions/network-connectivity-on-aws/images/network-connectivity-on-aws-1.png)

1. **Step 1**: (CF11-S3) Create a network AWS account in your environment to manage your network resources and delegate Amazon VPC IP Address Manager (IPAM) and AWS Network Manager to this account.
1. **Step 2**: (CF11-S3) Establish a central networking hub in your AWS account. AWS Cloud WAN provides a central dashboard for making connections between your branch offices, data centers, and Amazon Virtual Private Clouds (Amazon VPCs).
1. **Step 3**: (CF11-S2) Manage your hosted zones across your organization and networks leveraging Amazon IPAM, and configure your internal and external DNS using Amazon Route 53 hosted zones.
1. **Step 4**: (CF11-S2) Deploy your network attachments for Cloud WAN or AWS Transit Gateway, and connect the network back to your network account. Additionally, design the ingress traffic and cross account for each of your member accounts in the organization
1. **Step 5**: (CF11-S4) Establish connectivity outside of your environment through transit gateways or direct connect to your network account.
## Implementation resources

### Connectivity within the cloud

Connectivity within the cloud

- Establish private connectivity to services
- Implement a strategy to connect multiple environments

As you create virtual networks in your cloud environment, you need to establish connectivity between the different workloads and their components. These connections within the cloud can be consumed in a service model, where you grant access between the workloads to connect and retrieve or send data. On the cloud, your workloads can have private or public IP addresses, allowing connectivity between them.

As you begin the construction of your cloud environment, distinct workloads will be hosted on separate networks and may connect through the Internet. Nevertheless, as your environment expands and develops, you may structure your network so that unnecessary traffic never leaves your cloud environment. If you are working with Partners or Software as a Service (SaaS) providers, you can establish a private connection with them so that traffic never leaves your cloud environment.

There are several ways to build network connections to ensure the security of network traffic inside your environment. You can make VPN connections across multiple networks or services, connect the various networks and access points using the route tables of your network while leveraging the backbone network of your cloud provider, or establish a physical connection between two sites.

Keeping the traffic within your cloud environment helps decrease data transfer expenses across networks when communicating with a partner, a Software as a Service (SaaS) provider, or to your data centers, as the traffic does not leave your network and internet access is not required. In addition, adopting a private connection might improve your network's security, dependability, and latency because you are not sharing bandwidth with the internet.

To enhance discoverability of your workloads, services, and any prospective partner product you are consuming, you must plan and construct your internal and external Domain Name System (DNS) setups for private and public access.

Establish private connectivity to services

It is possible to utilize AWS services without leaving your AWS environment, which reduces the cost of data transmission for your workloads and protects your data and assets, since they do not need to travel over the internet. We recommend that you utilize [AWS PrivateLink](/vpc/latest/privatelink/what-is-privatelink.html) to create endpoints to the services you would access using private IP addresses. Visit to AWS Services that Integrate with [AWS PrivateLink](/vpc/latest/privatelink/what-is-privatelink.html) for a list of all compatible services.

Depending on the sort of traffic you transmit and how it is dispersed, you can build several types of VPC endpoints on your VPC:

- Interface
- Gateway
- Gateway LoadBalancer

Learn more about the different types of endpoints in the [PrivateLink documentation](/vpc/latest/privatelink/concepts.html#concepts-vpc-endpoints) .

Virtual Private Clouds (VPCs) are designed to be highly available. Consider [creating subnets](/vpc/latest/userguide/working-with-subnets.html#create-subnets) in more than one availability zone when designing your VPCs.

To learn more about how to secure your VPC, the usage of resource policies with VPC endpoints, how to use Security Groups, and how to use Network ACLs, review the [service documentation](/vpc/latest/userguide/what-is-amazon-vpc.html) .

For additional information related to VPC security, refer to Security and Filtering in the [Amazon VPC FAQ](https://aws.amazon.com/vpc/faqs/) .

Implement a strategy to connect multiple environments

When creating an environment on AWS, we recommend using multiple AWS accounts to establish separated environments to confine your resources. This makes it easier to maintain control over your workloads and resources.

When you employ several accounts, you must guarantee that connection exists between these resources so that they may communicate with one another over your network.

We recommend you set up a network AWS account to host your networking resources, and simplify the operation and management of your network across your AWS environment. Refer to the Cloud Foundations [Workload Isolation Boundary](https://docs.aws.amazon.com/solutions/workload-isolation-on-aws/) capability to create a network account.

As you establish your environment, we recommend you start with an [AWS Managed VPN](/whitepapers/latest/aws-vpc-connectivity-options/aws-managed-vpn-1.html) , which allows you to securely connect to your Amazon VPC from your remote network over the internet in a secure manner. One of the most common use cases is to set up a [Software VPN to AWS Managed VPN](/whitepapers/latest/aws-vpc-connectivity-options/software-vpn-to-aws-managed-vpn.html) , which allows you to connect your remote network VPN to your AWS environment.

If you utilize AWS Cloud Wide Area Networking (WAN) or AWS Transit Gateway, keep in mind that VPC CIDRs across linked networks must not have overlapping IP addresses to avoid IP collision across VPCs.

If you have multiple workloads and need to establish a way to centrally control your internal traffic for your organization, we recommend you use the Network Account to link the different Virtual Private Clouds (VPCs) across your environment to a centralized location using [AWS Cloud WAN](https://aws.amazon.com/cloud-wan/) , and then [share the core network](/vpc/latest/cloudwan/cloudwan-share-network.html) with your organization using [AWS Resource Access Manager (RAM)](/ram/) . Use a different AWS Transit Gateway for your production environments, so you can ensure the performance of each network can be measured separately.

Once you've shared the central AWS Cloud WAN with the business, establish attachments on the various accounts that will be connected to the global network. AWS Cloud WAN provides bandwidth of up to 50Gbps. On the network account, you may also activate VPC Flow Logs and publish them to [CloudWatch Logs](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-vpc-flow-logs-for-aws-transit-gateway/) so they can be saved in the AWS account log group, allowing you to analyze traffic and monitor network performance.

You may also centrally configure different security services.

### IP address and multiple network management

IP address and multiple network management

- Design IP address scheme
- Assign non-overlapping IP CIDRs
- Use your publicly routable IP address range from your on-premises network in the cloud

IP addresses are used by your workloads to interact with one another, within your cloud environment, or in hybrid settings with resources outside of your cloud environment. When you plan the many steps to install and run your workloads, IP address management is a critical component for you to manage your network.

You face the danger of overlapping CIDRs and IP address depletion if you don't plan how your IP address space will be assigned, which can lead to network or service disruptions. Having a strategy for how CIDR space will be distributed aids in the development of your fundamental environment, which includes support routing rules and route optimization.

CIDRs

For private communication, you allocate Classless Inter Domain Routing (CIDR) ranges to your LAN in traditional on-premises networking. Similarly, while configuring networks in your cloud environment, you must use non-overlapping CIDR ranges. Non-overlapping IP spaces enable you to create efficient routing, which improves network performance while avoiding intermittent connectivity difficulties and communication failures. In some circumstances, overlapping IP ranges cannot be avoided, thus network paths or translation devices must be designed to guarantee that communication between these networks functions as planned.

We propose that you choose a continuous CIDR range for geographic areas, places, or even services when building your network CIDR range. You may define or categorize your CIDRs by grouping them, allowing administrators to simply find and establish routes.

IP address utilization

An essential part of network planning and architecture is minimizing the possibility of IP address depletion.

IP depletion occurs when the number of IP addresses required in a particular network exceeds the number of IP addresses available. Because of the flexibility provided by the cloud, this is a significant concern in cloud setups. Your workloads use additional IP addresses in the given network as they grow up and down.

Scaling will fail if there are no IPs available in your network, putting your service at danger. Ensure that the IP range is broad enough to support both networking and non-networking resources in your cloud environment while designing. Planning should take into account the size of the CIDR for current and future needs.

Virtual networks

Based on your operational needs, virtual networks enable you to isolate resources from one another.

Using virtual networks allows your team to build a rigorous network border between resources, ensuring network isolation and mitigating the danger of resources in one virtual network accessing resources in another. Developers, for example, can use distinct networks to design and develop resources that are segregated from production workloads.

Developers' issues or dangerous behavior in one virtual network have no effect on network resources in another virtual network. At this stage, evaluate short- and long-term projects that may influence network topology types, like organizational mergers, big data center transfers, and adoption of new suppliers or technologies. Network administrators and executives must be prepared to construct virtual networks, reorganize subnetworks, and make changes to routing, switching, and physical layer networking in order to establish communication throughout their network.

IPv4 space is running out, posing problems for IT and networking departments all around the world. One of the most significant advances in networking technology has been the invention of IPv6. It not only solves the looming issue of IPv4 exhaustion, but it also simplifies routing and provides a nearly limitless pool of addresses, making mobile networks and Internet of Things (IoT) devices simple to build and configure. IPv4 networks present the problems and complications associated with creating an IP schema for a private network. With limited IPv4 space, one important design problem is determining how much space to provide to a specific application depending on its requirements. Using IPv4 spaces often leads to the following design constraints:

1. Network architectures are designed too small, which requires you to expand the size of the network by adding new CIDR blocks to the network.
2. Network architectures are designed too large, which requires customers to accept overlapping IP, causing connectivity issues, and impacting the performance of the network.

IPv6 uses 128 bits instead of the IPv4 32 bits, which essentially eliminates any size considerations, allowing you to create unique IP addresses, to almost eliminate the overlapping concerns.

Network configuration and management

The network is the foundation of any IT infrastructure. Whether it's post-deployment operational concerns or debugging, you'll frequently need to make modifications to specific network components, which will result in changes to the entire topology. These changes include updates to route tables, the assignment of new private and public IP addresses, and troubleshooting (connectivity, packet loss, throughput, bandwidth consumption, or latency issues) inside and beyond the resources of each team and your business. When any of these scenarios occurs, a robust network architecture lowers the need for large modifications to your network topology.

Design IP address scheme

Whether you bring your own IP addresses into your AWS environment or employ AWS IP addresses, developing a system for how your IP addresses are used inside your network will help you to avoid IP exhaustion and guarantee your network's performance matches your demand expectations.

We recommend separation between publicly routable IPv4 and IPv6 workloads from internally routed subnets. For IPv4 CIDRs, we recommend using IP address ranges in your subnet that allow you to deploy as many resources as you need. Some CIDR rages commonly used are /24, /22, and /20, as defined in [RFC 1918](http://www.faqs.org/rfcs/rfc1918.html) . For IPv6 CIDRs, by default /56 CIDR is assigned by AWS.

Please note that VPC CIDRs across connected networks must not have overlapping IP addresses. When you plan for your IP Address Management (IPAM) strategy, the Amazon IPAM service can help you keep track and automate the different CIDRs across your connected environments.

When designing your network environment, consider which networks will be publicly available and which will be kept private. This will have an impact on your IP allocation method as well as the architecture of your route tables for each of your subnets. Plan the amount of IP addresses that each of your subnets will utilize, and design the subnets with [subnet sizing limits](/vpc/latest/userguide/configure-subnets.html#subnet-sizing) in mind, to ensure you have enough IP addresses accessible inside each subnet. When you are using a public subnet, ensure that there is an Internet Gateway (IGW) attached to your subnet, to allow traffic from the internet to reach your workloads.

Private resources, like backend, APIs, or databases should be kept in private subnets, ensuring they are not accessible from the internet. Within these subnets, [configure the route tables](/vpc/latest/userguide/VPC_Route_Tables.html#route-table-routes) to ensure the resources in each subnet have access to the resources they need to, and do not provide access from other subnet or resources that should not have access to specific resources directly.

To allow access to the internet or other VPCs directly from private subnets, configure [AWS NAT Gateways](/vpc/latest/userguide/vpc-nat-gateway.html) in each VPC in which you deploy private subnets. When using multiple Availability Zones, deploy your AWS NAT gateways in at least two Availability Zones to provide redundancy across available zones.

Automating the assignment of non-overlapping IP CIDRs

For managing your IP addresses centrally, we recommend you delegate the administration of [Amazon VPC IP Address Manager](/organizations/latest/userguide/services-that-can-integrate-ipam.html) (IPAM) to your Network account in your Infrastructure OU.

[Amazon VPC IPAM](/vpc/latest/ipam/what-it-is-ipam.html) helps you maintain a unified view of IP assignments throughout your organization and easily organize IP addresses based on your routing and security needs, and set simple business rules to govern IP assignments.

When you use IPAM, you can automate IP address assignment to VPCs, which reduces the time it takes to allocate IP addresses to a new VPC for a new workload and reduces the risks of assigning overlapping IP CIDRs.

[Configure alerts using Amazon CloudWatch](/vpc/latest/ipam/cloudwatch-ipam.html) to proactively resolve any conflicting IP address issues to monitor visibility throughout your network. When transitioning to AWS, you must understand your workloads' and services' requirements for consumable Hybrid models. AWS networking simplifies connectivity options for your current on-premises networks, data centers, offices, satellite locations, and event internet.

Use your publicly routable IP address range from your on-premises network in the cloud

**Bring your own IP (BYOIP):** BYOIP allows you to migrate a portion or the complete range of publicly routable IPv4 or IPv6 addresses from your on-premises network to your AWS account. AWS advertises BYOIP CIDRs on the internet by default. When you bring the address range to AWS, it shows as an address pool in your account. These IP addresses can be assigned to AWS resources in your account, such as EC2 instances, Elastic Network Interfaces (ENI), NAT Gateways, and AWS Network Load Balancers (NLB).

With BYOIPv6, you can control whether IPv6 CIDRs are advertised externally by AWS or not. BYOIPv6 addresses work the same as Amazon-provided IPv6 addresses. They can be assigned to EC2 instances, and Elastic Network Interfaces and subnets in your VPC. To avoid using the same IPv6 subnets for internal and external connectivity, you can provision the BYOIP IPv6 address range that is not publicly advertised as a secondary IPv6 CIDR for the same VPC. For publicly advertised IPv6 CIDRs, /48 is the most specific address range that you can bring. CIDR blocks of /56 can be used when not advertised publicly. Each address range can be brought into to one Region at a time.

### Centralized or distributed network configuration and management

Centralized or distributed network configuration and management

- Centralize network management
- Route application traffic for cloud and on-premises workloads through inspection gateway/firewall

Centralized or distributed network configuration and management

You must choose between dispersed and centralized networking components for your organization when you develop your network. Starting with smaller networks, on-premises locations, and cloud provider networks can assist decrease difficult point-to-point communication. However, as the network expands and the number of nodes increases, so does the complexity of network administration, bringing scalability difficulties. Hub and spoke network topologies have benefits over point-to-point communication lines.

Centralized networks (hub and spoke networks) enable you to audit all of your traffic in a single location, govern entrance and egress traffic from your environment, and simplify connection administration.

Hub and spoke networks provide greater scalability for additional linkages and centralized management over speak locations. You may use these tools to centrally regulate access to public and private networks, restrict user access to resources through LAN and WIFI networks, control the installation and deletion of routing components, and ease the changing of your network's logical divisions (VLAN, VRFs, and so on).

Automating network infrastructure

In cloud environments, network engineers not only setup networks, but also work with orchestration technologies that use Infrastructure as Code (IaC) to create network infrastructure at scale. This reduces deployment time, reduces human error when setting repeating patterns, and simplifies lift and shift for your present network architecture if it has to be reproduced in a different environment.

IP address management (IPAM) systems can govern and automate IP address management. IPAM solutions aid in the enhancement of dynamic IP address assignments, the addition/deletion of new and existing CIDRs, and automated delivery and record management. Automation for network management reduces delays in onboarding new apps or expanding existing applications by allowing you to assign IP addresses to network resources. IPAM systems may also automatically track key IP address information, such as its assignment attributes, network location, and routing and security domain. Reducing the need to manually track or conduct bookkeeping for your IP addresses, as well as the likelihood of mistakes during IP assignment.

Traffic inspection

Consult with your networking and security teams about traffic inspection requirements in hybrid settings, and identify application traffic that needs to be examined. Any traffic leaving your cloud infrastructure and egressing to the public internet is typically subject to attack. To avoid this risk, every traffic generated by a key workload inside your network should be routed via an inspection device. While designing your network topology, your security and engineering teams should work with your networking team to determine the level of granularity of the inspection based on the traffic to be reviewed. Some examples include traffic direction (east-west, north-south), protocols, and origin and destination. These inspections must fulfill your policy's compliance and forensic standards. Furthermore, to avoid a single point of failure, we propose that you construct high availability (HA) inspection equipment.

Centralize network management

There are two types of network strategies to consider when developing your network strategy: centralized networks and dispersed networks. Although dispersed network architectures (also known as "Full Mesh" or point-to-point networks) allow you to implement infrastructure improvements as the network grows, they frequently present scalability concerns. As a result, we propose that you adopt a centralized approach (also known as a hub and spoke network) to grow, safeguard your network, and set controls throughout your environment.

To centrally manage your AWS VPC network, it is important to create an account that will be used for central network resources and management of the network. Reference the Cloud Foundations Workload Isolation Boundary capability to create a Network account.

**Option 1 - Managed Networking:**[AWS Cloud WAN](https://aws.amazon.com/cloud-wan/) links your Amazon Virtual Private Clouds (VPCs) and on-premises networks via a single hub. This simplifies your network and eliminates complicated peering arrangements. It functions as a cloud router, making each new connection just once. As you grow worldwide, inter-Region peering joins Amazon VPCs over the [AWS global network](https://aws.amazon.com/about-aws/global-infrastructure/) . Your data is automatically encrypted and never goes over the public internet.

[Create a global network](/vpc/latest/cloudwan/create-global-network.html) in your Network account in each Region that you want to connect to your centralized hub. This enables centralized management by network engineers who manage the Network services account. Use [AWS Resource Access Manager (RAM)](/ram/) to share a your [AWS Cloud WAN network attachments](/vpc/latest/cloudwan/cloudwan-create-attachment.html) instance for connecting VPCs across multiple accounts in your AWS Organization within the same Region. AWS RAM enables you to easily and securely share AWS resources with any AWS account, or within your AWS Organization.

**Option 2 - Custom Network Build:** If you use AWS Transit Gateway to build your network, we recommend that you utilize infrastructure as code (IaC) to deploy AWS Transit Gateways regularly, and that you use IaC to automatically establish the link from newly generated VPCs and subnets back to your central AWS Transit Gateway. To handle the deployment and configuration of your transit gateway throughout your environment, you may utilize an automated solution such as [Serverless Network Orchestrator on AWS](https://aws.amazon.com/solutions/implementations/serverless-transit-network-orchestrator/) .

To enhance your security, you can use AWS Network Firewall to inspect and filter outbound traffic, by integrating the service with your NAT Gateway. You can review how to build a high available AWS Network Firewall, with the route table design considerations using NAT gateway with AWS Network Firewall for centralized egress.

**Note:** AWS Network Firewall does not perform network address translation for you. This function is handled by the NAT gateway after traffic inspection through the AWS Network Firewall. Ingress routing is not required in this case, as return traffic is forwarded to the NATGW IPs by default.

### Hybrid connectivity

Hybrid connectivity

- Establish connectivity between on-premises and cloud
- Access compute resources (such as host operating systems)
- Setup redundant, highly available, and fault tolerant connection(s)

As customers build their cloud environment, it is common to have workloads on-premises and across different cloud providers. You might have connectivity requirements that you need to satisfy, so your workloads can communicate across different networks and environments.

The easiest way to connect different environments is over the public internet. However, the public internet is a shared network. This can impact your performance, and the traffic is not encrypted at the network layer. Communications between critical and production workloads should happen via dedicated secure network configurations. We recommend that you limit over-the-internet communications to test or development environments.

If you need to access resources in your cloud environment using the internet, we recommend you create a bastion host within your environment. Using a bastion host allows you to access all other cloud resources privately which increases the security of the resources you don’t need to expose on the internet. You can monitor access to your cloud environment and resources through this host.

The needs of your Business Units (BUs) often drive long and short-term connectivity initiatives. We recommend you work with your central IT team, security team, and the different workload owners to understand bandwidth, throughput, and compliance requirements. As you build your network Secure Sockets Layer (SSL), VPNs are great options for service connectivity and user-to-endpoint models. SSL or similar VPN clients can be installed on individual users’ systems/servers/laptops to secure connectivity between your cloud environment and your on-premises and individual user devices. VPN or a direct dedicated connectivity links between on-premises and cloud environment are some of the popular options chosen by customers. Both of these options typically require layer 2 and layer 3 connectivity between your data center/office and cloud provider’s network. With a VPN, you are encrypting traffic between two endpoints and traffic flows over private IP inside VPN tunnels. With physical links, traffic traverse over dedicated lease lines so you get dedicated bandwidth and predictable network performance compared to VPN.

To configure routing for your networks, you can select between static or dynamic routing. Static routing requires to the manual configuration of routes for source and destination on both ends. Dynamic (BGP or OSPF) routing allows you to propagate routes across your network automatically. For most network option configurations, we recommend a dynamic routing solution for scalability and adaptability.

[Edge connectivity](https://aws.amazon.com/products/networking/edge-networking/) is gradually becoming preferred option for applications with global user base. Content Delivery Networks (CDNs) and similar edge networking solutions employ edge locations distributed worldwide. This enables application traffic access through one of the nodes that is closer to the final user, reducing significantly the usage of the Internet Service Provider (ISP) network. These solutions are used to improve the end customer experience by enhancing performance of the network and workloads.

Regardless of the type of connectivity options you choose between your on-premises environment and your cloud environments, ensure **high availability** and **redundancy** for your communication channel. Routing maintenance, upgrades, other unexpected network, electrical incidences, and natural events can disrupt your primary connection. In these scenarios, a secondary (or failover) connection might be required to avoid outages.

When [establishing connectivity](/whitepapers/latest/hybrid-connectivity/connectivity-models.html) from a remote network to an Amazon VPC network, there are different options to consider. Depending on your bandwidth, cost, latency, and resilience requirements between your on-premises environment and AWS cloud environment, you may decide to go with a virtual connection ( [Amazon Managed VPN](/whitepapers/latest/aws-vpc-connectivity-options/aws-managed-vpn.html) or [Software Site-to-Site VPN](/whitepapers/latest/aws-vpc-connectivity-options/software-site-to-site-vpn.html) ), a dedicated network link ( [AWS Direct Connect](/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect.html) ), or a combination of both. Refer to the [Network-to-Amazon VPC](/whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.html) connectivity options table and the following bandwidth table to determine what type of connection(s) is the best option to connection your network to your Amazon VPC network.

Network-to-Amazon VPC bandwidth table:

|  |  |
| --- | --- |
| AWS Service | Bandwidth |
| Internet Gateway | NA |
| NAT Gateway | By default, supports 5 Gbps of bandwidth and automatically scales up to 100 Gbps |
| Transit Gateway | Up to 50 Gbps for maximum bandwidth per VPC attachment, AWS Direct Connect gateway, or peered transit gateway connection |
| PrivateLink | 10 Gbps per ENI. Burst Capacity of 40Gbps |
| Interface Endpoints | 10 Gbps per ENI. Burst Capacity of 40Gbps |
| Gateway Endpoint | NA |
| Direct Connect | Up to 100Gbps with dedicated connections. |
| Site to Site VPN | 1.25Gbps per IPsec tunnel on Virtual Private Gateway (VGW). Transit Gateway (TGW) VPN with equal cost multi-path (ECMP) can yield higher throughputs. |
| Client VPN | The throughput depends on multiple factors, such as the capacity of your connection from your location, and the network latency between your Client VPN desktop application on your computer and the VPC endpoint. |
| AWS Cloud WAN | Up to 50 Gbps for maximum bandwidth per VPC attachment, or peered transit gateway connection |

Access host operating systems

Once network connectivity has been established, we recommend that you set up security measures to access your resources in your environment, and that those resources can access any data hosted on your remote networks if you have any.

**Bastion hosts** If you need to access resources in your cloud environment using the internet, we recommend you create a bastion box within your environment. From the bastion box, you can access all other cloud resources privately. In this scenario, make sure the bastion box is secured and monitored, architected for high availability, and there is no single point of failure as you will use it to ingress into your cloud environment.

[Bastion hosts](https://aws.amazon.com/quickstart/architecture/linux-bastion/) are compute resources hosted on a public network which you can connect to remotely to access resources in your environment. To avoid managing SSH keys on these environments, we recommend you use [AWS Systems Manager Session Manager](/systems-manager/latest/userguide/session-manager.html) (SSM) Session Manager. Session Manager allows you to access a web-based terminal session from the AWS Management console. It gives the ability for your team access the host without need of creating inbound network access; SSM requires only outbound connection to the AWS SSM endpoint to allow access. The remote connection for SSM Session Manager is instantiated by the SSM agent, which is an application installed locally on the operating system.

If you are using an AWS-supplied EC2 image, then the SSM agent is already installed by default. To add the SSM agent to an EC2 instance that does not have it provided by default, refer to [Working with SSM Agent](/systems-manager/latest/userguide/ssm-agent.html) .

To get started with AWS SSM, follow the latest AWS documented steps for [Setting Up Session Manager](/systems-manager/latest/userguide/session-manager-getting-started.html) . In the documentation, you will find steps to complete all prerequisites, create IAM roles for Session Manager, and allow user access. Session Manager can be extended to limit user actions on the EC2 hosts, as well as to create reverse-tunnels for local SSH or RDP access that does not require any additional network inbound traffic.

AWS Systems Manager Session Manager is an important service for access your operating environment while still supporting a Zero-Trust network architecture.

Setup redundant, highly available, and fault tolerant connection(s)

When designing systems to connect to your AWS environment, you need to consider fault tolerance. To allow access to the internet or other VPCs directly from private subnets, configure AWS NAT Gateways in each VPC in which you deploy private subnets. We recommend you use multiple Availability Zones for your VPC deployment. Within the VPC, deploy redundant [AWS NAT Gateways](/vpc/latest/userguide/vpc-nat-gateway.html) operating out of at least two Availability Zones to provide resiliency to your network. Through deploying multiple NAT Gateways, your private network traffic can continue to function even if it loses an entire Availability Zone.

Each AWS Site-to-Site VPN connection has two tunnels, with each tunnel using a unique public IP address. It is important to configure both tunnels for redundancy. When one tunnel becomes unavailable (for example, down for maintenance), network traffic is automatically routed to the available tunnel for that specific Site-to-Site VPN connection. If using more than one Direct Connect connection, you will benefit from using the [Resiliency Toolkit](/directconnect/latest/UserGuide/resiliency_toolkit.html) for High or Maximum resiliency models.

If you are using bastion hosts, we recommend you establish a highly available, fault tolerant connection using multiple Bastion hosts across multiple Availability Zones or multiple Regions if you use a centralized or mesh network. You can use this [Quick Start to set up a highly available bastion host system](https://aws.amazon.com/quickstart/architecture/linux-bastion/) .

### Network monitoring and logging

Network monitoring and logging

- Enable network logging to view IP level traffic entering and leaving your network
- Monitor and analyze network logs and metrics
- Set up network monitoring dashboards to view metrics, historic logs, and network performance statistics

Observability in your network is critical to maintaining optimal performance and mitigating risks. Network logs contain information such as IP addresses, ports, protocols, and the kind of traffic being sent through your infrastructure that allows you to understand how your network is operating. Network logs, including application traffic for payload inspection, can be used to identify and perform corrective actions when unauthorized or malicious traffic is discovered. Network logs can also be used to troubleshoot network issues including connectivity and performance. Centralizing the network logs for analysis will help you reduce the complexity of a solution that works across all the devices generating traffic and logs in your network. Another benefit of centralizing these logs is the ease of use of a solution that can analyze traffic to identify patterns monitoring your network, and to perform proactive and reactive remediation actions.

During peak traffic and load for your workloads, your underlying infrastructure needs to be resilient and deliver the expected performance for your users. We recommend that you collect performance metrics of your infrastructure. This can help you identify whether the network is optimized correctly, and adjust as needed to enhance its performance. In cloud environments, all these metrics can be pushed to the same monitoring dashboard. You are basically monitoring your entire network and performance from single location. These dashboards can also implement alerts and implement different automations based on the data collected when unusual activity is detected. This helps IT teams reduce the time to remediate events identified in your network, and avoid issues with your workloads.

Although network constructs are unique, you should pair network monitoring with the full breadth of your observability implementation, including specifying network metrics captured in [Amazon CloudWatch](/cloudwatch/) . This is where customers can get started with monitoring and alerting based on telemetry data.

Automate the monitoring of your AWS networks and identify where network access to your environments may be misconfigured by implementing tools such as [VPC Reachability Analyzer](/vpc/latest/reachability/what-is-reachability-analyzer.html) and [Amazon Inspector Network Reachability](/inspector/latest/userguide/inspector_network-reachability.html) .

Enable network logging to view IP-level traffic entering and leaving your network

You can create a flow log for a VPC, a subnet, or a network interface. If you create a flow log for a subnet or VPC, each network interface in that subnet or VPC is monitored.

Enable [Amazon VPC Flow Logs](/vpc/latest/userguide/flow-logs.html) to capture information about the IP traffic going to and from network interfaces in your VPC. When you need to perform content inspection, threat monitoring, or troubleshooting, you can copy network traffic to specific monitoring appliances. While creating a flow log subscription, you can choose the metadata fields you wish to capture, the maximum aggregation interval, and your preferred log destination. We recommend you aggregate these logs in a centralized location, preferably within your Log Storage.

Flow logs can help you with a number of tasks, such as:

- Diagnosing overly restrictive security group rules
- Monitoring the traffic that is reaching your instance
- Determining the direction of the traffic to and from the network interfaces

You can also choose to capture all traffic, or only accepted or rejected traffic. You can use tools such as [CloudWatch Log Insights](/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) or [CloudWatch Contributor Insights](/AmazonCloudWatch/latest/monitoring/ContributorInsights.html) to analyze your VPC flow logs delivered to CloudWatch Logs. You can use tools such as [Amazon Athena](/athena/latest/ug/what-is.html) and [Amazon QuickSight](/quicksight/latest/user/welcome.html) to query and visualize your VPC flow logs delivered to Amazon S3. We recommend you create a central S3 bucket, following the instructions included in the Log Storage capability, and secure these logs so they are tamper resistant and protected in a way that allows to write-once-read-many. You can also build a custom downstream application to analyze your logs, or use a Partner solution such as Splunk, Datadog, Sumo Logic, Cisco StealthWatch, Checkpoint CloudGuard, New Relic, and so on.

**Note:** Flow log data is collected outside of the path of your network traffic, and therefore does not affect network throughput or latency. You can create or delete flow logs without any risk of impact to network performance.

Monitor and analyze network logs and metrics

Use Amazon CloudWatch for monitoring your network resources performance and metrics. [Metrics](/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) are data about the performance of your systems. Amazon CloudWatch can load all the metrics in your account for search, graphing, and alarms. CloudWatch can be also used to aggregate VPC Flow Logs. For example, all the logs can be sent to CloudWatch for monitoring and observability.

Set up a CloudWatch Alarm for VPC Flow Logs Metric Filter, where you can have an Amazon CloudWatch metric configured to filter “REJECTS” in VPC flow logs. Run a CloudWatch alarm based on that filter, where you can receive notifications when IP packets are rejected inside your VPC. This gives you more visibility into unauthorized or rejected IP traffic within your Virtual Private Cloud.

Use [CloudWatch Logs Insights](/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) to interactively query and analyze your log data in Amazon CloudWatch Logs. Refer to the [Route53 and VPC Flow](/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.html) log sample Insight queries to get started analyzing your network logs. You can perform queries to help you more efficiently and effectively respond to operational issues. If an issue occurs, you can use CloudWatch Logs Insights to identify potential causes and validate deployed fixes. CloudWatch Logs Insights automatically discovers fields in logs from AWS services such as Amazon Route 53 and Amazon VPC, and any application or custom log that emits log events as JSON.

Set up network monitoring dashboards to view metrics, historic logs, and network performance statistics

[Set up Amazon CloudWatch dashboards](/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) , which are customizable home pages in the CloudWatch console that you can use to monitor your resources in a single view, even if those resources that are spread across different Regions. You can use CloudWatch dashboards to create customized views of the metrics and alarms for your AWS resources. All network level metrics and alarms, can be monitored from single dashboard.

We recommend centralizing the view of your network CloudWatch metrics, alarms, and dashboards to a central monitoring account(s), so that network administrators can view the network performance and status of all organization accounts and Regions in one place. To share metrics, alarms, and dashboards to a centralized account, refer to the [CloudWatch Cross-account console guidance](/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html) in the CloudWatch user guide.

### DNS management

DNS management

- Implement DNS for your cloud resources
- Configure DNS resolution between cloud and on-premises
- Configure DNS routing
- Set up logging for DNS query auditing and troubleshooting

A Domain Name Service (DNS) is used by every application and organization to connect names to IP addresses. Organizations usually manage their own DNS servers or use public DNS systems to make DNS queries. Within a cloud environment, you can create DNS zones to publish your records without having to configure and maintain your own DNS servers and software.

We recommend you manage your internal workloads and server domain names in a private DNS zone, limited to your network. For your public facing workloads and services, we recommend that you set up a different DNS. The DNS should be publicly accessible for clients over the internet to connect.

Typical application architecture involves monolithic, virtual machines (VMs), or containerized versions of jobs and services, relational or key-value databases and other data sets, and front-end consisting API routing or Load Balancer. Each of these constructs need unique networking, planning, and designing. DNS plays a key role in forwarding traffic to your applications irrespective of their structure. You should work with your application team to evaluate their needs for user experience and application monitoring. You can use DNS health checks provided by a cloud provider to test your applications or databases, to ensure they are healthy in the production environment. Similarly, DNS policies can be applied for your application traffic in cloud to influence routing. For example, you can use DNS routing policies to control which endpoints serve content to users based on the specific geographical location of your applications, users, or latency. You can also configure DNS records to achieve active/passive or load balancing between two endpoints.

For customers with hybrid workloads which include on-premises and cloud-based resources, extra steps are necessary to configure DNS to work seamlessly across both environments. You can use different endpoints on AWS for DNS traffic to be routed in and out of your cloud and on-premises network. Further, centralizing DNS management for all your cloud network and on-premises domains should be considered for ease of management. Additionally, when you have hybrid connectivity between on-premises and cloud architecture, DNS provides an integral function, as resources on-premises need to resolve DNS names for resources in the cloud and vice-versa.

Finally, to get insights into DNS traffic for auditing, DNS logging should be enabled and pushed to a monitoring system to get more insights into DNS data, and perform necessary actions from that data.

Implement DNS for your cloud resources

DNS is one of the essential components for your network environment. Inefficient or incorrect DNS configurations are often major road blocks to resolve traffic propagation issues and can cause significant business impact.

We recommend you set up [Amazon Route 53](/Route53/latest/DeveloperGuide/dns-configuring.html) as your DNS service. Route 53 main functionalities include:

- Domain registration
- DNS routing
- Health checking

Route 53 allows you to create hosted zones, which are containers for DNS records that define how to route traffic for a domain or subdomain. There are two types of hosted zones:

- **Private Hosted Zones** allow you to configure DNS routing internally within your VPC. You can route traffic using VPC endpoints, and connect to AWS services (including services such as Amazon EC2, EKS, ECS, and S3) through the AWS network.
- **Public Hosted Zones** allow you to route traffic outside AWS, such as a traditional DNS Server.

Amazon Route 53 also allows you to create split-horizon DNS, where under the same domain, you can host private VPC endpoints and a domain name for a public website or endpoint.

Configure DNS resolution between cloud and on-premises

When you register a domain with Route 53, Route 53 automatically becomes the DNS service for the domain. Route 53 creates a hosted zone that has the same name as the domain, assigns four name servers to the hosted zone, and updates the domain to use those name servers. In case of existing domains switching to Route 53, you create a hosted zone that has the same name as your domain, and then you create records in the hosted zone. Each record indicates how you want to route traffic for a specified domain name or subdomain name. For example, when someone enters your domain name in a web browser, traffic can be routed to a web server in your data center, to an Amazon EC2 instance, to a CloudFront distribution, or to some other location.

You can create records individually, or by importing a zone file from your current domain service provider. We recommend that you change the Time To Live (TTL) on the Name Server (NS) records in the hosted zone for the current DNS service provider and on the NS record in the Amazon Route 53 hosted zone for your domain. If your domain is in use—for example, if your users are using the domain name to browse to a website or access a web application—then DNS resolvers have cached the names of the name servers that were provided by your current DNS service provider. A DNS resolver that cached that information a few minutes ago will save it for almost two more days. If you've configured DNSSEC for your domain, you also need to remove the Delegation Signer (DS) record from the parent zone before you migrate your domain to Route 53. Once Amazon Route 53 is your domain service, you can optionally transfer registration for the domain to Route 53 by contacting AWS support as well.

Amazon Route 53 Resolver Endpoints are a good alternative to Domain Controller and Conditional Forwarding rules to help you route DNS queries from your VPC to on-premises or other VPCs, and vice versa. Ensure that DNS attributes for VPC are enabled - [Enable DNS Resolution in the DNS support attributes](/vpc/latest/userguide/vpc-dns.html#vpc-dns-updating) , and there is on-premises connectivity such as Amazon Direct Connect or VPN between VPC and on-premises. When you create an Amazon VPC, the second IP of VPC CIDR or VPC CIDR IPv4 network range plus two (.2) is dedicated to VPC DNS resolver.

The Amazon VPC receives automatic DNS resolution from the Route 53 Resolver. You can configure the Outbound Resolver Endpoint to forward DNS queries for domain names from Amazon EC2 instances in your VPCs to DNS revolvers on your remote network. In case of outbound endpoints, you have to configure outbound rules to dictate how DNS queries should be routed outside of VPC based on domain names. Refer to [Route 53 Resolver Outbound Endpoint](//premiumsupport/knowledge-center/route53-resolve-with-outbound-endpoint/) . The inbound endpoint should be used to route DNS queries from on-premises to private domain names in Amazon VPC. Inbound and Outbound Resolver Endpoints also can route DNS queries between VPCs in different AWS accounts.

You should identify use cases for the flow of DNS traffic between your AWS and non-AWS workloads -Resolving on-premises domains from workloads running in your VPCs, resolving private domains in your AWS environment from workloads running on-premises, or resolving private domains between workloads running in different AWS accounts. Use Amazon-provided default DNS server and Resolver endpoints for routing traffic between on premises and AWS, and within AWS. Default VPC DNS on the central VPC acts as the primary domain resolver for all workloads running in participating AWS accounts. This is the second IP address in the VPC CIDR range.

The inbound endpoint receives queries forwarded from on-premises DNS servers, and from workloads running in participating AWS accounts. The outbound endpoint is used to forward domain queries from AWS to on-premises DNS. For this architecture, you need two forwarding rules: one to forward domain queries to the on-premises DNS server through the outbound endpoint, and a second rule to forward domain queries to the resolver inbound endpoint in central VPC. These two forwarding rules need to be shared with all other AWS accounts through [AWS Resource Access Manager](/ram/latest/userguide/what-is.html) , and are associated with all VPCs in these accounts.

Steps to complete this part of the process:

1. Open the [Route 53](https://console.aws.amazon.com/route53/) console (login required) in an AWS account.
2. In the navigation pane, choose Rules.
3. Select the rule that you want to share.
4. For Select Resource Type, choose Resolver Rules.
5. Select the Resolver Rule ID to share.
6. Specify the Principal to share. The Principal can be a single account or an organization.
7. Open the AWS RAM console and choose Shared with me, Resource shares.
8. Select the resource share ID for Route 53 resolver rules and choose Accept resource share.
9. In the other AWS account, choose Rule in Route 53 console.
10. Select the resolver rule you shared, and choose Associate VPC.
11. Lastly, choose the VPC from the list and choose Add.

DNS queries from this VPC can now use the outbound endpoint for the shared rule from central account. AWS RAM performs the function of managing connectivity between VPC and the outbound endpoint for the rule.

Reference the “ [Simplify management in a multi-account environment with Route 53 Resolver](https://aws.amazon.com/blogs/security/simplify-dns-management-in-a-multiaccount-environment-with-route-53-resolver/) ” blog post to see an example solution that explains how to resolve domains across multiple accounts, and between workloads running on AWS and on-premises without the need to run a domain controller in AWS.

Configure DNS routing

Amazon Transit Gateway and VPC peering support cross-Region EC2 domain name resolutions. AWS Transit Gateway also enables the resolution of public DNS hostnames to private IP addresses when queried from Amazon VPCs that are also attached to the AWS Transit Gateway. If you want to resolve records in Private Hosted Zones for VPC in another Region, you can use Cross-region VPC to Private Hosted Zone Functionality. You can also use Route 53 Resolver endpoints to resolve DNS queries when Private Hosted Zones are in a different AWS Region.

For example, suppose you have an EKS cluster in the us-east-1 Region. The EKS client needs to resolve records in the Private Hosted Zone for VPC located in AWS Region us-west-1. In this case, the Route 53 Resolver Inbound Endpoint will need to be associated to the VPC in us-west-1 so it can receive DNS queries from the us-east-1 VPC. Similarly, EKS VPC should have the Outbound Resolver Endpoint configured so it can route queries outside of EKS VPC in us-east-1. The Route 53 inbound and outbound endpoints can also be used to route DNS queries from on-premises to Amazon VPC, and from VPC to on-premises hosts respectively.

Log DNS Queries

DNS query logs are important for monitoring and troubleshooting DNS issues. DNS Query logging should be enabled when using Route 53 for DNS resolution. DNS query logs can be sent to one of three AWS services: Amazon CloudWatch Logs, [Amazon Simple Storage Service](/AmazonS3/latest/userguide/Welcome.html) (Amazon S3), and [Amazon Kinesis Data Firehose](/firehose/latest/dev/what-is-this-service.html) . Query logs contain the queries that DNS resolvers forward to Route 53 and provide information as the domain or subdomain that was requested, data and time of request, DNS record type, DNS response code, and the Route 53 edge location that responded to DNS Query.

You can configure Amazon Route 53 to log information about the public DNS queries that Route 53 receives, such as the following:

- Domain or subdomain that was requested
- Date and time of the request
- DNS record type (such as A or AAAA)
- Route 53 edge location that responded to the DNS query
- DNS response code, such as NoError or ServFail

Once you configure query logging, Route 53 sends logs to CloudWatch Logs. You use CloudWatch Logs tools to access the query logs.

### SaaS provider connectivity

SaaS provider connectivity

- Connect privately to SaaS provider
- Configure DNS for SaaS private connectivity

Construct DNS set up for applications

A DNS is used by every application and organization to connect names to IP addresses. In cloud environments, DNS management becomes a critical element, because it allows for the discovery of each workload and service among themselves. Organizations usually manage their own DNS servers or use public DNS systems to make DNS queries. Within a cloud environment, you can create DNS zones to publish your records without having to configure and maintain your own DNS servers and software.

We recommend you manage your internal workloads and server domain names in a private DNS zone, limited to your network. For your public facing workloads and services, we recommend you set up a different DNS. the DNS should be publicly accessible for clients over internet to connect.

Typical application architecture involves monolithic, virtual machines (VMs), or containerized version of jobs and services, Relational or key-value databases and other data sets, and front-end consisting API routing or Load Balancer. Each of these constructs needs unique networking, planning, and designing. DNS plays a key role in forwarding traffic to your applications, irrespective of their structure. Work with your application team to evaluate their needs for user experience and application monitoring. You can use DNS health checks provided by a cloud provider to test your applications or databases to ensure they are healthy in the production environment. Similarly, DNS policies can be applied for your application traffic in the cloud to influence routing. For example, you can use DNS routing policies to control which endpoints serve content to users based on the specific geographical location of your applications, users, or latency. You can also configure DNS records to achieve active/passive or load balancing between two endpoints.

For customers with hybrid workloads, which include on-premises and cloud-based resources, extra steps are necessary to configure DNS to work seamlessly across both environments. You can use different endpoints on AWS for DNS traffic to be routed in and out of your cloud and on-premises network. Further, centralizing DNS management for all your cloud network and on-premises domains should be considered for ease of management. Additionally, when you have hybrid connectivity between on-premises and cloud architecture of the DNS is one of the main players in the room as resources on-premises will need to resolve DNS names for resources in cloud and vice-versa.

Finally, to get insights into DNS traffic for auditing, DNS logging should be enabled and pushed to a monitoring system to get more insights into DNS data and perform necessary actions from that data.

Connect privately to SaaS provider

SaaS providers can extend the functionalities and benefits of their products through third-party integrations. [AWS PrivateLink](https://aws.amazon.com/privatelink/) can be used for these integrations which provides a network path that is not exposed to the public network. Some examples of SaaS provider products that work with AWS PrivateLink are Managed Databases, Log ingestion, and Analytics workloads.

Many AWS partners deliver SaaS services such as log analytics and security scans to their customers on AWS. SaaS providers install agents or clients in their customers' VPCs to generate and send data back to the provider. When using SaaS applications, customers have to choose between allowing internet access from their VPC, which can put the VPC resources at risk, and not using these applications at all. With AWS PrivateLink, you can connect to AWS services and SaaS applications from your VPC in a private, secure, and scalable manner. Because connections to a service can be initiated only by you, you are safeguarded against unwarranted communication by the service provider.

Interface [VPC endpoints](/vpc/latest/privatelink/endpoint-services-overview.html) , powered by AWS PrivateLink, connect you to services hosted by AWS Partners and supported solutions available in the [AWS Marketplace](/marketplace/latest/userguide/what-is-marketplace.html) . By powering [Gateway Load Balancer endpoints](/vpc/latest/privatelink/vpce-gateway-load-balancer.html) , AWS PrivateLink brings the same level of security and performance to your virtual network appliances or custom traffic inspection logic.

When setting up an interface endpoint, choose multiple subnets across multiple Availability Zones to implement high availability. The number of ENIs should equal to number of subnets chosen. Interface endpoints offer a throughput of 10 Gbps per ENI with a burst capability of 40 Gbps. If your use case requires higher throughput, contact [AWS Support](/awssupport/latest/user/getting-started.html) .

You can find a variety solutions for access connectivity from [AWS PrivateLink Partners](https://aws.amazon.com/privatelink/partners/) .

Configure DNS for SaaS private connectivity

When you set up AWS PrivateLink or interface endpoints, your clients can choose these DNS options to send traffic to endpoint:

- Endpoint-specific Regional DNS
- Endpoint-specific Zonal DNS
- Private DNS

When you enable the Private DNS option, endpoints for AWS services for which endpoint is being created will resolve to Private IP, which corresponds to PrivateLink network interface IPs. When Private DNS is disabled, the service DNS name will resolve to Public IPs and traffic will not route through AWS PrivateLink. In that case, you need to use an endpoint specific DNS name (either Regional or zonal) so that traffic is routed via AWS PrivateLink elastic network interfaces.

An AWS PrivateLink service provider configures instances running services in their VPC with a Network Load Balancer as the front end. Use intra-Region VPC peering (VPCs are in the same Region) and inter-Region VPC peering (VPCs are in different Regions) with AWS PrivateLink to allow private access to consumers across VPC peering connections. Consumers in remote VPCs cannot use Private DNS names across VPC peering connections. They can, however, create their own private hosted zone on Route 53, and attach it to their VPCs to use the same Private DNS name.

## Related content

- **Establishing Your Cloud Foundation on AWS: Network Connectivity**: This whitepaper provides foundational guidance for designing, managing, and monitoring secure and scalable networks, including cloud connectivity, hybrid environments, IP address management, and DNS setup.

[Read the whitepaper](/whitepapers/latest/establishing-your-cloud-foundation-on-aws/network-connectivity-capability.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
