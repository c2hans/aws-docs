---
source_url: https://docs.aws.amazon.com/solutions/building-your-enterprise-wan-on-aws/index.html
---

---
title: 'Guidance for Building Your Enterprise WAN on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-your-enterprise-wan-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Building Your Enterprise WAN on AWS

## Overview

This Guidance demonstrates a four-phased approach to progressively migrate your enterprise wide area network (WAN) to AWS. It includes the most common steps you could take in your network modernization journey to a Network-as-a-Service (NaaS) consumption model. However, this Guidance can be easily modified and tailored, depending on your network architecture, footprint, expertise, resources, and budget. Moreover, each phase includes an architecture diagram that allows you to envision the future state of your networking environment and the intermediate steps involved in the migrations process. This can help you make data-driven decisions when assessing the overall value of migrating your WAN to AWS. For detailed, step-by-step instructions on configuring the components outlined here, refer to the implementation resources section.

## Benefits

### Optimize Costs

With a Pay-As-You-Go model for networking infrastructure, you can optimize costs without the need for long-term contracts or fixed capacity networks sized for peak demand periods, regardless of usage.

### Reduce Complexity

Networking services likeAWS Cloud WANempower you to define your global networks using policy-as-code and automation. This speeds up your deployments, reduces human error, and allows you to scale your global network to thousands of VPCs across all supported regions using less resources.

### Increase Availability

The network infrastructure used by the AWS services in this Guidance is fully managed by AWS. These architecture diagrams can be configured in a highly available manner across multiple Availability Zones to reduce downtime and troubleshooting.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-your-enterprise-wan-on-aws.pdf)

![Architecture diagram](/images/solutions/building-your-enterprise-wan-on-aws/images/building-your-enterprise-wan-on-aws-1.png)

1. **Step 1**: Phase 1: Backup your connectivity between data centers. This phase deploys SiteLink, which creates an on-demand, consumption-based network connecting all of your data centers. This helps you establish a backup network path for your data centers.
1. **Step 2**: Phase 2: Connect your data centers. The objective in this phase is to achieve a consumption-based model for your primary on-premises network. It helps you deploy SiteLink as the primary connection between on-premises data centers and migrate your data centers to AWS.
1. **Step 3**: Phase 3: Connect branch offices and segment your enterprise WAN. On-premises connectivity requires branch office connectivity. In this phase, you can deploy AWS Cloud WAN, which provides a central dashboard for making connections between your branch offices, and Amazon Virtual Private Cloud (Amazon VPC).
1. **Step 4**: Phase 4: Expand your enterprise WAN footprint. During this phase, you can extend your WAN to additional cloud Regions and on-premises locations by using a combination of SiteLink and AWS Cloud WAN.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: A detailed guide is provided to experiment and use within your AWS account. Each stage of building the Guidance, including deployment, usage, and cleanup, is examined to prepare it for deployment.

