---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-amazon-rds-for-oracle-to-amazon-rds-for-postgresql-in-ssl-mode-by-using-aws-dms.html
---

# Migrate Amazon RDS for Oracle to Amazon RDS for PostgreSQL in SSL mode by using AWS DMS
<a name="migrate-amazon-rds-for-oracle-to-amazon-rds-for-postgresql-in-ssl-mode-by-using-aws-dms"></a>

*Pinesh Singal, Amazon Web Services*

## Summary
<a name="migrate-amazon-rds-for-oracle-to-amazon-rds-for-postgresql-in-ssl-mode-by-using-aws-dms-summary"></a>

This pattern provides guidance for migrating an Amazon Relational Database Service (Amazon RDS) for Oracle database instance to an Amazon RDS for PostgreSQL database on the Amazon Web Services (AWS) Cloud. To encrypt connections between the databases, the pattern uses certificate authority (CA) and SSL mode in Amazon RDS and AWS Database Migration Service (AWS DMS).

The pattern describes an online migration strategy with little or no downtime for a multi-terabyte Oracle source database with a high number of transactions. For data security, the pattern uses SSL when transferring the data.

This pattern uses AWS Schema Conversion Tool (AWS SCT) to convert the Amazon RDS for Oracle database schema to an Amazon RDS for PostgreSQL schema. Then the pattern uses AWS DMS to migrate data from the Amazon RDS for Oracle database to the Amazon RDS for PostgreSQL database.

## Prerequisites and limitations
<a name="migrate-amazon-rds-for-oracle-to-amazon-rds-for-postgresql-in-ssl-mode-by-using-aws-dms-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ Amazon RDS database certificate authority (CA) configured with ***rds-ca-rsa2048-g1*** only
  + The ***rds-ca-2019*** certificate expired in August 2024.
  + The ***rds-ca-2015*** certificate expired on March 5, 2020.
+ AWS SCT
+ AWS DMS
+ pgAdmin
+ SQL tools (for example, SQL Developer or SQL\*Plus)

**Limitations **
+ Amazon RDS for Oracle database – The minimum requirement is for Oracle versions 19c for the Enterprise and Standard Two editions.
+ Amazon RDS for PostgreSQL database – The minimum requirement is for PostgreSQL version 12 and later (for versions 9.x and later).

**Product versions**
+ Amazon RDS for Oracle database version 12.1.0.2 instance
+ Amazon RDS for PostgreSQL database version 11.5 instance

## Architecture
<a name="migrate-amazon-rds-for-oracle-to-amazon-rds-for-postgresql-in-ssl-mode-by-using-aws-dms-architecture"></a>

**Source technology stack  **
+ An Amazon RDS for Oracle database instance with version 12.1.0.2.v18.

**Target technology stack  **
+ AWS DMS
+ An Amazon RDS for PostgreSQL database instance with version 11.5.

**Target architecture**

The following diagram shows the architecture for data migration architecture between Oracle (source) and PostgreSQL (target) databases. The architecture includes the following:
+ A virtual private cloud (VPC)
+ An Availability Zone
+ A private subnet
+ An Amazon RDS for Oracle database
+ An AWS DMS replication instance
+ An RDS for PostgreSQL database

To encrypt connections for source and target databases, CA and SSL mode must be enabled in Amazon RDS and AWS DMS.

![Data moving between RDS for Oracle and AWS DMS, and between AWS DMS and RDS for PostgreSQL.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7098e2a3-b456-4e14-8881-c97145aef483/images/55b50ff7-1e6a-4ff0-9bcd-2fd419d5316a.png)

## Tools
<a name="migrate-amazon-rds-for-oracle-to-amazon-rds-for-postgresql-in-ssl-mode-by-using-aws-dms-tools"></a>

**AWS services**
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) helps you migrate data stores into the AWS Cloud or between combinations of cloud and on-premises setups.
+ [Amazon Relational Database Service (Amazon RDS) for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html) helps you set up, operate, and scale an Oracle relational database in the AWS Cloud.
+ [Amazon Relational Database Service (Amazon RDS) for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html) helps you set up, operate, and scale a PostgreSQL relational database in the AWS Cloud.
+ [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) supports heterogeneous database migrations by automatically converting the source database schema and a majority of the custom code to a format that’s compatible with the target database.

