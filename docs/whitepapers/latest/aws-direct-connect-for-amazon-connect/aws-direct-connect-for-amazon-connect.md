---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-direct-connect-for-amazon-connect/aws-direct-connect-for-amazon-connect.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS Direct Connect for Amazon Connect
<a name="aws-direct-connect-for-amazon-connect"></a>

Publication date: **November 2, 2022** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 Many contact centers and security architects want to use Amazon Connect in conjunction with AWS Direct Connect. This whitepaper outlines best practices, architecture considerations, and technical requirements for using these services together.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 [Amazon Connect](https://aws.amazon.com/connect/) is an easy-to-use omnichannel cloud contact center service that can operate over any public internet connection. For most customers, this means you can build an enterprise-grade contact center that can easily scale from a handful of agents to tens of thousands of agents—and your agents can log in with nothing but a web browser and headset.

 However, there are edge cases that might dictate private connectivity between the contact center and your AWS Cloud. Common scenarios that elicit this requirement include:
+  Public sector and regulated industries with elevated encryption requirements.
+  Customers with a history of poor internet service that require service levels with providers to improve network conditions.
+  Customers whose security protocols require minimization of traffic exposure to a public wide area network (WAN).
+  Customers with requirements for resiliency over public and private links.

### Public sector and regulated industries with elevated encryption requirements
<a name="public-sector-and-regulated-industries-with-elevated-encryption-requirements"></a>

 Amazon Connect uses Transport Layer Security (TLS) to encrypt signaling and messaging traffic and Secure Real-time Transport Protocol (SRTP) to encrypt voice traffic, to ensure that traffic is protected from interception and snooping. There are times when organizations require additional hardening to prevent the possibility of [man-in-the-middle attacks](https://en.wikipedia.org/wiki/Man-in-the-middle_attack). You can use AWS Direct Connect to minimize exposure. AWS Direct Connect supports [MACsec](https://en.wikipedia.org/wiki/IEEE_802.1AE) encryption to further encrypt traffic between the customer’s contact center and AWS infrastructure.

### Customers with a history of poor internet service that require service levels with providers to improve network conditions
<a name="customers-with-a-history-of-poor-internet-service-that-require-service-levels-with-providers-to-improve-network-conditions"></a>

 While software as a service (SaaS) adoption over public internet is both widely used and reliable, there are circumstances where contact centers may require the service level guarantees on throughput and latency that private links can provide. For these use cases, AWS Direct Connect lets you route traffic across dedicated links to the AWS Cloud.

### Customers whose security protocols require minimization of traffic exposure to public WAN
<a name="customers-whose-security-protocols-require-minimization-of-traffic-exposure-to-public-wan"></a>

 Similar to the previous use cases, customers may have security policies in place to prevent business-critical information from traversing public internet. These customers can use dedicated links to avoid routing through the public internet.

 Note that even though data is routed with public addresses, the public addresses are advertised through the Direct Connect service. Because of this, a more specific route is available at the customer's router, which prioritizes this private routing of data over the Direct Connect service. Once the traffic reaches the AWS edge routers in the Region, a network address translation takes place to reach the internal service.

### Customers with requirements for resiliency over public and private links
<a name="customers-with-requirements-for-resiliency-over-public-and-private-links"></a>

 In some cases, meeting business-defined uptime requirements may require redundant or resilient connectivity links. There are cases when multiple internet service providers (ISPs) are unavailable at specific locations, or additional ISPs may ride the same fiber links as the incumbent ISP. With AWS Direct Connect, customers can use a Site-to-Site VPN over private connections as well as public connections independently, to allow for maximum resilience to ISP or private networks. For more information about Transit Gateway peering and multicast, refer to [AWS Transit Gateway features](https://aws.amazon.com/transit-gateway/features/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
