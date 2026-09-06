---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-oracle-native-functions-to-postgresql-using-extensions.html
---

# Migrate Oracle native functions to PostgreSQL using extensions
<a name="migrate-oracle-native-functions-to-postgresql-using-extensions"></a>

*Pinesh Singal, Amazon Web Services*

## Summary
<a name="migrate-oracle-native-functions-to-postgresql-using-extensions-summary"></a>

This migration pattern provides step-by-step guidance for migrating an Amazon Relational Database Service (Amazon RDS) for Oracle database instance to an Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL-Compatible Edition database by modifying the `aws_oracle_ext` and `orafce` extensions to PostgreSQL (`psql`) native built-in code. This will save processing time.

The pattern describes an offline manual migration strategy with no downtime for a multi-terabyte Oracle source database with a high number of transactions.

The migration process uses AWS Schema Conversion Tool (AWS SCT) with the `aws_oracle_ext` and `orafce` extensions to convert an Amazon RDS for Oracle database schema to an Amazon RDS for PostgreSQL or Aurora PostgreSQL-Compatible database schema. Then the code is manually changed to PostgreSQL supported native `psql` built-in code. This is because the extension calls impact code processing on the PostgreSQL database server, and not all the extension code is fully complaint or compatible with PostgreSQL code.

This pattern primarily focuses on manually migrating SQL codes using AWS SCT and the extensions `aws_oracle_ext` and `orafce`. You convert the already used extensions into native PostgreSQL (`psql`) built-ins. Then you remove all references to the extensions and convert the codes accordingly.

## Prerequisites and limitations
<a name="migrate-oracle-native-functions-to-postgresql-using-extensions-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ Operating system (Windows or Mac) or Amazon EC2 instance (up and running)
+ Orafce

**Limitations **

Not all Oracle functions using `aws_oracle_ext` or `orafce` extensions can be converted to native PostgreSQL functions. It might need manual rework so as to compile it with PostgreSQL libraries.

