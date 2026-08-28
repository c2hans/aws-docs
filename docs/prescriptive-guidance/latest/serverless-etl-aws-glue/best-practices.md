---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/best-practices.html
---

# Best practices
<a name="best-practices"></a>

When developing with AWS Glue, consider the following best practices.

## Develop locally first
<a name="run-locally"></a>

To save on cost and time while building your ETL jobs, test your code and business logic locally first. For instructions on setting up a Docker container that can help you test AWS Glue ETL jobs both in a shell and in an integrated development environment (IDE), see the blog post [Develop and test AWS Glue jobs locally using a Docker container](https://aws.amazon.com/blogs/big-data/develop-and-test-aws-glue-version-3-0-jobs-locally-using-a-docker-container/).

## Use AWS Glue interactive sessions
<a name="dev-endpoint"></a>

AWS Glue interactive sessions provide a serverless Spark backend, coupled with an open-source Jupyter kernel that integrates with notebooks and IDEs such as PyCharm, IntelliJ, and VS Code. By using interactive sessions, you can test your code on real datasets with the AWS Glue Spark backend and the IDE of your choice. To get started, follow the steps in [Getting started with AWS Glue interactive sessions](https://docs.aws.amazon.com/glue/latest/dg/interactive-sessions.html).

## Use partitioning to query exactly what you need
<a name="partitioning"></a>

*Partitioning* refers to dividing a large dataset into smaller partitions based on specific columns or keys. When data is partitioned, AWS Glue can perform selective scans on a subset of data that satisfies specific partitioning criteria, rather than scanning the entire dataset. This results in faster and more efficient query processing, especially when working with large datasets.

Partition data based on the queries that will be run against it. For example, if most queries filter on a particular column, partitioning on that column can greatly reduce query time. To learn more about partitioning data, see [Work with partitioned data in AWS Glue](https://aws.amazon.com/blogs/big-data/work-with-partitioned-data-in-aws-glue/).

## Optimize memory management
<a name="memory"></a>

Memory management is crucial when writing AWS Glue ETL jobs because they run on the Apache Spark engine, which is optimized for in-memory processing. The blog post [Optimize memory management in AWS Glue](https://aws.amazon.com/blogs/big-data/optimize-memory-management-in-aws-glue/) provides details on the following memory management techniques:
+ Amazon S3 list implementation of AWS Glue
+ Grouping
+ Excluding irrelevant Amazon S3 paths and storage classes
+ Spark and AWS Glue read partitioning
+ Bulk inserts
+ Join optimizations
+ PySpark user-defined functions (UDFs)
+ Incremental processing

## Use efficient data storage formats
<a name="storage-formats"></a>

When authoring ETL jobs, we recommend outputting transformed data in a column-based data format. Columnar data formats, such as Apache Parquet and ORC, are commonly used in big data storage and analytics. They are designed to minimize data movement and maximize compression. These formats also enable splitting data to multiple readers for increased parallel reads during query processing.

Compressing data also helps reduce the amount of data stored, and it improves read/write operation performance. AWS Glue supports multiple compression formats natively. For more information about efficient data storage and compression, see [Building a performance efficient data pipeline](https://docs.aws.amazon.com/whitepapers/latest/aws-glue-best-practices-build-performant-data-pipeline/building-a-performance-efficient-data-pipeline.html#file-formats-and-data-compression).

## Use the appropriate type of scaling
<a name="scaling"></a>

Understanding when to scale horizontally (change the number of workers) or scale vertically (change the worker type) is important for AWS Glue because it can impact the cost and performance of the ETL jobs.

Generally, ETL jobs with complex transformations are more memory-intensive and require vertical scaling (for example, moving from the G.1X to the G.2X worker type). For compute-intensive ETL jobs with large volumes of data, we recommend horizontal scaling because AWS Glue is designed to process that data in parallel across multiple nodes.

Closely monitoring AWS Glue job metrics in Amazon CloudWatch helps you determine whether a performance bottleneck is caused by a lack of memory or compute. For more information about AWS Glue worker types and scaling, see [Best practices to scale Apache Spark jobs and partition data with AWS Glue](https://aws.amazon.com/blogs/big-data/best-practices-to-scale-apache-spark-jobs-and-partition-data-with-aws-glue/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
