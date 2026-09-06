---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-building-data-lake-for-games/data-cataloging.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data cataloging
<a name="data-cataloging"></a>

 Data catalogs have become a core component and central technology for modern data management and governance. They are essential for data sharing and self-service analytics enablement, increasing the business value of data and analytics. According to the [Gartner research report](https://www.gartner.com/en/documents/3957301):

 “Demand for data catalogs is soaring as organizations continue to struggle with finding, inventorying and analyzing vastly distributed and diverse data assets. Data and analytics leaders must investigate and adopt ML-augmented data catalogs as part of their overall data management solutions strategy."

 Successful data catalog implementations empower organizations to continuously improve the speed and quality of data analysis, and better achieve data democratization and productive use of data across the organization. Therefore, choosing the right data catalog technology to implement is an important decision to make while designing a data lake on AWS for games.

 A *data catalog* is a collection of metadata, combined with data discovery and management tools, and it provides an inventory of data assets across all your data sources. Data catalog helps data consumers within an organization to discover, understand, and consume data more productively. It helps organizations break down barriers to data lake adoption. A properly maintained data catalog empowers data analysts and users to work in self-service mode to discover trustworthy data quickly, evaluate and make informed decisions for which datasets to use, and perform data preparation and analysis efficiently and with confidence.

 Given multiple frameworks, tools and technologies can be employed within a data lake environment for data ingestion, transformation, visualization, and access control. The most efficient way to accomplish this is to maintain a central data catalog and use it across various frameworks such as AWS Glue, Amazon EMR, Amazon Athena, Apache Hadoop, Apache Spark, Hive, Impala, and [Presto](https://aws.amazon.com/big-data/what-is-presto/) on AWS. This makes the job of ensuring metadata integrity and applying data governance policies relatively easier.

## Use AWS Glue Data Catalog as a metadata store for your data lake
<a name="use-aws-glue-data-catalog-as-a-metadata-store-for-your-data-lake"></a>

 The [AWS Glue Data Catalog](https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/aws-glue-data-catalog.html) is a fully-managed persistent metadata store allowing you to store, annotate, and share metadata. It provides a unified metadata repository across a variety of data sources and data formats, integrating with Amazon EMR as well as Amazon RDS, Amazon Redshift and Redshift Spectrum, Amazon Athena, [AWS Lake Formation](https://aws.amazon.com/lake-formation/), and any application compatible with the Apache Hive metastore.

 With AWS Glue Data Catalog, you can store and find metadata, keep track of data in data silos, and use that metadata to query and transform the data. AWS Glue Data Catalog also provides comprehensive audit and governance capabilities with schema change tracking and data access controls, allowing you to audit changes to data schemas. This helps ensure that data is not inappropriately modified or inadvertently shared.

AWS Glue Data Catalog can be extended to meet many of your data cataloging requirements and needs. Sources for AWS Glue Data Catalog tables can include Amazon S3, Amazon Kinesis, [Amazon DocumentDB](https://aws.amazon.com/documentdb/), Amazon DynamoDB, Amazon Redshift, MongoDB, Apache Kafka, Java Database Connectivity (JDBC), and so on. Custom database and table descriptions and table properties can be added to the catalog either manually or through automation. For example, you can add the data owner, data description, and data sensitivity to AWS Glue tables.

 The AWS Glue Data Catalog is an index to the location, schema, and runtime metrics of your data. You can use the information in the Data Catalog to create and monitor your ETL jobs. Each AWS account can have one AWS Glue Data Catalog per AWS Region. Information in the Data Catalog is stored as metadata tables, where each table specifies a single data store. Typically, you run a crawler to take inventory of the data in your data stores, but there are other ways to add metadata tables into your Data Catalog. For information about how to use the AWS Glue Data Catalog, refer to [Populating the AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html).

![A diagram depicting how AWS Glue crawlers interact with data stores and other elements to populate the Data Catalog.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-building-data-lake-for-games/images/crawlers.png)

 When configuring the AWS Glue crawler to discover data in Amazon S3, you can choose from a full scan, where all objects in a given path are processed every time the crawler runs, or an incremental scan, where only the objects in a newly added folder are processed.

 Full scan is useful when changes to the table are non-deterministic and can affect any object or partition. Incremental crawl is useful when new partitions, or folders, are added to the table. For large, frequently changing tables, the incremental crawling mode can be enhanced to reduce the time it takes the crawler to determine which objects changed.

 With the support of [Amazon S3 Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/NotificationHowTo.html) as a source for AWS Glue crawlers, game developers can configure [Amazon S3 Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/NotificationHowTo.html) to be sent to an [Amazon Simple Queue Service](https://aws.amazon.com/sqs/) (Amazon SQS) queue, which the crawler uses to identify the newly added or deleted objects. With each run of the crawler, the SQS queue is inspected for new events, if none are found, the crawler stops. If events are found in the queue, the crawler inspects their respective folders and processes the new objects. This new mode reduces the cost and time a crawler needs to update large and frequently changing tables.

 Using Amazon EMR, you can configure Spark SQL to use the AWS Glue Data Catalog as its metastore. AWS recommends this configuration when you require a persistent metastore, or a metastore shared by different clusters, services, applications, or AWS accounts. [AWS Glue Data Catalog Client for Apache Hive Metastore](https://github.com/awslabs/aws-glue-data-catalog-client-for-apache-hive-metastore) is an open-source implementation of the Apache Hive Metastore client on Amazon EMR clusters that uses the AWS Glue Data Catalog as an external Hive Metastore. It serves as a reference implementation for building a Hive Metastore-compatible client that connects to the AWS Glue Data Catalog. It may be ported to other Hive Metastore-compatible platforms such as other Hadoop and Apache Spark distributions. You can migrate from Apache Hive metastore to AWS Glue Data Catalog. For more information, refer to [Migration between the Hive Metastore and the AWS Glue Data Catalog](https://github.com/aws-samples/aws-glue-samples/tree/master/utilities/Hive_metastore_migration) on GitHub.

 Because AWS Glue Data Catalog is used by many AWS services as their central metadata repository, you might want to query Data Catalog metadata. To do so, you can use SQL queries in Athena. You can use Athena to query AWS Glue catalog metadata such as databases, tables, partitions, and columns. For more information, refer to [Querying AWS Glue Data Catalog](https://docs.aws.amazon.com/athena/latest/ug/querying-glue-catalog.html).

 You can use [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) policies to control access to the data sources managed by the AWS Glue Data Catalog. These policies allow different groups in your enterprise to safely publish data to the wider organization while protecting sensitive information. IAM policies let you clearly and consistently define which users have access to which data, regardless of its location.

## Other options for data catalog
<a name="other-options-for-data-catalog"></a>

 If AWS Glue Data Catalog does not satisfy all of your business and technical requirements for data cataloging purpose, there are other enterprise-grade solutions available on the [AWS Marketplace](https://aws.amazon.com/marketplace) such as [Informatica](https://aws.amazon.com/marketplace/pp/prodview-yijhlpeolwv3k?ref_=beagle&applicationId=AWSMPContessa), [Alation](https://aws.amazon.com/marketplace/pp/prodview-k7yq2uauhjxgu?ref_=beagle&applicationId=AWSMPContessa), and [unifi](https://aws.amazon.com/marketplace/pp/prodview-dc4yyvgbvvln4?ref_=beagle&applicationId=AWSMPContessa) for your evaluation. Those solutions can also help you create and maintain a business glossary for mapping to the underlying tables and columns. Some of them provide connectors to integrate with native AWS Cloud services such as AWS Glue Data Catalog, Amazon S3, Athena, DynamoDB, and Amazon Redshift.

 Additionally, there are also many open-source metadata management solutions for improving the productivity of data consumers and accelerate time to insights. For example, [Apache Atlas](https://atlas.apache.org/#/), [Amundsen](https://github.com/amundsen-io/amundsen), [Metacat](https://github.com/Netflix/metacat), [Herd](https://finraos.github.io/herd/), and [Databook](https://eng.uber.com/databook/).
