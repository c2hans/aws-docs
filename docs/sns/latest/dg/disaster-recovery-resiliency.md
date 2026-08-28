---
source_url: https://docs.aws.amazon.com/sns/latest/dg/disaster-recovery-resiliency.html
---

# Resilience in Amazon SNS
<a name="disaster-recovery-resiliency"></a>

Resilience in Amazon SNS is ensured through leveraging the AWS global infrastructure, which revolves around AWS Regions and Availability Zones. AWS Regions offer physically separated and isolated Availability Zones connected by low-latency, high-throughput, and highly redundant networking. This architecture allows for seamless failover between Availability Zones without interruption, making applications and databases inherently more fault tolerant and scalable compared to traditional data center infrastructures. By using Availability Zones, Amazon SNS subscribers benefit from enhanced availability and reliability, guaranteeing message delivery despite potential disruptions. For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

Additionally, subscriptions to Amazon SNS topics can be configured with delivery retries and dead-letter queues, enabling automatic handling of transient failures and ensuring messages reliably reach their intended destinations.

Amazon SNS also supports message filtering and message attributes, which lets you tailor resilience strategies to their specific use cases, enhancing the overall robustness of your applications.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
