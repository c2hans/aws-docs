---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/data-sink-kinesis.html
---

# Data sink – Kinesis
<a name="data-sink-kinesis"></a>

 This data sink will stream the clickstream data collected by the ingestion endpoint into KDS. The guidance will create a KDS in your AWS account based on your specifications.

## Provision mode
<a name="provision-mode"></a>

 Two modes are available: **On-demand** and **Provisioned**
+  **On-demand**: In this mode, KDS shards are provisioned based on the workshop automatically. On-demand mode is suited for workloads with unpredictable and highly-variable traffic patterns.
+  **Provisioned**: In this mode, KDS shards are set at creation. The provisioned mode is suited for predictable traffic with capacity requirements that are easy to forecast. You can also use the provisioned mode if you want fine-grained control over how data is distributed across shards.
  +  Shard number: With the provisioned mode, you must specify the number of shards for the data stream. For more information, please refer to [provisioned mode](https://docs.aws.amazon.com/streams/latest/dev/how-do-i-size-a-stream.html#provisionedmode).

## Addtional settings
<a name="addtional-settings"></a>
+  **Sink maximum interval**: You can specify the maximum interval (in seconds) that records should be buffered before streaming to the AWS service.
+  **Batch size**: You can specify the maximum number of records to deliver in a single batch.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
