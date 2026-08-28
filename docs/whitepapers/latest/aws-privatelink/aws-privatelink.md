---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/aws-privatelink.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Securely Access Services Over AWS PrivateLink
<a name="aws-privatelink"></a>

Publication date: **June 3, 2021** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 Amazon Virtual Private Cloud (Amazon VPC) gives AWS customers the ability to define a virtual private network within the AWS Cloud. Customers can build services securely within an Amazon VPC and provide access to these services internally and externally using traditional methods such as an internet gateway, VPC peering, network address translation (NAT), a virtual private network (VPN), and Direct Connect. This whitepaper presents how AWS PrivateLink keeps network traffic private and allows connectivity from Amazon VPCs to services and data hosted on AWS in a secure and scalable manner.

 This paper is intended for IT professionals who are familiar with the basic concepts of networking and AWS. Each section has links to relevant AWS documentation.

### Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

### Introduction
<a name="introduction"></a>

 The introduction of Amazon Virtual Private Cloud (Amazon VPC) in 2009 made it possible for customers to provision a logically-isolated section of the AWS cloud and launch AWS resources in a virtual network that they define. Traditional methods to access third-party applications or public AWS services from an Amazon VPC include using an internet gateway, virtual private network (VPN), Direct Connect with a virtual private gateway, and VPC peering.

 The following figure illustrates an example Amazon VPC and its associated components:

![A diagram depicting traditional access from an Amazon VPC.](http://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/images/traditional-access.png)

### What is AWS PrivateLink?
<a name="what-is-aws-privatelink"></a>

AWS PrivateLink provides secure, private connectivity between Amazon VPCs, AWS services, and on-premises applications on the AWS network. As a result, customers can simply and securely access services on AWS using the private Amazon network, powering connectivity to AWS services through interface Amazon VPC endpoints. Refer to the following figure for Amazon VPC-to-VPC connectivity using AWS PrivateLink.

![A diagram depicting Amazon VPC-to-VPC connectivity with AWS PrivateLink.](http://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/images/vpc-vpc.png)

AWS PrivateLink also allows customers to create an application in their Amazon VPC, referred to as a service provider VPC, and offers that application as an AWS PrivateLink-enabled service or VPC endpoint service. A VPC endpoint service lets customers host a service and have it accessed by other consumers using AWS PrivateLink.

### Why use AWS PrivateLink?
<a name="why-use-aws-privatelink"></a>

 Prior to the availability of AWS PrivateLink, services residing in a single Amazon VPC were connected to multiple Amazon VPCs either:
+ Through public IP addresses using each VPC’s internet gateway, or
+  By private IP addresses using VPC peering. With AWS PrivateLink, service connectivity over Transmission Control Protocol (TCP) can be established from the service provider’s VPC to the service consumers’ VPCs in a secure and scalable manner.

 AWS PrivateLink provides the following three main benefits:

#### Use private IP addresses for traffic
<a name="use-private-ip-addresses-for-traffic"></a>

 AWS PrivateLink provides Amazon VPCs with a secure and scalable way to privately connect to AWS-hosted services. AWS PrivateLink traffic does not use public internet protocols (IP) addresses nor traverse the internet. AWS PrivateLink uses private IP addresses and security groups within an Amazon VPC so that services function as though they were hosted directly within an Amazon VPC.

#### Simplify network management
<a name="simplify-network-management"></a>

AWS PrivateLink helps avoid both (1) security policies that limit benefits of internet gateways and (2) complex networking across a large number of Amazon VPCs. AWS PrivateLink is easy to use and manage because it removes the need to allowlist public IPs and manage internet connectivity with internet gateways, NAT gateways, or firewall proxies.

 AWS PrivateLink allows for connectivity to services across different accounts and Amazon VPCs with no need for route table modifications. There is no longer a need to configure an internet gateway, VPC peering connection, or Transit VPC to enable connectivity.

 A Transit VPC connects multiple Amazon Virtual Private Clouds that might be geographically disparate or running in separate AWS accounts, to a common Amazon VPC that serves as a global network transit center. This network topology simplifies network management and minimizes the number of connections that you need to set up and manage. It is implemented virtually and does not require any physical network gear or a physical presence in a colocation transit hub.

#### Facilitate your cloud migration
<a name="facilitate-your-cloud-migration"></a>

 AWS PrivateLink gives on-premises networks private access to AWS services via Direct Connect. Customers can more easily migrate traditional on-premises applications to services hosted in the cloud and use cloud services with the confidence that traffic remains private.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
