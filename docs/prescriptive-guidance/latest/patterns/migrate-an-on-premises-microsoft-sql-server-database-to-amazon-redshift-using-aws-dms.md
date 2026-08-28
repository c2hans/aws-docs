---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-microsoft-sql-server-database-to-amazon-redshift-using-aws-dms.html
---

# Migrate an on-premises Microsoft SQL Server database to Amazon Redshift using AWS DMS
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-redshift-using-aws-dms"></a>

*Marcelo Fernandes, Amazon Web Services*

## Summary
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-redshift-using-aws-dms-summary"></a>

This pattern provides guidance for migrating an on-premises Microsoft SQL Server database to Amazon Redshift by using AWS Data Migration Service (AWS DMS).

## Prerequisites and limitations
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-redshift-using-aws-dms-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A source Microsoft SQL Server database in an on-premises data center
+ Completed prerequisites for using an Amazon Redshift database as a target for AWS DMS, as discussed in the [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redshift.html#CHAP_Target.Redshift.Prerequisites)

**Product versions**
+ SQL Server 2005-2019, Enterprise, Standard, Workgroup, Developer, and Web editions. For the latest list of supported versions, see [Using a Microsoft SQL Server Database as a Source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html) in the AWS documentation.

## Architecture
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-redshift-using-aws-dms-architecture"></a>

**Source technology stack**
+ An on-premises Microsoft SQL Server database

**Target technology stack**
+ Amazon Redshift

**Data migration architecture**

![Architecture for migrating an on-premises SQL Server database to Amazon Redshift using AWS DMS](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/65b2be1b-740e-4d4d-99a8-f77c4ea6553d/images/3a094bf2-be31-4d83-8dd2-9dc078321055.png)

## Tools
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-redshift-using-aws-dms-tools"></a>
+ [AWS DMS ](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)is a data migration service that supports several types of source and target databases. For information about the Microsoft SQL Server database versions and editions that are supported for use with AWS DMS, see [Using a Microsoft SQL Server Database as a Source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html) in the AWS DMS documentation. If AWS DMS doesn't support your source database, you must select an alternative method for data migration.

## Epics
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-redshift-using-aws-dms-epics"></a>

### Plan the migration
<a name="plan-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the source and target database version and engine. |  | DBA |
| Identify the hardware requirements for the target server instance. |  | DBA, Systems administrator |
| Identify the storage requirements (storage type and capacity). |  | DBA, Systems administrator |
| Choose the proper instance type based on capacity, storage features, and network features. |  | DBA, Systems administrator |
| Identify the network access security requirements for the source and target databases. |  | DBA, Systems administrator |
| Identify the application migration strategy. |  | DBA, App owner, Systems administrator |

### Configure the infrastructure
<a name="configure-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a virtual private cloud (VPC). | For more information, see [Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the AWS documentation. | Systems administrator |
| Create security groups. |  | Systems administrator |
| Configure and start an Amazon Redshift cluster. | For more information, see [Create a sample Amazon Redshift cluster](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-launch-sample-cluster.html) in the Amazon Redshift documentation. | DBA, Systems administrator |

### Migrate data
<a name="migrate-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Migrate the data from the Microsoft SQL Server database by using AWS DMS. |  | DBA |

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
| Shut down the temporary resources. |  | DBA, Systems administrator |
| Review and validate the project documents. |  | DBA, App owner, Systems administrator |
| Gather metrics such as time to migrate, percentage of manual versus automated tasks, and cost savings. |  | DBA, App owner, Systems administrator |
| Close out the project and provide feedback. |  | DBA, App owner, Systems administrator |

## Related resources
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-redshift-using-aws-dms-resources"></a>

**References**
+ [AWS DMS documentation](https://docs.aws.amazon.com/dms/index.html)
+ [Amazon Redshift documentation](https://docs.aws.amazon.com/redshift/)
+ [Amazon Redshift Pricing](https://aws.amazon.com/redshift/pricing/)

**Tutorials and videos**
+ [Getting Started with AWS DMS](https://aws.amazon.com/dms/getting-started/)
+ [Getting Started with Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html)
+ [Using an Amazon Redshift database as a target for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redshift.html)
+ [AWS DMS (video)](https://www.youtube.com/watch?v=zb4GcjEdl8U)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
