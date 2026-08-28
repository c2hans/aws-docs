---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-oracle-database-to-amazon-rds-for-oracle-by-using-oracle-goldengate-flat-file-adapters.html
---

# Migrate an Oracle database to Amazon RDS for Oracle by using Oracle GoldenGate flat file adapters
<a name="migrate-an-oracle-database-to-amazon-rds-for-oracle-by-using-oracle-goldengate-flat-file-adapters"></a>

*Dhairya Jindani and Baji Shaik, Amazon Web Services*

## Summary
<a name="migrate-an-oracle-database-to-amazon-rds-for-oracle-by-using-oracle-goldengate-flat-file-adapters-summary"></a>

Oracle GoldenGate is a real-time data capture and replication service for heterogeneous databases and IT environments. However, this service doesn’t currently support Amazon Relational Database Service (Amazon RDS) for Oracle. For a list of supported databases, see [Oracle GoldenGate for Heterogeneous Databases](https://docs.oracle.com/goldengate/c1230/gg-winux/GGHDB/12.3-what-is-oracle-goldengate-heterogeneous-databases.htm#GGHDB-GUID-08EAC588-F76C-4E37-BEBA-0DC57B98CA46) (Oracle documentation). This pattern describes how to use Oracle GoldenGate and Oracle GoldenGate flat file adapters to generate flat files from the source Oracle database, which can be on-premises or on an Amazon Elastic Compute Cloud (Amazon EC2) instance. You can then import those flat files to an Amazon RDS for Oracle database instance.

In this pattern, you use Oracle GoldenGate to extract the trail files from your source Oracle database. The data pump copies the trail files to an integration server, which is an Amazon EC2 instance. On the integration server, Oracle GoldenGate uses the flat file adapter to generate a series of sequential flat files based on the transational data capture of the trail files.Oracle GoldenGate formats the data as either delimiter-separated values or length-delimited values. You then use Oracle SQL\*Loader to import the flat files into the target Amazon RDS for Oracle database instance.

**Intended audience**

This pattern is intended for those who have experience with and knowledge of an Oracle GoldenGate's fundamental building blocks. For more information, see [Overview of the Oracle GoldenGate Architecture](https://docs.oracle.com/goldengate/1212/gg-winux/GWUAD/wu_about_gg.htm#GWUAD115) (Oracle documentation).

## Prerequisites and limitations
<a name="migrate-an-oracle-database-to-amazon-rds-for-oracle-by-using-oracle-goldengate-flat-file-adapters-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ An Oracle GoldenGate license.
+ A separate license for an Oracle GoldenGate adapter.
+ A source Oracle database, either running on-premises or on an Amazon EC2 instance.
+ An Amazon EC2 Linux instance that is used as the integration server. For more information, see [Get started with Amazon EC2 Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) (Amazon EC2 documentation).
+ A target Amazon RDS for Oracle database instance. For more information, see [Creating an Oracle DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.Oracle.html) (Amazon RDS documentation).

**Product versions**
+ Oracle Database Enterprise Edition version 10g, 11g, 12c, or later
+ Oracle GoldenGate version 12.2.0.1.1 or later

## Architecture
<a name="migrate-an-oracle-database-to-amazon-rds-for-oracle-by-using-oracle-goldengate-flat-file-adapters-architecture"></a>

**Source technology stack**

An Oracle database (on premises or on an Amazon EC2 instance)

**Target technology stack**

Amazon RDS for Oracle

**Source and target architecture**

![Migrating an Oracle database to Amazon RDS for Oracle by using an Oracle GoldenGate adapter.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/f34961f7-aa9a-41cb-b1ea-522e36ef2f67/images/21ef5177-e669-4591-aced-28d2f22decf2.png)

1. Oracle GoldenGate extracts trails from the source database logs.

1. The data pump extracts the trails and migrates them to an integration server.

1. The Oracle GoldenGate flat file adapter reads the trails, source definitions, and extract parameters.

1. You exit the extraction, which generates a control file and flat data files.

1. You migrate the flat data files to an Amazon RDS for Oracle database instance in the AWS Cloud.

## Tools
<a name="migrate-an-oracle-database-to-amazon-rds-for-oracle-by-using-oracle-goldengate-flat-file-adapters-tools"></a>

**AWS services**
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) for Oracle helps you set up, operate, and scale an Oracle relational database in the AWS Cloud.

