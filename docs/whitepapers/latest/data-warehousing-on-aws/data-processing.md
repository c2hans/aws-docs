---
source_url: https://docs.aws.amazon.com/whitepapers/latest/data-warehousing-on-aws/data-processing.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data processing
<a name="data-processing"></a>

 The collection process provides data that potentially has useful information. You can analyze the extracted information for intelligence that will help you grow your business. This intelligence might, for example, tell you about your user behavior and the relative popularity of your products. The best practice to gather this intelligence is to load your raw data into a data warehouse to perform further analysis.

 There are two types of processing workflows to accomplish this: *batch* processing and *real-time* processing. The most common forms of processing, online analytic processing (OLAP) and OLTP, each use one of these types. OLAP processing is generally batch-based. OLTP systems are oriented toward real-time processing, and are generally not well suited for batch-based processing. If you decouple data processing from your OLTP system, you keep the data processing from affecting your OLTP workload.

 First, let's look at what is involved in batch processing.

## Batch Processing
<a name="batch-processing"></a>
+  **Extract Transform Load (ETL)** — ETL is the process of pulling data from multiple sources to load into data warehousing systems. ETL is normally a continuous, ongoing process with a well-defined workflow. During this process, data is initially extracted from one or more sources. The extracted data is then cleansed, enriched, transformed, and loaded into a data warehouse. For batch ETL, use [AWS Glue](https://aws.amazon.com/glue/) or [Amazon EMR](https://aws.amazon.com/emr/). AWS Glue is a fully managed ETL service. You can create and run an ETL job with a few clicks in the [AWS Management Console](https://aws.amazon.com/console/). Amazon EMR is for big data processing and analysis. EMR offers an expandable, low-configuration service as an easier alternative to running in-house cluster computing.
+  **Extract Load Transform (ELT)** — ELT is a variant of ETL, where the extracted data is loaded into the target system first. Transformations are performed after the data is loaded into the data warehouse. ELT typically works well when your target system is powerful enough to handle transformations. Amazon Redshift is often used in ELT pipelines, because it is highly efficient in performing transformations.
+  **Online Analytical Processing (OLAP)** — OLAP systems store aggregated historical data in multidimensional schemas. Used widely for query, reporting, and analytics, OLAP systems enable you to extract data and spot trends on multiple dimensions. Because it is optimized for fast joins, Amazon Redshift is often used to build OLAP systems.

 Now let’s look at what’s involved in real-time processing of data.

## Real-time processing
<a name="real-time-processing"></a>

 We talked about streaming data earlier, and mentioned Amazon Kinesis Services and Amazon MSK as solutions to capture and store streaming data. You can process this data sequentially and incrementally on a record-by-record basis, or over sliding time windows. Use the processed data for a wide variety of analytics, including correlations, aggregations, filtering, and sampling. This type of processing is called *real-time* processing.

 Information derived from real-time processing gives companies visibility into many aspects of their business and customer activity, such as service usage (for metering or billing), server activity, website clicks, and geolocation of devices, people, and physical goods. This enables them to respond promptly to emerging situations. Real-time processing requires a highly concurrent and scalable processing layer.

 To process streaming data in real-time, use [AWS Lambda](https://aws.amazon.com/lambda/). Lambda can process the data directly from AWS IoT or [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/). Lambda enables you to run code without provisioning or managing servers.

 [Amazon Kinesis Client Library](https://docs.aws.amazon.com/streams/latest/dev/shared-throughput-kcl-consumers.html) (KCL) is another way to process data from Amazon Kinesis Streams. KCL gives you more flexibility than Lambda to batch your incoming data for further processing. You can also use KCL to apply extensive transformations and customizations in your processing logic.

 [Amazon Data Firehose](https://aws.amazon.com/kinesis/data-firehose/) is the easiest way to load streaming data into AWS. It can capture streaming data and automatically load it into Amazon Redshift, enabling near-real-time analytics with existing BI tools, and dashboards you’re already using today. Define batching rules with Firehose, and it takes care of reliably batching the data and delivering it to Amazon Redshift.

 [Amazon MSK](https://aws.amazon.com/msk/) is an easy way to build and run applications that use [Apache Kafka](https://aws.amazon.com/streaming-data/what-is-kafka/) to process streaming data. Apache Kafka is an open-source platform for building real-time streaming data pipelines and applications. With Amazon MSK, you can use native Apache Kafka APIs to populate data lakes, stream changes to and from databases, and power machine learning and analytics applications.

 [AWS Glue](https://aws.amazon.com/glue/) streaming jobs enable you to perform complex ETL on streaming data. Streaming ETL jobs in AWS Glue can consume data from streaming sources like Amazon Kinesis Data Streams and Amazon MSK, clean and transform those data streams in-flight, and continuously load the results into S3 data lakes, data warehouses, or other data stores. As you process streaming data in an AWS Glue job, you have access to the full capabilities of [Spark Structured Streaming](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html) to implement data transformations, such as aggregating, partitioning, and formatting, as well as joining with other data sets to enrich or cleanse the data for easier analysis.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
