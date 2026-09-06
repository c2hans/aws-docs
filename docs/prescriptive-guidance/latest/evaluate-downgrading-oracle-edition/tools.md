---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-oracle-edition/tools.html
---

# AWS services and other tools
<a name="tools"></a>
+ [Amazon Relational Database Service (Amazon RDS) for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html) helps you set up, operate, and scale an Oracle relational database in the AWS Cloud.
+ [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) supports heterogeneous database migrations by automatically converting the source database schema and a majority of the custom code to a format that's compatible with the target database. You can use AWS SCT to assess, convert, and copy the database schema of your source Oracle database into a format compatible with Amazon RDS for Oracle. Using AWS SCT, you can analyze the potential cost savings that you can achieve by changing your license type from Oracle Database Enterprise Edition to Oracle Database Standard Edition 2.
+ [Oracle SQL Developer](https://www.oracle.com/database/technologies/appdev/sqldeveloper-landing.html) is an integrated development environment that simplifies the development and management of Oracle databases in both traditional and cloud-based deployments.
+ [SQL\*Plus](https://docs.oracle.com/cd/B14117_01/server.101/b12170/ch1.htm) is an interactive tool for running SQL commands on an Oracle database.

If you are working with an AWS consulting team, ask about in-house tooling and scripting built by AWS database specialists. These tools and scripts can help with gathering and reviewing data dictionary information (such as the `DBA_FEATURE_USAGE_STATISTICS` view and the count of bitmap indexes).
