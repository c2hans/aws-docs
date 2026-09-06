---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-sql-server-edition/prerequisites.html
---

# Prerequisites and limitations
<a name="prerequisites"></a>

## Prerequisites
<a name="prerequisites.3d49ca57-c739-592f-acba-70b7741e724c"></a>
+ No application support requirements for Microsoft SQL Server Enterprise edition
+ An active AWS account
+ Secure network connectivity, through a virtual private network or [AWS Direct Connect](https://aws.amazon.com/directconnect/), between your on-premises data center and a virtual private cloud (VPC) on AWS
+ SQL Server Enterprise edition running in an on-premises data center or on an Amazon Elastic Compute Cloud (Amazon EC2) instance or on Amazon RDS for SQL Server
+ A database client tool, such as SQL Server Management Studio (SSMS), for running Transact-SQL (T-SQL) commands
+ Access to the database and permissions to run an [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) assessment

## Limitations
<a name="limitations.6d07a40f-70b9-5b52-8bf3-c012a3c23ab5"></a>
+ Amazon RDS for SQL Server has storage size and IOPs limits. For the current maximum, see the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.FeatureSupport.Limits).
+ AWS SCT supports SQL Server version 2008 and later.

## Product versions
<a name="product-versions.1c0f404f-07b1-58c1-911d-fd07824fe36f"></a>

The general logic described in this guide applies to SQL Server versions from 2005 and later. However, AWS SCT supports only SQL Server versions 2008 and later. To identify feature usage in cases where AWS SCT is not supported, run SQL queries on the source database.

For a current list of supported versions and editions, see [Microsoft SQL Server on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html) in the AWS documentation. For details on pricing and supported instance classes, see [Amazon RDS for SQL Server pricing](https://aws.amazon.com/rds/sqlserver/pricing/).
