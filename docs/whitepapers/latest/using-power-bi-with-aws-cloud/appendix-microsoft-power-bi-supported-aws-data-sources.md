---
source_url: https://docs.aws.amazon.com/whitepapers/latest/using-power-bi-with-aws-cloud/appendix-microsoft-power-bi-supported-aws-data-sources.html
---

# Appendix: Microsoft Power BI supported AWS data sources
<a name="appendix-microsoft-power-bi-supported-aws-data-sources"></a>

 The full list of supported data sources is provided by Microsoft (refer to [Power BI data sources](https://docs.microsoft.com/en-us/power-bi/connect-data/power-bi-data-sources)); however, the following sections for each AWS data source provide usage and configuration guidance that may be helpful for some readers.

## Amazon Redshift
<a name="amazon-redshift"></a>

 Amazon Redshift is a fully-managed, petabyte-scale data warehouse service in the AWS Cloud. An Amazon Redshift data warehouse is a collection of computing resources called nodes, which are organized into a group called a cluster. Each cluster runs an Amazon Redshift engine and contains one or more databases.

 You should consider using Amazon Redshift when:
+  You are building or migrating to a native cloud data warehouse.
+  You might need to scale from a few to hundreds of Terabytes.
+  You want to allow the Power BI users to transparently access data from the data lake stored in Amazon S3 and join it with tables in the data warehouse.
+  Your query workload includes:
  +  Queries which compute aggregation on large (multi-gigabyte and multi-terabyte) tables.
  +  Extremely complex SQL with multiple joins and sub-queries.
  +  A mix of complex analytical queries and simple, highly-filtered queries used in Dashboards.

 When using Amazon Redshift with Microsoft Power BI, keep the following points in mind:
+ Amazon Redshift is natively-supported as a Power BI data source in both Microsoft Power BI Desktop and Power BI services, and each supports import and direct query modes.
+ While a Redshift cluster can be launched in a public subnet and configured to allow access from the internet, the majority of customers prefer to launch it in a private subnet to increase security. When using a private subnet, make use of the on-premises data gateway to connect from the Power BI service to Amazon Redshift.
+ The Redshift connector supports Azure AD Authentication in Power BI Desktop and service.
+ External tables accessed via Spectrum are not treated any differently than native Redshift tables, and Power BI has no means to differentiate them. When accessing data in external tables, make sure that:
  +  Columns that contain strings of characters are catalogued as ‘VARCHAR’ in the AWS Glue Data Catalog and not as ‘STRING’, otherwise Power BI will throw the following error: ` Exception: OLE DB or ODBC error: [Expression.Error] We couldn't fold the expression to the data source. Please try a simpler expression..`
  +  Columns containing complex data types such as ARRAY, are not supported. When columns containing complex data types are used, Power BI will throw the following error: `Exception: ODBC: ERROR [42703] [Microsoft]Amazon Redshift Error occurred while trying to execute a query `

    If you need to include them in your model, you can either enable (in Amazon Redshift) the JSON serialization at the user level or store the complex data types in a SUPER column in a native table.

## Amazon RDS
<a name="amazon-rds"></a>

 Amazon RDS makes it easy to set up, operate, and scale a relational database in the cloud. Amazon RDS is available on several database instance types (optimized for memory, performance, or I/O) and provides you with six familiar database engines to choose from, including Amazon Aurora, PostgreSQL, MySQL, MariaDB, Oracle Database, and SQL Server.

You should consider using RDS when:
+  You are building an operational data store.
+  You are migrating SQL Server or Oracle Database data warehouse to the cloud but not interested in refactoring.
+  Your query workload includes:
  +  Queries which access highly-filtered data on tables that can be easily indexed.
  +  Analytics queries on small-to-medium sized tables (gigabytes).
  +  A mix of medium-complexity analytical queries and simple, highly-filtered queries used in Dashboards.

When using Amazon RDS with Microsoft Power BI, keep the following points in mind:
+  Amazon RDS provides multiple database engines including SQL Server, MariaDB, MySQL, Oracle Database, and PostgreSQL. Note that the database engines are listed in Power BI Desktop and Power BI service, not the Amazon RDS service.
+  For Amazon Aurora, use the My SQL or PostgreSQL connection type, depending on your selected database engine.
+  While an Amazon RDS instance can be launched in a public subnet and configured to allow access from the internet, the majority of customers prefer to launch it in a private subnet to increase security. When using a private subnet make use of the on-premises data gateway to connect from the Power BI service to RDS.
+  With Amazon RDS, you can deploy multiple editions of SQL Server (2012, 2014, 2016, 2017, and 2019) including Express, Web, Standard, and Enterprise.

## Amazon Athena
<a name="amazon-athena"></a>

 Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is out-of-the-box integrated with AWS Glue Data Catalog, allowing you to create a unified metadata repository across various services, crawl data sources to discover schemas, populate your Data Catalog with new and modified table and partition definitions, and maintain schema versioning.

You should consider Athena as a data source when:
+  You want to query your data lake directly.
+  Your query workload includes:
  +  Queries which compute aggregation on large (multi-gigabyte and multi-terabyte) tables
  +  Interactive ad hoc SQL, for exploratory purposes.

 When using Amazon Athena with Microsoft Power BI, keep the following points in mind:
+ With the July 2021 release of Microsoft Power BI, a Microsoft-certified connector has been introduced for Amazon Athena. You can use the Microsoft Power BI connector for Amazon Athena to analyze data from Amazon Athena in Microsoft Power BI Desktop. After you publish content to the Power BI service, you can use the Microsoft on-premises data gateway to keep the content up to date through on-demand or scheduled refreshes.
+ The Microsoft Power BI connector for Amazon Athena supports both Import and Direct Query data connectivity modes. With the Import mode, selected tables and columns are imported into Power BI Desktop for querying. With the Direct Query mode, no data is imported or copied into Power BI Desktop, and instead Power BI Desktop queries the underlying data source directly.
+  For more information on the Microsoft Power BI connector for Amazon Athena, refer to [Using the Amazon Athena Power BI Connector](https://docs.aws.amazon.com/athena/latest/ug/connect-with-odbc-and-power-bi.html).
+ Note that the Microsoft Power BI connector for Amazon Athena requires the use of the Amazon Athena ODBC driver and a valid ODBC DSN configuration on your system to query Amazon Athena. To download the latest ODBC driver and for configuration information, refer to [Connecting to Amazon Athena with ODBC](https://docs.aws.amazon.com/athena/latest/ug/connect-with-odbc.html).
+ For a tutorial on the configuration steps and best practices when using the Microsoft Power BI connector for Amazon Athena, refer to [Creating dashboards quickly on Microsoft Power BI using Amazon Athena](https://aws.amazon.com/blogs/big-data/creating-dashboards-quickly-on-microsoft-power-bi-using-amazon-athena/).

## Amazon OpenSearch Service
<a name="amazon-opensearch-service"></a>

 You can use SQL to query your Amazon OpenSearch Service, rather than using the JSON-based search query DSL. Querying with SQL is useful if you're already familiar with the language or want to integrate your domain with an application that uses it, such as Microsoft Power BI.

You should consider Amazon OpenSearch Service as a data source when:
+ You have semi-structured data such as log files or JSON output, and need to search, analyze, or visualize the information quickly.

 When using Amazon OpenSearch Service with Microsoft Power BI, keep the following points in mind:
+ Connectivity to Amazon OpenSearch Service requires the Open Database Connectivity (ODBC) driver, which is a read-only ODBC driver for Windows and macOS that lets you connect business intelligence (BI) and data visualization applications like [Tableau](https://github.com/opendistro-for-elasticsearch/sql/blob/develop/sql-odbc/docs/user/tableau_support.md), [Microsoft Excel](https://github.com/opendistro-for-elasticsearch/sql/blob/develop/sql-odbc/docs/user/microsoft_excel_support.md), and [Power BI](https://github.com/opendistro-for-elasticsearch/sql/blob/main/sql-odbc/docs/user/power_bi_support.md) to the SQL plugin on your cluster. The driver is available on the OpenSearch [Download & Get Started](https://opensearch.org/downloads/) website. For configuration instructions, refer to the “Customizing the ODBC driver” section in [OpenSearch ODBC driver website](https://opensearch.org/docs/latest/search-plugins/sql/sql/odbc/).
+ Only import mode is currently supported.
+ Power BI connectivity to Amazon OpenSearch Service currently requires the use of a beta connector. Refer to [ Microsoft Power Query Documentation - Connector reference: Amazon Opensearch Service (Beta) ](https://learn.microsoft.com/en-us/power-query/connectors/amazonopensearchservice)to get started.

## AWS Lake Formation
<a name="aws-lake-formation"></a>

 Lake Formation helps you collect and catalog data from databases and object storage, move the data into your new [Amazon S3](https://aws.amazon.com/s3/) data lake, clean and classify your data using machine learning algorithms, and secure access to your sensitive data. Your users can access a centralized [data catalog](https://aws.amazon.com/glue/faqs/#AWS_Glue_Data_Catalog/) which describes available data sets and their appropriate usage. Your users then utilize these data sets with their choice of analytics and machine learning services, like [Amazon Redshift](https://aws.amazon.com/redshift/), [Amazon Athena](https://aws.amazon.com/athena/), and (in beta) [Amazon EMR](https://aws.amazon.com/emr/) for Apache Spark. Lake Formation builds on the capabilities available in [AWS Glue](https://aws.amazon.com/glue/).

You should consider Lake Formation if you need fine-grained (row and column) level access to your data lake instead of the traditional IAM based controls.

When using Lake Formation with Microsoft Power BI, keep the following points in mind:
+ To query data from the Lake Formation Data Catalog with Power BI Desktop or Power BI service, use the same process and configuration as querying data in Athena. If you are making use of the Lake Formation permission model, ensure that the ODBC DSN configuration for Amazon Athena has the `LakeformationEnabled` property key set to a value of `true`. This tells the Amazon Athena ODBC driver to use the Lake Formation service for authorization, instead of AWS Security Token Service directly. For more information, refer to the documentation for [Connecting to Amazon Athena with ODBC](https://docs.aws.amazon.com/athena/latest/ug/connect-with-odbc.html#connect-with-odbc-driver-documentation).
+ The "Use only IAM access control" setting enabled for compatibility with existing Data Catalog behavior will provide full compatibility.
+ Upgrading AWS Glue Data Permissions to the Lake Formation Model may introduce incompatibilities and should tested before use. Preliminary testing indicates that column level grant or deny are being honored, but row and cell level filtering have not been tested by the authors, as this is still in preview and subject to change.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
