---
source_url: https://docs.aws.amazon.com/whitepapers/latest/derive-insights-from-aws-modern-data/why-use-aws-for-modern-data-analytics.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Why use AWS for Modern Data analytics?
<a name="why-use-aws-for-modern-data-analytics"></a>

 Customers build databases, data warehouses, and data lake solutions in isolation from each other, each having its own separate data ingestion, storage, management, and governance layers. These disjointed efforts to build separate data stores often end up creating data silos, data integration complexities, excessive data movement, and data consistency issues. These issues prevent customers from getting deeper insights. To overcome these issues and easily move data around, AWS introduced a [Modern Data approach](https://aws.amazon.com/blogs/big-data/harness-the-power-of-your-data-with-aws-analytics/).

 AWS provides a broad platform of managed services to help you build, secure, and seamlessly scale end-to-end data analytics applications quickly by using a Modern Data approach. There is no hardware to procure, no infrastructure to maintain and scale—only what you need to collect, store, process, and analyze your data. AWS offers analytical solutions specifically designed to handle this growing amount of data and provide insight into your business.

## AWS purpose-built analytics services
<a name="aws-purpose-built-analytics-services"></a>

 AWS gives you the broadest and deepest portfolio of purpose-built analytics services, including [Amazon Athena](https://aws.amazon.com/athena/?nc2=h_ql_prod_an_ath), [Amazon EMR](https://aws.amazon.com/emr/), [Amazon OpenSearch Service](https://aws.amazon.com/elasticsearch-service/), [Amazon Kinesis](https://aws.amazon.com/kinesis/), and [Amazon Redshift](https://aws.amazon.com/redshift/) for your unique analytics use cases. These services are all designed to be the best, which means you never have to compromise on performance, scale, or cost when using them.

 For example, [Amazon Redshift delivers up to three times better price performance than other cloud data warehouses](https://aws.amazon.com/blogs/big-data/get-up-to-3x-better-price-performance-with-amazon-redshift-than-other-cloud-data-warehouses/), and [Apache Spark on EMR runs 1.7 times faster than standard Apache Spark 3.0](https://aws.amazon.com/blogs/big-data/run-apache-spark-3-0-workloads-1-7-times-faster-with-amazon-emr-runtime-for-apache-spark/), which means petabyte-scale analysis can be run at less than half of the cost of traditional on-premises solutions.

![Picture showing Purpose-built analytics](https://docs.aws.amazon.com/whitepapers/latest/derive-insights-from-aws-modern-data/images/purpose-built-analytics.png)

## Scalable data lakes
<a name="scalable-data-lakes"></a>

 Tens of thousands of customers run their data lakes on AWS. Setting up and managing data lakes today involves a lot of manual and time-consuming tasks. [AWS Lake Formation](https://aws.amazon.com/lake-formation/) automates these tasks so [you can build and secure your data lake](https://aws.amazon.com/blogs/big-data/building-securing-and-managing-data-lakes-with-aws-lake-formation/) in days instead of months.

 For your data lake storage, [Amazon S3](https://aws.amazon.com/s3/) is the best place to build a data lake because it has:
+  Unmatched 99.999999999% of durability and 99.99% availability
+  The best security, compliance, and audit capabilities with object level audit logging and access control
+  The most flexibility with five storage tiers
+  The lowest cost with pricing that starts at less than $1 per TB per month

Amazon S3 gives you robust capabilities to manage access, cost, replication, and data protection.

![Diagram showing Scalable data lakes](https://docs.aws.amazon.com/whitepapers/latest/derive-insights-from-aws-modern-data/images/scalable-data-lakes.png)

## Performance and cost-effectiveness
<a name="performance-and-cost-effectiveness"></a>

 AWS is committed to providing the best performance at the lowest cost across all analytics services, and it is continually innovating to improve the price-performance of our services. In addition to industry-leading price performance for analytics services, S3 intelligent tiering saves you up to 70% on storage cost for data stored in your data lake. [Amazon EC2](https://aws.amazon.com/ec2/) provides access to an industry-leading choice of over 200 instance types, up to 100 billions of bits per second (Gbps) network bandwidth, and the ability to choose between on-demand, reserved, and spot instances.

 With [Amazon Redshift RA3 instances](https://aws.amazon.com/blogs/aws/amazon-redshift-update-next-generation-compute-instances-and-managed-analytics-optimized-storage/?&trk=em_a134p000006BjJ3AAK&trkCampaign=pac_q120_Redshift_RA3instances_blogpost&sc_channel=em&sc_campaign=) with managed storage, you can choose the number of nodes based on your performance requirements, and pay only for the managed storage that you use. [Advanced Query Accelerator](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-aqua.html) (AQUA) is an analytics query accelerator for Amazon Redshift that uses custom-designed hardware to speed up queries that scan large datasets. This hardware-accelerated cache enables Amazon Redshift to run up to ten times faster as it scales out and processes data in parallel across many nodes. Each node accelerates compression, encryption, and data processing tasks like scans, aggregates, and filtering.

## Seamless data movement
<a name="seamless-data-movement"></a>

 As the data in your data lakes and purpose-built data stores continues to grow, you need to be able to easily move a portion of that data from one data store to another. AWS enables you to combine, move, and replicate data across multiple data stores and your data lake.

 For example, [AWS Glue](https://aws.amazon.com/glue/) provides comprehensive data integration capabilities that make it easy to discover, prepare, and combine data for analytics, machine learning, and application development, while Amazon Redshift can easily query data in your S3 data lake.

![AWS Glue is a data integration ecosystem for building a Modern Data architecture faster](https://docs.aws.amazon.com/whitepapers/latest/derive-insights-from-aws-modern-data/images/glue-integration.png)

 Amazon Redshift and Amazon Athena both support federated queries, the ability to run queries across data stored in operational databases, data warehouses, and data lakes to provide insights across multiple data sources with no data movement and no need to set up and maintain complex extract, transform, and load (ETL) pipelines.

## Centralized governance
<a name="centralized-governance"></a>

 One of the most important pieces of a modern analytics architecture is the ability for customers to authorize, manage, and audit access to data. This can be challenging, because managing security, access control, and audit trails across all of the data stores in your organization is complex, time-consuming, and error-prone. With capabilities like centralized access control and policies, and column-level filtering of data, no other analytics provider gives you the governance capability to manage access to all of your data across your data lake and your purpose-built data stores from a single place.

With capabilities like centralized access control and policies combined with column and row-level filtering, AWS Lake Formation gives you the fine-grained access control and governance to manage access to data across a data lake and purpose-built data stores from a single point of control.

 AWS announced the preview of [row-level security for AWS Lake Formation](https://pages.awscloud.com/Lake_Formation_Feature_Preview.html), which makes it even easier to control access for all the people and applications that need to share data. Row-level security allows for filtering and setting data access policies at the row level.
