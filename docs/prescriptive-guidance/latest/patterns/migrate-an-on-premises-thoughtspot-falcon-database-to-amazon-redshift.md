---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-thoughtspot-falcon-database-to-amazon-redshift.html
---

# Migrate an on-premises ThoughtSpot Falcon database to Amazon Redshift
<a name="migrate-an-on-premises-thoughtspot-falcon-database-to-amazon-redshift"></a>

*Battulga Purevragchaa and Antony Prasad Thevaraj, Amazon Web Services*

## Summary
<a name="migrate-an-on-premises-thoughtspot-falcon-database-to-amazon-redshift-summary"></a>

On-premises data warehouses require significant administration time and resources, particularly for large datasets. The financial cost of building, maintaining, and growing these warehouses is also very high. To help manage costs, keep extract, transform, and load (ETL) complexity low, and deliver performance as your data grows, you must constantly choose which data to load and which data to archive.

By migrating your on-premises [ThoughtSpot Falcon databases](https://docs.thoughtspot.com/software/latest/data-caching) to the Amazon Web Services (AWS) Cloud, you can access cloud-based data lakes and data warehouses that increase your business agility, security, and application reliability, in addition to reducing your overall infrastructure costs. Amazon Redshift helps to significantly lower the cost and operational overhead of a data warehouse. You can also use Amazon Redshift Spectrum to analyze large amounts of data in its native format without data loading.

This pattern describes the steps and process for migrating a ThoughtSpot Falcon database from an on-premises data center to an Amazon Redshift database on the AWS Cloud.

## Prerequisites and limitations
<a name="migrate-an-on-premises-thoughtspot-falcon-database-to-amazon-redshift-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A ThoughtSpot Falcon database hosted in an on-premises data center

**Product versions**
+ ThoughtSpot version 7.0.1

## Architecture
<a name="migrate-an-on-premises-thoughtspot-falcon-database-to-amazon-redshift-architecture"></a>

![Migrating a ThoughtSpot Falcon database from an on-premises data center to Amazon Redshift.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/b0ca29f4-b269-4b57-b386-738693a6b334/images/2b483990-1f30-439c-ba13-dc0cb0650360.png)

The diagram shows the following workflow:

1. Data is hosted in an on-premises relational database.

1. AWS Schema Conversion Tool (AWS SCT) converts the data definition language (DDL) that is compatible with Amazon Redshift.

1. After the tables are created, you can migrate the data by using AWS Database Migration Service (AWS DMS).

1. The data is loaded into Amazon Redshift.

1. The data is stored in Amazon Simple Storage Service (Amazon S3) if you use Redshift Spectrum or already host the data in Amazon S3.

## Tools
<a name="migrate-an-on-premises-thoughtspot-falcon-database-to-amazon-redshift-tools"></a>
+ [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) – AWS Data Migration Service (AWS DMS) helps you quickly and securely migrate databases to AWS.
+ [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html) – Amazon Redshift is a fast, fully managed, petabyte-scale data warehouse service that makes it simple and cost-effective to efficiently analyze all your data using your existing business intelligence tools.
+ [AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) – AWS Schema Conversion Tool (AWS SCT) converts your existing database schema from one database engine to another.

## Epics
<a name="migrate-an-on-premises-thoughtspot-falcon-database-to-amazon-redshift-epics"></a>

### Prepare for the migration
<a name="prepare-for-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify the appropriate Amazon Redshift configuration. | Identify the appropriate Amazon Redshift cluster configuration based on your requirements and data volume. <br />For more information, see [Amazon Redshift clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html) in the Amazon Redshift documentation. | DBA |
| Research Amazon Redshift to evaluate if it meets your requirements. | Use the [Amazon Redshift FAQs](https://aws.amazon.com/redshift/faqs/) to understand and evaluate whether Amazon Redshift meets your requirements. | DBA |

### Prepare the target Amazon Redshift cluster
<a name="prepare-the-target-amazon-redshift-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon Redshift cluster. | Sign in to the AWS Management Console, open the Amazon Redshift console, and then create an Amazon Redshift cluster in a virtual private cloud (VPC). <br />For more information, see [Creating a cluster in a VPC](https://docs.aws.amazon.com/redshift/latest/mgmt/getting-started-cluster-in-vpc.html) in the Amazon Redshift documentation. | DBA |
| Conduct a PoC for your Amazon Redshift database design. | Follow Amazon Redshift best practices by conducting a proof of concept (PoC) for your database design. <br />For more information, see [Conducting a proof of concept for Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/proof-of-concept-playbook.html) in the Amazon Redshift documentation. | DBA |
| Create database users. | Create the users in your Amazon Redshift database and grant the appropriate roles for access to the schema and tables.  <br />For more information, see [Grant access privileges for a user or user group](https://docs.aws.amazon.com/redshift/latest/dg/r_GRANT.html) in the Amazon Redshift documentation. | DBA |
| Apply configuration settings to the target database. | Apply configuration settings to the Amazon Redshift database according to your requirements. <br />For more information about enabling database, session, and server-level parameters, see the [Configuration reference](https://docs.aws.amazon.com/redshift/latest/dg/cm_chap_ConfigurationRef.html) in the Amazon Redshift documentation. | DBA |

### Create objects in the Amazon Redshift cluster
<a name="create-objects-in-the-amazon-redshift-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Manually create tables with DDL in Amazon Redshift. | (Optional) If you use AWS SCT, the tables are automatically created. However, if there are failures when replicating DDLs, you have to manually create the tables | DBA |
| Create external tables for Redshift Spectrum. | Create an external table with an external schema for Amazon Redshift Spectrum. To create external tables, you must be the owner of the external schema or a [database superuser](https://docs.aws.amazon.com/redshift/latest/dg/r_superusers.html). <br />For more information, see [Creating external tables for Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-spectrum-external-tables.html) in the Amazon Redshift documentation. | DBA |

### Migrate data using AWS DMS
<a name="migrate-data-using-aws-dms"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Use AWS DMS to migrate the data. | After you create the DDL of the tables in the Amazon Redshift database, migrate your data to Amazon Redshift by using AWS DMS.<br />For detailed steps and instructions, see [Using an Amazon Redshift database as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redshift.html) in the AWS DMS documentation. | DBA |
| Use the COPY command to load the data. | Use the Amazon Redshift `COPY` command to load the data from Amazon S3 to Amazon Redshift.<br />For more information, see [Using the COPY command to load from Amazon S3](https://docs.aws.amazon.com/redshift/latest/dg/t_loading-tables-from-s3.html) in the Amazon Redshift documentation. | DBA |

### Validate the Amazon Redshift cluster
<a name="validate-the-amazon-redshift-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the source and target records.  | Validate the table count for the source and target records that were loaded from your source system. | DBA |
| Implement Amazon Redshift best practices for performance tuning. | Implement Amazon Redshift best practices for table and database design. <br />For more information, see the blog post [Top 10 performance tuning techniques for Amazon Redshift](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-techniques-for-amazon-redshift/). | DBA |
| Optimize query performance. | Amazon Redshift uses SQL-based queries to interact with data and objects in the system. Data manipulation language (DML) is the subset of SQL that you can use to view, add, change, and delete data. DDL is the subset of SQL that you use to add, change, and delete database objects such as tables and views.<br />For more information, see [Tuning query performance](https://docs.aws.amazon.com/redshift/latest/dg/c-optimizing-query-performance.html) in the Amazon Redshift documentation. | DBA |
| Implement WLM.  | You can use workload management (WLM) to define multiple query queues and route queries to appropriate queues at runtime.<br />For more information, see [Implementing workload management](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-implementing-workload-management.html) in the Amazon Redshift documentation. | DBA |
| Work with concurrency scaling. | By using the Concurrency Scaling feature, you can support virtually unlimited concurrent users and concurrent queries, with consistently fast query performance.<br />For more information, see [Working with concurrency scaling](https://docs.aws.amazon.com/redshift/latest/dg/concurrency-scaling.html) in the Amazon Redshift documentation. | DBA |
| Use Amazon Redshift best practices for table design. | When you plan your database, certain important table design decisions can strongly influence overall query performance.<br />For more information about choosing the most appropriate table design option, see [Amazon Redshift best practices for designing tables](https://docs.aws.amazon.com/redshift/latest/dg/c_designing-tables-best-practices.html) in the Amazon Redshift documentation. | DBA |
| Create materialized views in Amazon Redshift. | A materialized view contains a precomputed results set based on an SQL query over one or more base tables. You can issue `SELECT` statements to query a materialized view in the same way that you query other tables or views in the database.<br />For more information, see [Creating materialized views in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-overview.html) in the Amazon Redshift documentation. | DBA |
| Define joins between the tables. | To search more than one table at the same time in ThoughtSpot, you must define joins between the tables by specifying columns that contain matching data across two tables. These columns represent the `primary key` and `foreign key` of the join.<br />You can define them by using the `ALTER TABLE` command in Amazon Redshift or ThoughtSpot. For more information, see [ALTER TABLE](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_TABLE.html) in the Amazon Redshift documentation. | DBA |

### Set up ThoughtSpot connection to Amazon Redshift
<a name="set-up-thoughtspot-connection-to-amazon-redshift"></a>

| Task | Description | Skills required |
| --- | --- | --- |
|  Add an Amazon Redshift connection. | Add an Amazon Redshift connection to your on-premises ThoughtSpot Falcon database.<br />For more information, see [Add an Amazon Redshift connection](https://cloud-docs.thoughtspot.com/admin/ts-cloud/ts-cloud-embrace-redshift-add-connection.html) in the ThoughtSpot documentation. | DBA |
| Edit the Amazon Redshift connection. | You can edit the Amazon Redshift connection to add tables and columns.<br />For more information, see [Edit an Amazon Redshift connection](https://cloud-docs.thoughtspot.com/admin/ts-cloud/ts-cloud-embrace-redshift-edit-connection.html) in the ThoughtSpot documentation. | DBA |
| Remap the Amazon Redshift connection. | Modify the connection parameters by editing the source mapping .yaml file that was created when you added the Amazon Redshift connection. <br />For example, you can remap the existing table or column to a different table or column in an existing database connection. ThoughtSpot recommends that you check the dependencies before and after you remap a table or column in a connection to ensure that they display as required.<br />For more information, see [Remap an Amazon Redshift connection](https://cloud-docs.thoughtspot.com/admin/ts-cloud/ts-cloud-embrace-redshift-remap-connection.html) in the ThoughtSpot documentation. | DBA |
| Delete a table from the Amazon Redshift connection.  | (Optional) If you attempt to remove a table in an Amazon Redshift connection, ThoughtSpot checks for dependencies and shows a list of dependent objects. You can choose the listed objects to delete them or remove the dependency. You can then remove the table.<br />For more information, see [Delete a table from an Amazon Redshift connection](https://cloud-docs.thoughtspot.com/admin/ts-cloud/ts-cloud-embrace-redshift-delete-table.html) in the ThoughtSpot documentation. | DBA |
|  Delete a table with dependent objects from an Amazon Redshift connection. | (Optional) If you try to delete a table with dependent objects, the operation is blocked. A `Cannot delete` window appears, with a list of links to dependent objects. When all the dependencies are removed, you can then delete the table<br />For more information, see [Delete a table with dependent objects from an Amazon Redshift connection](https://cloud-docs.thoughtspot.com/admin/ts-cloud/ts-cloud-embrace-redshift-delete-table-dependencies.html) in the ThoughtSpot documentation. | DBA |
| Delete an Amazon Redshift connection. | (Optional) Because a connection can be used in multiple data sources or visualizations, you must delete all of the sources and tasks that use that connection before you can delete the Amazon Redshift connection.<br />For more information, see [Delete an Amazon Redshift connection](https://cloud-docs.thoughtspot.com/admin/ts-cloud/ts-cloud-embrace-redshift-delete-connection.html) in the ThoughtSpot documentation. | DBA |
|  Check connection reference for Amazon Redshift. | Make sure that you provide the required information for your Amazon Redshift connection by using the [Connection reference](https://cloud-docs.thoughtspot.com/admin/ts-cloud/ts-cloud-embrace-redshift-connection-reference.html) in the ThoughtSpot documentation. | DBA |

## Additional information
<a name="migrate-an-on-premises-thoughtspot-falcon-database-to-amazon-redshift-additional"></a>
+ [AI-driven analytics at any scale with ThoughtSpot and Amazon Redshift](https://aws.amazon.com/blogs/apn/ai-driven-analytics-at-any-scale-with-thoughtspot-and-amazon-redshift/)
+ [Amazon Redshift pricing](https://aws.amazon.com/redshift/pricing/)
+ [Getting started with AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_GettingStarted.html)
+ [Getting started with Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html)
+ [Using data extraction agents](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/agents.html)
+ [Chick-fil-A improves speed to insight with ThoughtSpot and AWS](https://www.thoughtspot.com/sites/default/files/pdf/ThoughtSpot-Chick-fil-A-AWS-Case-Study.pdf)
