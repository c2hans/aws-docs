---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-s3-bp-throughput.html
---

# Throughput and data freshness
<a name="msk-data-delivery-s3-bp-throughput"></a>
+ Set a Amazon CloudWatch alarm on `DataFreshness` to detect when freshness degrades beyond your configured interval.
+ You can configure multiple Channels to read from the same topic without consuming broker throughput.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
