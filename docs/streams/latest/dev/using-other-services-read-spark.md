---
source_url: https://docs.aws.amazon.com/streams/latest/dev/using-other-services-read-spark.html
---

# Apache Spark
<a name="using-other-services-read-spark"></a>

Apache Spark is a unified analytics engine for large-scale data processing. It provides high-level APIs in Java, Scala, Python and R, and an optimized engine that supports general execution graphs. You can use Apache Spark to build stream processing applications that consume the data in your Kinesis data streams.

To consume Kinesis data streams using Apache Spark Structured Streaming, use the Amazon Kinesis Data Streams [connector](https://github.com/awslabs/spark-sql-kinesis-connector). This connector supports consumption with Enhanced Fan-Out, which provides your application with dedicated read throughput of up to 2 MB of data per second per shard. For more information, see [Developing Custom Consumers with Dedicated Throughput (Enhanced Fan-Out)](https://docs.aws.amazon.com/streams/latest/dev/enhanced-consumers.html).

To consume Kinesis data streams using Spark Streaming, see [Spark Streaming \+ Kinesis Integration](https://spark.apache.org/docs/latest/streaming-kinesis-integration.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
