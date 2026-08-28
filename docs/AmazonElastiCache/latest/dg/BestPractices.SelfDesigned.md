---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.SelfDesigned.html
---

# Best practices when working with Valkey and Redis OSS node-based clusters
<a name="BestPractices.SelfDesigned"></a>

Multi-AZ use, having sufficient memory, cluster resizing and minimizing downtime are all useful concepts to keep in mind when working with node-based clusters in Valkey or Redis OSS. We recommend you review and follow these best practices.

**Topics**
+ [Minimizing downtime with Multi-AZ](multi-az.md)
+ [Ensuring you have enough memory to make a Valkey or Redis OSS snapshot](BestPractices.BGSAVE.md)
+ [Online cluster resizing](best-practices-online-resharding.md)
+ [Minimizing downtime during maintenance](BestPractices.MinimizeDowntime.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
