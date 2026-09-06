---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/aws-glue-data-catalog.html
---

# AWS Glue Data Catalog
<a name="aws-glue-data-catalog"></a>

The [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html) is a centralized metadata repository for all your data assets across various data sources. It provides a unified interface to store and query information about data formats, schemas, and sources. When an AWS Glue ETL job runs, it uses this catalog to understand information about the data and ensure that it is transformed correctly.

The [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html) is composed of the following components:
+ Databases and tables
+ Crawlers and classifiers
+ Connections
+ Schema Registry

## AWS Glue databases and tables
<a name="databases-tables"></a>

The [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html) is organized into [databases and tables](https://docs.aws.amazon.com/glue/latest/dg/tables-described.html) to provide a logical structure for storing and managing metadata. This structure supports precise data access control at a table or database level by using [AWS Identity and Access Management (IAM) policies](https://docs.aws.amazon.com/glue/latest/dg/security-iam.html).

An AWS Glue database can contain many tables, and each table must be associated with a single database. These tables contain references to the actual data, which can be stored in any of the various data sources that AWS Glue supports. AWS Glue tables also store essential metadata such as column names, data types, and partition keys.

There are several different methods for creating a table in AWS Glue:
+ AWS Glue crawler
+ AWS Glue ETL job
+ AWS Glue console
+ `CreateTable` operation in the [AWS Glue API](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api.html)
+ AWS CloudFormation template
+ AWS Cloud Development Kit (AWS CDK)
+ A migrated Apache Hive metastore

## AWS Glue crawlers and classifiers
<a name="crawlers-classifiers"></a>

An AWS Glue crawler automatically discovers and extracts metadata from a data store, and then it updates the AWS Glue Data Catalog accordingly. The crawler connects to the data store to infer the schema of the data. It then creates or updates tables within the Data Catalog with the schema information that it discovered. A crawler can crawl both file-based and table-based data stores. To learn more about supported data stores, see [Which data stores can I crawl?](https://docs.aws.amazon.com/glue/latest/dg/crawler-data-stores.html)

The crawler uses [classifiers](https://docs.aws.amazon.com/glue/latest/dg/add-classifier.html#classifier-when-used) to accurately recognize the format of data and determine how it should be processed. By default, the crawler uses a set of common [built-in classifiers](https://docs.aws.amazon.com/glue/latest/dg/add-classifier.html#classifier-built-in) provided by AWS Glue, but you can also [write custom classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html) to handle specific use-cases.

## AWS Glue connections
<a name="connections"></a>

You can use AWS Glue [connections](https://docs.aws.amazon.com/glue/latest/dg/console-connections.html) to define connection parameters that enable AWS Glue to connect to various data sources. Adding connections centralizes and simplifies the configuration required to connect to these sources.

When [defining a connection](https://docs.aws.amazon.com/glue/latest/dg/glue-connections.html), you specify the connection type, the connection endpoint, and any required credentials. After a connection is defined, it can be reused by multiple AWS Glue jobs and crawlers. Using connections with AWS Glue reduces the need to repeatedly enter the same connection information, such as login credentials or virtual private cloud (VPC) IDs.

## AWS Glue Schema Registry
<a name="schema-registry"></a>

The [AWS Glue Schema Registry](https://docs.aws.amazon.com/glue/latest/dg/schema-registry-gs.html) provides a centralized location for managing and enforcing data stream schemas. It enables disparate systems, such as data producers and consumers, to share a schema for serialization and deserialization. Sharing a schema helps these systems to communicate effectively and avoid errors during transformation.

The Schema Registry ensures that downstream data consumers can handle changes made upstream, because they are aware of the expected schema. It supports schema evolution, so that a schema can change over time while maintaining compatibility with previous versions of the schema.

The Schema Registry integrates with many AWS services, including Amazon Kinesis Data Streams, Firehose, and Amazon Managed Streaming for Apache Kafka. For examples of use cases and integrations, see [Integrating with AWS Glue Schema Registry](https://docs.aws.amazon.com/glue/latest/dg/schema-registry-integrations.html#schema-registry-integrations-amazon-msk).
