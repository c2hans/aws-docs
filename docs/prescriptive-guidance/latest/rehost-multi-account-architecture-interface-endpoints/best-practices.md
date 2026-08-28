---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-multi-account-architecture-interface-endpoints/best-practices.html
---

# Best practices
<a name="best-practices"></a>
+ Avoid single points of failure. For VPC endpoints and Route 53 Resolver endpoints, use two or more Availability Zones for high availability.
+ Do not use Route 53 Resolver endpoints to forward DNS queries between VPCs. We strongly recommend that you use the Amazon DNS Server (.2 resolver) as the DNS resolver for all instances inside Amazon EC2. This resolver provides the highest level of availability and scalability with the lowest latency.
+ For additional best practices, see [Best practices for Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver.html) in the Route 53 documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
