---
source_url: https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering-monitoring.html
---

# Data tiering monitoring
<a name="data-tiering-monitoring"></a>

MemoryDB offers metrics designed specifically to monitor the performance clusters that use data tiering. To monitor the ratio of items in DRAM compared to SSD, you can use the `CurrItems` metric at [Metrics for MemoryDB](metrics.memorydb.md). You can calculate the percentage as: `(CurrItems with Dimension: Tier = Memory * 100) / (CurrItems with no dimension filter)`.

 If the configured eviction policy allows, then MemoryDB will start evicting items when the percentage of items in memory decreases below 5 percent. On nodes configured with noeviction policy, write operations will receive an out of memory error.

 It is still recommended that you consider [Scaling MemoryDB clusters](scaling-cluster.md) when the percentage of items in memory decreases below 5 percent. For more information, see *Metrics for MemoryDB clusters that use data tiering* at [Metrics for MemoryDB](metrics.memorydb.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
