---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/options.html
---

# Networking access scenarios for SaaS offerings in the AWS Cloud
<a name="options"></a>

This section covers different network access options for your SaaS offerings in the AWS Cloud. It discusses the approaches from the perspective of your consumer, who might have connectivity needs within the AWS Cloud, from on-premises data centers, or from other cloud service providers (CSPs). Additionally, you might need to support access from multiple types of consumer environments.

Understanding the network connectivity requirements across these diverse environments is essential for creating a comprehensive access strategy. Your architectural decisions must account for varying security models, performance expectations, and technical constraints while maintaining operational efficiency. The right approach provides secure, reliable connectivity that scales with your business growth and minimizes both implementation complexity and ongoing management overhead.

When evaluating network access options, consider how each approach affects your total cost of ownership, including not just infrastructure costs but also operational overhead and compliance requirements. Some approaches excel at scalability but may introduce complexity, while others prioritize ease of integration at the expense of network isolation. Your consumers' technical capabilities and resources also play a significant role in determining the most appropriate solution.

For consumers on the AWS Cloud, services such as AWS PrivateLink offer significant advantages in security and scalability. On-premises consumers might benefit from AWS Direct Connect for consistent performance or benefit from Site-to-Site VPN for cost-effective connectivity. Multi-cloud scenarios often require careful consideration of interoperability challenges, and you might use transit VPC architectures to standardize access patterns. In all cases, your design should anticipate future consumer and traffic growth so that your network architecture remains resilient and adaptable as your SaaS offering evolves.

**This section contains the following scenarios:**
+ [SaaS consumers operating on AWS](options-aws.md)
+ [SaaS consumers operating on-premises](options-onprem.md)
+ [SaaS consumers operating on other cloud service providers](options-other-csps.md)
+ [Supporting hybrid environments](options-hybrid.md)
