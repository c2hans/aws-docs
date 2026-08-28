---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/IAMDBAuth.Connecting.Drivers.html
---

# Connecting to your DB cluster using IAM authentication with the AWS drivers
<a name="IAMDBAuth.Connecting.Drivers"></a>

The AWS suite of drivers has been designed to provide support for faster switchover and failover times, and authentication with AWS Secrets Manager, AWS Identity and Access Management (IAM), and Federated Identity. The AWS drivers rely on monitoring DB cluster status and being aware of the cluster topology to determine the new writer. This approach reduces switchover and failover times to single-digit seconds, compared to tens of seconds for open-source drivers.

For more information on the AWS drivers, see the corresponding language driver for your [Aurora MySQL](Aurora.Connecting.md#Aurora.Connecting.JDBCDriverMySQL) or [Aurora PostgreSQL](Aurora.Connecting.md#Aurora.Connecting.AuroraPostgreSQL.Utilities) DB cluster.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
