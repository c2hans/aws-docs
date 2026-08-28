---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/solutions.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Solutions
<a name="solutions"></a>

 The solutions in this whitepaper present options and best practices to architect a DNS solution in the hybrid cloud, keeping in mind criteria such as ease of implementation, management overhead, cost, resilience, and the distribution of DNS queries directed toward the Route 53 Resolver. We cover the following solutions:
+  **Route 53 Resolver endpoints and forwarding rules** – This solution focuses on using Route 53 Resolver endpoints to forward traffic between your Amazon VPC and on-premises data center over both [AWS Direct Connect](https://aws.amazon.com/directconnect/) and [Amazon VPN](https://aws.amazon.com/vpn/).
+  **Secondary DNS in an Amazon VPC** – This solution focuses on using Route 53 to mirror on-premises DNS zones that can then be natively resolved from within VPCs, without the need for additional DNS forwarding resources.
+  **Decentralized conditional forwarders** – This solution uses distributed conditional forwarders and provides two options for using them efficiently. While we use unbound as a conditional forwarder in some of these solutions, you can use any DNS server that supports conditional forwarding with similar features.
+  **Scaling DNS management across multiple accounts and VPCs** – This solution walks through options for managing DNS names as you scale your hybrid DNS solution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