**Other services**
+ [pgAdmin](https://www.pgadmin.org/) is an open source management tool for PostgreSQL. It provides a graphical interface that helps you create, maintain, and use database objects.

## Best practices
<a name="migrate-amazon-rds-for-oracle-to-amazon-rds-for-postgresql-in-ssl-mode-by-using-aws-dms-best-practices"></a>

Amazon RDS provides new CA certificates as an AWS security best practice. For information about the new certificates and the supported AWS Regions, see [Using SSL/TLS to encrypt a connection to a DB instance or cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html).

If your RDS instance is currently on CA certificate `rds-ca-2019`, and you want to upgrade to `rds-ca-rsa2048-g1`, follow the instructions in [Updating your CA certificate by modifying your DB instance or cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html#UsingWithRDS.SSL-certificate-rotation-updating) or [Updating your CA certificate by applying maintenance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html#UsingWithRDS.SSL-certificate-rotation-maintenance-update).

## Epics
<a name="migrate-amazon-rds-for-oracle-to-amazon-rds-for-postgresql-in-ssl-mode-by-using-aws-dms-epics"></a>

### Configure the Amazon RDS for Oracle instance
<a name="configure-the-amazon-rds-for-oracle-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Oracle database instance. | Sign in to your AWS account, open the AWS Management Console, and navigate to the Amazon RDS console. On the console, choose **Create database**, and then choose **Oracle**. | General AWS, DBA |
| Configure security groups. | Configure inbound and outbound security groups. | General AWS |
| Create an option group. | Create an option group in the same VPC and security group as the Amazon RDS for Oracle database. For **Option**, choose **SSL**. For **Port**, choose **2484** (for SSL connections). | General AWS |
| Configure the option settings. | Use the following settings:+ `SQLNET.CIPHER_SUITE`: `SSL_RSA_WITH_AES_256_CBC_SHA`<br />+ `SQLNET.SSL_VERSION`: `1.2 or 1.0` | General AWS |
| Modify the RDS for Oracle DB instance. | Set the CA certificate as **rds-ca-rsa2048-g1**. <br />Under **Option group**, attach the previously created option group. | DBA, General AWS |
| Confirm that the RDS for Oracle DB instance is available. | Make sure that the Amazon RDS for Oracle database instance is up and running and that the database schema is accessible.<br />To connect to the RDS for Oracle DB, use the `sqlplus` command from the command line.<pre>$ sqlplus orcl/****@myoracledb.cokmvis0v46q.us-east-1.rds.amazonaws.com:1521/ORCL<br />SQL*Plus: Release 12.1.0.2.0 Production on Tue Oct 15 18:11:07 2019<br />Copyright (c) 1982, 2016, Oracle.  All rights reserved.<br />Last Successful login time: Mon Dec 16 2019 23:17:31 +05:30<br />Connected to:<br />Oracle Database 12c Enterprise Edition Release 12.1.0.2.0 - 64bit Production<br />With the Partitioning, OLAP, Advanced Analytics and Real Application Testing options<br />SQL></pre> | DBA |
| Create objects and data in the RDS for Oracle database. | Create objects and insert data in the schema. | DBA |

### Configure the Amazon RDS for PostgreSQL instance
<a name="configure-the-amazon-rds-for-postgresql-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the RDS for PostgreSQL database. | On the Amazon RDS console **Create database** page, choose **PostgreSQL** to create an Amazon RDS for PostgreSQL database instance. | DBA, General AWS |
| Configure security groups. | Configure inbound and outbound security groups. | General AWS |
| Create a parameter group. | If you are using PostgreSQL version 11.x, create a parameter group to set SSL parameters. In PostgreSQL version 12, the SSL parameter group is enabled by default. | General AWS |
| Edit parameters. | Change the `rds.force_ssl` parameter to `1` (on).<br />By default, the `ssl` parameter is `1` (on). By setting the `rds.force_ssl` parameter to `1`, you force all connections to connect through SSL mode only. | General AWS |
| Modify the RDS for PostgreSQL DB instance. | Set the CA certificate as **rds-ca-rsa2048-g1**. <br />Attach the default parameter group or the previously created parameter group, depending on your PostgreSQL version. | DBA, General AWS |
| Confirm that the RDS for PostgreSQL DB instance is available. | Make sure that the Amazon RDS for PostgreSQL database is up and running.<br />The `psql` command establishes an SSL connection with `sslmode` set from the command line.<br />One option is to set `sslmode=1` in the parameter group and use a `psql` connection without including the `sslmode` parameter in the command.<br />The following output shows that the SSL connection is established.<pre>$ psql -h mypgdbinstance.cokmvis0v46q.us-east-1.rds.amazonaws.com -p 5432 "dbname=pgdb user=pguser"<br />Password for user pguser:<br />psql (11.3, server 11.5)<br />SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)<br />Type "help" for help.<br />pgdb=></pre><br />A second option is to set `sslmode=1` in the parameter group and to include the `sslmode` parameter in the `psql` command.<br />The following output shows that the SSL connection is established.<pre>$ psql -h mypgdbinstance.cokmvis0v46q.us-east-1.rds.amazonaws.com -p 5432 "dbname=pgdb user=pguser sslmode=require"<br />Password for user pguser: <br />psql (11.3, server 11.5)<br />SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)<br />Type "help" for help.<br />pgdb=></pre> | DBA |

### Configure and run AWS SCT
<a name="configure-and-run-aws-sct"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install AWS SCT. | Install the latest version of the AWS SCT application. | General AWS |
| Configure AWS SCT with JDBC drivers. | Download the Java Database Connectivity (JDBC) drivers for Oracle ([ojdbc8.jar](https://download.oracle.com/otn-pub/otn_software/jdbc/233/ojdbc8.jar)) and PostgreSQL ([postgresql-42.2.5.jar](https://jdbc.postgresql.org/download/postgresql-42.2.19.jar)).<br />To configure the drivers in AWS SCT, choose **Settings**, **Global settings**, **Drivers**. | General AWS |
| Create the AWS SCT project. | Create the AWS SCT project and report, using Oracle as the source DB engine and Amazon RDS for PostgreSQL as the target DB engine:1. Test connections to the source Oracle database and target Amazon RDS for PostgreSQL database by providing connection details.<br />For the source Oracle database, the following permissions or privileges are required:`CONNECT``SELECT_CATALOG_ROLE``SELECT ANY DICTIONARY``SELECT on SYS.USER$ TO <sct_user>`<br />For more information, see [Using Oracle Database as a source for AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Oracle.html).<br />Both source and target connections must be successful before AWS SCT can start the migration report.<br />2. After the report, enter the schema to be converted, and choose **Finish**. | General AWS |
| Validate database objects. | 1. Choose **Load schema**.<br />AWS SCT displays the source and the converted target objects, including objects that that have errors. Update any incorrect objects on the target database.<br />2. Review the errors, and clear them by using manual intervention.<br />3. After all errors are cleared, choose **Load schema** again.<br />4. Choose **Apply to database**.<br />5. Connect to pgAdmin, or any tool that supports a PostgreSQL DB connection, and check the schema and objects. | DBA, General AWS |

### Configure and run AWS DMS
<a name="configure-and-run-aws-dms"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a replication instance. | 1. Sign in to your account, open the AWS Management Console, and navigate to the AWS DMS console.<br />2. Create a replication instance with valid settings for the VPC, security group, Availability Zone, and extra connection attributes. | General AWS |
| Import the certificate. | Download the [certificate bundle (PEM)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html#UsingWithRDS.SSL.CertificatesAllRegions) for your AWS Region.<br />The bundle contains both the `rds-ca-2019` intermediate and root certificates. The bundle also contains the `rds-ca-rsa2048-g1`, `rds-ca-rsa4096-g1`, and `rds-ca-ecc384-g1` root CA certificates. Your application trust store needs to register only the root CA certificate. | General AWS |
| Create the source endpoint. | 1. Create a source endpoint for Amazon RDS for Oracle by choosing **Select RDS DB instance** and then selecting the RDS for Oracle DB instance that you created. The endpoint configuration details will be automatically populated.<br />2. Choose **Provide access information manually**. For **Port**, make sure that you enter **2484**.<br />3. Under **Secure Socket Layer (SSL) mode**, choose `verify-ca`, and then choose the CA certificate that you created previously.<br />4. Under **Endpoint settings**, add the extra connection attribute `NumberDataTypeScale=-2` to support the `NUMBER` data type with no size.For more information, see [Using an Oracle database as a source for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html). | General AWS |
| Create the target endpoint. | 1. Create a target endpoint for Amazon RDS for PostgreSQL by choosing **Select RDS DB instance** and then selecting your RDS for PostgreSQL DB instance. The endpoint configuration details will be automatically populated.<br />2. Choose** Provide access information manually**. For **Port**, make sure that you enter **2484**.For more information, see [Using a PostgreSQL database as a target for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html). | General AWS |
| Test the endpoints. | 1. Test the source and target endpoints to confirm that both are successful and available.<br />2. If a test fails, make sure that the security group inbound rules are valid. | General AWS |
| Create migration tasks. | To create a migration task for full load and change data capture (CDC) or for data validation, do the following:1. To create a database migration task, choose the replication instance, source database endpoint, target database endpoint. Specify the migration type as one of the following:**Migrate existing data** (full load)**Replicate data changes only (CDC)****Migrate existing data and replicate ongoing changes** (full load and CDC)<br />2. Under **Table mappings**, you can configure selection rules and transformation rules in GUI or JSON formats:Under **Selection rules**, select the schema, enter the table name, and select the action (Include or Exclude) to be configured; for example, Schema ORCL, Table name %, Action Include.Under **Transformation rules**, do one of the following:Select the schema and choose the action (case, prefix, suffix); for example, Target Schema ORCL, Action Make lowercase.Select the schema, enter the table name, and choose the action (case, prefix, suffix); for example, Target Schema ORCL, Table %, Action Make lowercase.<br />3. Turn on Amazon CloudWatch Logs monitoring.<br />4. For the mapping rules, add the following JSON code.<pre>{<br />    "rules": [<br />        {<br />            "rule-type": "transformation",<br />            "rule-id": "1",<br />            "rule-name": "1",<br />            "rule-target": "table",<br />            "object-locator": {<br />                "schema-name": "%",<br />                "table-name": "%"<br />            },<br />            "rule-action": "convert-lowercase",<br />            "value": null,<br />            "old-value": null<br />        },<br />        {<br />            "rule-type": "transformation",<br />            "rule-id": "2",<br />            "rule-name": "2",<br />            "rule-target": "schema",<br />            "object-locator": {<br />                "schema-name": "ORCL",<br />                "table-name": "%"<br />            },<br />            "rule-action": "convert-lowercase",<br />            "value": null,<br />            "old-value": null<br />        },<br />        {<br />            "rule-type": "selection",<br />            "rule-id": "3",<br />            "rule-name": "3",<br />            "object-locator": {<br />                "schema-name": "ORCL",<br />                "table-name": "DEPT"<br />            },<br />            "rule-action": "include",<br />            "filters": []<br />        }<br />    ]<br />}</pre> | General AWS |
| Plan the production run. | Confirm downtime with stakeholders such as application owners to run AWS DMS in production systems. | Migration lead |
| Run the migration task. | 1. Start the AWS DMS task that has a status of **Ready**, and monitor the migration task logs in Amazon CloudWatch for any errors.<br />If you chose **Migrate existing data and replicate ongoing changes** as the migration type, and the status is **Load complete ongoing replication**, the full load with CDC data migration is completed and validation is ongoing.<br />2. After you start the migration, you can obtain additional SSL-connection information in CloudWatch. For Oracle, CloudWatch shows the following connection string.<br />`2019-12-17T09:15:11 [SOURCE_UNLOAD ]I: Connecting to Oracle: Beginning session (oracle_endpoint_conn.c:834)`<br />The PostgreSQL connection string will be similar to the following example.<br />`2019-12-17T09:15:11 [TARGET_LOAD ]I: Going to connect to ODBC connection string: PROTOCOL=7.4-0;DRIVER={PostgreSQL};SERVER=mypgdbinstance.cokmvis0v46q.us-east-1.rds.amazonaws.com;DATABASE=pgdb;PORT=5432;sslmode=require;UID=pguser; (odbc_endpoint_imp.c:2218)` | General AWS |
| Validate the data. | Review migration task results and data in the source Oracle and target PostgreSQL databases:1. Connect to pgAdmin and check the data in your PostgreSQL database with schema `ORCL`.<br />2. For CDC, check the ongoing changes by inserting or updating data in the source Oracle database. | DBA |
| Stop the migration task. | After you successfully complete the data validation, stop the migration task. | General AWS |

### Clean up the resources
<a name="clean-up-the-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the AWS DMS tasks. | 1. On the AWS DMS console, navigate to **Database migration tasks**, and stop any ongoing or running AWS DMS task.<br />2. Select the task or tasks, choose **Actions**, and choose **Delete**. | General AWS |
| Delete the AWS DMS endpoints. | Select the source and target endpoints that you created, choose **Actions**, and choose **Delete**. | General AWS |
| Delete the AWS DMS replication instance. | Choose the replication instance, choose **Actions**, and then choose **Delete**. | General AWS |
| Delete the PostgreSQL database. | 1. On the Amazon RDS console, choose **Databases**.<br />2. Select the PostgreSQL database instance that you created, choose **Actions**, and then choose **Delete**. | General AWS |
| Delete the Oracle database. | On the Amazon RDS console, select the Oracle database instance, choose **Actions**, and then choose **Delete**. | General AWS |

## Troubleshooting
<a name="migrate-amazon-rds-for-oracle-to-amazon-rds-for-postgresql-in-ssl-mode-by-using-aws-dms-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| AWS SCT source and target test connections are failing. | Configure JDBC driver versions and VPC security group inbound rules to accept the incoming traffic. |
| The Oracle source endpoint test run fails. | Check the endpoint settings and whether the replication instance is available. |
| The AWS DMS task full-load run fails. | Check whether the source and target databases have matching data types and sizes. |
| The AWS DMS validation migration task returns errors. | 1. Check whether the table has a primary key. Tables without a primary key are not validated.<br />2. If the table has a primary key but returns errors, check the extra connection attribute in the source endpoint. The extra connection attribute must have `numberDataTypeScale=-2` to support the `NUMBER` data type with no size dynamically based on data available in table. |

## Related resources
<a name="migrate-amazon-rds-for-oracle-to-amazon-rds-for-postgresql-in-ssl-mode-by-using-aws-dms-resources"></a>

**Databases**
+ [Amazon RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html)
+ [Amazon RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html)

**SSL DB connection**
+ [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html)
  + [Using SSL with an RDS for Oracle DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.SSL.html)
  + [Securing connections to RDS for PostgreSQL with SSL/TLS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.Security.html)
  + [Download certificate bundles for specific AWS Regions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html#UsingWithRDS.SSL.CertificatesAllRegions)
    + [Download CA-2019 root certificate](https://s3.amazonaws.com/rds-downloads/rds-ca-2019-root.pem) (expired in August 2024)
+ [Working with option groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.html)
  + [Adding options to Oracle DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.html)
  + [Oracle Secure Sockets Layer](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.SSL.html)
+ [Working with parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html)
+ [PostgreSQL sslmode connection parameter](https://www.postgresql.org/docs/11/libpq-connect.html#LIBPQ-CONNECT-SSLMODE)
+ [Using SSL from JDBC](https://jdbc.postgresql.org/documentation/ssl/)
+ [Rotating your SSL/TLS certificate](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html)
  + [Updating your CA certificate by modifying your DB instance or cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html#UsingWithRDS.SSL-certificate-rotation-updating)
  + [Updating your CA certificate by applying maintenance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html#UsingWithRDS.SSL-certificate-rotation-maintenance-update)

**AWS SCT**
+ [AWS Schema Conversion Tool](https://aws.amazon.com/dms/schema-conversion-tool/)
+ [AWS Schema Conversion Tool User Guide](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)
+ [Using the AWS SCT user interface](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.html)
+ [Using Oracle Database as a source for AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Oracle.html)

**AWS DMS**
+ [AWS Database Migration Service](https://aws.amazon.com/dms/)
+ [AWS Database Migration Service User Guide](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)
  + [Using an Oracle database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html)
  + [Using a PostgreSQL database as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html)
+ [Using SSL with AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.SSL.html)
+ [Migrating Applications Running Relational Databases to AWS](https://d1.awsstatic.com/whitepapers/Migration/migrating-applications-to-aws.pdf)

## Additional information
<a name="migrate-amazon-rds-for-oracle-to-amazon-rds-for-postgresql-in-ssl-mode-by-using-aws-dms-additional"></a>

Amazon RDS Certificate Authority certificates `rds-ca-2019` expired in August 2024. If you use or plan to use SSL or TLS with certificate verification to connect to your RDS DB instances or Multi-AZ DB clusters, consider using one of the new CA certificates: `rds-ca-rsa2048-g1`, `rds-ca-rsa4096-g1`, or `rds-ca-ecc384-g1`.
