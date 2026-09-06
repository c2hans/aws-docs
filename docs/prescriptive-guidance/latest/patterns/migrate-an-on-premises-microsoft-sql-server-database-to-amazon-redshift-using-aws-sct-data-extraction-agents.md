---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-microsoft-sql-server-database-to-amazon-redshift-using-aws-sct-data-extraction-agents.html
---

# Migrate an on-premises Microsoft SQL Server database to Amazon Redshift using AWS SCT data extraction agents
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-redshift-using-aws-sct-data-extraction-agents"></a>

*Neha Thakur, Amazon Web Services*

## Summary
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-redshift-using-aws-sct-data-extraction-agents-summary"></a>

This pattern outlines steps for migrating an on-premises Microsoft SQL Server source database to an Amazon Redshift target database by using AWS Schema Conversion Tool (AWS SCT) data extraction agents. An agent is an external program that is integrated with AWS SCT but performs data transformation elsewhere and interacts with other AWS services on your behalf.

## Prerequisites and limitations
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-redshift-using-aws-sct-data-extraction-agents-prereqs"></a>

**Prerequisites**
+ A Microsoft SQL Server source database used for the data warehouse workload in an on-premises data center
+ An active AWS account

**Product versions**
+ Microsoft SQL Server version 2008 or later. For the latest list of supported versions, see [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html).

## Architecture
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-redshift-using-aws-sct-data-extraction-agents-architecture"></a>

**technology stack****Source  **
+ An on-premises Microsoft SQL Server database

**technology stack****Target  **
+ Amazon Redshift

**Data migration architecture**

![Migrating a SQL Server database to Amazon Redshift by using AWS SCT data extraction agents.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/6975f67a-0705-47b4-a1b8-90aaa2597a04/images/dbff958b-7601-442e-9e23-4d07edd0ccfd.png)

## Tools
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-redshift-using-aws-sct-data-extraction-agents-tools"></a>
+ [AWS Schema Conversion Tool](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) (AWS SCT) handles heterogeneous database migrations by automatically converting the source database schema and a majority of the custom code to a format that's compatible with the target database. When the source and target databases are very different, you can use an AWS SCT agent to perform additional data transformation. For more information, see [Migrating Data from an On-Premises Data Warehouse to Amazon Redshift](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/agents.dw.html) in the AWS documentation.

## Best practices
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-redshift-using-aws-sct-data-extraction-agents-best-practices"></a>
+ [Best practices for AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_BestPractices.html)
+ [Best practices for Amazon Redshift ](https://docs.aws.amazon.com/redshift/latest/dg/best-practices.html)

## Epics
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-redshift-using-aws-sct-data-extraction-agents-epics"></a>

### Prepare for migration
<a name="prepare-for-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the source and target database versions and engines. |  | DBA |
| Identify hardware requirements for the target server instance. |  | DBA, SysAdmin |
| Identify storage requirements (storage type and capacity). |  | DBA, SysAdmin |
| Choose the proper instance type (capacity, storage features, network features). |  | DBA, SysAdmin |
| Identify network access security requirements for the source and target databases. |  | DBA, SysAdmin |
| Choose an application migration strategy. |  | DBA, SysAdmin, App owner |

### Configure infrastructure
<a name="configure-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a virtual private cloud (VPC) and subnets. |  | SysAdmin |
| Create security groups. |  | SysAdmin |
| Configure and start the Amazon Redshift cluster. |  | SysAdmin |

### Migrate data
<a name="migrate-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Migrate the data using the AWS SCT data extraction agents. |  | DBA |

### Migrate applications
<a name="migrate-applications"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Follow the chosen application migration strategy. |  | DBA, SysAdmin, App owner |

### Cut over to the target database
<a name="cut-over-to-the-target-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Switch application clients over to the new infrastructure. |  | DBA, SysAdmin, App owner |

### Close the project
<a name="close-the-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Shut down temporary AWS resources. |  | DBA, SysAdmin |
| Review and validate the project documents. |  | DBA, SysAdmin, App owner |
| Gather metrics such as time to migrate, percentage of manual versus automated tasks, and cost savings. |  | DBA, SysAdmin, App owner |
| Close the project and provide any feedback. |  | DBA, SysAdmin, App owner |

## Related resources
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-redshift-using-aws-sct-data-extraction-agents-resources"></a>

**References**
+ [AWS SCT User Guide](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)
+ [Using Data Extraction Agents](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/agents.html)
+ [Amazon Redshift Pricing](https://aws.amazon.com/redshift/pricing/)

**Tutorials and videos**
+ [Getting Started with the AWS Schema Conversion Tool](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_GettingStarted.html)
+ [Getting Started with Amazon Redshift](http://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html)
