---
source_url: https://docs.aws.amazon.com/whitepapers/latest/genomics-data-transfer-analytics-and-machine-learning/performing-tertiary-analysis-with-data-lakes-using-aws-glue-and-amazon-athena.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Performing tertiary analysis with data lakes using AWS Glue and Amazon Athena
<a name="performing-tertiary-analysis-with-data-lakes-using-aws-glue-and-amazon-athena"></a>

 Genomic tertiary analysis can be performed on data in an Amazon S3 data lake using AWS Glue, Amazon Athena, and Amazon SageMaker AI Jupyter notebooks.

## Recommendations
<a name="recommendations-2"></a>

 When building and operating a genomics data lake in AWS, consider the following recommendations to optimize data lake operations, performance, and cost.

 **Use AWS Glue extract, transform, and load (ETL) jobs, crawlers, and triggers to build your data workflows**—AWS Glue is a fully managed ETL service that makes it easy for you to prepare and load data for analytics. You can create Spark jobs to transform data, Python jobs to perform PHI and virus scans, crawlers to catalog the data, and workflows to orchestrate data ingestion, all within the same service.

 **Use AWS Glue Python jobs to integrate with external services**—Use Python shells in AWS Glue to execute tasks in workflows that require callouts to external services such as running a virus scan or a personal health information (PHI) scan.

 **Use AWS Glue Spark ETL to transform data**—AWS Glue Spark jobs make it easy to run a complex data processing job across a cluster of instances using Apache Spark.

 **Promote data across S3 buckets, multiple accounts are not necessary**—Use different Amazon S3 buckets to implement different access controls and auditing mechanisms as data is promoted through your data ingestion pipeline, such as, quarantine, pre-curated, and curated. Segregating data across accounts is not necessary.

 **For interactive queries, use Amazon Athena or Amazon Redshift**— Query data residing in Amazon S3 using either Amazon Redshift or Athena. Amazon Redshift efficiently queries and retrieves structured and semi-structured data from files in Amazon S3 by leveraging Redshift Spectrum Request Accelerator to improve performance. Athena is a serverless engine for querying data directly in Amazon S3. Users who already have Amazon Redshift can extend their analytical queries to Amazon S3 by pointing to their AWS AWS Glue Data Catalog. Users who are looking for a fast, serverless analytics query engine for data on Amazon S3 can use Athena. Many customers use both services to meet diverse use cases.

 **For queries that require low latency such as dashboards, use Amazon Redshift**—Amazon Redshift is a large-scale data warehouse solution ideal for big data, and low latency queries, such as dashboard queries.

 **Use partitions and the AWS Glue Data Catalog for data changes instead of creating new databases**—Use table partitions in an AWS Glue Data Catalog to accommodate multiple versions of a dataset with minimal overhead and operational burden.

 **Design data access around least privileges and provide data governance using AWS Lake Formation**—Limit data lake users to select permissions only. Service accounts used for ETL may have create/update permissions for tables.

 **Use a tenant/year/month/day partitioning scheme in Amazon S3 to support multiple data providers**—Data producers provide recurring delivery of datasets that need to be ingested, processed, and made available for query. Partitioning the incoming datasets by tenant/year/month/day allows you to maintain versions of datasets, lifecycle the data over time, and re-ingest older datasets, if necessary.

 **Use data lifecycle management in Amazon S3 to lifecycle data and restore, if needed**—Manage your data lake objects for cost effective storage throughout their lifecycle. Archive data when it is no longer being used and consider Amazon S3 Intelligent-Tiering if the access patterns are unpredictable.

 **Convert your datasets to parquet format to optimize query performance**—Parquet is a compressed, columnar data format optimized for big data queries. Analytics services that support columnar format only need to read accessed columns which greatly reduces I/O and speed of data processing.

 **Treat configuration as code for jobs and workflows**—Fully automate the building and deployment of ETL jobs and workflows to more easily move your genomics data into production. Automation provides control and a repeatable development process for handling your genomics data.

## Reference architecture
<a name="reference-architecture-2"></a>

![Tertiary analysis with data lakes reference architecture](http://docs.aws.amazon.com/whitepapers/latest/genomics-data-transfer-analytics-and-machine-learning/images/image4.png)

1.  A CloudWatch Events triggers an ingestion workflow for variant or annotation files into the Amazon S3 genomics data lake.

1.  A bioinformatician uses a Jupyter notebook to query the data in the data lake using Amazon Athena with the [PyAthena](https://pypi.org/project/PyAthena/) python driver. Queries can also be performed using the Amazon Athena console, AWS CLI, or an API.

 Processing and ingesting data into your Amazon S3 genomics data lake starts with triggering the data ingestion workflows to run in AWS Glue. Workflow runs are triggered through the AWS Glue console, the AWS CLI, or using an API within a Jupyter notebook. You can use a Glue ETL job to transform annotation datasets like Clinvar from TSV format to Parquet format and write the Parquet files to a data lake bucket.

 You can convert VCF to Parquet in an Apache Spark ETL job by using open-source frameworks like Hail to read the VCF into a Spark data frame and then write the data as Parquet to your data lake bucket. Use AWS Glue crawlers to crawl the data lake dataset files, infer their schema, and create or update a table in your AWS Glue data catalog, making the dataset available for query with Amazon Redshift or Amazon Athena.

 To run AWS Glue jobs and crawlers in a workflow, use AWS Glue triggers to stitch together workflows, then start the trigger. To run queries on Amazon Athena, use the Amazon Athena console, AWS CLI, or an API. You can also run Athena queries from within Jupyter notebooks using the PyAthena python package that can be installed using pip.

 Optimizing data lake query cost and performance are important considerations when working with large amounts of genomics data. To learn more about optimizing data lake query performance with Amazon Athena, see [Optimizing the performance of data lake queries](appendix-k-optimizing-the-performance-of-data-lake-queries.md). To learn more about optimizing data lake query cost with Amazon Athena, see [Optimizing the cost of data lake queries](appendix-l-optimizing-the-cost-of-data-lake-queries.md).

**Note**
 To access an AWS Solutions Implementation providing an AWS CloudFormation template to automate the deployment of the solution in the AWS Cloud, see the [Guidance for Multi-Omics and Multi-Modal Data Integration and Analysis on AWS](https://docs.aws.amazon.com/solutions/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/solution-overview.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
