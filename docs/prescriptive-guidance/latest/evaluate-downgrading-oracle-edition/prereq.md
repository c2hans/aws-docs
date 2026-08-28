---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-oracle-edition/prereq.html
---

# Prerequisites and limitations
<a name="prereq"></a>

## Prerequisites
<a name="prerequisites"></a>
+ No application support requirements for Oracle Database Enterprise Edition (EE)
+ Oracle Database EE running in an on-premises data center, or on [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/), or on Amazon RDS for Oracle or Amazon RDS Custom for Oracle
+ A database client tool, such as Oracle SQL Developer or SQL\*Plus, for running SQL commands
+ Access to the database and [privileges](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Permissions) to run an [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) assessment

## Limitations
<a name="limitations"></a>
+ Amazon RDS for Oracle has storage size and IOPs limits. For the current maximum, see the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html).
+ Oracle Standard Edition 2 supports a maximum of 16 CPU threads. For currently supported instance classes for Amazon RDS for Oracle Standard Edition 2, see the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.InstanceClasses.html).
+ AWS SCT supports Oracle 10.2 and later.

## Product versions
<a name="versions"></a>

The general logic described in this guide applies to Oracle versions from 9i and later. However, AWS SCT supports only Oracle Database versions 10g and later. To identify feature usage in cases where AWS SCT is not supported, run SQL queries on the source database.

For a current list of supported versions and editions, see [Oracle on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html) in the AWS documentation. For details on pricing and supported instance classes, see [Amazon RDS for Oracle pricing](https://aws.amazon.com/rds/oracle/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
