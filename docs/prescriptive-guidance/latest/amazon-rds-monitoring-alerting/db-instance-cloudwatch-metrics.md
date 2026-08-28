---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/db-instance-cloudwatch-metrics.html
---

# CloudWatch metrics for DB instances
<a name="db-instance-cloudwatch-metrics"></a>

Amazon CloudWatch also contains metrics that Amazon RDS publishes automatically. The metrics that reside in the `AWS/RDS` namespace are *instance-level metrics*, which refers to the Amazon RDS (service) instance (that is, the isolated database environment running in the cloud) rather than the DB instance in the strict sense of the [mysqld](https://dev.mysql.com/doc/refman/8.0/en/mysqld.html) process. Therefore, most of those [default metrics](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-metrics.html) fall under the category of OS metrics, in the strict definition of the term. Examples include: `CPUUtilization`, `WriteIOPS`, `SwapUsage`, and others. Nevertheless, there are some DB instance metrics that are applicable to MariaDB and MySQL:
+ `BinLogDiskUsage` – The amount of disk space occupied by binary logs.
+ `DatabaseConnections` – The number of client network connections to the DB instance.
+ `ReplicaLag` – The amount of time a read replica DB instance lags behind the source DB instance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
