---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-microsoft-sql-server-database-to-aurora-mysql-by-using-aws-dms-and-aws-sct.html
---

# Migrate a Microsoft SQL Server database to Aurora MySQL by using AWS DMS and AWS SCT
<a name="migrate-a-microsoft-sql-server-database-to-aurora-mysql-by-using-aws-dms-and-aws-sct"></a>

*Mark Szalkiewicz and Pavan Pusuluri, Amazon Web Services*

## Summary
<a name="migrate-a-microsoft-sql-server-database-to-aurora-mysql-by-using-aws-dms-and-aws-sct-summary"></a>

This pattern describes how to migrate a Microsoft SQL Server database that is either on premises or on an Amazon Elastic Compute Cloud (Amazon EC2) instance to Amazon Aurora MySQL. The pattern uses AWS Database Migration Service (AWS DMS) and AWS Schema Conversion Tool (AWS SCT) for data migration and schema conversion.

## Prerequisites and limitations
<a name="migrate-a-microsoft-sql-server-database-to-aurora-mysql-by-using-aws-dms-and-aws-sct-prerequisites-and-limitations"></a>

**Prerequisites**
+ An active AWS account
+ A Microsoft SQL Server source database in an on-premises data center or on an EC2 instance
+ Java Database Connectivity (JDBC) drivers for AWS SCT connectors, installed on either a local machine or an EC2 instance where AWS SCT is installed

**Limitations**
+ Database size limit: 64 TB

**Product versions**
+ Microsoft SQL Server 2008, 2008R2, 2012, 2014, 2016, and 2017 for the Enterprise, Standard, Workgroup, and Developer editions. The Web and Express editions aren't supported by AWS DMS. For the latest list of supported versions, see [Using a Microsoft SQL Server Database as a Source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html). We recommend that you use the latest version of AWS DMS for the most comprehensive version and feature support. For information about Microsoft SQL Server versions supported by AWS SCT, see the [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html).
+ MySQL versions 5.5, 5.6, and 5.7. For the latest list of supported versions, see [Using a MySQL-Compatible Database as a Target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html).

## Architecture
<a name="migrate-a-microsoft-sql-server-database-to-aurora-mysql-by-using-aws-dms-and-aws-sct-architecture"></a>

**Source technology stack**

One of the following:
+ An on-premises Microsoft SQL Server database
+ A Microsoft SQL Server database on an EC2 instance

**Target technology stack**
+ Aurora MySQL

**Data migration architecture**
+ From a Microsoft SQL Server database running in the AWS Cloud

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e2de4507-82a8-4bd6-b25b-1e830b197b9f/images/c675ada4-e92c-4ddb-b49f-69668f532504.png)

+ From a Microsoft SQL Server database running in an on-premises data center

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e2de4507-82a8-4bd6-b25b-1e830b197b9f/images/b6ce0199-fc56-4bf2-a8cc-67de161e3cf0.png)

