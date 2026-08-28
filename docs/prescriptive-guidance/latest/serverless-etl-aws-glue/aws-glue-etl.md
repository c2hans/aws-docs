---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/aws-glue-etl.html
---

# AWS Glue ETL
<a name="aws-glue-etl"></a>

AWS Glue ETL supports extracting data from various sources, transforming it to meet your business needs, and loading it into a destination of your choice. This service uses the Apache Spark engine to distribute big data workloads across worker nodes, enabling faster transformations with in-memory processing.

AWS Glue supports a variety of data sources, including Amazon Simple Storage Service (Amazon S3), Amazon DynamoDB, and Amazon Relational Database Service (Amazon RDS). To learn more about supported data sources, see [Connection types and options for ETL in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect.html).

## Authoring in AWS Glue
<a name="authoring-etl"></a>

AWS Glue provides multiple ways to author ETL jobs, depending on your experience and use-case:
+ [Python shell jobs](https://docs.aws.amazon.com/glue/latest/dg/add-job-python.html) are designed for running basic ETL scripts written in Python. These jobs run on a single machine, and are better suited for small or medium-sized datasets.
+ [Apache Spark jobs](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming.html) can be written in either Python or Scala. These jobs use Spark to horizontally scale workloads across many worker nodes, so that they can handle large datasets and complex transformations.
+ [AWS Glue streaming ETL](https://docs.aws.amazon.com/glue/latest/dg/add-job-streaming.html) uses the Apache Spark Structured Streaming engine to transform streaming data in micro-batch jobs using [exactly-once](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#overview) semantics. You can author AWS Glue streaming jobs in either Python or Scala.
+ [AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/author-job-glue.html) is a visual boxes-and-arrows style interface to make Spark-based ETL accessible to developers who are new to Apache Spark programming.

## Data processing units
<a name="dpu-worker-type"></a>

AWS Glue uses data processing units (DPUs) to measure the compute resources allocated to an ETL job and calculate cost. Each DPU is equivalent to 4 vCPUs and 16 GB memory. DPUs should be allocated to your AWS Glue job depending on its complexity and data volume. [Allocating the appropriate amount of DPUs](https://docs.aws.amazon.com/glue/latest/dg/monitor-debug-capacity.html#monitor-debug-capacity-fix) will allow you to balance performance needs with cost constraints.

AWS Glue provides [several worker types](https://docs.aws.amazon.com/glue/latest/dg/add-job.html#create-job) that are optimized for various workloads:
+ G.1X or G.2X (for most data transforms, joins, and queries)
+ G.4X or G.8X (for more demanding data transforms, aggregations, joins, and queries)
+ G.025X (for low-volume and sporadic data streams)
+ Standard (for AWS Glue versions 1.0 or earlier; not recommended for later versions of AWS Glue)

## Using Python shell
<a name="python-shell"></a>

For a Python shell job, you can use either 1 DPU to use 16 GB of memory or 0.0625 DPU to use 1 GB of memory. Python shell is intended for basic ETL jobs with small or medium-sized datasets (up to approximately 10 GB).

## Comparing worker types
<a name="compare-worker-types"></a>

The following table shows the different AWS Glue worker types for batch, streaming, and AWS Glue Studio ETL workloads using the Apache Spark environment.

|  |
| --- |
|  | G.1X | G.2X | G.4X | G.8X | G.025X | Standard |
| --- |--- |--- |--- |--- |--- |--- |
| vCPU | 4 | 8 | 16 | 32 | 2 | 4 |
| Memory | 16 GB | 32 GB | 64 GB | 128 GB | 4 GB | 16 GB |
| Disk space | 64 GB | 128 GB | 256 GB | 512 GB | 64 GB | 50 GB |
| Executor per worker | 1  | 1 | 1 | 1 | 1 | 2 |
| DPU | 1 | 2 | 4 | 8 | 0.25 | 1 |

The Standard worker type is not recommended for AWS Glue version 2.0 and later. The G.025X worker type is available only for streaming jobs using AWS Glue version 3.0 or later.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
