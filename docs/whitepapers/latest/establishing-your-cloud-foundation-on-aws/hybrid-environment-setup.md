---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/hybrid-environment-setup.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Hybrid environment set up
<a name="hybrid-environment-setup"></a>

As customers build their cloud environment it is common to have workloads on-premises and across different cloud providers. You might have connectivity requirements that you need to satisfy, so your workloads can communicate across different networks and environments.

The easiest way to connect different environments is over the public Internet. However, the public internet is a shared network, this can impact your performance, and the traffic is not encrypted at the network layer. We recommend that communications between critical and production workloads do not communicate through the internet, and limit over the internet communications to isolated test or development environments.

If you need to access resources in your cloud environment by using the internet, we recommend you create a bastion box within your environment. Using a bastion box allows you to access all other cloud resources privately which increases the security of the resources you don’t need to expose on the internet. You can monitor access to your cloud environment and resources through this host.

The needs of your Business Units (BUs) often drive long and short-term connectivity initiatives. We recommend you work with your central IT team, security team, and the different workload owners to understand bandwidth, throughput, and compliance requirements. As you build your network SSL VPNs are great options for service connectivity and user to endpoint models. SSL or similar VPN clients can be installed on individual users’ systems/servers/laptops to secure connectivity between your cloud environment and your on-premises and individual user devices. Virtual Private Networks (VPN) or a direct dedicated connectivity links between on-premises and cloud environment are some of the popular options chosen by customers. Both of these options typically require layer 2 and layer 3 connectivity between your data center/office and cloud provider’s network. With a Virtual Private Network (VPN), you are encrypting traffic between two endpoints and traffic flows over private IP inside VPN tunnels. With physical links, traffic traverse over dedicated lease lines so you get dedicated bandwidth and predictable network performance compared to VPN.

To configure routing for your networks, you can select between static or dynamic routing. Static routing requires to the manual configuration of routes for source and destination on both ends. Dynamic (BGP or OSPF) routing allows you to propagate routes across your network automatically. For most network option configurations, we recommend a dynamic routing solution for scalability and adaptability.

[Edge connectivity](https://aws.amazon.com/products/networking/edge-networking/) is gradually becoming preferred option for applications with global user base. Content Delivery Networks (CDNs) and similar edge networking solutions employ edge locations distributed worldwide. This enables application traffic access through one of the nodes that is closer to the final user, reducing significantly the usage of the Internet Service Provider (ISP) network. These solutions are used to improve the end customer experience by enhancing performance of the network and workloads.

Regardless of the type of connectivity options you choose between your on-premises environment and your cloud environments, ensure** high availability** and **redundancy** for your communication channel. Routing maintenance, upgrades, other unexpected network, electrical incidences, and natural events can disrupt your primary connection. In these scenarios, a secondary (or fail over) connection might be required to avoid outages.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
