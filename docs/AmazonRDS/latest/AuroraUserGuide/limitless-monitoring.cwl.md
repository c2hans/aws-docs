---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-monitoring.cwl.html
---

# Monitoring Aurora PostgreSQL Limitless Database with Amazon CloudWatch Logs
<a name="limitless-monitoring.cwl"></a>

Exporting PostgreSQL logs to CloudWatch Logs is required as part of enabling Aurora PostgreSQL Limitless Database. You can access and analyze these logs in CloudWatch Logs Insights, similar to accessing PostgreSQL logs for a standard Aurora PostgreSQL DB cluster. For more information, see [Analyzing PostgreSQL logs using CloudWatch Logs Insights](AuroraPostgreSQL.CloudWatch.Analyzing.md).

The log group name for the DB cluster is the same as in Aurora PostgreSQL:

```
/aws/rds/cluster/{{DB_cluster_ID}}/postgresql
```

The log group name for the DB shard group takes the following form:

```
/aws/rds/cluster/{{DB_cluster_ID}}/{{DB_shard_group_ID}}/postgresql
```

There are log streams for each node (router or shard). Their names have the following form:

```
[DistributedTransactionRouter|DataAccessShard]/{{node_cluster_serial_ID}}-{{node_instance_serial_ID}}/{{n}}
```

For example:
+ Router – `DistributedTransactionRouter/6-6.2`
+ Shard – `DataAccessShard/22-22.0`

**Note**
You can't view PostgreSQL log files for the DB shard group directly in the RDS console, AWS CLI, or RDS API as you can for the DB cluster. You must use CloudWatch Logs Insights to view them.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
