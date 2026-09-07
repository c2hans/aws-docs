---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-oracle-database-to-amazon-redshift-using-aws-dms-and-aws-sct.html
---

# Migrate an Oracle Database to Amazon Redshift using AWS DMS and AWS SCT
<a name="migrate-an-oracle-database-to-amazon-redshift-using-aws-dms-and-aws-sct"></a>

*Piyush Goyal and Brian motzer, Amazon Web Services*

## Summary
<a name="migrate-an-oracle-database-to-amazon-redshift-using-aws-dms-and-aws-sct-summary"></a>

This pattern provides guidance for migrating Oracle databases to an Amazon Redshift cloud data warehouse in the Amazon Web Services (AWS) Cloud by using AWS Database Migration Service (AWS DMS) and AWS Schema Conversion Tool (AWS SCT). The pattern covers source Oracle databases that are on premises or installed on an Amazon Elastic Compute Cloud (Amazon EC2) instance. It also covers Amazon Relational Database Service (Amazon RDS) for Oracle databases.

## Prerequisites and limitations
<a name="migrate-an-oracle-database-to-amazon-redshift-using-aws-dms-and-aws-sct-prereqs"></a>

**Prerequisites **
+ An Oracle database that is running in an on-premises data center or in the AWS Cloud
+ An active AWS account
+ Familiarity with [using an Oracle database as a source for AWS DMS](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html)
+ Familiarity with [using an Amazon Redshift database as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redshift.html)
+ Knowledge of Amazon RDS, Amazon Redshift, the applicable database technologies, and SQL
+ Java Database Connectivity (JDBC) drivers for AWS SCT connectors, where AWS SCT is installed

**Product versions**
+ For self-managed Oracle databases, AWS DMS supports all Oracle database editions for versions 10.2 and later (for versions 10.*x*), 11g and up to 12.2, 18c, and 19c. For Amazon RDS for Oracle databases that AWS manages, AWS DMS supports all Oracle database editions for versions 11g (versions 11.2.0.4 and later) and up to 12.2, 18c, and 19c. We recommend that you use the latest version of AWS DMS for the most comprehensive version and feature support.

## Architecture
<a name="migrate-an-oracle-database-to-amazon-redshift-using-aws-dms-and-aws-sct-architecture"></a>

**Source technology stack  **

One of the following:
+ An on-premises Oracle database
+ An Oracle database on an EC2 instance
+ An Amazon RDS for Oracle DB instance

**Target technology stack  **
+ Amazon Redshift

**Target architecture **

*From an Oracle database running in the AWS Cloud to Amazon Redshift:*

![Migrating an Oracle database in the AWS Cloud to an Amazon Redshift data warehouse.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/22807be0-c7e0-49c6-8923-7d23bf83a50d/images/7140e819-81d6-45c4-805b-8e10828076a7.png)

*From an Oracle database running in an on-premises data center to Amazon Redshift:*

![Migrating an on-premises Oracle database to an Amazon Redshift data warehouse.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/22807be0-c7e0-49c6-8923-7d23bf83a50d/images/d6654b48-0e1b-4b01-a261-5a640be01fd7.png)

## Tools
<a name="migrate-an-oracle-database-to-amazon-redshift-using-aws-dms-and-aws-sct-tools"></a>
+ [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) -  AWS Data Migration Service (AWS DMS) helps you migrate databases to AWS quickly and securely. The source database remains fully operational during the migration, minimizing downtime to applications that rely on the database. AWS DMS can migrate your data to and from most widely used commercial and open-source databases.
+ [AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) - AWS Schema Conversion Tool (AWS SCT) can be used to convert your existing database schema from one database engine to another. It supports various database engines, including Oracle, SQL Server, and PostgresSQL, as sources.

## Epics
<a name="migrate-an-oracle-database-to-amazon-redshift-using-aws-dms-and-aws-sct-epics"></a>

### Prepare for the migration
<a name="prepare-for-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the database versions. | Validate the source and target database versions and make sure they are supported by AWS DMS. For information about supported Oracle Database versions, see [Using an Oracle database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html). For information about using Amazon Redshift as a target, see [Using an Amazon Redshift database as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redshift.html). | DBA |
| Create a VPC and security group. | In your AWS account, create a virtual private cloud (VPC), if it doesn’t exist. Create a security group for outbound traffic to source and target databases. For more information, see the [Amazon Virtual Private Cloud (Amazon VPC) documentation](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html). | Systems administrator |
| Install AWS SCT. | Download and install the latest version of AWS SCT and its corresponding drivers. For more information, see [Installing, verifying, and updating the AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Installing.html). | DBA |
| Create a user for the AWS DMS task. | Create an AWS DMS user in the source database and grant it READ privileges. This user will be used by both AWS SCT and AWS DMS. | DBA |
| Test the DB connectivity. | Test the connectivity to the Oracle DB instance. | DBA |
| Create a new project in AWS SCT. | Open the AWS SCT tool and create a new project. | DBA |
| Analyze the Oracle schema to be migrated. | Use AWS SCT to analyze the schema to be migrated, and generate a database migration assessment report. For more information, see [Creating a database migration assessment report](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.Create.html) in the AWS SCT documentation. | DBA |
| Review the assessment report. | Review the report for migration feasibility. Some DB objects might require manual conversion. For more information about the report, see [Viewing the assessment report](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.View.html) in the AWS SCT documentation. | DBA |

