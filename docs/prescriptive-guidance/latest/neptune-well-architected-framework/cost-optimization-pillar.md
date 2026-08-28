---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/neptune-well-architected-framework/cost-optimization-pillar.html
---

# Cost optimization pillar
<a name="cost-optimization-pillar"></a>

The [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-optimization.html) of the AWS Well-Architected Framework focuses on avoiding unnecessary costs. The following recommendations can help you meet the cost optimization design principles and architectural best practices for Amazon Neptune.

The cost optimization pillar focuses on the following key areas:
+ Understanding spending over time and controlling fund allocation
+ Selecting resources of the right type and quantity
+ Scaling to meet business needs without overspending

## Understand usage patterns and services needed
<a name="usage"></a>

Neptune is a good fit for your workload if your data model has a discernible graph structure, and your queries need to explore relationships and traverse multiple hops. A graph database isn't a good fit for the following patterns:
+ Mainly single-hop queries (consider whether your data might be better represented as attributes of an object)
+ JSON or BLOB data stored as properties
+ Queries that aggregate across a dataset, such as calculating the sum of a numeric property across a large number of nodes

Consider whether using several purpose-built databases together for specific access patterns might address all of your needs. For example:
+ An API that requires less frequent complex graph navigations alongside highly concurrent retrieval of properties for a single node might be best presented by using one or more of Neptune, DynamoDB, or Amazon DocumentDB.
+ Relational databases can co-exist with Neptune to maintain your existing functionality, but use Neptune only for multiple-hop traversals that do not perform and scale well in relational databases.

Understand the costs associated with services that interact with and complement Neptune, including the following:
+ Amazon Simple Storage Service (Amazon S3) storage costs for data files being bulk loaded into Neptune
+ Lambda functions used for insert or upsert queries, read queries, and Neptune streams processing
+ The API layer built on Neptune to interact with the client application (instead of having direct connections to the database) in Amazon API Gateway or AWS AppSync
+ AWS Glue jobs used to transfer data to and from Neptune
+ Amazon Kinesis or Amazon Managed Streaming for Apache Kafka (Amazon MSK) instances receiving streaming data for near real-time ingestion into Neptune.
+ AWS Database Migration Service for migration of relational data to Neptune
+ Amazon SageMaker Runtime costs for Jupyter notebooks and deep graph library machine learning models

## Select resources with attention to cost
<a name="attention"></a>

