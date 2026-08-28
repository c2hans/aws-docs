---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost04-bp02.html
---

# ADVCOST04-BP02 Consider multi-level caching for user profile data
<a name="advcost04-bp02"></a>

 DynamoDB Accelerator provides a powerful, cost-effective solution for caching user profile data by dramatically reducing read latency and minimizing direct database operations. By creating an in-memory caching layer, DAX can reduce DynamoDB read capacity unit (RCU) consumption, translating to significant cost savings for applications with high-frequency profile lookups. For user profile systems with repetitive access patterns, DAX automatically caches frequently retrieved items, delivering microsecond-level response times while substantially lowering infrastructure expenses.

 The intelligent caching mechanism avoids redundant database queries, allowing organizations to optimize their database performance without complex manual caching implementations, making it an ideal solution for scalable, cost-conscious applications that require rapid access to user information.

 Moreover, the seamless integration of DAX with existing DynamoDB architectures means minimal code changes are required to achieve these performance and cost benefits, providing an efficient path to enhanced application responsiveness and reduced operational costs.

1.  Create a DAX Cluster:

   1.  Select the same VPC as DynamoDB table

   1.  Select node type (recommend r5.large for medium workloads)

   1.  Configure cluster size (minimum 3 nodes for high availability)

   1.  Set cache TTL

1.  Modify application code to support DAX

1.  Caching strategy implementation:

   1.  Configure cache invalidation mechanisms

   1.  Implement write-through or write-behind strategies

   1.  Set appropriate TTL for cached items

1.  Monitoring and optimization: CloudWatch metrics to track

   1.  Cache hit or miss ratio

   1.  Latency

   1.  Consumed read capacity

   1.  Error rates

   1.  Recommended monitoring dashboard

1.  Performance and cost optimization tuning:

   1.  Adjust cluster size based on traffic

   1.  Use reserved instances

   1.  Implement intelligent caching

   1.  Monitor and adjust regularly

## Resources
<a name="resources-72"></a>
+  [Reduce latency and cost in read-heavy applications using Amazon DynamoDB Accelerator](https://aws.amazon.com/blogs/database/reduce-latency-and-cost-in-read-heavy-applications-using-amazon-dynamodb-accelerator/)

## Key AWS services
<a name="key-aws-services-49"></a>
+  DynamoDB Accelerator
+  ElastiCache (Redis OSS)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
