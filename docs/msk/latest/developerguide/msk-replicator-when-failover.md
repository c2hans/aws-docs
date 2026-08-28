---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-when-failover.html
---

# Failover to the secondary AWS Region
<a name="msk-replicator-when-failover"></a>

We recommend that you monitor replication latency in the secondary AWS Region using Amazon CloudWatch. During a service event in the primary AWS Region, replication latency may suddenly increase. If the latency keeps increasing, use the [AWS Service Health Dashboard](https://health.aws.amazon.com/health/status) to check for service events in the primary AWS Region. If there is a service event, you can failover to the secondary AWS Region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