[Neptune pricing](https://aws.amazon.com/neptune/pricing/) is based on hourly instance cost (or Neptune Compute Units consumed for serverless), data I/O, and storage usage. Instances make up, on average, 85 percent of the overall cost, so right-sizing can have significant cost implications. The best way to right-size instances is to test application performance on a variety of instances and compare following factors:
+ Does the `MainRequestQueuePendingRequests` CloudWatch metric stay at a consistently low number near zero?
+ Does the `BufferCacheHitRatio` CloudWatch metric stay at or above 99.9 percent a majority of the time?
+ What are the cost and performance curves for instance costs and for associated data I/O costs? Data read costs might increase significantly with an undersized instance that requires frequent buffer cache swapping with storage. `BufferCacheHitRatio` will be dropping frequently in these scenarios.

Instance costs scale linearly with size within the same instance family. The hourly cost of the `db.r6i.2xlarge` instance is twice that of the `db.r6i.xlarge` instance and also has twice the resource allocation. The `db.r6i.24xlarge` instance is 24 times the hourly cost of the `db.r6i.xlarge` instance.

Estimate the number of concurrent queries you must support. You can have between zero and fifteen read replicas for processing read-only queries. If your requirements vary by the time of day, week, or month, you can use multiple smaller instances to scale on a schedule. Each vCPU on an instance provides two threads for handling concurrent queries. Three `db.r6i.xlarge` read replicas, with 4 vCPU each, can handle 24 concurrent queries..

If your traffic volume is instead measured in queries per second (QPS), you must experiment to determine the average latency of your queries. The number of queries per second a Neptune cluster can support is equal to `vCPU × 2 × (1 second/average query latency)`. For example, if you have 4 vCPU and query latency of 100 milliseconds (0.1 second), `QPS = 4 × 2 × (1s/0.1s) = 80 queries per second`.

Provisioned instances are cheaper than serverless for continuous, stable, and predictable workloads. Serverless provides opportunities for optimizing costs when you have a workload that requires very high usage for just a few hours per day (for example, `db.r6i.4xlarge`) and then almost no traffic for the remainder of the day (for example, 1 Neptune Compute Unit). A serverless instance that scales up for a few hours and then back down will be less expensive than using a provisioned `db.r6i.4xlarge` instance all day.

Consider upgrading to Neptune 1.4.5.0 or later and utilizing `r8g` instances to achieve better read and write throughput at a lower cost than older generation instances, such as `r7g` or `r6g`. For more information, see [4.7 times better write query price-performance with AWS Graviton4 R8g instances using Amazon Neptune v1.4.5](https://aws.amazon.com/blogs/database/4-7-times-better-write-query-price-performance-with-aws-graviton4-r8g-instances-using-amazon-neptune-v1-4-5/) (AWS blog post).

Neptune clusters are created by default with [standard storage](https://docs.aws.amazon.com/neptune/latest/userguide/storage-types.html) (if you create using the console, it will default to selecting I/O-optimized storage). With I/O-optimized storage, you pay a slightly higher cost for storage and instances, but there are no I/O costs. This leads to more predictable recurring costs, but if your I/O usage is generally low, it may be more cost efficient to utilize standard storage. If you intend to load a lot of data initially, you can optimize cost by choosing I/O-optimized storage, performing your initial data load, and then switch to standard storage. The storage type affects the billing model only and has no technical difference in the Neptune DB cluster or instance configuration. You can change the storage type once per 30 days. After 30 days, check your detailed Neptune costs and use the [Neptune pricing page](https://aws.amazon.com/neptune/pricing/) to calculate whether your costs would have been higher using I/O-optimized storage. If they would have been, continue to use standard storage, otherwise switch back to I/O-optimized.

## Choose the best Neptune instance configuration for your workload
<a name="instance-configuration"></a>

If you created your AWS account before July 15th, 2025, you can use the [AWS Free Tier ](https://aws.amazon.com/free/legacy/)for entry-level experimentation with Neptune. The 750 free hours of `db.t3.medium` and `db.t4g.medium` instance usage are enough for you to get a good understanding of Neptune at low scale. Your cluster will remain after the free trial period ends, although you will be charged for usage going forward from that point.

The `db.t3.medium` and `db.t4g.medium` instances are good for low-cost development environments where you are not using openCypher, Graph Explorer, or various generative AI integrations. These instances have a smaller RAM-to-vCPU ratio (2:1) than the `R` family instances (8:1) or `X` family instances (16:1). This reduces ratio prevents the use of [DFE engine statistics](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-dfe-statistics.html) that enable openCypher performance, GenAI integrations (to inform the LLM of the graph schema), and Graph Explorer. Performance profiles might differ significantly when using `T` family instances, especially for the previously mentioned workloads. These instances can also increase the occurrence of `OutOfMemoryExceptions` when queries navigate across a significant portion of the graph. To determine whether the latter condition might be affected, check the `BufferCacheHitRatio` CloudWatch metric.

We strongly advise against doing any performance or load testing with `T` family instances because you might experience inconsistent results that are not indicative of a production environment.

Provisioned instances give you the best cost and performance combination when your workload is fairly stable and predictable. Choose the instance size based on the request concurrency required and the query complexity. Higher concurrency requires more vCPUs. Higher query complexity requires more RAM. Use the `MainRequestQueuePendingRequests` CloudWatch metric to determine the impact of the former (greater than zero represents more concurrent requests than can be handled). Use the `BufferCacheHitRatio` CloudWatch metric to determine the impact of the latter. A ratio that is frequently falling lower than 99.9 percent suggests that there isn't enough RAM to contain the working portion of the graph being evaluated, which results in more frequent cache swapping. If the R family of instances provides sufficient concurrency but not enough RAM, consider trying the `X` family of instances.

Ideal use cases for serverless instances are described in the [Neptune documentation](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-serverless.html#neptune-serverless-uses). If you are unsure whether provisioned or serverless is best for you, and cost is your primary concern, test your workload in serverless to determine the number of NCUs used and compare the cost of provisioned (`N hours × hourly provisioned cost`) with serverless (`sum of NCUs × hourly cost per NCU`). If you are unsure about the equivalent sized provision instance, one NCU is equivalent to approximately 2 GB of RAM and associated vCPU and networking. If your provisioned instance is from the `r6i` family, the ratio is 1 vCPU per 8 GB of RAM, or 4 NCUs, along with associated networking. The [Amazon Neptune Pricing Calculator](https://pricingcalc.neptunedemos.com/) also provides a comparison to help you decide your optimal cost configuration.

When using serverless for primary and replica instances, remember that read replicas in promotion tiers 0 and 1 will scale their NCUs in line with the writer instance so that they are properly scaled if a failover event occurs. Set your NCU limits for these instances based on which of your instances—writer or readers—receive the most traffic.

In environments where the cluster is not needed 24 hours per day, 7 days a week, consider writing scripts that will turn off the Neptune instances when not in use and start them again before they are used. Neptune instances will automatically restart every 7 days to ensure required maintenance updates are applied. If you intend to leave the instances off for long durations, use a weekly script to shut them down again.

## Right-size data storage and transfer
<a name="storage-transfer"></a>

More efficient queries (for example, queries that need to touch fewer nodes, edges, and properties in the graph) require less I/O transfer and potentially can make use of smaller instances because less buffer cache is required. Use the profile or explain endpoints for your query language to optimize your query, and consider optimizing your graph model for your query performance.

Neptune uses dictionary encoding on large strings, and that dictionary is optimized for performance, not efficiency. If you have large BLOBs, JSON, or frequently changing strings for properties, consider storing them outside Neptune in Amazon S3, Amazon DynamoDB, or Amazon DocumentDB, and store only a reference within the Neptune node.

In some cases, choosing a larger instance size can be cheaper. If your I/O costs are very high because of a low `BufferCacheHitRatio`, it's possible that the larger buffer cache would significantly reduce that cost. That's because all of the data would fit in the cache instead of being frequently swapped from storage and incurring the I/O transfer rate.

Neptune uses copy-on-write cloning. When cloning to split a graph into multiple shards, it might be more efficient not to delete the unwanted data on the cloned cluster because that will involve the creation of new data pages, resulting in increased storage costs. Data that is unchanged from before the cloning event will exist in a single data page shared across the two clusters and will be charged only for that single copy.

Do not enable the OSGP index or use R5d instances unless you have tested to confirm that they make a substantial difference in your workload. Both are designed for rarely occurring scenarios, and they might increase your costs for minimal or no gains.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
