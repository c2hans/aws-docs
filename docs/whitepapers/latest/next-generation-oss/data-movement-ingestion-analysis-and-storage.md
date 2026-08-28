---
source_url: https://docs.aws.amazon.com/whitepapers/latest/next-generation-oss/data-movement-ingestion-analysis-and-storage.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data Movement, Ingestion, Analysis, and Storage
<a name="data-movement-ingestion-analysis-and-storage"></a>

 AWS provides you with managed services to help you ingest network data at scale, and move, analyze, and store the data. [Amazon Managed Streaming for Apache Kafka](https://aws.amazon.com/msk) (Amazon MSK) provides you with a path to migrate your Kafka Streams applications to AWS Cloud. Amazon MSK provides you with scaling capabilities while eliminating the effort taken to self-manage Apache Kafka brokers and its associated components.

 [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) (KDS) provides you with a serverless, scalable, and durable real-time data streaming service, allowing your OSS solution to ingest network events such as alarms, configuration changes, and signaling events. A Kinesis stream is comprised of one or more shard, where the latter is a uniquely-identified sequence of data records in a stream. The rate of data flowing through the stream is a function of the number of shards in a stream. Using prediction models, defined schedules, or monitored KPIs, you can perform *resharding* on a stream to maintain a data rate when a network condition obliges. For example, when a hurricane generates a large number of network alarms and service failures, *resharding* allows you to scale your stream to maintain the rate of data and support your Service Assurance applications.

 [AWS Glue](https://aws.amazon.com/glue) is a serverless data integration service that enables you to discover and prepare data to support your OSS application. For example, using AWS Glue, you can transform the format of data ingested from a newly-integrated network element into a format that is suitable for your Service Assurance, Domain Management, and/or Network Analytic solution. AWS Glue helps you build applications that automatically discover network elements, network services, and north-south-east-west application inputs.

 AWS provides you with [purpose-built, managed database services](https://aws.amazon.com/products/databases/) to support your OSS data structures and transactions needs. For example, [Amazon Neptune](https://aws.amazon.com/neptune) is a fully-managed graph database service that enables you to represent complex network service relationships, enabling your Service Assurance applications to detect network anomalies and misconfigurations, and provides your network engineering teams with recommendations. [Amazon Aurora](https://aws.amazon.com/rds/aurora) provides you with a MySQL and PostgreSQL-compatible relational database built for the cloud. Amazon Aurora is up to five times faster than standard MySQL databases and three times faster than standard PostgreSQL databases, providing you with the performance to enable your next-generation OSS solution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
