---
source_url: https://docs.aws.amazon.com/whitepapers/latest/data-warehousing-on-aws/modern-analytics-and-data-warehousing-architecture.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Modern analytics and data warehousing architecture
<a name="modern-analytics-and-data-warehousing-architecture"></a>

 Data typically flows into a data warehouse from transactional systems and other relational databases, and typically includes structured, semi-structured, and unstructured data. This data is processed, transformed, and ingested at a regular cadence. Users, including data scientists, business analysts, and decision-makers, access the data through BI tools, SQL clients, and other tools.

 So why build a data warehouse at all? Why not just run analytics queries directly on an online transaction processing (OLTP) database, where the transactions are recorded? To answer the question, let’s look at the differences between data warehouses and OLTP databases.
+  **Data warehouses** are optimized for batched write operations and reading high volumes of data.
+  **OLTP databases** are optimized for continuous write operations and high volumes of small read operations.

 Data warehouses generally employ denormalized schemas like the [Star schema and Snowflake schema](https://www.guru99.com/star-snowflake-data-warehousing.html) because of high data throughput requirements, whereas OLTP databases employ highly [normalized](http://agiledata.org/essays/dataNormalization.html) schemas, which are more suited for high transaction throughput requirements.

 To get the benefits of using a data warehouse managed as a separate data store with your source OLTP or other source system, we recommend that you build an efficient data pipeline. Such a pipeline extracts the data from the source system, converts it into a schema suitable for data warehousing, and then loads it into the data warehouse. In the next section, we discuss the building blocks of an analytics pipeline and the different AWS services you can use to architect the pipeline.

## AWS analytics services
<a name="aws-analytics-services"></a>

 AWS analytics services help enterprises quickly convert their data to answers by providing mature and integrated analytics services, ranging from cloud data warehouses to serverless data lakes. Getting answers quickly means less time building plumbing and configuring cloud analytics services to work together. AWS helps you do exactly that by giving you:
+  An easy path to build data lakes and data warehouses, and start running diverse analytics workloads.
+  A secure cloud storage, compute, and network infrastructure that meets the specific needs of analytic workloads.
+  A fully integrated analytics stack with a mature set of analytics tools, covering all common use cases and leveraging open file formats, standard SQL language, open-source engines, and platforms.
+  The best performance, the most scalability, and the lowest cost for analytics.

 Many enterprises choose cloud data lakes and cloud data warehouses as the foundation for their data and analytics architectures. AWS is focused on helping customers build and secure data lakes and data warehouses in the cloud within days, not months. [AWS Lake Formation](https://aws.amazon.com/lake-formation/) enables secured, self-service discovery and access for users. Lake Formation provides easy, on-demand access to specific resources that fit the requirements of each analytics workload. The data is curated and cataloged, already prepared for any type of analytics. Related records are matched and [de-duplicated](https://en.wikipedia.org/wiki/Data_deduplication) with machine learning.

 AWS provides a diverse set of analytics services that are deeply integrated with the infrastructure layers. This enables you to take advantage of features like intelligent tiering and [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2) spot instances, to reduce cost and run analytics faster. When you’re ready for more advanced analytic approaches, use our broad collection of machine learning (ML) and artificial intelligence (AI) services against that same data in S3 to gain even more insight without the delays and costs of moving or transforming your data.
