---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-optimization-for-enterpriseone/introduction.html
---

# Optimizing SQL Server on Amazon EC2 for Oracle JD Edwards EnterpriseOne
<a name="introduction"></a>

*Jeremy Shearer, Amazon Web Services*

JD Edwards EnterpriseOne can be used with multiple database platforms, including Oracle Database, SQL Server, and IBM Db2. Many users find that SQL Server is a good database choice because of its balance of cost and features combined with their existing skills for managing a SQL Server database.

Each database platform supports multiple deployment options for EnterpriseOne on AWS, including Amazon Elastic Compute Cloud (Amazon EC2), VMware Cloud on AWS, and Amazon Relational Database Service (Amazon RDS), as the following table shows.

|
|
| EnterpriseOne platform | Deployment options on AWS |
| --- |--- |
| Amazon EC2 | VMware Cloud on AWS | Amazon RDS | Other |
| **Oracle Database** | Yes | Yes | Yes | [IBM Power Systems (i/AIX) and AWS Hybrid Architecture](https://aws.amazon.com/marketplace/pp/prodview-7vj3cq2balphq) |
| **SQL Server** | Yes | Yes | Yes |   |
| **IBM Db2** | Yes | Yes | No | [IBM Power Systems (i/AIX) and AWS Hybrid Architecture](https://aws.amazon.com/marketplace/pp/prodview-7vj3cq2balphq) |

This guide focuses on deploying an EnterpriseOne database with SQL Server on Amazon EC2. For a detailed discussion of other SQL Server deployment options, see [Choosing between Amazon EC2 and Amazon RDS](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/comparison.html).

When you use Oracle JD Edwards EnterpriseOne with a SQL Server database on Amazon EC2, you can take advantage of specific optimization techniques to achieve a highly performant and cost-optimized system. This guide focuses on performance optimization of a SQL Server instance and doesn't cover high availability, disaster recovery, backups, or other complementary configurations covered in other documents, including [Migrating Microsoft SQL Server databases to the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/welcome.html).

This guide builds upon the guide [Best practices for deploying SQL Server on Amazon EC2](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-best-practices/) and is intended for architects and DBAs who have a good understanding of SQL Server and JD Edwards EnterpriseOne.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