**Other services**
+ [Oracle GoldenGate](https://docs.oracle.com/goldengate/1212/gg-winux/GWUAD/wu_about_gg.htm#GWUAD110) is a service that helps you to replicate, filter, and transform data from one database to another heterogeneous database or to another target topology, such as flat files.
+ [Oracle GoldenGate application adapters](https://docs.oracle.com/goldengate/gg121211/gg-adapter/GADAD/flatfile_config.htm#GADAD424) enable Oracle GoldenGate to produce a series of sequential flat files and control files from transactional data captured in the trail files of a source database. These adapters are widely used for extract, transform, and load (ETL) operations in data warehouse applications and proprietary or legacy applications. Oracle GoldenGate performs this capture and applies it in near real-time across heterogeneous databases, platforms, and operating systems. The adapters support different formats for the output files, such as CSV or Apache Parquet. You can load these generated files in order to load the data into different heterogeneous databases.

## Epics
<a name="migrate-an-oracle-database-to-amazon-rds-for-oracle-by-using-oracle-goldengate-flat-file-adapters-epics"></a>

### Set up Oracle GoldenGate on the source database server
<a name="set-up-oracle-goldengate-on-the-source-database-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download Oracle GoldenGate. | On the source database server, download Oracle GoldenGate version 12.2.0.1.1 or later. For instructions, see [Downloading Oracle GoldenGate](https://docs.oracle.com/goldengate/1212/gg-winux/GIORA/install.htm#GIORA164) (Oracle documentation). | DBA |
| Install Oracle GoldenGate. | For instructions, see [Installing Oracle GoldenGate](https://docs.oracle.com/goldengate/1212/gg-winux/GIORA/install.htm#GIORA162) (Oracle documentation). | DBA |
| Set up Oracle GoldenGate. | For instructions, see [Preparing the Database for Oracle GoldenGate](https://docs.oracle.com/goldengate/1212/gg-winux/GIORA/setup.htm#GIORA357) (Oracle documentation). | DBA |

### Set up Oracle GoldenGate on the integration server
<a name="set-up-oracle-goldengate-on-the-integration-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download Oracle GoldenGate. | On the integration server, download Oracle GoldenGate version 12.2.0.1.1 or later. For instructions, see [Downloading Oracle GoldenGate](https://docs.oracle.com/goldengate/1212/gg-winux/GIORA/install.htm#GIORA164) (Oracle documentation). | DBA |
| Install Oracle GoldenGate. | Create directories, set up the manager process, and create the `defgen` file for a heterogeneous environment. For instructions, see [Installing Oracle GoldenGate](https://docs.oracle.com/goldengate/1212/gg-winux/GIORA/install.htm#GIORA162) (Oracle documentation). | DBA |

### Change the Oracle GoldenGate data capture configuration
<a name="change-the-oracle-goldengate-data-capture-configuration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare the Oracle GoldenGate adapters. | On the integration server, set up the Oracle GoldenGate adapter software. Do the following:1. From [Oracle Software Delivery Cloud](https://edelivery.oracle.com/), download **ggs\_Adapters\_Linux\_x64.zip**.<br />2. Unzip **ggs\_Adapters\_Linux\_x64.zip**.<br />3. Run the following command to install the adapters:<pre>tar -xvf ggs_Adapters_Linux_x64.tar</pre> | DBA |
| Configure the data pump. | On the source server, configure the data pump to transfer the trail file from the source server to the integration server. Create the data pump parameter file and trails file directory. For instructions, see [Configuring the Flat File Adapter](https://docs.oracle.com/goldengate/gg12201/gg-adapter/GADAD/GUID-DF13488D-E0E9-497C-8AFF-70B839DE4843.htm#GADAD424) (Oracle documentation). | DBA |

### Generate and migrate the flat files
<a name="generate-and-migrate-the-flat-files"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Generate the flat files. | Create the extract file and control file, and then start the extraction process on the integration server. This extracts the database changes and writes the source database to the flat files. For instructions, see [Using the Flat File Adapter](https://docs.oracle.com/goldengate/gg12201/gg-adapter/GADAD/GUID-D30CC70D-B90F-4209-BEB5-9BA53EA869EF.htm#GADAD432) (Oracle documentation). | DBA |
| Load the flat files to the target database. | Load the flat files into the target Amazon RDS for Oracle database instance. For more information, see [Importing using Oracle SQL\*Loader](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Procedural.Importing.SQLLoader.html) (Amazon RDS documentation). | DBA |

## Troubleshooting
<a name="migrate-an-oracle-database-to-amazon-rds-for-oracle-by-using-oracle-goldengate-flat-file-adapters-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| The Oracle GoldenGate flat file adapter generates an error. | For a description of the adapter errors, see [Locating Error Messages](https://docs.oracle.com/goldengate/gg12201/gg-adapter/GADAD/GUID-D30CC70D-B90F-4209-BEB5-9BA53EA869EF.htm#GADAD437) (Oracle documentation). For troubleshooting instructions, see [Troubleshooting the Flat File Adapter](https://docs.oracle.com/goldengate/gg12201/gg-adapter/GADAD/GUID-CB3D9B2C-49CC-408A-8C00-06E0C7923DD6.htm#GADAD552) (Oracle documentation). |

## Related resources
<a name="migrate-an-oracle-database-to-amazon-rds-for-oracle-by-using-oracle-goldengate-flat-file-adapters-resources"></a>
+ [Installing Oracle GoldenGate](https://docs.oracle.com/goldengate/1212/gg-winux/GIORA/install.htm#GIORA162) (Oracle documentation)
+ [Configuring Oracle GoldenGate](https://docs.oracle.com/goldengate/1212/gg-winux/GIORA/setup.htm#GIORA357) (Oracle documentation)
+ [Understanding Oracle GoldenGate Adapters](https://docs.oracle.com/goldengate/gg12201/gg-adapter/GADAD/GUID-F9105B02-9836-4F98-99F8-6E9C46D42764.htm#GADAD101) (Oracle documentation)
+ [Configuring the Flat File Adapter](https://docs.oracle.com/goldengate/gg12201/gg-adapter/GADAD/GUID-DF13488D-E0E9-497C-8AFF-70B839DE4843.htm#GADAD424) (Oracle documentation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
