---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-trino-advanced.html
---

# Best practices for Trino on Amazon EMR
<a name="emr-trino-advanced"></a>

Trino’s architecture is designed for fast, distributed SQL queries on large datasets across multiple data sources, following a coordinator-worker model, where each component has a specialized role in query execution. There are a few areas or categories you can focus on in order to configure your Amazon EMR cluster running Trino for its best performance. These include the following:
+ Adjusting cluster configuration settings for memory optimization.
+ Optimizing settings for data partitioning and data distribution.
+ Using dynamic filtering to reduce query-result counts.

Some of these settings are tuned automatically when you use Trino with Amazon EMR. Others can be set manually through the console or through CLI commands. The topics in this section help you configure your data and your cluster optimally.

**Topics**
+ [Key areas of focus for performance improvement](emr-trino-performance-areas.md)
+ [Collect and Utilize table statistics](emr-trino-performance-areas-collect-stats.md)
+ [Common challenges when scaling Trino workloads](emr-trino-common-issues.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
