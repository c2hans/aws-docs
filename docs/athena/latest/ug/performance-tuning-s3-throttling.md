---
source_url: https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-s3-throttling.html
---

# Prevent Amazon S3 throttling
<a name="performance-tuning-s3-throttling"></a>

Throttling is the process of limiting the rate at which you use a service, an application, or a system. In AWS, you can use throttling to prevent overuse of the Amazon S3 service and increase the availability and responsiveness of Amazon S3 for all users. However, because throttling limits the rate at which the data can be transferred to or from Amazon S3, it's important to consider preventing your interactions from being throttled.

As pointed out in the [performance tuning](performance-tuning.md) chapter, optimizations can depend on your service level decisions, on how you structure your tables and data, and on how you write your queries.

**Topics**
+ [Reduce throttling at the service level](performance-tuning-s3-throttling-reduce-throttling-at-the-service-level.md)
+ [Optimize your tables](performance-tuning-s3-throttling-optimizing-your-tables.md)
+ [Optimize your queries](performance-tuning-s3-throttling-optimizing-queries.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
