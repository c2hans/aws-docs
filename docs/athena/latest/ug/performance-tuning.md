---
source_url: https://docs.aws.amazon.com/athena/latest/ug/performance-tuning.html
---

# Optimize Athena performance
<a name="performance-tuning"></a>

This topic provides general information and specific suggestions for improving the performance of your Athena queries, and how to work around errors related to limits and resource usage.

Broadly speaking, optimizations can be grouped into service, query, and data structure categories. Decisions made at the service level, on how you write your queries, and on how you structure your data and tables can all influence performance.

**Topics**
+ [Optimize service use](performance-tuning-service-level-considerations.md)
+ [Optimize queries](performance-tuning-query-optimization-techniques.md)
+ [Optimize data](performance-tuning-data-optimization-techniques.md)
+ [Use columnar storage formats](columnar-storage.md)
+ [Use partitioning and bucketing](ctas-partitioning-and-bucketing.md)
+ [Partition your data](partitions.md)
+ [Use partition projection with Amazon Athena](partition-projection.md)
+ [Prevent Amazon S3 throttling](performance-tuning-s3-throttling.md)
+ [Additional resources](performance-tuning-additional-resources.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