One drawback of using AWS SCT extensions is its slow performance in running and fetching the results. Its cost can be understood from simple [PostgreSQL EXPLAIN plan](https://www.postgresql.org/docs/current/sql-explain.html) (execution plan of a statement) on the Oracle `SYSDATE` function migration to the PostgreSQL `NOW()` function between all three codes (`aws_oracle_ext`, `orafce`, and `psql` default), as explained in the *Performance comparison check* section in the attached document.

**Product versions**
+ **Source: **Amazon RDS for Oracle database 10.2 and later (for 10.x), 11g (11.2.0.3.v1 and later) and up to 12.2, 18c, and 19c (and later) for Enterprise Edition, Standard Edition, Standard Edition 1, and Standard Edition 2
+ **Target**: Amazon RDS for PostgreSQL or Aurora PostgreSQL-Compatible database 9.4 and later (for 9.x), 10.x, 11.x, 12.x, 13.x, and 14.x (and later)
+ **AWS SCT**: Latest version (this pattern was tested with 1.0.632)
+ **Orafce**: Latest version (this pattern was tested with 3.9.0)

## Architecture
<a name="migrate-oracle-native-functions-to-postgresql-using-extensions-architecture"></a>

**Source technology stack  **
+ An Amazon RDS for Oracle database instance with version 12.1.0.2.v18

**Target technology stack  **
+ An Amazon RDS for PostgreSQL or Aurora PostgreSQL-Compatible database instance with version 11.5

**Database migration architecture**

The following diagram represents the database migration architecture between the source Oracle and target PostgreSQL databases. The architecture involves AWS Cloud, a virtual private cloud (VPC), Availability Zones, a private subnet, an Amazon RDS for Oracle database, AWS SCT, an Amazon RDS for PostgreSQL or Aurora PostgreSQL-Compatible database, extensions for Oracle (`aws_oracle_ext` and `orafce`), and structured query language (SQL) files.

![The process is explained in the following list.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/158847bb-27ef-4915-a9ca-7d87073792c1/images/234b824a-bfe5-4ef0-9fa7-8401370b92a5.png)

1. Launch Amazon RDS for Oracle DB instance (source DB).

1. Use AWS SCT with the `aws_oracle_ext` and `orafce` extension packs to convert the source code from Oracle to PostreSQL.

1. The conversion produces PostgreSQL-supported migrated .sql files.

1. Manually convert the non-converted Oracle extension codes to PostgreSQL (`psql`) codes.

1. The manual conversion produces PostgreSQL-supported converted .sql files.

1. Run these .sql files on your Amazon RDS for PostgreSQL DB instance (target DB).

## Tools
<a name="migrate-oracle-native-functions-to-postgresql-using-extensions-tools"></a>

**Tools**

*AWS services*
+ [AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) - AWS Schema Conversion Tool (AWS SCT) converts your existing database schema from one database engine to another. You can convert relational Online Transactional Processing (OLTP) schema, or data warehouse schema. Your converted schema is suitable for an Amazon RDS for MySQL DB instance, an Amazon Aurora DB cluster, an Amazon RDS for PostgreSQL DB instance, or an Amazon Redshift cluster. The converted schema can also be used with a database on an Amazon EC2 instance or stored as data in an Amazon S3 bucket.

  AWS SCT provides a project-based user interface to automatically convert the database schema of your source database into a format compatible with your target Amazon RDS instance.

  You can use AWS SCT to do migration from an Oracle source database to any of the targets listed preceding. Using AWS SCT, you can export the source database object definitions such as schema, views, stored procedures, and functions.

  You can use AWS SCT to convert data from Oracle to Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL-Compatible Edition.

  In this pattern, you use AWS SCT to convert and migrate Oracle code into PostgreSQL using the extensions `aws_oracle_ext` and `orafce`, and manually migrating the extension codes into `psql` default or native built-in code.
+ The [AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_ExtensionPack.html) extension pack is an add-on module that emulates functions present in the source database that are required when converting objects to the target database. Before you can install the AWS SCT extension pack, you need to convert your database schema.

  When you convert your database or data warehouse schema, AWS SCT adds an additional schema to your target database. This schema implements SQL system functions of the source database that are required when writing your converted schema to your target database. This additional schema is called the extension pack schema.

  The extension pack schema for OLTP databases is named according to the source database. For Oracle databases, the extension pack schema is `AWS_ORACLE_EXT`.

*Other tools*
+ [Orafce](https://github.com/orafce/orafce) – Orafce is a module that implements Oracle compatible functions, data types, and packages. It’s an open-source tool with a Berkeley Source Distribution (BSD) license so that anyone can use it. The `orafce` module is useful for migrating from Oracle to PostgreSQL because it has many Oracle functions implemented in PostgreSQL.

**Code**

For a list of all commonly used and migrated code from Oracle to PostgreSQL to avoid AWS SCT extension code usage, see the attached document.

## Epics
<a name="migrate-oracle-native-functions-to-postgresql-using-extensions-epics"></a>

### Configure the Amazon RDS for Oracle source database
<a name="configure-the-amazon-rds-for-oracle-source-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Oracle database instance. | Create an Amazon RDS for Oracle or Aurora PostgreSQL-Compatible database instance from the Amazon RDS console. | General AWS, DBA |
| Configure the security groups. | Configure inbound and outbound security groups. | General AWS |
| Create the database. | Create the Oracle database with needed users and schemas. | General AWS, DBA |
| Create the objects. | Create objects and insert data in schema. | DBA |

### Configure the Amazon RDS for PostgreSQL target database
<a name="configure-the-amazon-rds-for-postgresql-target-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the PostgreSQL database instance. | Create an Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL database instance from the Amazon RDS console. | General AWS, DBA |
| Configure the security groups. | Configure inbound and outbound security groups. | General AWS |
| Create the database. | Create the PostgreSQL database with needed users and schemas. | General AWS, DBA |
| Validate the extensions. | Make sure that `aws_oracle_ext` and `orafce` are installed and configured correctly in the PostgreSQL database. | DBA |
| Verify that the PostgreSQL database is available. | Make sure that the PostgreSQL database is up and running. | DBA |

### Migrate the Oracle schema into PostgreSQL using AWS SCT and the extensions
<a name="migrate-the-oracle-schema-into-postgresql-using-aws-sct-and-the-extensions"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install AWS SCT. | Install the latest version of AWS SCT. | DBA |
| Configure AWS SCT. | Configure AWS SCT with Java Database Connectivity (JDBC) drivers for Oracle (`ojdbc8.jar`) and PostgreSQL (`postgresql-42.2.5.jar`). | DBA |
| Enable the AWS SCT extension pack or template. | Under AWS SCT **Project Settings**, enable built-in function implementation with the `aws_oracle_ext` and `orafce` extensions for the Oracle database schema. | DBA |
| Convert the schema. | In AWS SCT, choose **Convert Schema** to convert the schema from Oracle to PostgreSQL and generate the .sql files. | DBA |

### Convert AWS SCT extension code to psql code
<a name="convert-aws-sct-extension-code-to-psql-code"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Manually convert the code. | Manually convert each line of extension-supported code into `psql` default built-in code, as detailed in the attached document. For example, change `AWS_ORACLE_EXT.SYSDATE()` or `ORACLE.SYSDATE()` to `NOW()`. | DBA |
| Validate the code | (Optional) Validate each line of code by temporary running it in the PostgreSQL database. | DBA |
| Create objects in the PostgreSQL database. | To create objects in the PostgreSQL database, run the .sql files that were generated by AWS SCT and modified in the previous two steps. | DBA |

## Related resources
<a name="migrate-oracle-native-functions-to-postgresql-using-extensions-resources"></a>
+ Database
  + [Oracle on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html)
  + [PostgreSQL on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html)
  + [Working with Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html)
  + [PostgreSQL EXPLAIN plan](https://www.postgresql.org/docs/current/sql-explain.html)
+ AWS SCT
  + [AWS Schema Conversion Tool Overview](https://aws.amazon.com/dms/schema-conversion-tool/)
  + [AWS SCT User Guide](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)
  + [Using the AWS SCT user interface](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.html)
  + [Using Oracle Database as a source for AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Oracle.html)
+ Extensions for AWS SCT
  + [Using the AWS SCT extension pack](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_ExtensionPack.html)
  + [Oracle functionality (en)](https://postgres.cz/wiki/Oracle_functionality_(en))
  + [PGXN orafce](https://pgxn.org/dist/orafce/)
  + [GitHub orafce](https://github.com/orafce/orafce)

## Additional information
<a name="migrate-oracle-native-functions-to-postgresql-using-extensions-additional"></a>

For more information, follow the detailed commands, with syntax and examples, for manually converting code in the attached document.

## Attachments
<a name="attachments-158847bb-27ef-4915-a9ca-7d87073792c1"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/158847bb-27ef-4915-a9ca-7d87073792c1/attachments/attachment.zip)
