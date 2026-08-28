---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/datasets.connecting-to-data.html
---

# Connecting to your data
<a name="datasets.connecting-to-data"></a>

For more information on connecting to the following data sources, choose the section that applies to you.
+ **AWS Glue Data Catalog** – You can use the Data Catalog to define references to data objects stored in the AWS Cloud, including the following services:
  + Amazon Redshift
  + Aurora MySQL
  + Aurora PostgreSQL
  + Amazon RDS for MySQL
  + Amazon RDS for PostgreSQL

  DataBrew recognizes all Lake Formation permissions that have been applied to Data Catalog resources, so DataBrew users can only access these resources if they're authorized.

  To create a dataset, you specify a Data Catalog database name and a table name. DataBrew takes care of the other connection details.
+ **AWS Data Exchange** – You can choose from hundreds of third-party data sources that are available in AWS Data Exchange. By subscribing to these data sources, you always have the most up-to-date version of the data.

  To create a dataset, you specify the name of a Data Exchange data product that you're subscribed to or entitled to use.
+  **JDBC driver connections** – You can create a dataset by connecting DataBrew to a JDBC-compatible data source. DataBrew supports connecting to the following sources through JDBC:
  + Amazon Redshift
  + Microsoft SQL Server
  + MySQL
  + Oracle
  + PostgreSQL
  + Snowflake

**Topics**
+ [Using drivers with AWS Glue DataBrew](dbms-driver-connections.md)
+ [Supported JDBC drivers](jdbc-drivers.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
