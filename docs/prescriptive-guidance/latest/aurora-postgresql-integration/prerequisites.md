---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aurora-postgresql-integration/prerequisites.html
---

# Prerequisites
<a name="prerequisites"></a>

To follow along with this guide, ensure that you have access to the following:
+ An active AWS account
+ An Amazon Aurora PostgreSQL-Compatible Edition cluster (For instructions, see [Create an Aurora PostgreSQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.AuroraPostgreSQL.html#CHAP_GettingStarted.AuroraPostgreSQL.CreateDBCluster).)
+ Amazon Simple Storage Service (Amazon S3)
+ Amazon CloudWatch Logs
+ AWS Lambda
+ AWS Glue
+ AWS Database Migration Service (AWS DMS)
+ An Amazon Elastic Compute Cloud (Amazon EC2) instance with SQL Server, Oracle, and PostgreSQL databases installed

The Aurora PostgreSQL-Compatible instance and the other databases or AWS services must in be the same virtual private cloud (VPC), or network connectivity must be established between them. Additionally, you must have the required roles and security privileges assigned.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
