---
source_url: https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html
---

# Building a Scalable and Secure Multi-VPC AWS Network Infrastructure
<a name="welcome"></a>

Publication date: **April 17, 2024** ([Document history](document-revisions.md))

Amazon Web Services (AWS) customers often rely on hundreds of accounts and virtual private clouds (VPCs) to segment their workloads and expand their footprint.This level of scale often creates challenges around resource sharing, inter-VPC connectivity, and on-premises facilities to VPC connectivity.

This whitepaper describes best practices for creating scalable and secure network architectures in a large network using AWS services such as [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC), [AWS Transit Gateway](https://aws.amazon.com/transit-gateway), [AWS PrivateLink](https://aws.amazon.com/privatelink/), [Direct Connect](https://aws.amazon.com/directconnect/), [Gateway Load Balancer](https://aws.amazon.com/elasticloadbalancing/gateway-load-balancer/), [AWS Network Firewall](https://aws.amazon.com/network-firewall/), and [Amazon Route 53](https://aws.amazon.com/route53/). It demonstrates solutions for managing growing infrastructure—ensuring scalability, high availability, and security while keeping overhead costs low.

## Introduction
<a name="introduction"></a>

AWS customers begin by building resources in a single AWS account that represents a management boundary which segments permissions, costs, and services. However, as the customer’s organization grows, greater segmentation of services becomes necessary to monitor costs, control access, and provide easier environmental management. A multi-account solution solves these issues by providing specific accounts for IT services and users within an organization. AWS provides several tools to manage and configure this infrastructure, including [AWS Control Tower](https://aws.amazon.com/controltower/).

![A diagram depicting AWS Control Tower initial deployment](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/images/control-tower-deployment.png)

When you set up your multi-account environment using AWS Control Tower, it creates two Organizational Units (OUs):
+ **Security OU** – Within this OU, AWS Control Tower creates two accounts:
+ Log Archive
+ Audit (This account corresponds to the security Tooling account discussed previously in the guidance.)
+ **Sandbox OU** – This OU is the default destination for accounts created within AWS Control Tower. It contains accounts in which your builders can explore and experiment with AWS services, and other tools and services, subject to your team’s acceptable use policies.

**AWS Control Tower allows you to create, register, and manage additional OUs to expand the initial environment to implement the guidance. **

 The following diagram shows the OUs initially deployed by AWS Control Tower. You can expand your AWS environment to implement any of the recommended OUs included in the diagram, to meet your requirements.

![A diagram depicting AWS organizational OUs.](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/images/organization-ous.png)

For further details on multi-account environment using AWS Control Tower, refer to [*Appendix E*](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/appendix-e-establish-multi-account.html) in the *Organizing Your AWS Environment Using Multiple Accounts* whitepaper.

Most customers begin with a few VPCs to deploy their infrastructure. The number of VPCs a customer creates is usually related to their number of accounts, users, and staged environments (production, development, test, and so on). As cloud usage grows, the number of users, business units, applications, and Regions that a customer interacts with also grow, leading to the creation of new VPCs.

As the number of VPCs grows, cross-VPC management becomes essential for the operation of the customer’s cloud network. This whitepaper covers best practices for three speciﬁc areas in cross-VPC and hybrid connectivity:
+ **Network connectivity** – Interconnecting VPCs and on-premises networks at scale.
+ **Network security** – Building centralized egress points for accessing the internet and endpoints such as [network address translation (NAT) gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html), [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html) , [AWS PrivateLink](https://aws.amazon.com/privatelink/) , [AWS Network Firewall](https://aws.amazon.com/network-firewall/) , and [Gateway Load Balancers](https://aws.amazon.com/elasticloadbalancing/gateway-load-balancer/).
+ **DNS management** – Resolving DNS within the Control Tower and hybrid DNS.

## IP address planning and management
<a name="ip-address-planning-and-management"></a>

 In order to build a scalable multi-account multi-VPC network design, IP address planning and management is imperative. A good IP addressing scheme needs to consider your current and future networking needs. Your IP address scheme IP needs to cover your on-prem workloads, your cloud workloads, and should also allow for future expansion (for example, addition of new AWS Regions, business units, and mergers or acquisitions). It should also prevent your teams from inadvertently creating overlapping IP CIDRs. If overlapping IP CIDR is desired such as for isolated or disconnected workloads, this decision needs to be conscious and should account for implications on routing, security and cost. You might also need to consider creating necessary approval processes for such exceptions. A good IP addressing scheme also helps with simplifying your network design and routing configuration.

 Key considerations:
+  Plan your IP addressing scheme (both public and private IPs) up front and select an IP address management tool to allocate, manage, and track IP address usage across all of your workloads.
+  Use hierarchical and summarized IP addressing schemes.
+  Plan for consistent IP assignment based on environment, AWS Region, organization, or business unit.
+  Designate distinct IP CIDRs (both IPv4 and IPv6) for on-premises and cloud networks.
+  Proactively prevent and track overlapping IP CIDRs.
+  Size your IP CIDRs appropriately to enable scaling and future growth.
+  Enable your workloads for IPv6 or dual-stack compatibility to reduce IP conflicts and address IPv4 space depletion.

 You can use Amazon VPC IP Address Manager (IPAM) to simplify planning, tracking, and monitoring both public and private IP addresses for your AWS workloads. IPAM allows you to organize, allocate, monitor, and share IP address space across multiple AWS Regions and AWS accounts. It also helps with automatic allocation of CIDRs to VPCs using specific business rules.

 Refer to the [Amazon VPC IP Address Manager Best Practices](https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-vpc-ip-address-manager-best-practices/), [Managing IP pools across VPCs and Regions using Amazon VPC IP Address Manager](https://aws.amazon.com/blogs/networking-and-content-delivery/managing-ip-pools-across-vpcs-and-regions-using-amazon-vpc-ip-address-manager/), and [IP Address Management for AWS Control Tower](https://aws.amazon.com/blogs/networking-and-content-delivery/ip-address-management-for-aws-control-tower/) blog posts to learn IP addressing best practices and how to use IPAM to manage IP pools across VPCs, AWS Regions, and AWS Control Tower.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).
