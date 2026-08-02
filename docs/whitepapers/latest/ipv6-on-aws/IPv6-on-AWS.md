---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/IPv6-on-AWS.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# IPv6 on AWS
<a name="IPv6-on-AWS"></a>

Publication date: **October 26, 2021** ([Document Revisions](document-revisions.md))

 Every node connected to an Internet Protocol (IP) network must have an IP address for communication purposes. As the internet continues to grow, so does the need for IP addresses. IPv6 is a version of the Internet Protocol that uses a larger address space than its predecessor, IPv4. This whitepaper focuses on best practices for adopting and designing IPv6-based networks on the Amazon Web Services (AWS) Cloud. It covers IPv6-only and dual-stack networks for both internet-facing and private IPv6 networks use cases.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 An increasing number of organizations operate dual-stack IPv4/IPv6 networks. Carrier networks and ISPs were the first groups to start deploying IPv6 on their networks, with mobile networks leading the charge. Adoption of IPv6 has been delayed, partly due to network address translation (NAT) with IPv4, which takes private IP addresses and turns them into public IP addresses.

 An increasing number of organizations are adopting IPv6 in their environments, driven by the public IPv4 space exhaustion, private IPv4 scarcity, especially within large-scale networks, and the need to provide connectivity to IPv6-only clients. There is no one-size-fits-all approach with IPv6; however, there are best practices AWS customers can follow to plan and implement IPv6 into their existing cloud networks.

 This whitepaper explains key drivers for adoption and highlights best practices to guide you while leaving enough space for you to decide, based on your specific use case and implementation, how to approach IPv6 in your network.

### Tenets for IPv6 adoption
<a name="tenets-for-ipv6-adoption"></a>

 Adhering to the following tenets for IPv6 adoption can help make the process and decision more manageable:
+  **Re-evaluate network controls** — IPv6 offers opportunities to rethink your approach to perimeter security and make design decisions that further improve your security posture.
+  **Design for scale** — More usable IPv6 addresses doesn’t mean you can shortcut IP allocation and planning.
+  **Phase your IPv6 adoption** — Focus on your business needs to implement IPv6 where needed, and remember that IPv4 and IPv6 can be made to coexist as long as needed.

### Intended audience
<a name="intended-audience"></a>

 Considering the variety of drivers, both internal and external, IPv6 adoption affects organizations regardless of size, industry sector, or geography. The best practices and design considerations outlined in this paper are oriented toward cloud architects and network technical leads who are responsible for the overall network design and architecture of their AWS environment. Whether you are new to AWS or you have already been using AWS for years, your team will benefit from reviewing this paper and deciding what is applicable based on your requirements and your current AWS environment.

**Note**
This paper doesn’t repeat the guidance found in other resources, but rather complements them by focusing on the IPv6-specific differences. Customers are advised to consult the guidance in this paper in addition to the existing literature that covers individual topics in detail.
