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
