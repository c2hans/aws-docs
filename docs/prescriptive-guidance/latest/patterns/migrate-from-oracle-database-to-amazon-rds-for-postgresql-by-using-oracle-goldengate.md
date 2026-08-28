---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-oracle-database-to-amazon-rds-for-postgresql-by-using-oracle-goldengate.html
---

# Migrate from Oracle Database to Amazon RDS for PostgreSQL by using Oracle GoldenGate
<a name="migrate-from-oracle-database-to-amazon-rds-for-postgresql-by-using-oracle-goldengate"></a>

*Dhairya Jindani, Sindhusha Paturu, and Rajeshkumar Sabankar, Amazon Web Services*

## Summary
<a name="migrate-from-oracle-database-to-amazon-rds-for-postgresql-by-using-oracle-goldengate-summary"></a>

This pattern shows how to migrate an Oracle database to Amazon Relational Database Service (Amazon RDS) for PostgreSQL by using Oracle Cloud Infrastructure (OCI) GoldenGate.

By using Oracle GoldenGate, you can replicate data between your source database and one or more destination databases with minimal downtime.

**Note**
The source Oracle database can be either on-premises or on an Amazon Elastic Compute Cloud (Amazon EC2) instance. You can use a similar procedure when using on-premises replication tools.

## Prerequisites and limitations
<a name="migrate-from-oracle-database-to-amazon-rds-for-postgresql-by-using-oracle-goldengate-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An Oracle GoldenGate license
+ Java Database Connectivity (JDBC) driver to connect to the PostgreSQL database
+ Schema and tables created with the [AWS Schema Conversion Tool (AWS SCT)](https://aws.amazon.com/dms/schema-conversion-tool/) on the target Amazon RDS for PostgreSQL database

**Limitations**
+ Oracle GoldenGate can replicate existing table data (initial load) and ongoing changes (change data capture) only

**Product versions**
+ Oracle Database Enterprise Edition 10g or newer versions
+ Oracle GoldenGate 12.2.0.1.1 for Oracle or newer versions
+ Oracle GoldenGate 12.2.0.1.1 for PostgreSQL or newer versions

## Architecture
<a name="migrate-from-oracle-database-to-amazon-rds-for-postgresql-by-using-oracle-goldengate-architecture"></a>

The following diagram shows an example workflow for migrating an Oracle database to Amazon RDS for PostgreSQL by using Oracle GoldenGate:

![Migration workflow from on-premises Oracle database to Amazon RDS for PostgreSQL.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/384f0eaf-8582-474a-a7f4-ec1048a4feb3/images/de541887-0d5f-4a9a-b136-ce2599355cb8.png)

The diagram shows the following workflow:

1. The Oracle GoldenGate [Extract process](https://docs.oracle.com/goldengate/c1230/gg-winux/GGCON/processes-and-terminology.htm#GUID-6419F3A9-71EC-4D14-9C41-3BAA1E3CA19C) runs against the source database to extract data.

1. The Oracle GoldenGate [Replicat process](https://docs.oracle.com/goldengate/c1230/gg-winux/GGCON/processes-and-terminology.htm#GUID-5EF0326C-9058-4C40-8925-98A223388C95) delivers the extracted data to the target Amazon RDS for PostgreSQL database.

## Tools
<a name="migrate-from-oracle-database-to-amazon-rds-for-postgresql-by-using-oracle-goldengate-tools"></a>
+ [Oracle GoldenGate](https://www.oracle.com/integration/goldengate/#:~:text=OCI%20GoldenGate%20is%20a%20real,in%20the%20Oracle%20Cloud%20Infrastructure.) helps you design, run, orchestrate, and monitor your data replication and stream data processing solutions in the Oracle Cloud Infrastructure.
+ [Amazon Relational Database Service (Amazon RDS) for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html) helps you set up, operate, and scale a PostgreSQL relational database in the AWS Cloud.

## Epics
<a name="migrate-from-oracle-database-to-amazon-rds-for-postgresql-by-using-oracle-goldengate-epics"></a>

### Download and install Oracle GoldenGate
<a name="download-and-install-oracle-goldengate"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download Oracle GoldenGate. | Download the following versions of Oracle GoldenGate:+ Oracle GoldenGate 12.2.0.1.1 for Oracle or a newer version<br />+ Oracle GoldenGate 12.2.0.1.1 for PostgreSQL or a newer version<br />To download the software, see [Oracle GoldenGate Downloads](https://www.oracle.com/middleware/technologies/goldengate-downloads.html) on the Oracle website. | DBA |
| Install Oracle GoldenGate for Oracle on the source Oracle Database server. | For instructions, see the [Oracle GoldenGate documentation](https://docs.oracle.com/goldengate/1212/gg-winux/GIORA/toc.htm). | DBA |
| Install Oracle GoldenGate for PostgreSQL database on the Amazon EC2 instance. | For instructions, see the [Oracle GoldenGate documentation](https://docs.oracle.com/goldengate/1212/gg-winux/GIORA/toc.htm). | DBA |

### Configure Oracle GoldenGate on the source and target databases
<a name="configure-oracle-goldengate-on-the-source-and-target-databases"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up Oracle GoldenGate for Oracle Database on the source database. | For instructions, see the [Oracle GoldenGate documentation](https://docs.oracle.com/goldengate/1212/gg-winux/GIORA/toc.htm).<br />Make sure that you configure the following:+ Supplemental logging<br />+ Oracle GoldenGate users<br />+ Any required grants and permissions<br />+ Parameter files<br />+ Manager process<br />+ Directory<br />+ **GLOBALS** files<br />+ Oracle Wallet | DBA |
| Set up Oracle GoldenGate for PostgreSQL on the target database. | For instructions, see [Part VI Using Oracle GoldenGate for PostgreSQL](https://docs.oracle.com/en/middleware/goldengate/core/19.1/gghdb/using-oracle-goldengate-postgresql.html) on the Oracle website.<br />Make sure that you configure the following:+ Manager process<br />+ **GLOBALS** files<br />+ Oracle Wallet | DBA |

### Configure the data capture
<a name="configure-the-data-capture"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the Extract process in the source database. | In the source Oracle Database, create an extract file to extract data.<br />For instructions, see [ADD EXTRACT](https://docs.oracle.com/goldengate/1212/gg-winux/GWURF/ggsci_commands006.htm#GWURF122) in the Oracle documentation.The extract file includes the creation of the extract parameter file and trail file directory. | DBA |
| Set up a data pump to transfer the trail file from the source to the target database. | Create an EXTRACT parameter file and trail file directory by following the instructions in [PARFILE](https://docs.oracle.com/database/121/SUTIL/GUID-7A045C82-5993-44EB-AFAD-B7D39C34BCCD.htm#SUTIL859) in *Database Utilities* on the Oracle website.<br />For more information, see [What is a Trail?](https://docs.oracle.com/goldengate/c1230/gg-winux/GGCON/processes-and-terminology.htm#GUID-88674F53-1E07-4C00-9868-598F82D7113C) in *Fusion Middleware Understanding Oracle GoldenGate* on the Oracle website. | DBA |
| Set up replication on the Amazon EC2 instance. | Create a replication parameter file and trail file directory.<br />For more information about creating replication parameter files, see section [3.5 Validating a parameter file](https://docs.oracle.com/en/middleware/goldengate/core/21.3/admin/using-oracle-goldengate-parameter-files.html#GUID-1E32A9AD-25DB-4243-93CD-E643E7116215) in the Oracle Database documentation.<br />For more information about creating a trail file directory, see [Creating a trail](https://docs.oracle.com/en/cloud/paas/goldengate-cloud/gwuad/creating-trail.html) in the Oracle Cloud documentation.Make sure that you add a checkpoint table entry in the GLOBALS file at the target.<br />For more information, see [What is a Replicat?](https://docs.oracle.com/goldengate/c1230/gg-winux/GGCON/processes-and-terminology.htm#GGCON-GUID-5EF0326C-9058-4C40-8925-98A223388C95) in *Fusion Middleware Understanding Oracle GoldenGate* on the Oracle website. | DBA |

### Configure the data replication
<a name="configure-the-data-replication"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| In the source database, create a parameter file to extract data for the initial load. | Follow the instructions in [Creating a parameter file in GGSCI](https://docs.oracle.com/en/cloud/paas/goldengate-cloud/gwuad/using-oracle-goldengate-parameter-files.html#GUID-5C49C522-8B28-4E4B-908D-66A33717CE6C) in the Oracle Cloud documentation.Make sure that the Manager is running on the target. | DBA |
| In the target database, create a parameter file to replicate data for the initial load. | Follow the instructions in [Creating a parameter file in GGSCI](https://docs.oracle.com/en/cloud/paas/goldengate-cloud/gwuad/using-oracle-goldengate-parameter-files.html#GUID-5C49C522-8B28-4E4B-908D-66A33717CE6C) in the Oracle Cloud documentation.Make sure that you add and start the Replicat process. | DBA |

### Cut over to the Amazon RDS for PostgreSQL database
<a name="cut-over-to-the-amazon-rds-for-postgresql-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Stop the Replicat process and make sure that the source and target databases are in sync. | Compare row counts between the source and target databases to make sure that the data replication was successful. | DBA |
| Configure data definition language (DDL) support. | Run the DDL script for creating triggers, sequence, synonyms, and referential keys on PostgreSQL.You can use any standard SQL client application to connect to a database in your DB cluster. For example, you can use [pgAdmin](https://www.pgadmin.org/) to connect to your DB instance. | DBA |

## Related resources
<a name="migrate-from-oracle-database-to-amazon-rds-for-postgresql-by-using-oracle-goldengate-resources"></a>
+ [Amazon RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html) (*Amazon RDS User Guide*)
+ [Amazon EC2 documentation](https://docs.aws.amazon.com/ec2/)
+ [Oracle GoldenGate supported processing methods and databases](https://docs.oracle.com/goldengate/1212/gg-winux/GWUAD/wu_about_gg.htm#GWUAD112) (Oracle documentation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
