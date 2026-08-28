---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-replication-gtid.configuring-aurora.html
---

# Enabling GTID-based replication for an Aurora MySQL cluster
<a name="mysql-replication-gtid.configuring-aurora"></a><a name="gtid"></a>

When GTID-based replication is enabled for an Aurora MySQL DB cluster, the GTID settings apply to both inbound and outbound binlog replication.

**To enable GTID-based replication for an Aurora MySQL cluster**

1. Create or edit a DB cluster parameter group using the following parameter settings:
   + `gtid_mode` – `ON` or `ON_PERMISSIVE`
   + `enforce_gtid_consistency` – `ON`

1. Associate the DB cluster parameter group with the Aurora MySQL cluster. To do so, follow the procedures in [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md).

1. (Optional) Specify how to assign GTIDs to transactions that don't include them. To do so, call the stored procedure in [mysql.rds\_assign\_gtids\_to\_anonymous\_transactions (Aurora MySQL version 3)](mysql-stored-proc-gtid.md#mysql_assign_gtids_to_anonymous_transactions).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
