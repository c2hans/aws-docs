---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/convert-varchar2-1-data-type-for-oracle-to-boolean-data-type-for-amazon-aurora-postgresql.html
---

# Convert VARCHAR2(1) data type for Oracle to Boolean data type for Amazon Aurora PostgreSQL
<a name="convert-varchar2-1-data-type-for-oracle-to-boolean-data-type-for-amazon-aurora-postgresql"></a>

*Naresh Damera, Amazon Web Services*

## Summary
<a name="convert-varchar2-1-data-type-for-oracle-to-boolean-data-type-for-amazon-aurora-postgresql-summary"></a>

During a migration from Amazon Relational Database Service (Amazon RDS) for Oracle to Amazon Aurora PostgreSQL-Compatible Edition, you might encounter a data mismatch when validating the migration in AWS Database Migration Service (AWS DMS). To prevent this mismatch, you can convert VARCHAR2(1) data type to Boolean data type.

VARCHAR2 data type stores variable-length text strings, and VARCHAR2(1) indicates that the string is 1 character in length or 1 byte. For more information about VARCHAR2, see [Oracle built-in data types](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#SQLRF30020) (Oracle documentation).

In this pattern, in the sample source data table column, the VARCHAR2(1) data is either a **Y**, for *Yes*, or **N**, for *No*.  This pattern includes instructions for using AWS DMS and AWS Schema Conversion Tool (AWS SCT) to convert this data type from the **Y** and **N** values in VARCHAR2(1) to **true** or **false** values in Boolean.

**Intended audience**

This pattern is recommended for those who have experience migrating Oracle databases to Aurora PostgreSQL-Compatible by using AWS DMS. As you complete the migration, adhere to the recommendations in [Converting Oracle to Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Oracle.ToPostgreSQL.html) (AWS SCT documentation).

## Prerequisites and limitations
<a name="convert-varchar2-1-data-type-for-oracle-to-boolean-data-type-for-amazon-aurora-postgresql-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ Confirm that your environment is prepared for Aurora, including setting up credentials, permissions, and a security group. For more information, see [Setting up your environment for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_SettingUp_Aurora.html) (Aurora documentation).
+ A source Amazon RDS for Oracle database that contains a table column with VARCHAR2(1) data.
+ A target Amazon Aurora PostgreSQL-Compatible database instance. For more information, see [Creating a database cluster and connecting to a database on an Aurora PostgreSQL database cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.AuroraPostgreSQL.html#CHAP_GettingStarted.AuroraPostgreSQL.CreateDBCluster) (Aurora documentation).

**Product versions**
+ Amazon RDS for Oracle version 12.1.0.2 or later.
+ AWS DMS version 3.1.4 or later. For more information, see [Using an Oracle database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html) and [Using a PostgreSQL database as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html) (AWS DMS documentation). We recommend that you use the latest version of AWS DMS for the most comprehensive version and feature support.
+ AWS Schema Conversion Tool (AWS SCT) version 1.0.632 or later. We recommend that you use the latest version of AWS SCT for the most comprehensive version and feature support.
+ Aurora supports the PostgreSQL versions listed in [Database Engine Versions for Aurora PostgreSQL-Compatible](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.20180305.html) (Aurora documentation).

## Architecture
<a name="convert-varchar2-1-data-type-for-oracle-to-boolean-data-type-for-amazon-aurora-postgresql-architecture"></a>

**Source technology stack**

Amazon RDS for Oracle database instance

**Target technology stack**

Amazon Aurora PostgreSQL-Compatible database instance

**Source and target architecture**

![Changing data types from VARCHAR2(1) to Boolean](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/5d4dc568-20d8-4883-a942-21c81039d8e6/images/9fd82ae2-56e6-439c-b4cd-9e74fe77b480.png)

## Tools
<a name="convert-varchar2-1-data-type-for-oracle-to-boolean-data-type-for-amazon-aurora-postgresql-tools"></a>

**AWS services**
+ [Amazon Aurora PostgreSQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) is a fully managed, ACID-compliant relational database engine that helps you set up, operate, and scale PostgreSQL deployments.
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) helps you migrate data stores into the AWS Cloud or between combinations of cloud and on-premises setups.
+ [Amazon Relational Database Service (Amazon RDS) for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale an Oracle relational database in the AWS Cloud.
+ [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) supports heterogeneous database migrations by automatically converting the source database schema and a majority of the custom code to a format compatible with the target database.

**Other services**
+ [Oracle SQL Developer](https://docs.oracle.com/en/database/oracle/sql-developer/) is an integrated development environment that simplifies the development and management of Oracle databases in both traditional and cloud-based deployments. In this pattern, you use this tool to connect to the Amazon RDS for Oracle database instance and query the data.
+ [pgAdmin](https://www.pgadmin.org/docs/) is an open-source management tool for PostgreSQL. It provides a graphical interface that helps you create, maintain, and use database objects. In this pattern, you use this tool to connect to the Aurora database instance and query the data.

## Epics
<a name="convert-varchar2-1-data-type-for-oracle-to-boolean-data-type-for-amazon-aurora-postgresql-epics"></a>

### Prepare for the migration
<a name="prepare-for-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create database migration report. | 1. In AWS SCT, create a database migration assessment report. For more information, see [Creating migration assessment reports](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.html).<br />2. Review and perform the action items in the migration assessment report. For more information, see [Assessment report action items](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.ActionItems.html). | DBA, Developer |
| Disable foreign key constraints on the target database. | In PostgreSQL, foreign keys are implemented by using triggers. During the full load phase, AWS DMS loads each table one at a time. We strongly recommend that you disable foreign key constraints during a full load by using one of the following methods:+ Temporarily disable all triggers from the instance, and finish the full load.<br />+ Use the `session_replication_role` parameter in PostgreSQL.<br />If disabling foreign key constraints is not feasible, create an AWS DMS migration task for the primary data that is specific to the parent table and child table. | DBA, Developer |
| Disable the primary keys and unique keys on the target database. | Using the following commands, disable the primary keys and constraints on the target database. This helps improve the performance of the initial load task.<pre>ALTER TABLE <table> DISABLE PRIMARY KEY;</pre><pre>ALTER TABLE <table> DISABLE CONSTRAINT <constraint_name>;</pre> | DBA, Developer |
| Create the initial load task. | In AWS DMS, create the migration task for the initial load. For instructions, see [Creating a task](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.Creating.html). For the migration method, choose **Migrate existing data**. This migration method is** **called `Full Load` in the API. Do not start this task yet. | DBA, Developer |
| Edit task settings for the initial load task. | Edit the task settings to add data validation. These validation settings must be created in a JSON file. For instructions and examples, see [Specifying task settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html). Add the following validations:+ To validate that the VARCHAR2(1) data is accurately converted to Boolean in the target database, add the code in *Data validation script* in the [Additional information](#convert-varchar2-1-data-type-for-oracle-to-boolean-data-type-for-amazon-aurora-postgresql-additional) section of this pattern. The validation script converts the Boolean values of **1** to **Y** and **0** to **N** in the target table, and then it compares the values in the target table to the source table.<br />To validate the rest of the data migration, enable data validation in the task. For more information, see [Data validation task settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.DataValidation.html). | AWS administrator, DBA |
| Create the ongoing replication task. | In AWS DMS, create the migration task that keeps the target database in sync with the source database. For instructions, see [Creating a task](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.Creating.html). For the migration method, choose **Replicate data changes only**. Do not start this task yet. | DBA |

### Test the migration tasks
<a name="test-the-migration-tasks"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create sample data for testing. | In the source database, create a sample table with data for testing purposes. | Developer |
| Confirm there are no conflicting activities. | Use the `pg_stat_activity` to check for any activity on the server that might affect the migration. For more information, see [The Statistics Collector](https://www.postgresql.org/docs/current/monitoring-stats.html) (PostgreSQL documentation). | AWS administrator |
| Start the AWS DMS migration tasks. | In the AWS DMS console, on the **Dashboard** page, start the initial load and ongoing replication tasks that you created in the previous epic. | AWS administrator |
| Monitor the tasks and table load states. | During the migration, monitor the [task status](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Monitoring.html#CHAP_Tasks.Status) and the [table states](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Monitoring.html#CHAP_Tasks.CustomizingTasks.TableState). When the initial load task is complete, on the **Table statistics** tab:+ The **Load state** should be **Table completed**.<br />+ The **Validation state** should be **Validated**. | AWS administrator |
| Verify the migration results. | Using pgAdmin, query the table on target database. A successful query indicates that the data was migrated successfully. | Developer |
| Add primary keys and foreign keys on the target database. | Create the primary key and foreign key on the target database. For more information, see [ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html) (PostgreSQL website). | DBA |
| Clean up the test data. | On the source and target databases, clean up data that was created for unit testing. | Developer |

### Cut over
<a name="cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Complete the migration. | Repeat the previous epic, *Test the migration tasks*, using the real source data. This migrates the data from the source to the target database. | Developer |
| Validate that the source and target databases are in sync. | Validate that the source and target databases are in sync. For more information and instructions, see [AWS DMS data validation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html). | Developer |
| Stop the source database. | Stop the Amazon RDS for Oracle database. For instructions, see [Stopping an Amazon RDS DB instance temporarily](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_StopInstance.html). When you stop the source database, the initial load and ongoing replication tasks in AWS DMS are automatically stopped. No additional action is required to stop these tasks. | Developer |

## Related resources
<a name="convert-varchar2-1-data-type-for-oracle-to-boolean-data-type-for-amazon-aurora-postgresql-resources"></a>

**AWS references**
+ [Migrate an Oracle database to Aurora PostgreSQL using AWS DMS and AWS SCT](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-oracle-database-to-aurora-postgresql-using-aws-dms-and-aws-sct.html) (AWS Prescriptive Guidance)
+ [Converting Oracle to Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Oracle.ToPostgreSQL.html) (AWS SCT documentation)
+ [How AWS DMS Works](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.html) (AWS DMS documentation)

**Other references**
+ [Boolean data type](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-boolean/) (PostgreSQL documentation)
+ [Oracle built-in data types](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#SQLRF30020) (Oracle documentation)
+ [pgAdmin](https://www.pgadmin.org/) (pgAdmin website)
+ [SQL Developer](https://www.oracle.com/database/technologies/appdev/sql-developer.html) (Oracle website)

**Tutorials and videos**
+ [Getting Started with AWS DMS](https://aws.amazon.com/dms/getting-started/)
+ [Getting Started With Amazon RDS](https://aws.amazon.com/rds/getting-started/)
+ [Introduction to AWS DMS](https://www.youtube.com/watch?v=ouia1Sc5QGo) (Video)
+ [Understanding Amazon RDS](https://www.youtube.com/watch?v=eMzCI7S1P9M) (Video)

## Additional information
<a name="convert-varchar2-1-data-type-for-oracle-to-boolean-data-type-for-amazon-aurora-postgresql-additional"></a>

**Data validation script**

The following data validation script converts **1** to **Y** and **0** to **N**. This helps the AWS DMS task successfully complete and pass the table validation.

```
{
"rule-type": "validation",
"rule-id": "5",
"rule-name": "5",
"rule-target": "column",
"object-locator": {
"schema-name": "ADMIN",
"table-name": "TEMP_CHRA_BOOL",
"column-name": "GRADE"
},
"rule-action": "override-validation-function",
"target-function": "case grade when '1' then 'Y' else 'N' end"
        }
```

The `case` statement in the script performs the validation. If validation fails, AWS DMS inserts a record in the **public.awsdms\_validation\_failures\_v1** table on the target database instance. This record includes the table name, error time, and details about the mismatched values in the source and target tables.

If you do not add this data validation script to the AWS DMS task and the data is inserted in the target table, the AWS DMS task shows validation state as **Mismatched Records**.

During AWS SCT conversion, the AWS DMS migration task changes the data type of VARCHAR2(1) data type to Boolean and adds a primary key constraint on the `"NO"` column.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
