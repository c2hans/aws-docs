---
source_url: https://docs.aws.amazon.com/whitepapers/latest/data-warehousing-on-aws/migrating-to-amazon-redshift.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Migrating to Amazon Redshift
<a name="migrating-to-amazon-redshift"></a>

 If you decide to migrate from an existing data warehouse to Amazon Redshift, which migration strategy you should choose depends on several factors:
+  The size of the database and its tables and objects
+  Network bandwidth between the source server and AWS
+  Whether the migration and switchover to AWS will be done in one step, or a sequence of steps over time
+  The data change rate in the source system
+  Transformations during migration
+  The partner tool that you plan to use for migration and ETL

## One-step migration
<a name="one-step-migration"></a>

 One-step migration is a good option for small databases that don’t require continuous operation. Customers can extract existing databases as comma separated value (CSV) files, or columnar format like Parquet, then use services such as [AWS Snowball Edge](https://aws.amazon.com/snowball) to deliver datasets to S3 for loading into Amazon Redshift. Customers then test the destination Amazon Redshift database for data consistency with the source. After all validations have passed, the database is switched over to AWS.

## Two-step migration
<a name="two-step-migration"></a>

 Two-step migration is commonly used for databases of any size:
+  **Initial data migration** — The data is extracted from the source database, preferably during non-peak usage to minimize the impact. The data is then migrated to Amazon Redshift by following the one-step migration approach described previously.
+  **Changed data migration** — Data that changed in the source database after the initial data migration is propagated to the destination before switchover. This step synchronizes the source and destination databases.

   After all the changed data is migrated, you can validate the data in the destination database, perform necessary tests, and if all tests are passed, switch over to the Amazon Redshift data warehouse.

## Wave-based migration
<a name="wave-based-migration"></a>

 Large-scale MPP data warehouse migration presents a challenge in terms of project complexity, and is riskier. Taking precautions to break a complex migration project into multiple logical and systematic waves can significantly reduce the complexity and risk. Starting from a workload that covers a good number of data sources and subject areas with medium complexity, then add more data sources and subject areas in each subsequent wave. See [Develop an application migration methodology to modernize your data warehouse with Amazon Redshift](https://aws.amazon.com/blogs/big-data/develop-an-application-migration-methodology-to-modernize-your-data-warehouse-with-amazon-redshift/) for a description of how to migrate from the source MPP data warehouse to Amazon Redshift using the wave-based migration approach.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