## Tools
<a name="migrate-a-microsoft-sql-server-database-to-aurora-mysql-by-using-aws-dms-and-aws-sct-tools"></a>
+ **AWS DMS** - [AWS Data Migration Service](http://docs.aws.amazon.com/dms/latest/sbs/DMS-SBS-Welcome.html) (AWS DMS) helps you migrate your data to and from widely used commercial and open-source databases, including Oracle, SQL Server, MySQL, and PostgreSQL. You can use AWS DMS to migrate your data into the AWS Cloud, between on-premises instances (through an AWS Cloud setup), or between combinations of cloud and on-premises setups.
+ **AWS SCT** - [AWS Schema Conversion Tool](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) (AWS SCT) makes heterogeneous database migrations easy by automatically converting the source database schema and a majority of the custom code to a format compatible with the target database.

## Epics
<a name="migrate-a-microsoft-sql-server-database-to-aurora-mysql-by-using-aws-dms-and-aws-sct-epics"></a>

### Prepare for the migration
<a name="prepare-for-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the source and target database version and engine. |  | DBA |
| Create an outbound security group for the source and target databases. |  | SysAdmin |
| Create and configure an EC2 instance for AWS SCT, if required. |  | DBA |
| Download the latest version of AWS SCT and associated drivers. |  | DBA |
| Add and validate the prerequisite users and grants in the source database. |  | DBA |
| Create an AWS SCT project for the workload and connect to the source database. |  | DBA |
| Generate an assessment report and evaluate feasibility. |  | DBA |

### Prepare the target database
<a name="prepare-the-target-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a target Amazon RDS DB instance, using Amazon Aurora as the database engine. |  | DBA |
| Extract the list of users, roles, and grants from the source. |  | DBA |
| Map the existing database users to the new database users. |  | App owner |
| Create users in the target database. |  | DBA |
| Apply roles from the previous step to the target database. |  | DBA |
| Review the database options, parameters, network files, and database links in the source database, and then evaluate their applicability to the target database. |  | DBA |
| Apply any relevant settings to the target. |  | DBA |

### Transfer objects
<a name="transfer-objects"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure AWS SCT connectivity to the target database. |  | DBA |
| Convert the schema using AWS SCT. | AWS SCT automatically converts the source database schema and most of the custom code to a format that is compatible with the target database. Any code that the tool cannot convert automatically is clearly marked so that you can convert it yourself. | DBA |
| Review the generated SQL report and save any errors and warnings. |  | DBA |
| Apply automated schema changes to the target or save them as a .sql file. |  | DBA |
| Validate that AWS SCT created the objects on the target.  |  | DBA |
| Manually rewrite, reject, or redesign any items that failed to convert automatically. |  | DBA |
| Apply the generated role and user grants and review any exceptions. |  | DBA |

### Migrate the data
<a name="migrate-the-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Determine the migration method. |  | DBA |
| Create a replication instance from the AWS DMS console. | For detailed information on using AWS DMS, see the links in the "Related resources" section. | DBA |
| Create the source and target endpoints. |  | DBA |
| Create a replication task. |  | DBA |
| Start the replication task and monitor the logs. |  | DBA |

### Migrate the application
<a name="migrate-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Use AWS SCT to analyze and convert the SQL items within the application code. | When you convert your database schema from one engine to another, you also need to update the SQL code in your applications to interact with the new database engine instead of the old one. You can view, analyze, edit, and save the converted SQL code. For detailed information on using AWS SCT, see the links in the "Related resources" section. | App owner |
| Create the new application servers on AWS. |  | App owner |
| Migrate the application code to the new servers. |  | App owner |
| Configure the application server for the target database and drivers. |  | App owner |
| Fix any code that's specific to the source database engine in the application. |  | App owner |
| Optimize the application code for the target engine. |  | App owner |

### Cut over
<a name="cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Apply any new users, grants, and code changes to the target. |  | DBA |
| Lock the application for any changes. |  | App owner |
| Validate that all changes were propagated to the target database. |  | DBA |
| Point the new application server to the target database. |  | App owner |
| Recheck everything. |  | App owner |
| Go live. |  | App owner |

### Close the project
<a name="close-the-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Shut down the temporary AWS resources (AWS DMS replication instance and EC2 instance used for AWS SCT). |  | DBA, App owner |
| Update feedback on the AWS DMS process for internal teams. |  | DBA, App owner |
| Revise the AWS DMS process and improve the template if necessary. |  | DBA, App owner |
| Review and validate the project documents. |  | DBA, App owner |
| Gather metrics around time to migrate, percent of manual versus tool cost savings, and so on. |  | DBA, App owner |
| Close the project and provide any feedback. |  | DBA, App owner |

## Related resources
<a name="migrate-a-microsoft-sql-server-database-to-aurora-mysql-by-using-aws-dms-and-aws-sct-related-resources"></a>

**References**
+ [AWS DMS User Guide](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)
+ [AWS SCT User Guide](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)
+ [Amazon Aurora Pricing](https://aws.amazon.com/rds/aurora/pricing/)

**Tutorials and videos**
+ [Getting Started with AWS Database Migration Service](https://aws.amazon.com/dms/getting-started/)
+ [Getting Started with the AWS Schema Conversion Tool](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)
+ [Amazon RDS resources](https://aws.amazon.com/rds/getting-started/)
+ [AWS DMS Step-by-Step Walkthroughs](http://docs.aws.amazon.com/dms/latest/sbs/DMS-SBS-Welcome.html)
