---
source_url: https://docs.aws.amazon.com/memorydb/latest/devguide/scaling.html
---

# Scaling
<a name="scaling"></a>

The amount of data your application needs to process is seldom static. It increases and decreases as your business grows or experiences normal fluctuations in demand. If you self-manage your applications, you need to provision sufficient hardware for your demand peaks, which can be expensive. By using MemoryDB you can scale to meet current demand, paying only for what you use.

The following helps you find the correct topic for the scaling actions that you want to perform.

**Scaling MemoryDB**

| Action | MemoryDB |
| --- | --- |
| Scaling out | [Online resharding for MemoryDB](cluster-resharding-online.md) |
| Changing node types | [Online vertical scaling by modifying node type](cluster-vertical-scaling.md) |
| Changing the number of shards | [Scaling MemoryDB clusters](scaling-cluster.md) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
