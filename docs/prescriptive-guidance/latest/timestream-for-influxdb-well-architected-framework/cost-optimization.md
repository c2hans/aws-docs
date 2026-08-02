---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/timestream-for-influxdb-well-architected-framework/cost-optimization.html
---

# Cost optimization pillar
<a name="cost-optimization"></a>

The [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-optimization.html) of the AWS Well-Architected Framework focuses on avoiding unnecessary costs and building architectures in a cost-optimized way. The following recommendations can help you meet the cost optimization design principles and architectural best practices for Amazon Timestream for InfluxDB.

The cost optimization pillar focuses on the following key areas:
+ Understanding your use case's requirements and costs
+ Selecting resources with attention to cost
+ Scaling to meet business needs without overspending
+ Right-sizing data storage and transfer

## Understanding your use case's requirements and costs
<a name="requirements-costs"></a>

We recommend not using Timestream for InfluxDB in the following use cases:
+ If your data model has relational data, Timestream for InfluxDB is not the right solution.
+ If you cannot use time filters in your queries, Influx will scan all series, which is inefficient.

## Selecting resources with attention to cost
<a name="select-resources"></a>

[InfluxDB instance](https://aws.amazon.com/timestream/pricing/) costs are based on an hourly rate for the hours that your instance runs. Instances make up, on average, 85 percent of the overall cost of running a database on AWS, so right-sizing can have significant cost implications. The best way to right-size instances is to test application performance:
+ Are the `CPUUtilization` and `MemoryUtilization` constantly high or low?
+ What is the balance between price and performance?

Instance costs scale linearly. The hourly cost of the `db.influx.2xlarge` instance is twice that of the `db.influx.xlarge` instance, although it also has twice the resource allocation. The `db.influx.16xlarge` instance is 16 times the hourly cost of the `db.influx.xlarge` instance.

Estimate your workload's number of writes and reads for a specific time frame (second, minute, hour, or day). Timestream for InfluxDB instances support 50,000 to more than 500,000 writes per second and 10‒100 queries per second (QPS) based on the instance type. For example, `db.influx.2xlarge` typically supports up to 150,000 writes per second and approximately 25 QPS. With an efficient data model and efficient querying, it can exceed that performance. If your requirements vary by the time of day, week, or month, you can schedule scaling up and down by doing the following:
+ [Create and schedule an AWS Lambda function](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-run-lambda-schedule.html).
+ Use a custom scheduler and run an API or an SDK to [scale up and down](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influx-managing-modifying-db.html) with some buffer time.

## Scaling to meet business needs without overspending
<a name="scaling"></a>

For entry-level experimentation with Timestream for InfluxDB, you can use `db.influx.medium` and `db.influx.large`. These instances are large enough for you to get experience with Timestream for InfluxDB before you invest in larger instances.

The `db.influx.medium` and `db.influx.large` instances are good for low-cost development environments. However, they have a smaller RAM (8 GiB and 16 GiB), fewer vCPUs (1 vCPU and 2 vCPUs), and network performance up to only 10 GB. Not all workloads are suitable for these instance classes. Monitor `CPUUtilization` and `MemoryUtilization`, and scale up or down as needed. There is often a consistent ratio between memory and vCPU. The db.influx instance class has a memory-to-vCPU ratio similar to the Amazon EC2 r7g instance class. We strongly recommend running end-to-end performance or load testing before going to production.

Efficient data modeling, batch writing, and optimized queries require less memory and compute usage. When less resources are required, you can potentially use smaller instances.

## Right-sizing data storage and transfer
<a name="right-sizing"></a>

For storing data, use the following best practices:
+ Store only time-series data in Timestream for InfluxDB.
+ Set appropriate retention on the InfluxDB bucket so that data older than the retention is deleted, and shards are periodically compacted automatically. For more information, see the [InfluxDB documentation](https://docs.influxdata.com/influxdb/v2/reference/internals/shards/#shard-compaction).
+ Optimize disk usage for future writes.
+ Delete any InfluxDB buckets that are not required for your workloads. InfluxDB supports deletes. You can perform scheduled cleanups if that fits your use case.

For data transfer, we recommend deploying your application in same AWS Region as your Timestream for InfluxDB database instance to avoid cross-Region network overhead. There might also be data transfer charges. For more information about data transfer, see the [pricing page](https://aws.amazon.com/timestream/pricing/).
