---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.sqlserveralwayson2aurorapostgresql.prerequisites.html
---

# Prerequisties for migrating SQL Server AlwaysOn databases on primary replica to Amazon Aurora PostgreSQL
<a name="chap-manageddatabases.sqlserveralwayson2aurorapostgresql.prerequisites"></a>

The following prerequisites are required to complete this migration:
+ An AWS account with AWS Identity and Access Management (IAM) credentials that allow you to launch Amazon RDS and AWS Database Migration Service (AWS DMS) instances in your AWS Region. For information about IAM credentials, see [Create an IAM User](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SettingUp.html#CHAP_SettingUp.IAM).
+ A general understanding of Amazon Virtual Private Cloud (Amazon VPC), DNS, and security groups concepts. For information about using Amazon VPC with Amazon RDS, see [Amazon Virtual Private Cloud (VPCs) and Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html). For information about Amazon RDS security groups, see [Amazon RDS Security Groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html). For information about network setup to support AWS DMS replication instances, see [Setting up network for replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.VPC.html). For information about AWS DMS using Route53 for endpoint name resolution, see [Using Amazon Route 53 Resolver with AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.html).
+ A general understanding of using Microsoft SQL Server as a source and Amazon Aurora PostgreSQL as a target endpoint in an AWS DMS] based migration. For information about working with SQL Server as a source, see [Using a SQL Server Database as a Source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html). Aurora PostgreSQL is a PostgreSQL compatible database. For information about working with Aurora PostgreSQL as a target, see [Using a PostgreSQL database as a Target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html).
+ An understanding of your source table structure, backup policy, and resource constraints.
+ Convert your SQL Server database schema to PostgreSQL using a optional tool such as [Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Installing.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
