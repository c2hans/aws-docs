---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-mariadb-database-to-amazon-rds-for-mariadb-using-native-tools.html
---

# Migrate an on-premises MariaDB database to Amazon RDS for MariaDB using native tools
<a name="migrate-an-on-premises-mariadb-database-to-amazon-rds-for-mariadb-using-native-tools"></a>

*Shyam Sunder Rakhecha, Amazon Web Services*

## Summary
<a name="migrate-an-on-premises-mariadb-database-to-amazon-rds-for-mariadb-using-native-tools-summary"></a>

This pattern provides guidance for migrating an on-premises MariaDB database to Amazon Relational Database Service (Amazon RDS) for MariaDB by using native tools. If you have MySQL tools installed, you can use **mysql **and **mysqldump**. If you have MariaDB tools installed, you can use **mariadb** and **mariadb-dump**. MySQL and MariaDB tools have the same origin, but there are minor differences in MariaDB version 10.6 and later.

## Prerequisites and limitations
<a name="migrate-an-on-premises-mariadb-database-to-amazon-rds-for-mariadb-using-native-tools-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A MariaDB source database in an on-premises data center

**Limitations**
+ Database size limit: 64 TB

**Product versions**
+ MariaDB versions 10.0-10.6 (for the latest list of supported versions, see [MariaDB on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MariaDB.html#MariaDB.Concepts.VersionMgmt) in the AWS documentation)

## Architecture
<a name="migrate-an-on-premises-mariadb-database-to-amazon-rds-for-mariadb-using-native-tools-architecture"></a>

**Source technology stack**
+ MariaDB database in an on-premises data center

**Target technology stack**
+ Amazon RDS for MariaDB DB instance

**Target architecture**

![Architecture diagram with primary and standby RDS DB instances in different Availability Zones.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7be644e0-da42-4515-87b7-04da7a054adb/images/eca8eb55-579a-42e2-96ce-9b14b097b4c9.png)

**Data migration architecture**

![Architecture diagram of migrating an on-premises MariaDB database to Amazon RDS](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7be644e0-da42-4515-87b7-04da7a054adb/images/daba40e2-a2b1-44f8-8e69-31458206a823.png)

## Tools
<a name="migrate-an-on-premises-mariadb-database-to-amazon-rds-for-mariadb-using-native-tools-tools"></a>
+ Native MySQL tools: **mysql** and **mysqldump**
+ Native MariaDB tools: **mariadb** and **mariadb-dump**

## Epics
<a name="migrate-an-on-premises-mariadb-database-to-amazon-rds-for-mariadb-using-native-tools-epics"></a>

### Plan the migration
<a name="plan-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate source and target database versions and engines. |  | DBA |
| Identify hardware requirements for the target server instance. |  | DBA, Systems administrator |
| Identify storage requirements (storage type and capacity). |  | DBA, Systems administrator |
| Choose the proper instance type based on capacity, storage features, and network features. |  | DBA, Systems administrator |
| Identify the network access security requirements for source and target databases. |  | DBA, Systems administrator |
| Identify the application migration strategy. |  | DBA, App owner, Systems administrator |

### Configure the infrastructure
<a name="configure-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a virtual private cloud (VPC). |  | Systems administrator |
| Create security groups. |  | Systems administrator |
| Configure and start an Amazon RDS DB instance running MariaDB. |  | Systems administrator |

### Migrate data
<a name="migrate-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Use native tools to migrate database objects and data. | In the source database, use **mysqldump **or** mariadb-dump** to create an output file that contains database objects and data. In the target database, use **mysql **or **mariadb **to restore the data. | DBA |
| Validate the data. | Check the source and target databases to confirm that the data migration was successful. | DBA |

### Migrate the application
<a name="migrate-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Follow the application migration strategy. |  | DBA, App owner, Systems administrator |

### Cut over
<a name="cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Switch the application clients over to the new infrastructure. |  | DBA, App owner, Systems administrator |

### Close the project
<a name="close-the-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Shut down the temporary AWS resources. |  | Systems administrator |
| Review and validate the project documents. |  | DBA, App owner, Systems administrator |
| Gather metrics around time to migrate, cost savings provided by tools, and so on. |  | DBA, App owner, Systems administrator |
| Close out the project and provide feedback. |  | DBA, App owner, Systems administrator |

## Related resources
<a name="migrate-an-on-premises-mariadb-database-to-amazon-rds-for-mariadb-using-native-tools-resources"></a>

**Amazon RDS references**
+ [Amazon RDS for MariaDB](https://aws.amazon.com/rds/mariadb/)
+ [Amazon Virtual Private Cloud VPCs and Amazon RDS](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html)
+ [Amazon RDS Multi-AZ Deployments](https://aws.amazon.com/rds/details/multi-az/)
+ [Amazon RDS Pricing](https://aws.amazon.com/rds/pricing/)

**MySQL and MariaDB references**
+ [mariadb-dump/mysqldump](https://mariadb.com/kb/en/mariadb-dumpmysqldump/)
+ [mysql Command-line Client](https://mariadb.com/kb/en/mysql-command-line-client/)

**Tutorials and videos**
+ [Getting Started with Amazon RDS](https://aws.amazon.com/rds/getting-started/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
