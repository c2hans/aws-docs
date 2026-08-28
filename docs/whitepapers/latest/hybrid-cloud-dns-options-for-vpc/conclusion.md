---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/conclusion.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Conclusion
<a name="conclusion"></a>

 For organizations with on-premises resources, operating in a hybrid architecture is a necessary part of the cloud adoption process. As such, architecture patterns that streamline this transition are essential for success.

 We discussed concepts as well as constraints to help you better understand the fundamental building blocks of the solutions provided here, as well as the limitations that help to create the most optimal solution for your workload. The provided solutions included how to use Route 53 Resolver endpoints with conditional forwarding rules, how to set up Secondary DNS in the Amazon VPC with AWS Lambda and Route 53 Private hosted zones, and solutions that use decentralized forwarders using the unbound DNS server. We also provided guidance on how to select the appropriate solution for your intended workload. Finally, we examined some additional considerations to help you to better tailor your solution for different workload requirements, faster failover, and better DNS server resiliency.

 By using the architectures provided, you can achieve the most ideal private DNS interoperability between your on-premises environments and your Amazon VPC.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
