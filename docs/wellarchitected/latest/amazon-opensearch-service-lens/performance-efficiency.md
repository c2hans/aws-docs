---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/amazon-opensearch-service-lens/performance-efficiency.html
---

# Performance efficiency
<a name="performance-efficiency"></a>

The performance efficiency pillar refers to the ability to deliver optimal performance while efficiently using system resources. Amazon OpenSearch Service is designed to handle large-scale distributed search and analytics workloads, and achieving performance efficiency is crucial for delivering timely and responsive results. The following questions and best practices are designed to complement the best practices in the Well-Architected Performance Efficiency Pillar whitepaper.

**Topics**
+ [Design principles](#design-principles-perf)
+ [Architecture selection](architecture-selection.md)
+ [Data management](data-management.md)
+ [Process and culture](process-and-culture.md)
+ [Key AWS services](key-aws-services-perf.md)
+ [Resources](resources-perf.md)

## Design principles
<a name="design-principles-perf"></a>
+  **Optimize resource utilization:** Use resources efficiently by optimizing resource utilization through monitoring.
+  **Sharding effectiveness:** Use an effective sharding strategy based on your workload type.
+  **Optimize storage resources:** Optimize storage resources by distributing data evenly across data nodes.
+  **Optimize query efficiency:** Optimize query efficiency by monitoring search and indexing logs.
+  **Decide on optimal bulk request size:** Optimize bulk request size to improve data ingestion.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
