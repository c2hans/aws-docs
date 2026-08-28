---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-iceberg-ts-throughput.html
---

# Throughput exceeds the supported limit
<a name="msk-data-delivery-iceberg-ts-throughput"></a>
+ **Symptom:** Data freshness climbs or delivery slows during sustained high-throughput periods.
+ **Causes:** The source throughput exceeds what the Channel can deliver at the configured freshness.
+ **Resolution:** Reduce the source produce rate, increase the configured data freshness, or distribute load across multiple topics/Channels. Monitor `DataFreshness` and the `BytesIn` / `BytesOut` metrics to confirm the delivery path keeps up. See the throughput figures in [Amazon MSK Data Delivery quotas](limits.md#msk-data-delivery-quota).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
