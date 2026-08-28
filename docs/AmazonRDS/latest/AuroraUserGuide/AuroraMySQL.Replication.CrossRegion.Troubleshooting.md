---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.CrossRegion.Troubleshooting.html
---

# Troubleshooting cross-Region replicas for Amazon Aurora MySQL
<a name="AuroraMySQL.Replication.CrossRegion.Troubleshooting"></a>

 Following you can find a list of common error messages that you might encounter when creating an Amazon Aurora cross-Region read replica, and how to resolve the specified errors.

## Source cluster [DB cluster ARN] doesn't have binlogs enabled
<a name="AuroraMySQL.Replication.CrossRegion.Troubleshooting.1"></a>

 To resolve this issue, turn on binary logging on the source DB cluster. For more information, see [Before you begin](AuroraMySQL.Replication.CrossRegion.md#AuroraMySQL.Replication.CrossRegion.Prerequisites).

## Source cluster [DB cluster ARN] doesn't have cluster parameter group in sync on writer
<a name="AuroraMySQL.Replication.CrossRegion.Troubleshooting.2"></a>

 You receive this error if you have updated the `binlog_format` DB cluster parameter, but have not rebooted the primary instance for the DB cluster. Reboot the primary instance (that is, the writer) for the DB cluster and try again.

## Source cluster [DB cluster ARN] already has a read replica in this region
<a name="AuroraMySQL.Replication.CrossRegion.Troubleshooting.3"></a>

 You can have up to five cross-Region DB clusters that are read replicas for each source DB cluster in any AWS Region. If you already have the maximum number of read replicas for a DB cluster in a particular AWS Region, you must delete an existing one before you can create a new cross-Region DB cluster in that Region.

## DB cluster [DB cluster ARN] requires a database engine upgrade for cross-Region replication support
<a name="AuroraMySQL.Replication.CrossRegion.Troubleshooting.4"></a>

 To resolve this issue, upgrade the database engine version for all of the instances in the source DB cluster to the most recent database engine version, and then try creating a cross-Region read replica DB again.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
