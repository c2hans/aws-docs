---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aurora-postgresql-integration/analytics-aws-glue.html
---

# Aurora PostgreSQL-Compatible integration with AWS Glue
<a name="analytics-aws-glue"></a>

AWS Glue is a fully managed extract, transform, and load (ETL) service for preparing and loading data for analytics. You can integrate AWS Glue with Amazon Aurora PostgreSQL-Compatible Edition for any data processing and analytics workflows.

## AWS Glue use cases and high-level steps
<a name="aws-glue"></a>

Integration of Aurora PostgreSQL-Compatible with AWS Glue supports the following use cases:
+ **Data warehousing and analytics** ‒ Use AWS Glue integration with Aurora PostgreSQL-Compatible to build data warehousing and analytics solutions. AWS Glue can extract data from Aurora PostgreSQL-Compatible databases, and transform it according to your requirements. Then AWS Glue can load the transformed data into a data warehouse such as Amazon Redshift or Amazon Athena for advanced analytics and reporting.
+ **Data lake creation** ‒ Use AWS Glue to extract data from Aurora PostgreSQL-Compatible and load it into a data lake stored in Amazon S3. You can then use this data lake for various purposes, such as machine learning, data exploration, or feeding other analytical systems.
+ **ETL pipelines** ‒ Use the AWS Glue serverless ETL service to build robust data pipelines. You can extract data from Aurora PostgreSQL-Compatible, and perform complex transformations by using Apache Spark or PySpark. You can load the processed data into a target such as Amazon S3 or Amazon Redshift, or  you can load it back into Aurora PostgreSQL-Compatible.
+ **Data cataloging and metadata management** ‒ Use AWS Glue Data Catalog to automatically crawl and catalog metadata from Aurora PostgreSQL-Compatible databases and tables. AWS services such as Amazon Athena and Amazon Redshift Spectrum can use this centralized metadata repository for querying and analyzing data.
+ **Data preparation for machine learning** ‒ Use AWS Glue to prepare data from Aurora PostgreSQL-Compatible for machine learning (ML) workloads. The processed data can be loaded into Amazon SageMaker AI or other ML services for training and deploying models.
+ **Data migration and replication** ‒ While AWS Database Migration Service (AWS DMS) is the primary service for database migrations, you can also use AWS Glue. Migrate or replicate data from Aurora PostgreSQL-Compatible to other data stores, such as Amazon S3, Amazon Redshift, or even other database engines.

Your organization can use the power of AWS data integration and analytics services with the scalability, performance, and compatibility of Aurora PostgreSQL-Compatible. With these use cases, you can build robust data pipelines, perform complex data transformations, and integrate with other AWS services for advanced analytics and reporting.

To integrate Aurora PostgreSQL-Compatible with AWS Glue, use the following high-level steps:

1. Sign in to the AWS Management Console, navigate to the AWS Glue console, and create an AWS Glue Data Catalog.

   Data Catalog is a central repository that stores metadata about your data sources, including Aurora PostgreSQL-Compatible databases and tables.

1. Create an AWS Glue connection.

   Navigate to the **Connections** page, and create an AWS Glue connection. Select **Aurora PostgreSQL-Compatible** as the connection type, and provide the Aurora PostgreSQL-Compatible cluster endpoint, database name, and your database username and password.

1. Crawl the Aurora PostgreSQL-Compatible data source.

   Navigate to the **Crawlers** section, and create a crawler configured to use the connection that you created. Specify the database and table names that you want to crawl and include in the Data Catalog, and run the crawler.

1. Create and run an AWS Glue ETL job.

   Navigate to the **Jobs** section, and create an ETL job to access and query data from the Aurora PostgreSQL-Compatible database by using the Data Catalog. Choose the job type based on your requirements. In the ETL job script, perform any necessary transformations or processing, and specify the target location for the processed data. The target location can be Amazon S3, Amazon Redshift, or another Aurora PostgreSQL-Compatible database.

For detailed instructions, see the [AWS Glue documentation](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
