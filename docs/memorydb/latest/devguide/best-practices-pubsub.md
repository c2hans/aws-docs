---
source_url: https://docs.aws.amazon.com/memorydb/latest/devguide/best-practices-pubsub.html
---

# Best practices: Pub/Sub and Enhanced I/O Multiplexing
<a name="best-practices-pubsub"></a>

When using Valkey or Redis OSS version 7 or later, we recommend using [sharded Pub/Sub](https://valkey.io/topics/pubsub/). You also improve throughput and latency using [enhanced I/O multiplexing](https://aws.amazon.com/memorydb/features/#Ultra-fast_performance), which is automatically available when using Valkey or Redis OSS version 7 or later and requires no client changes. It is ideal for pub/sub workloads, which often are throughput-bound with multiple client connections.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