[Open guide](https://aws-solutions-library-samples.github.io/networking/building-your-enterprise-wan-on-aws.html)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS Cloud WAN and SiteLink are used throughout this Guidance to enhance your operational excellence. AWS Cloud WAN allows you to accelerate workload migration by simplifying your global connectivity patterns through network policies and automated network management. It provides a centralized dashboard that helps you visualize and control your network by monitoring performance and health, and automating routine tasks. With features like SiteLink, you can easily simplify on-premises connectivity between your data centers, helping you reduce operational overhead and human errors for your global network. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

In this Guidance, we recommend you use Direct Connect or Site-to-Site VPN to connect your on-premises environment to AWS. To encrypt your traffic, you can either use Direct Connect with MAC Security (MACsec) or Site-to-Site VPN, which supports Internet Protocol security (IPsec) VPN connections. Furthermore, Traffic Encryption Options in AWS Direct Connect lists various ways you can build a secure, consistent, low latency network experience. Also, all data flowing across AWS Regions over the AWS global network is automatically encrypted at the physical layer before it leaves AWS secured facilities. More information about encryption in transit within AWS can be found in Data protection in Amazon EC2. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance consists of AWS Cloud WAN, Direct Connect, and Site-to-Site VPN, which are AWS managed networking services built on top of the AWS Global Infrastructure that delivers the highest network availability of any cloud provider. Additionally, this Guidance requires you to connect your on-premises network to the cloud. While the reliability of the on-premises network is your responsibility, this Guidance uses Direct Connect which has a resiliency model that provides recommendations on how to build a highly available network connection between your on-premises environment and AWS. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance helps you improve your performance efficiency in a number of ways. For one, you can decide to use Site-to-Site VPN over the internet compared to dedicated circuits through Direct Connect for your hybrid connectivity. Second, you can choose Direct Connect locations to be closest to your data centers to improve latency, jitter, and other performance parameters. Third, for your global network, you can use AWS Cloud WAN to track network events, routes, and performance. Using this Guidance to replace existing WAN services, such as multiprotocol label switching (MPLS), can decrease round-trip network latency by 200ms and increase bandwidth by 66x for long-haul intercontinental connections (for example, US West to Asia-Pacific). [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

AWS Cloud WAN, Direct Connect, and Site-to-Site VPN offer usage-based pricing, allowing you the flexibility to pay only for the network resources you use. Data transfer out (DTO), in the case of Direct Connect, and data processing, in the case of AWS Cloud WAN, are based on the amount of traffic consumed. Additionally, data transfer for network traffic that is sent into AWS over Direct Connect is free of charge. Finally, you have the flexibility to increase your usage over time, so you can avoid unnecessary costs, build, and operate cost-aware workloads. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

AWS Cloud WAN, an AWS managed service, allows you to scale your Regional connections, as well as your global network footprint, in minutes. Also, because this Guidance uses Site-to-Site VPN and Direct Connect, you can choose the optimal on-premises connectivity option based on your current requirements. This helps you optimize your workloads as your demand grows and minimize the environmental impacts of running cloud workloads. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Introducing AWS Direct Connect SiteLink**: This blog post talks about how customers can quickly create a WAN using SiteLink, a feature of AWS Direct Connect, to connect across their data centers by sending data from one Direct Connect location to another, bypassing AWS Regions.

[Learn more](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-aws-direct-connect-sitelink/)

- **Introducing AWS Cloud WAN (Preview)**: This blog post looks at the main use cases for Cloud WAN. We cover how you can get started, and look at the key functionality available.

[Learn more](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-aws-cloud-wan-preview/)

- **Guidance for Automating Amazon VPC Routing in a Global Cloud WAN Deployment**: This Guidance demonstrates how to automatically update the routing tables of your Amazon Virtual Private Cloud (Amazon VPC) when the Amazon VPC is attached or detached from an AWS Cloud WAN segment.

[Learn more](/solutions/automating-amazon-vpc-routing-in-a-global-cloud-wan-deployment/)

- **Centralized outbound inspection architecture in AWS Cloud WAN**: This blog post describes architectural patterns for centrally managing and inspecting outbound network traffic from AWS workloads in a Cloud WAN network.

[Learn more](https://aws.amazon.com/blogs/networking-and-content-delivery/centralized-outbound-inspection-architecture-in-aws-cloud-wan/)

- **Inspecting network traffic between Amazon VPCs with AWS Cloud WAN**: This blog post takes a closer look at centralized architectures for native East-West (VPC-to-VPC) inspection both within and across Regions with Cloud WAN.

[Learn more](https://aws.amazon.com/blogs/networking-and-content-delivery/inspecting-network-traffic-between-amazon-vpcs-with-aws-cloud-wan/)

- **Advanced Routing scenarios with AWS Direct Connect SiteLink**: This blog post walks through advanced routing scenarios and best practices that customer architects can use to meet such requirements while using AWS Direct Connect with SiteLink.

[Learn more](https://aws.amazon.com/blogs/networking-and-content-delivery/advanced-routing-scenarios-with-aws-direct-connect-sitelink/)

- **AWS Cloud WAN and AWS Transit Gateway migration and interoperability patterns**: This blog post discusses interoperability design patterns and how to migrate from Transit Gateway to Cloud WAN.

[Learn more](https://aws.amazon.com/blogs/networking-and-content-delivery/aws-cloud-wan-and-aws-transit-gateway-migration-and-interoperability-patterns/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