### Prepare the target database
<a name="prepare-the-target-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon Redshift cluster. | Create an Amazon Redshift cluster within the VPC that you created previously. For more information, see [Amazon Redshift clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html) in the Amazon Redshift documentation. | DBA |
| Create database users. | Extract the list of users, roles, and grants from the Oracle source database. Create users in the target Amazon Redshift database and apply the roles from the previous step. | DBA |
| Evaluate database parameters. | Review the database options, parameters, network files, and database links from the Oracle source database, and evaluate their applicability to the target.             | DBA |
| Apply any relevant settings to the target.  | For more information about this step, see [Configuration reference](https://docs.aws.amazon.com/redshift/latest/dg/cm_chap_ConfigurationRef.html) in the Amazon Redshift documentation. | DBA |

### Create objects in the target database
<a name="create-objects-in-the-target-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an AWS DMS user in the target database. | Create an AWS DMS user in the target database and grant it read and write privileges. Validate the connectivity from AWS SCT. | DBA |
| Convert the schema, review the SQL report, and save any errors or warnings. | For more information, see [Converting database schemas using the AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Converting.html) in the AWS SCT documentation. | DBA |
| Apply the schema changes to the target database or save them as a .sql file. | For instructions, see [Saving and applying your converted schema in the AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Converting.DW.html#CHAP_Converting.DW.SaveAndApply) in the AWS SCT documentation. | DBA |
| Validate the objects in the target database. | Validate the objects that were created in the previous step in the target database. Rewrite or redesign any objects that weren’t successfully converted. | DBA |
| Disable foreign keys and triggers. | Disable any foreign key and triggers. These can cause data loading issues during the full load process when running AWS DMS. | DBA |

### Migrate data using AWS DMS
<a name="migrate-data-using-aws-dms"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an AWS DMS replication instance. | Sign in to the AWS Management Console, and open the AWS DMS console. In the navigation pane, choose **Replication instances**, **Create replication instance**. For detailed instructions, see [step 1](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html#CHAP_GettingStarted.ReplicationInstance) in *Getting started with AWS DMS* in the AWS DMS documentation. | DBA |
| Create source and target endpoints. | Create source and target endpoints, Test the connection from the replication instance to both source and target endpoints. For detailed instructions, see [step 2](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html#CHAP_GettingStarted.Endpoints) in *Getting started with AWS DMS* in the AWS DMS documentation. | DBA |
| Create a replication task. | Create a replication task and select the appropriate migration method. For detailed instructions, see [step 3](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html#CHAP_GettingStarted.Tasks) in *Getting started with AWS DMS* in the AWS DMS documentation. | DBA |
| Start the data replication. | Start the replication task and monitor the logs for any errors. | DBA |

### Migrate your application
<a name="migrate-your-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create application servers. | Create the new application servers on AWS. | Application owner |
| Migrate the application code. | Migrate the application code to the new servers. | Application owner |
| Configure the application server. | Configure the application server for the target database and drivers. | Application owner |
| Optimize the application code. | Optimize the application code for the target engine. | Application owner |

### Cut over to the target database
<a name="cut-over-to-the-target-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate users. | In the target Amazon Redshift database, validate users and grant them roles and privileges. | DBA |
| Validate that the application is locked. | Make sure that the application is locked, to prevent further changes. | Application owner |
| Validate the data. | Validate the data in the target Amazon Redshift database. | DBA |
| Enable foreign keys and triggers. | Enable foreign keys and triggers in the target Amazon Redshift database. | DBA |
| Connect to the new database. | Configure the application to connect to the new Amazon Redshift database. | Application owner |
| Perform final checks. | Perform a final, comprehensive system check before going live. | DBA, Application owner |
| Go live. | Go live with the target Amazon Redshift database. | DBA |

### Close the migration project
<a name="close-the-migration-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Shut down temporary AWS resources. | Shut down temporary AWS resources such as the AWS DMS replication instance and the EC2 instance used for AWS SCT.  | DBA, Systems administrator |
| Review documents.  | Review and validate the migration project documents.     | DBA, Systems administrator |
| Gather metrics. | Collect information about the migration project, such as the time to migrate, the percentage of manual versus tool tasks, and total cost savings.  | DBA, Systems administrator |
| Close out the project. | Close out the project and provide feedback. | DBA, Systems administrator |

## Related resources
<a name="migrate-an-oracle-database-to-amazon-redshift-using-aws-dms-and-aws-sct-resources"></a>

**References**
+ [AWS DMS user guide](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)
+ [AWS SCT user guide](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)
+ [Amazon Redshift getting started guide](https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html)

**Tutorials and videos**
+ [Dive Deep into AWS SCT and AWS DMS](https://www.youtube.com/watch?v=kJs9U4ys5FE) (presentation from AWS re:Invent 2019)
+ [Getting Started with AWS Database Migration Service](https://aws.amazon.com/dms/getting-started/)
