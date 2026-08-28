---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/connectivity-within-cloud-environment.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Connectivity within the cloud environment
<a name="connectivity-within-cloud-environment"></a>

As you create virtual networks in your cloud environment you need to establish connectivity between the different workloads and their components. These connections within the cloud can be consumed in a service model, where you grant access between the workloads to connect and retrieve or send data. On the cloud, your workloads can have private or public IP addresses, allowing connectivity between them.

As you start building your cloud environment, different workloads will be hosted in different networks, and they may communicate through the Internet. However, as your environment grows and matures, you can configure your network so the traffic does not leave your cloud environment unless necessary. If you are working with Partners, or SaaS providers, you can work with them to establish a private connection, so the traffic never leaves your cloud environment.

There are multiple ways to establish network connections to ensure the traffic within your environment is secure. You can establish VPN connections between different networks or services, you can connect the different networks and access points through the route tables of your network benefiting from your cloud provider backbone network, or you can establish a physical connection between two locations.

 Keeping the traffic within your cloud environment can help you reduce unnecessary data transfer costs between networks when you communicate with a partner, a SaaS provider, or to your data centers, since the traffic does not leave your network, and no internet connectivity is required. Additionally, it can help you to enhance your network security, reliability, and reduce latency when using private connection, since you will not be sharing bandwidth through the internet.

To improve discoverability of your workloads, services, and any possible partner product you are consuming, you need to plan and build your internal and external DNS configurations for private and public access.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
