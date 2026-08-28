---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/minimize-planning-overhead.html
---

# Minimize planning overhead
<a name="minimize-planning-overhead"></a>

As discussed [Key topics in Apache Spark](key-topics-apache-spark.md), the Spark driver generates the execution plan. Based on that plan, tasks are assigned to the Spark executor for distributed processing. However, the Spark driver can become a bottleneck if there is a large number of small files or if the AWS Glue Data Catalog contains a large number of partitions. To identify high planning overhead, assess the following metrics.

## CloudWatch metrics
<a name="overhead-metrics"></a>

Check** CPU Load** and **Memory Utilization** for the following situations:
+ Spark driver **CPU Load** and **Memory Utilization** are recorded as high. Normally, the Spark driver doesn't process your data, so CPU load and memory utilization don't spike. However, if the Amazon S3 data source has too many small files, listing all the S3 objects and managing a large number of tasks might cause resource utilization to be high.
+ There is a long gap before processing starts in Spark executor. In the following example screenshot, the Spark executor's CPU Load is too low until 10:57, even though the AWS Glue job started at 10:00. This indicates that the Spark driver might be taking a long time to generate an execution plan. In this example, retrieving the large number of partitions in the Data Catalog and listing the large number of small files in the Spark driver is taking a long time.
![Graph showing driver and executors.](http://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/20b000ee-02ae-4653-8e07-2c9163c8ce47.png)

## Spark UI
<a name="overhead-spark"></a>

On the **Job** tab in the Spark UI, you can see the **Submitted** time. In the following example, the Spark driver started job0 at 10:56:46, even though the AWS Glue job started at 10:00:00.

![""](http://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/50c144d1-8b21-4df0-ba9f-e90342229208.png)

You can also see the **Tasks (for all stages): Succeeded/Total** time on the **Job** tab. In this case, the number of tasks is recorded as `58100`. As explained in the Amazon S3 section of the [Parallelize tasks](parallelize-tasks.md) page, the number of tasks approximately corresponds to the number of S3 objects. This means that there are about 58,100 objects in Amazon S3.

For more details about this job and timeline, review the **Stage** tab. If you observe a bottleneck with the Spark driver, consider the following solutions:
+ When Amazon S3 has too many files, consider the guidance on excessive parallelism in the *Too many partitions *section of the [Parallelize tasks](parallelize-tasks.md) page.
+ When Amazon S3 has too many partitions, consider the guidance on excessive partitioning in the *Too many Amazon S3 partitions *section of the [Reduce the amount of data scan](reduce-data-scan.md) page. Enable [AWS Glue partition indexes](https://docs.aws.amazon.com/glue/latest/dg/partition-indexes.html) if there are many partitions to reduce latency for retrieving partition metadata from the Data Catalog. For more information, see [Improve query performance using AWS Glue partition indexes](https://aws.amazon.com/blogs/big-data/improve-query-performance-using-aws-glue-partition-indexes/).
+ When JDBC has too many partitions, lower the `hashpartition` value.
+ When DynamoDB has too many partitions, lower the `dynamodb.splits` value.
+ When streaming jobs have too many partitions, lower the number of shards.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
